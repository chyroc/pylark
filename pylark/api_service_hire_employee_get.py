# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class GetHireEmployeeReq(object):
    employee_id: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "employee_id"}
    )  # 员工ID, 示例值："123"


@attr.s
class GetHireEmployeeRespEmployee(object):
    id: str = attr.ib(default="", metadata={"req_type": "json", "key": "id"})  # 员工ID
    application_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "application_id"}
    )  # 投递ID
    onboard_status: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "onboard_status"}
    )  # 入职状态, 可选值有: `1`：已入职, `2`：已离职
    conversion_status: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "conversion_status"}
    )  # 转正状态, 可选值有: `1`：未转正, `2`：已转正
    onboard_time: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "onboard_time"}
    )  # 实际入职时间
    expected_conversion_time: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "expected_conversion_time"}
    )  # 预期转正时间
    actual_conversion_time: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "actual_conversion_time"}
    )  # 实际转正时间
    overboard_time: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "overboard_time"}
    )  # 离职时间
    overboard_note: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "overboard_note"}
    )  # 离职原因


@attr.s
class GetHireEmployeeResp(object):
    employee: GetHireEmployeeRespEmployee = attr.ib(
        default=None, metadata={"req_type": "json", "key": "employee"}
    )  # 员工信息


def _gen_get_hire_employee_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetHireEmployeeResp,
        scope="Hire",
        api="GetHireEmployee",
        method="GET",
        url="https://open.feishu.cn/open-apis/hire/v1/employees/:employee_id",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
