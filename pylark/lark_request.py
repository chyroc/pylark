import logging
from typing import TypeVar, Type, TYPE_CHECKING, Tuple
import attr
import requests

from pylark.helper import _make_dataclass_from_dict, _to_attr_dict
from pylark.lark_exception import PyLarkError
from pylark.log import logger

if TYPE_CHECKING:
    from pylark import Lark

RawRequestDataClass = TypeVar("RawRequestDataClass")


@attr.s
class Response(object):
    method = attr.ib(default="")
    url = attr.ib(default="")
    header = attr.ib(factory=lambda: dict())
    status_code = attr.ib(default=0)
    request_id = attr.ib(default="")
    content_length = attr.ib(default=0)


@attr.s
class MethodOption(object):
    user_access_token = attr.ib(default="")


# type MethodOptionFunc func(*MethodOption)


def _new_method_option(options=None) -> MethodOption:
    return MethodOption()


@attr.s
class RawRequestReq(object):
    scope = attr.ib(default="")
    api = attr.ib(default="")
    method = attr.ib(default="")
    url = attr.ib(default="")
    body = attr.ib(default=None)
    is_file = attr.ib(default=False)
    need_tenant_access_token = attr.ib(default=False)
    need_app_access_token = attr.ib(default=False)
    need_user_access_token = attr.ib(default=False)
    need_helpdesk_access_token = attr.ib(default=False)
    need_helpdesk_auth = attr.ib(default=False)
    method_option: MethodOption = attr.ib(factory=lambda: MethodOption())
    headers: dict = attr.ib(factory=lambda: dict())
    dataclass: Type[RawRequestDataClass] = attr.ib(default=None)


class Request(object):
    @staticmethod
    def raw_request(
        cli: "Lark", req: RawRequestReq
    ) -> Tuple[RawRequestDataClass, Response]:
        req.headers = Request._prepare_headers(cli, req)

        data, response = Request.do_request(req)

        if not req.dataclass:
            return data, response

        return _make_dataclass_from_dict(req.dataclass, data), response

    @staticmethod
    def _prepare_headers(cli: "Lark", req: RawRequestReq) -> dict:
        headers = {}
        if req.method != "GET":
            headers["Content-Type"] = "application/json; charset=utf-8"

        if req.need_user_access_token and req.method_option.user_access_token != "":
            headers["Authorization"] = "Bearer " + req.method_option.user_access_token
        elif req.need_tenant_access_token:
            res, _ = cli.auth.get_tenant_access_token()
            headers["Authorization"] = "Bearer " + res.token
        elif req.need_app_access_token:
            res, _ = cli.auth.get_app_access_token()
            headers["Authorization"] = "Bearer " + res.token

        if req.need_helpdesk_access_token:
            headers[
                "X-Lark-Helpdesk-Authorization"
            ] = ""  # base64.StdEncoding.EncodeToString([]byte(r.helpdeskID + ":" + r.helpdeskToken))

        return headers

    @staticmethod
    def do_request(request_parm: RawRequestReq) -> Tuple[dict, Response]:
        response = Response()
        real_req = Request._parse_request_param(request_parm)

        query = real_req["query"]
        body = real_req["body"]
        header = real_req["header"]
        method = real_req["method"]
        url = real_req["url"]

        response.method = method
        response.url = url

        logger.debug(
            "[lark] request %s#%s, %s %s, header=%s, body=%s",
            request_parm.scope,
            request_parm.api,
            method,
            url,
            header,
            body,
        )

        body = _to_attr_dict(body)

        r = requests.request(
            response.method,
            response.url,
            json=body,
            headers=header,
            params=query,
        )
        resp_body = r.json()
        response.request_id = r.headers.get("X-Request-Id")

        logger.debug(
            "[lark] request %s#%s, request_id=%s, response=%s",
            request_parm.scope,
            request_parm.api,
            response.request_id,
            resp_body,
        )

        # r.raise_for_status()

        # 	response.StatusCode = resp.StatusCode
        # 	response.RequestID = resp.Header.Get("X-Request-Id")
        # 	response.Header = resp.Header
        # 	response.ContentLength = resp.ContentLength

        code = resp_body.get("code") or 0
        msg = resp_body.get("msg") or ""
        if "data" in resp_body:
            data = resp_body.get("data") or {}
        else:
            data = resp_body
        if code != 0:
            raise PyLarkError(
                scope=request_parm.scope, func=request_parm.method, code=code, msg=msg
            )

        return data, response

    @staticmethod
    def _parse_request_param(req: RawRequestReq):
        file_key = ""
        body = {}
        query = {}
        uri = req.url
        headers = req.headers
        if not headers:
            headers = {}

        if isinstance(req.body, dict):
            body = req.body
        else:
            for field in attr.fields(type(req.body)):
                req_type = field.metadata["req_type"]
                if req_type == "json":
                    field_val = getattr(req.body, field.name, None)
                    if field_val:
                        body[field.name] = getattr(req.body, field.name)
                elif req_type == "query":
                    field_val = getattr(req.body, field.name, None)
                    if field_val:
                        query[field.name] = getattr(req.body, field.name)
                else:
                    field_val = getattr(req.body, field.name, None)
                    if field_val:
                        uri = uri.replace(":" + field.name, field_val)

        return {
            "query": query,
            "body": body,
            "method": req.method,
            "url": uri,
            "header": headers,
        }
