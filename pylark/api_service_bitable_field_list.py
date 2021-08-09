# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing


@attr.s
class GetBitableFieldListReq(object):
    view_id: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # 视图 ID, 示例值："vewOVMEXPF"
    page_token: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果, 示例值："fldwJ4YrtB"
    page_size: int = attr.ib(
        default=0, metadata={"req_type": "query"}
    )  # 分页大小, 示例值：10, 最大值：`100`
    app_token: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # bitable app token, 示例值："appbcbWCzen6D8dezhoCH2RpMAh"
    table_id: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # table id, 示例值："tblsRc9GRRXKqhvW"


@attr.s
class GetBitableFieldListRespItemPropertyOption(object):
    name: str = attr.ib(default="", metadata={"req_type": "json"})  # 选项名
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # 选项id


@attr.s
class GetBitableFieldListRespItemProperty(object):
    options: typing.List[GetBitableFieldListRespItemPropertyOption] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 单选/多选字段的选项信息
    formatter: str = attr.ib(default="", metadata={"req_type": "json"})  # 数字字段的数字显示格式
    date_format: str = attr.ib(default="", metadata={"req_type": "json"})  # 日期格式
    time_format: str = attr.ib(default="", metadata={"req_type": "json"})  # 时间格式
    auto_fill: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 是否自动填入创建时间
    multiple: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 多选标记
    table_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 关联字段中关联表的id
    view_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 关联字段中关联表的视图id
    fields: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 关联字段要展示的字段


@attr.s
class GetBitableFieldListRespItem(object):
    field_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 多维表格字段 id
    field_name: str = attr.ib(default="", metadata={"req_type": "json"})  # 多维表格字段名
    type: int = attr.ib(default=0, metadata={"req_type": "json"})  # 多维表格字段类型
    property: GetBitableFieldListRespItemProperty = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 字段属性, 具体参考: [Property说明](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/bitable/development-guide/bitable-structure#b286b4ee)


@attr.s
class GetBitableFieldListResp(object):
    has_more: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 是否还有更多项
    page_token: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token
    items: typing.List[GetBitableFieldListRespItem] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 字段信息


def _gen_get_bitable_field_list_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetBitableFieldListResp,
        scope="Bitable",
        api="GetBitableFieldList",
        method="GET",
        url="https://open.feishu.cn/open-apis/bitable/v1/apps/:app_token/tables/:table_id/fields",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )