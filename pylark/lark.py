import logging

from dacite import from_dict
import requests

from pylark.api_service_ai import LarkAIService
from pylark.api_service_auth import LarkAuthService
from pylark.log import logger
from pylark.lark_request import RawRequestReq, Response, RawRequestDataClass, Request


class Lark(object):
    app_id: str
    app_secret: str
    custom_url: str
    custom_secret: str

    auth: LarkAuthService
    ai: LarkAIService

    def __init__(
        self,
        app_id="",
        app_secret="",
        custom_url="",
        custom_secret="",
    ):
        self.auth = LarkAuthService(cli=self)
        self.ai = LarkAIService(cli=self)
        self.app_id = app_id
        self.app_secret = app_secret
        self.custom_secret = custom_secret
        self.custom_url = custom_url

    def raw_request(self, req: RawRequestReq) -> tuple[RawRequestDataClass, Response]:
        logger.info("[lark] %s#%s call api", req.scope, req.api)

        req.headers = self.prepare_headers(req)

        return Request.raw_request(cli=self, req=req)

    def prepare_headers(self, req: RawRequestReq) -> dict:
        headers = {}
        if req.method != "GET":
            headers["Content-Type"] = "application/json; charset=utf-8"

        if req.need_user_access_token and req.method_option.user_access_token != "":
            headers["Authorization"] = "Bearer " + req.method_option.user_access_token
        elif req.need_tenant_access_token:
            res, _ = self.auth.get_tenant_access_token()
            headers["Authorization"] = "Bearer " + res.token

        if req.need_helpdesk_access_token:
            headers[
                "X-Lark-Helpdesk-Authorization"
            ] = ""  # base64.StdEncoding.EncodeToString([]byte(r.helpdeskID + ":" + r.helpdeskToken))

        return headers

    def do_request(self, request_parm: RawRequestReq, real_response) -> Response:
        response = Response()
        real_req = self.parse_request_param(request_parm)

        response.method = real_req["method"]
        response.url = real_req["url"]
        response.header = real_req["header"]

        logger.debug("[lark] request %s#%s, %s %s, header=%s, body=%s", "")

    def parse_request_param(self, req: RawRequestReq):
        return {"method": "", "url": "", "header": {}}
