# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
from pylark import lark_type_enum, lark_type_sheet
import attr
import typing
import io


@attr.s
class ReplyMeetingRoomInstanceReq(object):
    room_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "room_id"}
    )  # 会议室的 ID
    uid: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "uid"}
    )  # 会议室的日程 ID
    original_time: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "original_time"}
    )  # 日程实例原始时间，非重复日程必为0。重复日程若为0则表示回复其所有实例，否则表示回复单个实例。
    status: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "status"}
    )  # 回复状态，NOT_CHECK_IN 表示未签到，ENDED_BEFORE_DUE 表示提前结束


@attr.s
class ReplyMeetingRoomInstanceResp(object):
    pass


def _gen_reply_meeting_room_instance_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=ReplyMeetingRoomInstanceResp,
        scope="MeetingRoom",
        api="ReplyMeetingRoomInstance",
        method="POST",
        url="https://open.feishu.cn/open-apis/meeting_room/instance/reply",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
