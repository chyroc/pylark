# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class GetDepartmentReqDepartmentIDType(object):
    pass


@attr.s
class GetDepartmentReqUserIDType(object):
    pass


@attr.s
class GetDepartmentReq(object):
    user_id_type: GetDepartmentReqUserIDType = attr.ib(
        default=None, metadata={"req_type": "query", "key": "user_id_type"}
    )  # 用户 ID 类型, 示例值："open_id", 可选值有: `open_id`：用户的 open id, `union_id`：用户的 union id, `user_id`：用户的 user id, 默认值: `open_id`, 当值为 `user_id`, 字段权限要求:  获取用户 user ID
    department_id_type: GetDepartmentReqDepartmentIDType = attr.ib(
        default=None, metadata={"req_type": "query", "key": "department_id_type"}
    )  # 此次调用中使用的部门ID的类型, 示例值："open_department_id", 可选值有: `department_id`：以自定义department_id来标识部门, `open_department_id`：以open_department_id来标识部门, 默认值: `open_department_id`
    department_id: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "department_id"}
    )  # 需要获取的部门ID, 示例值："od-4e6ac4d14bcd5071a37a39de902c7141", 最大长度：`64` 字符, 正则校验：`^0|[^od][A-Za-z0-9]*`


@attr.s
class GetDepartmentRespDepartmentStatus(object):
    is_deleted: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json", "key": "is_deleted"}
    )  # 是否被删除


@attr.s
class GetDepartmentRespDepartmentI18nName(object):
    zh_cn: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "zh_cn"}
    )  # 部门的中文名
    ja_jp: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "ja_jp"}
    )  # 部门的日文名
    en_us: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "en_us"}
    )  # 部门的英文名


@attr.s
class GetDepartmentRespDepartment(object):
    name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "name"}
    )  # 部门名称,**字段权限要求（满足任一）**：, 获取部门基础信息, 以应用身份读取通讯录
    i18n_name: GetDepartmentRespDepartmentI18nName = attr.ib(
        default=None, metadata={"req_type": "json", "key": "i18n_name"}
    )  # 国际化的部门名称,**字段权限要求（满足任一）**：, 获取部门基础信息, 以应用身份读取通讯录
    parent_department_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "parent_department_id"}
    )  # 父部门的ID,* 创建根部门，该参数值为 “0”,**字段权限要求（满足任一）**：, 获取部门组织架构信息, 以应用身份读取通讯录
    department_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "department_id"}
    )  # 本部门的自定义部门ID,**字段权限要求（满足任一）**：, 获取部门基础信息, 以应用身份读取通讯录
    open_department_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "open_department_id"}
    )  # 部门的open_id
    leader_user_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "leader_user_id"}
    )  # 部门主管用户ID,**字段权限要求（满足任一）**：, 获取部门组织架构信息, 以应用身份读取通讯录
    chat_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "chat_id"}
    )  # 部门群ID,**字段权限要求（满足任一）**：, 获取部门基础信息, 以应用身份读取通讯录
    order: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "order"}
    )  # 部门的排序，即部门在其同级部门的展示顺序,**字段权限要求（满足任一）**：, 获取部门组织架构信息, 以应用身份读取通讯录
    unit_ids: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "unit_ids"}
    )  # 部门单位自定义ID列表，当前只支持一个,**字段权限要求（满足任一）**：, 获取部门组织架构信息, 以应用身份读取通讯录
    member_count: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "member_count"}
    )  # 部门下用户的个数,**字段权限要求（满足任一）**：, 获取部门组织架构信息, 以应用身份读取通讯录
    status: GetDepartmentRespDepartmentStatus = attr.ib(
        default=None, metadata={"req_type": "json", "key": "status"}
    )  # 部门状态,**字段权限要求（满足任一）**：, 获取部门基础信息, 以应用身份读取通讯录


@attr.s
class GetDepartmentResp(object):
    department: GetDepartmentRespDepartment = attr.ib(
        default=None, metadata={"req_type": "json", "key": "department"}
    )  # 部门信息


def _gen_get_department_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetDepartmentResp,
        scope="Contact",
        api="GetDepartment",
        method="GET",
        url="https://open.feishu.cn/open-apis/contact/v3/departments/:department_id",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        need_user_access_token=True,
    )
