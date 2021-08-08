import logging
from typing import TypeVar, Type, TYPE_CHECKING
from dataclasses import dataclass, field

import requests
from dacite import from_dict

from pylark.lark_exception import PyLarkError
from pylark.log import logger
import dataclasses

if TYPE_CHECKING:
    from pylark import Lark

RawRequestDataClass = TypeVar("RawRequestDataClass")


@dataclass
class Response(object):
    method: str = ""
    url: str = ""
    header: dict = field(default_factory=lambda: dict())
    status_code: int = 0
    request_id: str = ""
    content_length: int = 0


@dataclass
class MethodOption(object):
    user_access_token: str = ""


# type MethodOptionFunc func(*MethodOption)


def _new_method_option(options=None) -> MethodOption:
    return MethodOption()


@dataclass
class RawRequestReq(object):
    scope: str = ""
    api: str = ""
    method: str = ""
    url: str = ""
    body: any = None
    is_file: bool = False
    need_tenant_access_token: bool = False
    need_app_access_token: bool = False
    need_user_access_token: bool = False
    need_helpdesk_access_token: bool = False
    method_option: MethodOption = field(default_factory=lambda: MethodOption())
    headers: dict = field(default_factory=lambda: dict())
    dataclass: Type[RawRequestDataClass] = None


class Request(object):
    @staticmethod
    def raw_request(
        cli: "Lark", req: RawRequestReq
    ) -> tuple[RawRequestDataClass, Response]:
        print("req", req)
        req.headers = Request._prepare_headers(cli, req)

        data, response = Request.do_request(req)
        print("data", data)
        print("response", response)

        if not req.dataclass:
            return data, response

        return from_dict(data_class=req.dataclass, data=data), response

    @staticmethod
    def _prepare_headers(cli: "Lark", req: RawRequestReq) -> dict:
        headers = {}
        if req.method != "GET":
            headers["Content-Type"] = "application/json; charset=utf-8"

        if req.need_user_access_token and req.method_option.user_access_token != "":
            headers["Authorization"] = "Bearer " + req.method_option.user_access_token
        elif req.need_tenant_access_token:
            token = ""
            res, _ = cli.auth.get_tenant_access_token()
            headers["Authorization"] = "Bearer " + res.token

        if req.need_helpdesk_access_token:
            headers[
                "X-Lark-Helpdesk-Authorization"
            ] = ""  # base64.StdEncoding.EncodeToString([]byte(r.helpdeskID + ":" + r.helpdeskToken))

        return headers

    @staticmethod
    def do_request(request_parm: RawRequestReq) -> tuple[dict, Response]:
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

        r.raise_for_status()

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
            for field in dataclasses.fields(req.body):
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
