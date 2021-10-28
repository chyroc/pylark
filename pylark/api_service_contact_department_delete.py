# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class DeleteDepartmentReqDepartmentIDType(object):
    pass


@attr.s
class DeleteDepartmentReq(object):
    department_id_type: DeleteDepartmentReqDepartmentIDType = attr.ib(
        default=None, metadata={"req_type": "query"}
    )  # 此次调用中使用的部门ID的类型, 示例值："open_department_id", 可选值有: `department_id`：以自定义department_id来标识部门, `open_department_id`：以open_department_id来标识部门, 默认值: `open_department_id`
    department_id: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 部门ID，需要与查询参数中传入的department_id_type类型保持一致。, 示例值："od-4e6ac4d14bcd5071a37a39de902c7141", 最大长度：`64` 字符, 正则校验：`^0|[^od][A-Za-z0-9]*`


@attr.s
class DeleteDepartmentResp(object):
    pass


def _gen_delete_department_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=DeleteDepartmentResp,
        scope="Contact",
        api="DeleteDepartment",
        method="DELETE",
        url="https://open.feishu.cn/open-apis/contact/v3/departments/:department_id",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
