# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
from pylark import lark_type_enum, lark_type_sheet
import attr
import typing
import io


@attr.s
class GetAttendanceStatisticsHeaderReqEmployeeType(object):
    pass


@attr.s
class GetAttendanceStatisticsHeaderReq(object):
    employee_type: GetAttendanceStatisticsHeaderReqEmployeeType = attr.ib(
        factory=lambda: GetAttendanceStatisticsHeaderReqEmployeeType(),
        metadata={"req_type": "query", "key": "employee_type"},
    )  # 用户 ID 类型, 可选值有: `employee_id`, `employee_no`
    locale: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "locale"}
    )  # 语言类型, 可选值有: `en`：英文, `ja`：日文, `zh`：中文
    stats_type: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "stats_type"}
    )  # 统计类型,      , **可选值有**：     , `daily`：日度统计, `month`：月度统计
    start_date: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "start_date"}
    )  # 开始时间, 示例值：20210316,      ,      （时间间隔不超过 40 天）
    end_date: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "end_date"}
    )  # 结束时间, 示例值：20210323


@attr.s
class GetAttendanceStatisticsHeaderRespUserStatsFieldFieldChildField(object):
    code: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "code"}
    )  # 字段编号
    title: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "title"}
    )  # 字段名称
    time_unit: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "time_unit"}
    )  # 时间类型


@attr.s
class GetAttendanceStatisticsHeaderRespUserStatsFieldField(object):
    code: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "code"}
    )  # 字段编号
    title: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "title"}
    )  # 字段标题
    child_fields: typing.List[
        GetAttendanceStatisticsHeaderRespUserStatsFieldFieldChildField
    ] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "child_fields"}
    )  # 子字段列表


@attr.s
class GetAttendanceStatisticsHeaderRespUserStatsField(object):
    stats_type: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "stats_type"}
    )  # 统计类型,    , 可选值有: `daily`：日度统计, `month`：月度统计
    user_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "user_id"}
    )  # 用户 ID
    fields: typing.List[GetAttendanceStatisticsHeaderRespUserStatsFieldField] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "fields"}
    )  # 字段列表


@attr.s
class GetAttendanceStatisticsHeaderResp(object):
    user_stats_field: GetAttendanceStatisticsHeaderRespUserStatsField = attr.ib(
        default=None, metadata={"req_type": "json", "key": "user_stats_field"}
    )  # 统计数据表头


def _gen_get_attendance_statistics_header_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetAttendanceStatisticsHeaderResp,
        scope="Attendance",
        api="GetAttendanceStatisticsHeader",
        method="POST",
        url="https://open.feishu.cn/open-apis/attendance/v1/user_stats_fields/query",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
