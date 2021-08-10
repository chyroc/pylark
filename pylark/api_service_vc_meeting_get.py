# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class GetVCMeetingReqUserIDType(object):
    pass


@attr.s
class GetVCMeetingReq(object):
    with_participants: bool = attr.ib(
        default=None, metadata={"req_type": "query"}
    )  # 是否需要参会人列表, 示例值：false
    with_meeting_ability: bool = attr.ib(
        default=None, metadata={"req_type": "query"}
    )  # 是否需要会中使用能力统计（仅限tenant_access_token）, 示例值：false
    user_id_type: GetVCMeetingReqUserIDType = attr.ib(
        default=None, metadata={"req_type": "query"}
    )  # 用户 ID 类型, 示例值："open_id", 可选值有: `open_id`：用户的 open id, `union_id`：用户的 union id, `user_id`：用户的 user id, 默认值: `open_id`, 当值为 `user_id`, 字段权限要求: 获取用户 userid
    meeting_id: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 会议ID（视频会议的唯一标识，视频会议开始后才会产生）, 示例值："6911188411932033028"


@attr.s
class GetVCMeetingRespMeetingAbility(object):
    use_video: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 是否使用视频
    use_audio: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 是否使用音频
    use_share_screen: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 是否使用共享屏幕
    use_follow_screen: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 是否使用妙享（magic share）
    use_recording: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 是否使用录制
    use_pstn: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 是否使用PSTN


@attr.s
class GetVCMeetingRespMeetingParticipant(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户ID
    user_type: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 用户类型, 可选值有: `1`：lark用户, `2`：rooms用户, `3`：文档用户, `4`：neo单品用户, `5`：neo单品游客用户, `6`：pstn用户, `7`：sip用户
    is_host: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 是否为主持人
    is_cohost: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 是否为联席主持人
    is_external: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 是否为外部参会人
    status: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 参会人状态, 可选值有: `1`：呼叫中, `2`：在会中, `3`：正在响铃, `4`：不在会中或已经离开会议


@attr.s
class GetVCMeetingRespMeetingHostUser(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户ID
    user_type: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 用户类型, 可选值有: `1`：lark用户, `2`：rooms用户, `3`：文档用户, `4`：neo单品用户, `5`：neo单品游客用户, `6`：pstn用户, `7`：sip用户


@attr.s
class GetVCMeetingRespMeeting(object):
    id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 会议ID（视频会议的唯一标识，视频会议开始后才会产生）
    topic: str = attr.ib(default="", metadata={"req_type": "json"})  # 会议主题
    url: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 会议链接（飞书用户可通过点击会议链接快捷入会）
    create_time: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 会议创建时间（unix时间，单位sec）
    start_time: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 会议开始时间（unix时间，单位sec）
    end_time: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 会议结束时间（unix时间，单位sec）
    host_user: GetVCMeetingRespMeetingHostUser = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 主持人
    status: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 会议状态, 可选值有: `1`：会议呼叫中, `2`：会议进行中, `3`：会议已结束
    participant_count: str = attr.ib(default="", metadata={"req_type": "json"})  # 参会人数
    participants: typing.List[GetVCMeetingRespMeetingParticipant] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 参会人列表
    ability: GetVCMeetingRespMeetingAbility = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 会中使用的能力


@attr.s
class GetVCMeetingResp(object):
    meeting: GetVCMeetingRespMeeting = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 会议数据


def _gen_get_vc_meeting_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetVCMeetingResp,
        scope="VC",
        api="GetVCMeeting",
        method="GET",
        url="https://open.feishu.cn/open-apis/vc/v1/meetings/:meeting_id",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        need_user_access_token=True,
    )
