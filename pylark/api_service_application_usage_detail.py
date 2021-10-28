# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
from pylark import lark_type_enum, lark_type_sheet
import attr
import typing
import io


@attr.s
class GetApplicationUsageDetailReqFilter(object):
    key: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "key"}
    )  # 过滤字段，支持`department_id`
    op: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "op"}
    )  # 过滤操作，支持`in`、`=`
    value: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "value"}
    )  # 过滤字段值，多个使用英文逗号分隔


@attr.s
class GetApplicationUsageDetailReq(object):
    app_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "app_id"}
    )  # 目标应用的 ID，支持自建应用
    ability: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "ability"}
    )  # 应用能力，mp：小程序
    time_start: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "time_start"}
    )  # 起始时间戳（秒），时间跨度最长支持180天
    time_end: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "time_end"}
    )  # 截止时间戳（秒），时间跨度最长支持180天
    filters: typing.List[GetApplicationUsageDetailReqFilter] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "filters"}
    )  # 过滤条件
    order_by: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "order_by"}
    )  # 排序字段，大小写不敏感，支持open_id、timestamp，默认为open_id
    order: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "order"}
    )  # 排序方式，大小写不敏感，desc：降序；asc：升序，默认值
    page_token: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "page_token"}
    )  # 分页标记，首次传空，非首次使用返回中的page_token
    page_size: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "page_size"}
    )  # 分页大小，默认为512，取值区间[1,1000]


@attr.s
class GetApplicationUsageDetailRespUser(object):
    open_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "open_id"}
    )  # open_id


@attr.s
class GetApplicationUsageDetailResp(object):
    has_more: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json", "key": "has_more"}
    )  # 是否还有更多分页，当 has_more 为 true 时，会同时返回新的 page_token
    page_token: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "page_token"}
    )  # 分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token
    users: typing.List[GetApplicationUsageDetailRespUser] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "users"}
    )  # 用户列表


def _gen_get_application_usage_detail_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetApplicationUsageDetailResp,
        scope="Application",
        api="GetApplicationUsageDetail",
        method="POST",
        url="https://open.feishu.cn/open-apis/application/v1/app_usage_detail",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
