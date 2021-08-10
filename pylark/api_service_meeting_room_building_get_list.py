# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class GetMeetingRoomBuildingListReq(object):
    page_size: int = attr.ib(
        default=0, metadata={"req_type": "query"}
    )  # 请求期望返回的建筑物数量，不足则返回全部，该值默认为 10，最大为 100
    page_token: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # 用于标记当前请求的分页标记，将返回以当前分页标记开始，往后 page_size 个元素
    order_by: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # 提供用于对名称进行升序/降序排序的方式查询，可选项有："name-asc,name-desc"，传入其他字符串不做处理，默认无序
    fields: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # 用于指定返回的字段名，每个字段名之间用逗号 "," 分隔，如：“id,name”，"*" 表示返回全部字段，可选字段有："id,name,description,floors"，默认返回所有字段


@attr.s
class GetMeetingRoomBuildingListRespBuildings(object):
    building_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 建筑物 ID
    description: str = attr.ib(default="", metadata={"req_type": "json"})  # 建筑物的相关描述
    floors: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 属于当前建筑物的所有楼层列表
    name: str = attr.ib(default="", metadata={"req_type": "json"})  # 建筑物名称


@attr.s
class GetMeetingRoomBuildingListResp(object):
    page_token: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 分页标记，存在下一页时返回
    has_more: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 存在下一页时，该值为 true，否则为 false
    buildings: GetMeetingRoomBuildingListRespBuildings = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 建筑列表


def _gen_get_meeting_room_building_list_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetMeetingRoomBuildingListResp,
        scope="MeetingRoom",
        api="GetMeetingRoomBuildingList",
        method="GET",
        url="https://open.feishu.cn/open-apis/meeting_room/building/list",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
