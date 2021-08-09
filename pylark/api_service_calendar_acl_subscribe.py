# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing


@attr.s
class SubscribeCalendarACLReq(object):
    calendar_id: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 日历ID, 示例值："feishu.cn_xxxxxxxxxx@group.calendar.feishu.cn"


@attr.s
class SubscribeCalendarACLResp(object):
    pass


def _gen_subscribe_calendar_acl_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=SubscribeCalendarACLResp,
        scope="Calendar",
        api="SubscribeCalendarACL",
        method="POST",
        url="https://open.feishu.cn/open-apis/calendar/v4/calendars/:calendar_id/acls/subscription",
        body=request,
        method_option=_new_method_option(options),
    )
