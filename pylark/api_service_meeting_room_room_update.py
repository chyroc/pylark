# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class UpdateMeetingRoomRoomReq(object):
    room_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 要更新的会议室ID
    name: str = attr.ib(default="", metadata={"req_type": "json"})  # 会议室名称
    capacity: int = attr.ib(default=0, metadata={"req_type": "json"})  # 容量
    custom_room_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 租户自定义会议室ID


@attr.s
class UpdateMeetingRoomRoomResp(object):
    pass


def _gen_update_meeting_room_room_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=UpdateMeetingRoomRoomResp,
        scope="MeetingRoom",
        api="UpdateMeetingRoomRoom",
        method="POST",
        url="https://open.feishu.cn/open-apis/meeting_room/room/update",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
