# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing


@attr.s
class OpenCalenderReq(object):
    pass


@attr.s
class OpenCalenderResp(object):
    pass


def _gen_open_calender_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=OpenCalenderResp,
        scope="AppLink",
        api="OpenCalender",
        method="",
        url="https://applink.feishu.cn/client/calendar/open",
        body=request,
        method_option=_new_method_option(options),
    )