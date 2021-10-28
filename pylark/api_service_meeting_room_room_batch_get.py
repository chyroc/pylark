# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class BatchGetMeetingRoomRoomReq(object):
    room_ids: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "query", "key": "room_ids"}
    )  # 用于查询指定会议室的 ID
    fields: str = attr.ib(
        default="", metadata={"req_type": "query", "key": "fields"}
    )  # 用于指定返回的字段名，每个字段名之间用逗号 "," 分隔，如：“id,name”，"*" 表示返回全部字段，可选字段有："id,name,description,capacity,building_id,building_name,floor_name,is_disabled,display_id"，默认返回所有字段


@attr.s
class BatchGetMeetingRoomRoomRespRoom(object):
    room_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "room_id"}
    )  # 会议室 ID
    building_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "building_id"}
    )  # 会议室所属建筑物 ID
    building_name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "building_name"}
    )  # 会议室所属建筑物名称
    capacity: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "capacity"}
    )  # 会议室能容纳的人数
    description: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "description"}
    )  # 会议室的相关描述
    display_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "display_id"}
    )  # 会议室的展示 ID
    floor_name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "floor_name"}
    )  # 会议室所在楼层名称
    is_disabled: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json", "key": "is_disabled"}
    )  # 会议室是否不可用，若会议室不可用，则该值为 true，否则为 false
    name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "name"}
    )  # 会议室名称


@attr.s
class BatchGetMeetingRoomRoomResp(object):
    rooms: BatchGetMeetingRoomRoomRespRoom = attr.ib(
        default=None, metadata={"req_type": "json", "key": "rooms"}
    )  # 会议室列表


def _gen_batch_get_meeting_room_room_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=BatchGetMeetingRoomRoomResp,
        scope="MeetingRoom",
        api="BatchGetMeetingRoomRoom",
        method="GET",
        url="https://open.feishu.cn/open-apis/meeting_room/room/batch_get",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
