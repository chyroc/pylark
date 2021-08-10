# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class GetAttendanceUserTaskRemedyReqEmployeeType(object):
    pass


@attr.s
class GetAttendanceUserTaskRemedyReq(object):
    employee_type: GetAttendanceUserTaskRemedyReqEmployeeType = attr.ib(
        factory=lambda: GetAttendanceUserTaskRemedyReqEmployeeType(),
        metadata={"req_type": "query"},
    )  # 请求体中的 user_id 的员工工号类型，可用值：【employee_id（员工的 employeeId），employee_no（员工工号）】，示例值：“employee_id”
    user_ids: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # employee_no 或 employee_id 列表
    check_time_from: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 查询的起始时间，精确到秒的时间戳
    check_time_to: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 查询的结束时间，精确到秒的时间戳


@attr.s
class GetAttendanceUserTaskRemedyRespUserRemedy(object):
    user_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 员工工号
    status: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 补卡状态，可用值：【0（pending），2（已通过），3（已取消），4（通过后撤销）】
    reason: str = attr.ib(default="", metadata={"req_type": "json"})  # 补卡原因
    time: str = attr.ib(default="", metadata={"req_type": "json"})  # 补卡时间，精确到秒的时间戳
    time_zone: str = attr.ib(default="", metadata={"req_type": "json"})  # 补卡时的考勤组时区
    create_time: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 补卡发起时间，精确到秒的时间戳
    update_time: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 补卡状态更新时间，精确到秒的时间戳


@attr.s
class GetAttendanceUserTaskRemedyResp(object):
    user_remedys: typing.List[GetAttendanceUserTaskRemedyRespUserRemedy] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 补卡记录列表


def _gen_get_attendance_user_task_remedy_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetAttendanceUserTaskRemedyResp,
        scope="Attendance",
        api="GetAttendanceUserTaskRemedy",
        method="POST",
        url="https://open.feishu.cn/open-apis/attendance/v1/user_task_remedys/query",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
