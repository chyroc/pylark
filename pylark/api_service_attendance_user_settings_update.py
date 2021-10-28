# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
from pylark import lark_type_enum, lark_type_sheet
import attr
import typing
import io


@attr.s
class UpdateAttendanceUserSettingsReqUserSetting(object):
    user_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "user_id"}
    )  # 用户 ID
    face_key: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "face_key"}
    )  # 人脸照片 key（通过文件上传接口得到）


@attr.s
class UpdateAttendanceUserSettingsReqEmployeeType(object):
    pass


@attr.s
class UpdateAttendanceUserSettingsReq(object):
    employee_type: UpdateAttendanceUserSettingsReqEmployeeType = attr.ib(
        factory=lambda: UpdateAttendanceUserSettingsReqEmployeeType(),
        metadata={"req_type": "query", "key": "employee_type"},
    )  # 用户类型,      , 可选值有: `employee_id`： 员工 ID, `employee_no`： 员工工号
    user_setting: UpdateAttendanceUserSettingsReqUserSetting = attr.ib(
        default=None, metadata={"req_type": "json", "key": "user_setting"}
    )  # 用户信息


@attr.s
class UpdateAttendanceUserSettingsRespUserSetting(object):
    user_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "user_id"}
    )  # 用户 ID
    face_key: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "face_key"}
    )  # 人脸照片 key


@attr.s
class UpdateAttendanceUserSettingsResp(object):
    user_setting: UpdateAttendanceUserSettingsRespUserSetting = attr.ib(
        default=None, metadata={"req_type": "json", "key": "user_setting"}
    )  # 用户设置


def _gen_update_attendance_user_settings_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=UpdateAttendanceUserSettingsResp,
        scope="Attendance",
        api="UpdateAttendanceUserSettings",
        method="POST",
        url="https://open.feishu.cn/open-apis/attendance/v1/user_settings/modify",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
