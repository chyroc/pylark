# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class GetUserListReqDepartmentIDType(object):
    pass


@attr.s
class GetUserListReqUserIDType(object):
    pass


@attr.s
class GetUserListReq(object):
    user_id_type: GetUserListReqUserIDType = attr.ib(
        default=None, metadata={"req_type": "query"}
    )  # 用户 ID 类型, 示例值："open_id", 可选值有: `open_id`：用户的 open id, `union_id`：用户的 union id, `user_id`：用户的 user id, 默认值: `open_id`, 当值为 `user_id`, 字段权限要求:  获取用户 user ID
    department_id_type: GetUserListReqDepartmentIDType = attr.ib(
        default=None, metadata={"req_type": "query"}
    )  # 此次调用中使用的部门ID的类型, 示例值："open_department_type", 可选值有: `department_id`：以自定义department_id来标识部门, `open_department_id`：以open_department_id来标识部门, 默认值: `open_department_id`
    department_id: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # 填写该字段表示获取部门下所有用户，选填。, 示例值："od-xxxxxxxxxxxxx"
    page_token: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果, 示例值："AQD9/Rn9eij9Pm39ED40/dk53s4Ebp882DYfFaPFbz00L4CMZJrqGdzNyc8BcZtDbwVUvRmQTvyMYicnGWrde9X56TgdBuS%2BJKiSIkdexPw="
    page_size: int = attr.ib(
        default=0, metadata={"req_type": "query"}
    )  # 分页大小, 示例值：10, 最大值：`50`


@attr.s
class GetUserListRespItemCustomAttrValueGenericUser(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户的user_id
    type: int = attr.ib(default=0, metadata={"req_type": "json"})  # 用户类型    1：用户


@attr.s
class GetUserListRespItemCustomAttrValue(object):
    text: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 字段类型为 TEXT 时该参数定义字段值，字段类型为 HREF 时该参数定义网页标题
    url: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 字段类型为 HREF 时，该参数定义默认 URL
    pc_url: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 字段类型为 HREF 时，该参数定义PC端 URL
    option_value: str = attr.ib(default="", metadata={"req_type": "json"})  # 选项值
    name: str = attr.ib(default="", metadata={"req_type": "json"})  # 名称
    picture_url: str = attr.ib(default="", metadata={"req_type": "json"})  # 图片链接
    generic_user: GetUserListRespItemCustomAttrValueGenericUser = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 字段类型为 GENERIC_USER 时，该参数定义引用人员


@attr.s
class GetUserListRespItemCustomAttr(object):
    type: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 自定义字段类型   , `TEXT`：文本, `HREF`：网页, `ENUMERATION`：枚举, `PICTURE_ENUM`：图片, `GENERIC_USER`：用户
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # 自定义字段ID
    value: GetUserListRespItemCustomAttrValue = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 自定义字段取值


@attr.s
class GetUserListRespItemOrder(object):
    department_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 排序信息对应的部门ID, ID值与查询参数中的department_id_type 对应。,不同 ID 的说明参见 [部门ID说明](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/department/field-overview)
    user_order: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 用户在其直属部门内的排序，数值越大，排序越靠前
    department_order: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 用户所属的多个部门间的排序，数值越大，排序越靠前


@attr.s
class GetUserListRespItemStatus(object):
    is_frozen: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 是否暂停
    is_resigned: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 是否离职
    is_activated: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 是否激活


@attr.s
class GetUserListRespItemAvatar(object):
    avatar_72: str = attr.ib(default="", metadata={"req_type": "json"})  # 72*72像素头像链接
    avatar_240: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 240*240像素头像链接
    avatar_640: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 640*640像素头像链接
    avatar_origin: str = attr.ib(default="", metadata={"req_type": "json"})  # 原始头像链接


@attr.s
class GetUserListRespItem(object):
    union_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 用户的union_id，不同ID的说明参见 [用户相关的 ID 概念](https://open.feishu.cn/document/home/user-identity-introduction/introduction)
    user_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 租户内用户的唯一标识，ID值与查询参数中的user_id_type 对应。,不同 ID 的说明参见 [用户相关的 ID 概念](https://open.feishu.cn/document/home/user-identity-introduction/introduction), 字段权限要求:  获取用户 user ID
    open_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 用户的open_id，不同ID的说明参见 [用户相关的 ID 概念](https://open.feishu.cn/document/home/user-identity-introduction/introduction)
    name: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 用户名,**字段权限要求（满足任一）**：, 获取用户基本信息, 以应用身份读取通讯录
    en_name: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 英文名,**字段权限要求（满足任一）**：, 获取用户基本信息, 以应用身份读取通讯录
    email: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 邮箱, 字段权限要求:  获取用户邮箱信息
    mobile: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 手机号, 字段权限要求:  获取用户手机号
    mobile_visible: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 手机号码可见性，true 为可见，false 为不可见，目前默认为 true。不可见时，组织员工将无法查看该员工的手机号码
    gender: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 性别, 可选值有: `0`：保密, `1`：男, `2`：女,**字段权限要求（满足任一）**：, 获取用户性别, 以应用身份读取通讯录
    avatar: GetUserListRespItemAvatar = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 用户头像信息,**字段权限要求（满足任一）**：, 获取用户基本信息, 以应用身份读取通讯录
    status: GetUserListRespItemStatus = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 用户状态,**字段权限要求（满足任一）**：, 获取用户雇佣信息, 以应用身份读取通讯录
    department_ids: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 用户所属部门的ID列表，一个用户可属于多个部门。,ID值与查询参数中的department_id_type 对应。,不同 ID 的说明参见 [部门ID说明](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/department/field-overview#23857fe0),**字段权限要求（满足任一）**：, 获取用户组织架构信息, 以应用身份读取通讯录
    leader_user_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 用户的直接主管的用户ID，ID值与查询参数中的user_id_type 对应。,不同 ID 的说明参见 [用户相关的 ID 概念](https://open.feishu.cn/document/home/user-identity-introduction/introduction),**字段权限要求（满足任一）**：, 获取用户组织架构信息, 以应用身份读取通讯录
    city: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 城市,**字段权限要求（满足任一）**：, 获取用户雇佣信息, 以应用身份读取通讯录
    country: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 国家或地区Code缩写，具体写入格式请参考 [国家/地区码表](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/user/country-code-description),**字段权限要求（满足任一）**：, 获取用户雇佣信息, 以应用身份读取通讯录
    work_station: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 工位,**字段权限要求（满足任一）**：, 获取用户雇佣信息, 以应用身份读取通讯录
    join_time: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 入职时间,**字段权限要求（满足任一）**：, 获取用户雇佣信息, 以应用身份读取通讯录
    is_tenant_manager: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 是否是租户超级管理员,**字段权限要求（满足任一）**：, 获取用户雇佣信息, 以应用身份读取通讯录
    employee_no: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 工号,**字段权限要求（满足任一）**：, 获取用户雇佣信息, 以应用身份读取通讯录
    employee_type: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 员工类型，可选值有：, `1`：正式员工, `2`：实习生, `3`：外包, `4`：劳务, `5`：顾问   ,同时可读取到自定义员工类型的 int 值，可通过下方接口获取到该租户的自定义员工类型的名称   ,[获取人员类型](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/employee_type_enum/list),**字段权限要求（满足任一）**：, 获取用户雇佣信息, 以应用身份读取通讯录
    orders: typing.List[GetUserListRespItemOrder] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 用户排序信息,**字段权限要求（满足任一）**：, 获取用户组织架构信息, 以应用身份读取通讯录
    custom_attrs: typing.List[GetUserListRespItemCustomAttr] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 自定义字段，请确保你的组织管理员已在管理后台/组织架构/成员字段管理/自定义字段管理/全局设置中开启了“允许开放平台 API 调用“，否则该字段不会生效/返回。,**字段权限要求（满足任一）**：, 获取用户雇佣信息, 以应用身份读取通讯录
    enterprise_email: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 企业邮箱，请先确保已在管理后台启用飞书邮箱服务,**字段权限要求（满足任一）**：, 获取用户雇佣信息, 以应用身份读取通讯录
    job_title: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 职务,**字段权限要求（满足任一）**：, 获取用户雇佣信息, 以应用身份读取通讯录


@attr.s
class GetUserListResp(object):
    has_more: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 是否还有更多项
    page_token: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token
    items: typing.List[GetUserListRespItem] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # -


def _gen_get_user_list_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetUserListResp,
        scope="Contact",
        api="GetUserList",
        method="GET",
        url="https://open.feishu.cn/open-apis/contact/v3/users",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        need_user_access_token=True,
    )
