# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class DeleteCalendarEventAttendeeReq(object):
    calendar_id: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 日历 ID, 示例值："feishu.cn_xxxxxxxxxx@group.calendar.feishu.cn"
    event_id: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 日程 ID, 示例值："xxxxxxxxx_0"
    attendee_ids: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 要移除的参与人 ID 列表
    need_notification: bool = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 删除日程参与人时是否要给参与人发送bot通知，默认为true, 示例值：false


@attr.s
class DeleteCalendarEventAttendeeResp(object):
    pass


def _gen_delete_calendar_event_attendee_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=DeleteCalendarEventAttendeeResp,
        scope="Calendar",
        api="DeleteCalendarEventAttendee",
        method="POST",
        url="https://open.feishu.cn/open-apis/calendar/v4/calendars/:calendar_id/events/:event_id/attendees/batch_delete",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        need_user_access_token=True,
    )
