# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class UpdateVCReserveReqMeetingSettingsCallSettingCalleePstnSipInfo(object):
    nickname: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "nickname"}
    )  # 给pstn/sip用户设置的临时昵称, 示例值："dodo"
    main_address: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "main_address"}
    )  # pstn/sip主机号，格式为：[国际冠字]-[电话区号][电话号码]，当前仅支持国内手机及固定电话号码, 示例值："+86-02187654321"


@attr.s
class UpdateVCReserveReqMeetingSettingsCallSettingCallee(object):
    id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "id"}
    )  # 用户ID, 示例值："ou_3ec3f6a28a0d08c45d895276e8e5e19b"
    user_type: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "user_type"}
    )  # 用户类型，当前仅支持用户类型6(pstn用户), 示例值：1, 可选值有: `1`：lark用户, `2`：rooms用户, `3`：文档用户, `4`：neo单品用户, `5`：neo单品游客用户, `6`：pstn用户, `7`：sip用户
    pstn_sip_info: UpdateVCReserveReqMeetingSettingsCallSettingCalleePstnSipInfo = (
        attr.ib(default=None, metadata={"req_type": "json", "key": "pstn_sip_info"})
    )  # pstn/sip信息


@attr.s
class UpdateVCReserveReqMeetingSettingsCallSetting(object):
    callee: UpdateVCReserveReqMeetingSettingsCallSettingCallee = attr.ib(
        default=None, metadata={"req_type": "json", "key": "callee"}
    )  # 被呼叫的用户


@attr.s
class UpdateVCReserveReqMeetingSettingsActionPermissionPermissionChecker(object):
    check_field: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "check_field"}
    )  # 检查字段类型, 示例值：1, 可选值有: `1`：用户ID, `2`：用户类型, `3`：租户ID
    check_mode: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "check_mode"}
    )  # 检查方式, 示例值：1, 可选值有: `1`：在check_list中为有权限（白名单）, `2`：不在check_list中为有权限（黑名单）
    check_list: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "check_list"}
    )  # 检查字段列表


@attr.s
class UpdateVCReserveReqMeetingSettingsActionPermission(object):
    permission: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "permission"}
    )  # 权限项, 示例值：1, 可选值有: `1`：是否能成为主持人, `2`：是否能邀请参会人, `3`：是否能加入会议
    permission_checkers: typing.List[
        UpdateVCReserveReqMeetingSettingsActionPermissionPermissionChecker
    ] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "permission_checkers"}
    )  # 权限检查器列表，权限检查器之间为"逻辑或"的关系（即 有一个为true则拥有该权限）


@attr.s
class UpdateVCReserveReqMeetingSettings(object):
    topic: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "topic"}
    )  # 会议主题, 示例值："my meeting"
    action_permissions: typing.List[
        UpdateVCReserveReqMeetingSettingsActionPermission
    ] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "action_permissions"}
    )  # 会议权限配置列表，如果存在相同的权限配置项则它们之间为"逻辑或"的关系（即 有一个为true则拥有该权限）
    meeting_initial_type: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "meeting_initial_type"}
    )  # 会议初始类型, 示例值：1, 可选值有: `1`：多人会议, `2`：1v1呼叫
    call_setting: UpdateVCReserveReqMeetingSettingsCallSetting = attr.ib(
        default=None, metadata={"req_type": "json", "key": "call_setting"}
    )  # 1v1呼叫相关参数


@attr.s
class UpdateVCReserveReqUserIDType(object):
    pass


@attr.s
class UpdateVCReserveReq(object):
    user_id_type: UpdateVCReserveReqUserIDType = attr.ib(
        default=None, metadata={"req_type": "query", "key": "user_id_type"}
    )  # 用户 ID 类型, 示例值："open_id", 可选值有: `open_id`：用户的 open id, `union_id`：用户的 union id, `user_id`：用户的 user id, 默认值: `open_id`, 当值为 `user_id`, 字段权限要求: 获取用户 user ID
    reserve_id: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "reserve_id"}
    )  # 预约ID（预约的唯一标识）, 示例值："6911188411932033028"
    end_time: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "end_time"}
    )  # 预约到期时间（unix时间，单位sec）, 示例值："1608888867"
    meeting_settings: UpdateVCReserveReqMeetingSettings = attr.ib(
        default=None, metadata={"req_type": "json", "key": "meeting_settings"}
    )  # 会议设置


@attr.s
class UpdateVCReserveRespReserve(object):
    id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "id"}
    )  # 预约ID（预约的唯一标识）
    meeting_no: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "meeting_no"}
    )  # 9位会议号（飞书用户可通过输入9位会议号快捷入会）
    url: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "url"}
    )  # 会议链接（飞书用户可通过点击会议链接快捷入会）
    end_time: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "end_time"}
    )  # 预约到期时间（unix时间，单位sec）
    expire_status: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "expire_status"}
    )  # 过期状态, 可选值有: `1`：未过期, `2`：已过期


@attr.s
class UpdateVCReserveResp(object):
    reserve: UpdateVCReserveRespReserve = attr.ib(
        default=None, metadata={"req_type": "json", "key": "reserve"}
    )  # 预约数据


def _gen_update_vc_reserve_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=UpdateVCReserveResp,
        scope="VC",
        api="UpdateVCReserve",
        method="PUT",
        url="https://open.feishu.cn/open-apis/vc/v1/reserves/:reserve_id",
        body=request,
        method_option=_new_method_option(options),
        need_user_access_token=True,
    )
