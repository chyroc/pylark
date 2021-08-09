# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing


@attr.s
class DeleteEmployeeTypeEnumReq(object):
    enum_id: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 枚举值id, 示例值："exGeIjow7zIqWMy+ONkFxA=="


@attr.s
class DeleteEmployeeTypeEnumResp(object):
    pass


def _gen_delete_employee_type_enum_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=DeleteEmployeeTypeEnumResp,
        scope="Contact",
        api="DeleteEmployeeTypeEnum",
        method="DELETE",
        url="https://open.feishu.cn/open-apis/contact/v3/employee_type_enums/:enum_id",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )