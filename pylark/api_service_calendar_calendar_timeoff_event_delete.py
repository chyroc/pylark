# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing


@attr.s
class DeleteCalendarTimeoffEventReq(object):
    timeoff_event_id: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 休假申请的唯一标识id, 示例值："timeoff:XXXXXX-XXXX-0917-1623-aa493d591a39"


@attr.s
class DeleteCalendarTimeoffEventResp(object):
    pass


def _gen_delete_calendar_timeoff_event_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=DeleteCalendarTimeoffEventResp,
        scope="Calendar",
        api="DeleteCalendarTimeoffEvent",
        method="DELETE",
        url="https://open.feishu.cn/open-apis/calendar/v4/timeoff_events/:timeoff_event_id",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )