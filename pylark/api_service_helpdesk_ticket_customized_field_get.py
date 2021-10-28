# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class GetHelpdeskTicketCustomizedFieldReq(object):
    ticket_customized_field_id: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "ticket_customized_field_id"}
    )  # 工单自定义字段ID, 示例值："6948728206392295444"


@attr.s
class GetHelpdeskTicketCustomizedFieldRespUpdatedByDropdownOptionsChildrenChildren(
    object
):
    pass


@attr.s
class GetHelpdeskTicketCustomizedFieldRespUpdatedByDropdownOptionsChildren(object):
    tag: str = attr.ib(default="", metadata={"req_type": "json", "key": "tag"})  # 选项ID
    display_name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "display_name"}
    )  # 展示名称
    children: typing.List[
        GetHelpdeskTicketCustomizedFieldRespUpdatedByDropdownOptionsChildrenChildren
    ] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "children"}
    )  # 同上：选项列表，只适用于多层下拉列表（最多可以设置三级下拉列表）


@attr.s
class GetHelpdeskTicketCustomizedFieldRespUpdatedByDropdownOptions(object):
    children: GetHelpdeskTicketCustomizedFieldRespUpdatedByDropdownOptionsChildren = (
        attr.ib(default=None, metadata={"req_type": "json", "key": "children"})
    )  # 选项列表


@attr.s
class GetHelpdeskTicketCustomizedFieldRespUpdatedBy(object):
    id: str = attr.ib(default="", metadata={"req_type": "json", "key": "id"})  # 用户ID
    avatar_url: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "avatar_url"}
    )  # 用户头像url
    name: str = attr.ib(default="", metadata={"req_type": "json", "key": "name"})  # 用户名
    email: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "email"}
    )  # 用户邮箱
    dropdown_options: GetHelpdeskTicketCustomizedFieldRespUpdatedByDropdownOptions = (
        attr.ib(default=None, metadata={"req_type": "json", "key": "dropdown_options"})
    )  # 下拉列表选项


@attr.s
class GetHelpdeskTicketCustomizedFieldRespCreatedBy(object):
    id: str = attr.ib(default="", metadata={"req_type": "json", "key": "id"})  # 用户ID
    avatar_url: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "avatar_url"}
    )  # 用户头像url
    name: str = attr.ib(default="", metadata={"req_type": "json", "key": "name"})  # 用户名
    email: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "email"}
    )  # 用户邮箱


@attr.s
class GetHelpdeskTicketCustomizedFieldResp(object):
    ticket_customized_field_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "ticket_customized_field_id"}
    )  # 工单自定义字段ID
    helpdesk_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "helpdesk_id"}
    )  # 服务台ID
    key_name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "key_name"}
    )  # 键名
    display_name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "display_name"}
    )  # 名称
    position: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "position"}
    )  # 字段在列表后台管理列表中的位置
    field_type: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "field_type"}
    )  # 类型
    description: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "description"}
    )  # 描述
    visible: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json", "key": "visible"}
    )  # 是否可见
    editable: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json", "key": "editable"}
    )  # 是否可以修改
    required: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json", "key": "required"}
    )  # 是否必填
    created_at: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "created_at"}
    )  # 创建时间
    updated_at: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "updated_at"}
    )  # 更新时间
    created_by: GetHelpdeskTicketCustomizedFieldRespCreatedBy = attr.ib(
        default=None, metadata={"req_type": "json", "key": "created_by"}
    )  # 创建用户
    updated_by: GetHelpdeskTicketCustomizedFieldRespUpdatedBy = attr.ib(
        default=None, metadata={"req_type": "json", "key": "updated_by"}
    )  # 更新用户
    dropdown_allow_multiple: bool = attr.ib(
        factory=lambda: bool(),
        metadata={"req_type": "json", "key": "dropdown_allow_multiple"},
    )  # 是否支持多选，仅在字段类型是dropdown的时候有效


def _gen_get_helpdesk_ticket_customized_field_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetHelpdeskTicketCustomizedFieldResp,
        scope="Helpdesk",
        api="GetHelpdeskTicketCustomizedField",
        method="GET",
        url="https://open.feishu.cn/open-apis/helpdesk/v1/ticket_customized_fields/:ticket_customized_field_id",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        need_helpdesk_auth=True,
    )
