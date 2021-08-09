# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing


@attr.s
class GetHelpdeskTicketCustomizedFieldListReq(object):
    page_token: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果, 示例值："6948728206392295444"
    page_size: int = attr.ib(
        default=0, metadata={"req_type": "query"}
    )  # 分页大小, 示例值：10；默认为20, 最大值：`100`
    visible: bool = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 是否可见, 示例值：true


@attr.s
class GetHelpdeskTicketCustomizedFieldListRespItemDropdownOptionsChildrenChildren(
    object
):
    pass


@attr.s
class GetHelpdeskTicketCustomizedFieldListRespItemDropdownOptionsChildren(object):
    tag: str = attr.ib(default="", metadata={"req_type": "json"})  # 选项ID
    display_name: str = attr.ib(default="", metadata={"req_type": "json"})  # 展示名称
    children: typing.List[dropdown_option] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 同上：选项列表，只适用于多层下拉列表（最多可以设置三级下拉列表）


@attr.s
class GetHelpdeskTicketCustomizedFieldListRespItemDropdownOptions(object):
    children: GetHelpdeskTicketCustomizedFieldListRespItemDropdownOptionsChildren = (
        attr.ib(default=None, metadata={"req_type": "json"})
    )  # 选项列表


@attr.s
class GetHelpdeskTicketCustomizedFieldListRespItemUpdatedBy(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户ID
    avatar_url: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户头像url
    name: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户名
    email: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户邮箱


@attr.s
class GetHelpdeskTicketCustomizedFieldListRespItemCreatedBy(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户ID
    avatar_url: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户头像url
    name: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户名
    email: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户邮箱


@attr.s
class GetHelpdeskTicketCustomizedFieldListRespItem(object):
    ticket_customized_field_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 工单自定义字段ID
    helpdesk_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 服务台ID
    key_name: str = attr.ib(default="", metadata={"req_type": "json"})  # 键名
    display_name: str = attr.ib(default="", metadata={"req_type": "json"})  # 名称
    position: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 字段在列表后台管理列表中的位置
    field_type: str = attr.ib(default="", metadata={"req_type": "json"})  # 类型
    description: str = attr.ib(default="", metadata={"req_type": "json"})  # 描述
    visible: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 是否可见
    editable: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 是否可以修改
    required: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 是否必填
    created_at: str = attr.ib(default="", metadata={"req_type": "json"})  # 创建时间
    updated_at: str = attr.ib(default="", metadata={"req_type": "json"})  # 更新时间
    created_by: GetHelpdeskTicketCustomizedFieldListRespItemCreatedBy = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 创建用户
    updated_by: GetHelpdeskTicketCustomizedFieldListRespItemUpdatedBy = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 更新用户
    dropdown_options: HelpdeskDropdownOption = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 下拉列表选项
    dropdown_allow_multiple: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 是否支持多选，仅在字段类型是dropdown的时候有效


@attr.s
class GetHelpdeskTicketCustomizedFieldListResp(object):
    has_more: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 是否还有更多项
    next_page_token: str = attr.ib(default="", metadata={"req_type": "json"})  # 下一分页标识
    items: typing.List[GetHelpdeskTicketCustomizedFieldListRespItem] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 工单自定义字段列表


def _gen_get_helpdesk_ticket_customized_field_list_req(
    request, options
) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetHelpdeskTicketCustomizedFieldListResp,
        scope="Helpdesk",
        api="GetHelpdeskTicketCustomizedFieldList",
        method="GET",
        url="https://open.feishu.cn/open-apis/helpdesk/v1/ticket_customized_fields",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
