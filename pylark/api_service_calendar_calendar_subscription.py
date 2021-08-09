# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing


@attr.s
class SubscribeCalendarChangeEventReq(object):
    pass


@attr.s
class SubscribeCalendarChangeEventResp(object):
    pass


def _gen_subscribe_calendar_change_event_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=SubscribeCalendarChangeEventResp,
        scope="Calendar",
        api="SubscribeCalendarChangeEvent",
        method="POST",
        url="https://open.feishu.cn/open-apis/calendar/v4/calendars/subscription",
        body=request,
        method_option=_new_method_option(options),
    )
