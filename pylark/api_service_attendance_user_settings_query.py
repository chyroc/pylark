# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
from pylark import lark_type_enum, lark_type_sheet
import attr
import typing
import io


@attr.s
class QueryAttendanceUserSettingsReqEmployeeType(object):
    pass


@attr.s
class QueryAttendanceUserSettingsReq(object):
    employee_type: QueryAttendanceUserSettingsReqEmployeeType = attr.ib(
        factory=lambda: QueryAttendanceUserSettingsReqEmployeeType(),
        metadata={"req_type": "query", "key": "employee_type"},
    )  # 请求体中的 user_ids 的员工工号类型，可用值：【employee_id（员工的 employeeId），employee_no（员工工号）】，示例值：“employee_id”
    user_ids: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "user_ids"}
    )  # employee_no 或 employee_id 列表，长度不超过 100


@attr.s
class QueryAttendanceUserSettingsRespUserSetting(object):
    user_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "user_id"}
    )  # 员工工号
    face_key: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "face_key"}
    )  # 人脸照片文件 ID
    face_key_update_time: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "face_key_update_time"}
    )  # 人脸照片更新时间，精确到秒的时间戳


@attr.s
class QueryAttendanceUserSettingsResp(object):
    user_settings: typing.List[QueryAttendanceUserSettingsRespUserSetting] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "user_settings"}
    )  # 用户设置信息列表


def _gen_query_attendance_user_settings_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=QueryAttendanceUserSettingsResp,
        scope="Attendance",
        api="QueryAttendanceUserSettings",
        method="GET",
        url="https://open.feishu.cn/open-apis/attendance/v1/user_settings/query",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
