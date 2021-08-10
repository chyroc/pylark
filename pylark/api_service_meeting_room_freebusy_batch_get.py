# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class BatchGetMeetingRoomFreebusyReq(object):
    room_ids: str = attr.ib(default="", metadata={"req_type": "query"})  # 用于查询指定会议室的 ID
    time_min: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # 查询会议室忙闲的起始时间，需要遵循格式 [RFC3339](https://tools.ietf.org/html/rfc3339)，需要进行URL Encode
    time_max: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # 查询会议室忙闲的结束时间，需要遵循格式 [RFC3339](https://tools.ietf.org/html/rfc3339)，需要进行URL Encode


@attr.s
class BatchGetMeetingRoomFreebusyRespFreeBusyRoomIDOrganizerInfo(object):
    name: str = attr.ib(default="", metadata={"req_type": "json"})  # 组织者姓名
    open_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 组织者 open_id


@attr.s
class BatchGetMeetingRoomFreebusyRespFreeBusyRoomID(object):
    start_time: str = attr.ib(default="", metadata={"req_type": "json"})  # 忙碌起始时间
    end_time: str = attr.ib(default="", metadata={"req_type": "json"})  # 忙碌结束时间
    uid: str = attr.ib(default="", metadata={"req_type": "json"})  # 日程 ID
    original_time: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 日程实例的原始时间, 非重复日程为0，重复日程为非0
    organizer_info: BatchGetMeetingRoomFreebusyRespFreeBusyRoomIDOrganizerInfo = (
        attr.ib(default=None, metadata={"req_type": "json"})
    )  # 组织者信息, 私密日程不返回该信息


@attr.s
class BatchGetMeetingRoomFreebusyRespFreeBusy(object):
    room_id: BatchGetMeetingRoomFreebusyRespFreeBusyRoomID = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 与请求合法参数相同，表示之后是对应会议室的忙闲状态


@attr.s
class BatchGetMeetingRoomFreebusyResp(object):
    time_min: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 查询会议室忙闲的起始时间，与请求参数完全相同
    time_max: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 查询会议室忙闲的结束时间，与请求参数完全相同
    free_busy: BatchGetMeetingRoomFreebusyRespFreeBusy = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 会议室忙闲列表


def _gen_batch_get_meeting_room_freebusy_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=BatchGetMeetingRoomFreebusyResp,
        scope="MeetingRoom",
        api="BatchGetMeetingRoomFreebusy",
        method="GET",
        url="https://open.feishu.cn/open-apis/meeting_room/freebusy/batch_get",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
