# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
from pylark import lark_type_enum, lark_type_sheet
import attr
import typing
import io


@attr.s
class GetBitableRecordListReqUserIDType(object):
    pass


@attr.s
class GetBitableRecordListReq(object):
    view_id: str = attr.ib(
        default="", metadata={"req_type": "query", "key": "view_id"}
    )  # 视图 id, 如filter或sort有值, view_id会被忽略, 示例值："vewqhz51lk"
    filter: str = attr.ib(
        default="", metadata={"req_type": "query", "key": "filter"}
    )  # filter, 不超过2000个字符, 不支持对带特殊字段(关联和公式)的表的使用, 示例值："AND(CurrentValue.[身高]>180, CurrentValue.[体重]>150)"
    sort: str = attr.ib(
        default="", metadata={"req_type": "query", "key": "sort"}
    )  # sort, 不超过1000字符, 不支持对带特殊字段(关联和公式)的表的使用, 示例值："["字段1 DESC","字段2 ASC"]"
    field_names: str = attr.ib(
        default="", metadata={"req_type": "query", "key": "field_names"}
    )  # field_names, 示例值："["字段1"]"
    text_field_as_array: bool = attr.ib(
        default=None, metadata={"req_type": "query", "key": "text_field_as_array"}
    )  # 控制多行文本字段数据的返回格式, true 表示以数组形式返回, 示例值：true
    page_token: str = attr.ib(
        default="", metadata={"req_type": "query", "key": "page_token"}
    )  # 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果, 示例值："recn0hoyXL"
    page_size: int = attr.ib(
        default=0, metadata={"req_type": "query", "key": "page_size"}
    )  # 分页大小, 示例值：10, 最大值：`100`
    user_id_type: lark_type_enum.IDType = attr.ib(
        default=None, metadata={"req_type": "query", "key": "user_id_type"}
    )  # 用户 ID 类型, 示例值："open_id", 可选值有: `open_id`：用户的 open id, `union_id`：用户的 union id, `user_id`：用户的 user id, 默认值: `open_id`, 当值为 `user_id`, 字段权限要求:  获取用户 user ID
    app_token: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "app_token"}
    )  # bitable app token, 示例值："bascnCMII2ORej2RItqpZZUNMIe"
    table_id: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "table_id"}
    )  # table id, 示例值："tblxI2tWaxP5dG7p"


@attr.s
class GetBitableRecordListRespItemFieldsValue(object):
    pass


@attr.s
class GetBitableRecordListRespItemFields(object):
    key: str = attr.ib(default="", metadata={"req_type": "json", "key": "key"})  # 字段名
    value: typing.Any = attr.ib(
        default=None, metadata={"req_type": "json", "key": "value"}
    )  # 内容


@attr.s
class GetBitableRecordListRespItem(object):
    record_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "record_id"}
    )  # 记录 id
    fields: GetBitableRecordListRespItemFields = attr.ib(
        factory=lambda: GetBitableRecordListRespItemFields(),
        metadata={"req_type": "json", "key": "fields"},
    )  # 记录字段


@attr.s
class GetBitableRecordListResp(object):
    has_more: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json", "key": "has_more"}
    )  # 是否还有更多项
    page_token: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "page_token"}
    )  # 分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token
    total: int = attr.ib(default=0, metadata={"req_type": "json", "key": "total"})  # 总数
    items: typing.List[GetBitableRecordListRespItem] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "items"}
    )  # 记录信息


def _gen_get_bitable_record_list_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetBitableRecordListResp,
        scope="Bitable",
        api="GetBitableRecordList",
        method="GET",
        url="https://open.feishu.cn/open-apis/bitable/v1/apps/:app_token/tables/:table_id/records",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        need_user_access_token=True,
    )
