import typing

import attr


@attr.s
class HelpdeskDropdownOption(object):
    """下拉列表选项"""

    tag: str = attr.ib(default="", metadata={"req_type": "json", "key": "tag"})  # 选项ID
    display_name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "display_name"}
    )  # 展示名称
    children: typing.List["HelpdeskDropdownOption"] = attr.ib(
        factory=list, metadata={"req_type": "json", "key": "children"}
    )  # 同上：选项列表，只适用于多层下拉列表（最多可以设置三级下拉列表）
