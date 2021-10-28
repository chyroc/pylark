# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class UnsubscribeCalendarReq(object):
    calendar_id: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "calendar_id"}
    )  # 日历ID, 示例值："feishu.cn_xxxxxxxxxx@group.calendar.feishu.cn"


@attr.s
class UnsubscribeCalendarResp(object):
    pass


def _gen_unsubscribe_calendar_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=UnsubscribeCalendarResp,
        scope="Calendar",
        api="UnsubscribeCalendar",
        method="POST",
        url="https://open.feishu.cn/open-apis/calendar/v4/calendars/:calendar_id/unsubscribe",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        need_user_access_token=True,
    )
