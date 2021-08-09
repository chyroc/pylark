# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing


@attr.s
class UpdateHelpdeskTicketCustomizedFieldReqDropdownOptionsChildrenTagChildren(object):
    pass


@attr.s
class UpdateHelpdeskTicketCustomizedFieldReqDropdownOptionsChildrenTag(object):
    display_name: str = attr.ib(default="", metadata={"req_type": "json"})  # 展示名称
    children: dropdown_option = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 同上：选项列表，只适用于多层下拉列表（最多可以设置三级下拉列表）


@attr.s
class UpdateHelpdeskTicketCustomizedFieldReqDropdownOptionsChildren(object):
    tag: UpdateHelpdeskTicketCustomizedFieldReqDropdownOptionsChildrenTag = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 选项ID


@attr.s
class UpdateHelpdeskTicketCustomizedFieldReqDropdownOptions(object):
    children: UpdateHelpdeskTicketCustomizedFieldReqDropdownOptionsChildren = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 选项列表


@attr.s
class UpdateHelpdeskTicketCustomizedFieldReq(object):
    ticket_customized_field_id: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 工单自定义字段ID, 示例值："6948728206392295444"
    display_name: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 名称, 示例值："test dropdown"
    position: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 字段在列表后台管理列表中的位置, 示例值："3"
    description: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 描述, 示例值："下拉示例"
    visible: bool = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 是否可见, 示例值：true
    required: bool = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 是否必填, 示例值：false
    dropdown_options: HelpdeskDropdownOption = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 下拉列表选项


@attr.s
class UpdateHelpdeskTicketCustomizedFieldResp(object):
    pass


def _gen_update_helpdesk_ticket_customized_field_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=UpdateHelpdeskTicketCustomizedFieldResp,
        scope="Helpdesk",
        api="UpdateHelpdeskTicketCustomizedField",
        method="PATCH",
        url="https://open.feishu.cn/open-apis/helpdesk/v1/ticket_customized_fields/:ticket_customized_field_id",
        body=request,
        method_option=_new_method_option(options),
    )