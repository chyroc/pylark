# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing


@attr.s
class GetApplicationUserAdminScopeReq(object):
    employee_id: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # 支持通过 open_id 或者 employee_id 查询，不支持混合两种 ID 进行查询，其中 employee_id 同通讯录 v3 版本中的 user_id
    open_id: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # 支持通过 open_id 或者 employee_id 查询，不支持混合两种 ID 进行查询，其中 employee_id 同通讯录 v3 版本中的 user_id


@attr.s
class GetApplicationUserAdminScopeResp(object):
    is_all: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 是否管理所有部门
    department_list: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 管理的部门列表，当 is_all 为 true 时，不返回该字段


def _gen_get_application_user_admin_scope_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetApplicationUserAdminScopeResp,
        scope="Application",
        api="GetApplicationUserAdminScope",
        method="GET",
        url="https://open.feishu.cn/open-apis/contact/v1/user/admin_scope/get",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
