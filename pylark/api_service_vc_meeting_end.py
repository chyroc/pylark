# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing


@attr.s
class EndVCMeetingReq(object):
    meeting_id: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 会议ID（视频会议的唯一标识，视频会议开始后才会产生）, 示例值："6911188411932033028"


@attr.s
class EndVCMeetingResp(object):
    pass


def _gen_end_vc_meeting_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=EndVCMeetingResp,
        scope="VC",
        api="EndVCMeeting",
        method="PATCH",
        url="https://open.feishu.cn/open-apis/vc/v1/meetings/:meeting_id/end",
        body=request,
        method_option=_new_method_option(options),
    )
