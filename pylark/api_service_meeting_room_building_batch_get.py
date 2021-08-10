# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class BatchGetMeetingRoomBuildingReq(object):
    building_ids: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # 用于查询指定建筑物的 ID
    fields: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # 用于指定返回的字段名，每个字段名之间用逗号 "," 分隔，如：“id,name”，"*" 表示返回全部字段，可选字段有："id,name,description,floors"，默认返回所有字段


@attr.s
class BatchGetMeetingRoomBuildingRespBuilding(object):
    building_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 建筑物 ID
    description: str = attr.ib(default="", metadata={"req_type": "json"})  # 建筑物的相关描述
    floors: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 属于当前建筑物的所有楼层列表
    name: str = attr.ib(default="", metadata={"req_type": "json"})  # 建筑物名称


@attr.s
class BatchGetMeetingRoomBuildingResp(object):
    buildings: BatchGetMeetingRoomBuildingRespBuilding = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 建筑列表


def _gen_batch_get_meeting_room_building_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=BatchGetMeetingRoomBuildingResp,
        scope="MeetingRoom",
        api="BatchGetMeetingRoomBuilding",
        method="GET",
        url="https://open.feishu.cn/open-apis/meeting_room/building/batch_get",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
