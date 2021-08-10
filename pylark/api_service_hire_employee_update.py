# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class UpdateHireEmployeeReqOverboardInfo(object):
    actual_overboard_time: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 实际离职日期, 示例值：1637596800000
    overboard_note: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 离职原因, 示例值："职业发展考虑"


@attr.s
class UpdateHireEmployeeReqConversionInfo(object):
    actual_conversion_time: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 实际转正日期, 示例值：1637596800000


@attr.s
class UpdateHireEmployeeReq(object):
    employee_id: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 员工ID, 示例值："123"
    operation: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 修改状态操作, 示例值：1, 可选值有: `1`：转正, `2`：离职
    conversion_info: UpdateHireEmployeeReqConversionInfo = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 转正信息
    overboard_info: UpdateHireEmployeeReqOverboardInfo = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 离职信息


@attr.s
class UpdateHireEmployeeRespEmployee(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # 员工ID
    application_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 投递ID
    onboard_status: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 入职状态, 可选值有: `1`：已入职, `2`：已离职
    conversion_status: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 转正状态, 可选值有: `1`：未转正, `2`：已转正
    onboard_time: int = attr.ib(default=0, metadata={"req_type": "json"})  # 实际入职时间
    expected_conversion_time: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 预期转正时间
    actual_conversion_time: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 实际转正时间
    overboard_time: int = attr.ib(default=0, metadata={"req_type": "json"})  # 离职时间
    overboard_note: str = attr.ib(default="", metadata={"req_type": "json"})  # 离职原因


@attr.s
class UpdateHireEmployeeResp(object):
    employee: UpdateHireEmployeeRespEmployee = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 员工信息


def _gen_update_hire_employee_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=UpdateHireEmployeeResp,
        scope="Hire",
        api="UpdateHireEmployee",
        method="PATCH",
        url="https://open.feishu.cn/open-apis/hire/v1/employees/:employee_id",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
