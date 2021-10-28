# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
from pylark import lark_type_enum, lark_type_sheet
import attr
import typing
import io


@attr.s
class SubscribeHelpdeskEventReqEvent(object):
    type: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "type"}
    )  # 事件类型, 示例值："helpdesk.ticket_message"
    subtype: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "subtype"}
    )  # 事件子类型, 示例值："ticket_message.created_v1"


@attr.s
class SubscribeHelpdeskEventReq(object):
    events: typing.List[SubscribeHelpdeskEventReqEvent] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "events"}
    )  # 可订阅的事件列表


@attr.s
class SubscribeHelpdeskEventResp(object):
    pass


def _gen_subscribe_helpdesk_event_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=SubscribeHelpdeskEventResp,
        scope="Helpdesk",
        api="SubscribeHelpdeskEvent",
        method="POST",
        url="https://open.feishu.cn/open-apis/helpdesk/v1/events/subscribe",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        need_helpdesk_auth=True,
    )
