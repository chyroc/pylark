# Code generated by lark_sdk_gen. DO NOT EDIT.

import typing
from pylark.lark_request import Response

from pylark.api_service_okr_period_get_list import (
    GetOKRPeriodListReq,
    GetOKRPeriodListResp,
    _gen_get_okr_period_list_req,
)
from pylark.api_service_okr_okr_batch_get import (
    BatchGetOKRReq,
    BatchGetOKRResp,
    _gen_batch_get_okr_req,
)
from pylark.api_service_okr_user_okr_get_list import (
    GetUserOKRListReq,
    GetUserOKRListResp,
    _gen_get_user_okr_list_req,
)


if typing.TYPE_CHECKING:
    from lark import Lark


class LarkOKRService(object):
    cli: "Lark"

    def __init__(self, cli: "Lark"):
        self.cli = cli

    def get_okr_period_list(
        self, request: GetOKRPeriodListReq, options: typing.List[str] = None
    ) -> typing.Tuple[GetOKRPeriodListResp, Response]:
        return self.cli.raw_request(_gen_get_okr_period_list_req(request, options))

    def batch_get_okr(
        self, request: BatchGetOKRReq, options: typing.List[str] = None
    ) -> typing.Tuple[BatchGetOKRResp, Response]:
        return self.cli.raw_request(_gen_batch_get_okr_req(request, options))

    def get_user_okr_list(
        self, request: GetUserOKRListReq, options: typing.List[str] = None
    ) -> typing.Tuple[GetUserOKRListResp, Response]:
        return self.cli.raw_request(_gen_get_user_okr_list_req(request, options))
