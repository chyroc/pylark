import typing
from enum import Enum

import attr


class ApprovalWidgetType(Enum):
    input = "input"  # 单行文本
    textarea = "textarea"  # 多行文本
    text = "text"  # 说明
    number = "number"  # 数字
    amount = "amount"  # 金额
    date = "date"  # 日期
    date_interval = "dateInterval"  # 日期区间
    field_list = "fieldList"  # 明细
    formula = "formula"  # 计算公式
    radio = "radio"  # 单选
    radio_v2 = "radioV2"  # 单选
    checkbox = "checkbox"  # 多选
    checkbox_v2 = "checkboxV2"  # 多选
    attachment = "attachement"  # 附件
    attachment_v2 = "attachmentV2"  # 附件
    department = "department"  # 部门
    image = "image"  # 图片
    image_v2 = "imageV2"  # 图片
    contact = "contact"  # 联系人
    connect = "connect"  # 关联审批
    address = "address"  # 地址
    leave_group = "leaveGroup"  # 请假控件组
    work_group = "workGroup"  # 加班控件组
    shift_group = "shiftGroup"  # 换班控件组
    remedy_group = "remedyGroup"  # 补卡控件组
    trip_group = "tripGroup"  # 出差控件组
    out_group = "outGroup"  # 外出控件组


@attr.s
class ApprovalWidget(object):
    id: str = attr.ib(default="", metadata={"req_type": "json", "key": "id"})
    name: str = attr.ib(default="", metadata={"req_type": "json", "key": "name"})
    type: ApprovalWidgetType = attr.ib(
        default=None, metadata={"req_type": "json", "key": "type"}
    )
    value: typing.Any = attr.ib(
        default=None, metadata={"req_type": "json", "key": "value"}
    )
    option: str = attr.ib(default="", metadata={"req_type": "json", "key": "option"})
    children: typing.List["ApprovalWidget"] = attr.ib(
        default=list, metadata={"req_type": "json", "key": "children"}
    )
    # Option   *ApprovalWidgetOptions `json:"option,omitempty"`


@attr.s
class ApprovalWidgetOption(object):
    key = attr.ib(default="", metadata={"req_type": "json", "key": "key"})
    value = attr.ib(default="", metadata={"req_type": "json", "key": "value"})
    text = attr.ib(default="", metadata={"req_type": "json", "key": "text"})


@attr.s
class ApprovalWidgetList(object):
    pass
