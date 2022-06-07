# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
from pylark import lark_type, lark_type_sheet, lark_type_approval
import attr
import typing
import io


@attr.s
class GetAttendanceUserApprovalReq(object):
    employee_type: lark_type.EmployeeType = attr.ib(
        factory=lambda: lark_type.EmployeeType(),
        metadata={"req_type": "query", "key": "employee_type"},
    )  # 请求体中的 user_ids 的员工工号类型，必选字段，可用值：【employee_id（员工的 employeeId），employee_no（员工工号）】，示例值："employee_id"
    user_ids: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "user_ids"}
    )  # employee_no 或 employee_id 列表
    check_date_from: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "check_date_from"}
    )  # 查询的起始工作日
    check_date_to: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "check_date_to"}
    )  # 查询的结束工作日，与 check_date_from 的时间间隔不超过30天


@attr.s
class GetAttendanceUserApprovalRespUserApprovalTrip(object):
    start_time: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "start_time"}
    )  # 开始时间，时间格式为 yyyy-MM-dd HH:mm:ss
    end_time: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "end_time"}
    )  # 结束时间，时间格式为 yyyy-MM-dd HH:mm:ss
    reason: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "reason"}
    )  # 出差理由
    approve_pass_time: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "approve_pass_time"}
    )  # 审批通过时间，时间格式为 yyyy-MM-dd HH:mm:ss
    approve_apply_time: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "approve_apply_time"}
    )  # 审批申请时间，时间格式为 yyyy-MM-dd HH:mm:ss


@attr.s
class GetAttendanceUserApprovalRespUserApprovalOvertimeWork(object):
    duration: float = attr.ib(
        default=None, metadata={"req_type": "json", "key": "duration"}
    )  # 加班时长
    unit: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "unit"}
    )  # 加班时长单位，可用值：【1（天），2（小时）】
    category: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "category"}
    )  # 加班日期类型，可用值：【1（工作日），2（休息日），3（节假日）】
    type: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "type"}
    )  # 加班规则类型，可用值：【0（不关联加班规则），1（调休），2（加班费）】
    start_time: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "start_time"}
    )  # 开始时间，时间格式为 yyyy-MM-dd HH:mm:ss
    end_time: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "end_time"}
    )  # 结束时间，时间格式为 yyyy-MM-dd HH:mm:ss


@attr.s
class GetAttendanceUserApprovalRespUserApprovalLeave(object):
    uniq_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "uniq_id"}
    )  # 假期类型唯一 ID，代表一种假期类型，长度小于 14
    unit: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "unit"}
    )  # 假期时长单位，可用值：【1（天），0（小时），4（分钟）】
    start_time: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "start_time"}
    )  # 开始时间，时间格式为 yyyy-MM-dd HH:mm:ss
    end_time: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "end_time"}
    )  # 结束时间，时间格式为 yyyy-MM-dd HH:mm:ss
    i18n_names: lark_type.I18nNames = attr.ib(
        default=None, metadata={"req_type": "json", "key": "i18n_names"}
    )  # 假期多语言展示，格式为 map，key 为["ch"、"en"、"ja"]，其中 ch 代表中文，en 代表英文、ja 代表日文
    default_locale: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "default_locale"}
    )  # 默认语言类型，由于飞书客户端支持中、英、日三种语言，当用户切换语言时，如果假期名称没有所对应语言的名称，则会使用默认语言的名称，可用值：【ch（中文），en（英文），ja（日文）】
    reason: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "reason"}
    )  # 请假理由
    approve_pass_time: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "approve_pass_time"}
    )  # 审批通过时间，时间格式为 yyyy-MM-dd HH:mm:ss
    approve_apply_time: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "approve_apply_time"}
    )  # 审批申请时间，时间格式为 yyyy-MM-dd HH:mm:ss


@attr.s
class GetAttendanceUserApprovalRespUserApprovalOut(object):
    uniq_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "uniq_id"}
    )  # 外出类型唯一 ID，代表一种外出类型，长度小于 14
    unit: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "unit"}
    )  # 外出时长单位，可用值：【1（天），2（小时），3（半天），4（半小时）】
    interval: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "interval"}
    )  # 外出时长（单位秒）
    start_time: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "start_time"}
    )  # 开始时间，时间格式为 yyyy-MM-dd HH:mm:ss
    end_time: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "end_time"}
    )  # 结束时间，时间格式为 yyyy-MM-dd HH:mm:ss
    i18n_names: lark_type.I18nNames = attr.ib(
        default=None, metadata={"req_type": "json", "key": "i18n_names"}
    )  # 外出多语言展示，格式为 map，key 为["ch"、"en"、"ja"]，其中 ch 代表中文，en 代表英文、ja 代表日文
    default_locale: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "default_locale"}
    )  # 默认语言类型，由于飞书客户端支持中、英、日三种语言，当用户切换语言时，如果外出名称没有所对应语言的名称，则会使用默认语言的名称
    reason: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "reason"}
    )  # 外出理由
    approve_pass_time: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "approve_pass_time"}
    )  # 审批通过时间
    approve_apply_time: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "approve_apply_time"}
    )  # 审批申请时间


@attr.s
class GetAttendanceUserApprovalRespUserApproval(object):
    user_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "user_id"}
    )  # 审批用户 ID
    date: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "date"}
    )  # 审批作用时间
    outs: typing.List[GetAttendanceUserApprovalRespUserApprovalOut] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "outs"}
    )  # 外出信息
    leaves: typing.List[GetAttendanceUserApprovalRespUserApprovalLeave] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "leaves"}
    )  # 请假信息
    overtime_works: typing.List[
        GetAttendanceUserApprovalRespUserApprovalOvertimeWork
    ] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "overtime_works"}
    )  # 加班信息
    trips: typing.List[GetAttendanceUserApprovalRespUserApprovalTrip] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "trips"}
    )  # 出差信息


@attr.s
class GetAttendanceUserApprovalResp(object):
    user_approvals: typing.List[GetAttendanceUserApprovalRespUserApproval] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "user_approvals"}
    )  # 审批结果列表


def _gen_get_attendance_user_approval_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetAttendanceUserApprovalResp,
        scope="Attendance",
        api="GetAttendanceUserApproval",
        method="POST",
        url="https://open.feishu.cn/open-apis/attendance/v1/user_approvals/query",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
