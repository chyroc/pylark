# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class BatchGetMeetingRoomSummaryReqEventUid(object):
    uid: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "uid"}
    )  # 日程的唯一id
    original_time: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "original_time"}
    )  # 日程实例原始时间，非重复日程必为0。若为0则表示回复其重复日程的名字（不包含重复日程中的单个例外），否则表示回复单个实例。


@attr.s
class BatchGetMeetingRoomSummaryReq(object):
    event_uids: BatchGetMeetingRoomSummaryReqEventUid = attr.ib(
        default=None, metadata={"req_type": "json", "key": "EventUids"}
    )  # 需要查询的日程Uid和Original time


@attr.s
class BatchGetMeetingRoomSummaryRespErrorEventUid(object):
    uid: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "uid"}
    )  # 日程的唯一id
    original_time: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "original_time"}
    )  # 日程实例原始时间，非重复日程必为0。若为0则表示回复其重复日程的名字（不包含重复日程中的单个例外），否则表示回复单个实例。
    error_msg: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "error_msg"}
    )  # 错误信息


@attr.s
class BatchGetMeetingRoomSummaryRespEventInfo(object):
    uid: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "uid"}
    )  # 日程的唯一id
    original_time: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "original_time"}
    )  # 日程实例原始时间，非重复日程必为0。重复日程若为0则表示回复其所有实例，否则表示回复单个实例。
    summary: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "summary"}
    )  # 日程主题


@attr.s
class BatchGetMeetingRoomSummaryResp(object):
    event_infos: BatchGetMeetingRoomSummaryRespEventInfo = attr.ib(
        default=None, metadata={"req_type": "json", "key": "EventInfos"}
    )  # 成功查询到的日程信息
    error_event_uids: BatchGetMeetingRoomSummaryRespErrorEventUid = attr.ib(
        default=None, metadata={"req_type": "json", "key": "ErrorEventUids"}
    )  # 没有查询到的日程


def _gen_batch_get_meeting_room_summary_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=BatchGetMeetingRoomSummaryResp,
        scope="MeetingRoom",
        api="BatchGetMeetingRoomSummary",
        method="POST",
        url="https://open.feishu.cn/open-apis/meeting_room/summary/batch_get",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
