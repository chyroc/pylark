# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class GetVCMeetingRecordingReq(object):
    meeting_id: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "meeting_id"}
    )  # 会议ID（视频会议的唯一标识，视频会议开始后才会产生）, 示例值："6911188411932033028"


@attr.s
class GetVCMeetingRecordingRespRecording(object):
    url: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "url"}
    )  # 录制文件URL
    duration: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "duration"}
    )  # 录制总时长（单位msec）


@attr.s
class GetVCMeetingRecordingResp(object):
    recording: GetVCMeetingRecordingRespRecording = attr.ib(
        default=None, metadata={"req_type": "json", "key": "recording"}
    )  # 录制文件数据


def _gen_get_vc_meeting_recording_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetVCMeetingRecordingResp,
        scope="VC",
        api="GetVCMeetingRecording",
        method="GET",
        url="https://open.feishu.cn/open-apis/vc/v1/meetings/:meeting_id/recording",
        body=request,
        method_option=_new_method_option(options),
        need_user_access_token=True,
    )
