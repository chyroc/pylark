# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing


@attr.s
class UpdateSearchDataSourceReq(object):
    data_source_id: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 数据源的唯一标识, 示例值："service_ticket"
    name: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 数据源的展示名称, 示例值："客服工单"
    state: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 数据源状态，0-未上线，1-已上线, 示例值：0, 可选值有: `0`：未上线, `1`：已上线
    description: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 对于数据源的描述, 示例值："搜索客服工单"


@attr.s
class UpdateSearchDataSourceRespDataSource(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # 数据源的唯一标识
    name: str = attr.ib(default="", metadata={"req_type": "json"})  # data_source的展示名称
    state: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 数据源状态，0-未上线，1-已上线, 可选值有: `0`：未上线, `1`：已上线
    description: str = attr.ib(default="", metadata={"req_type": "json"})  # 对于数据源的描述
    create_time: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 创建时间，使用Unix时间戳，单位为“秒”
    update_time: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 更新时间，使用Unix时间戳，单位为“秒”
    is_exceed_quota: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 是否超限


@attr.s
class UpdateSearchDataSourceResp(object):
    data_source: UpdateSearchDataSourceRespDataSource = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 数据源


def _gen_update_search_data_source_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=UpdateSearchDataSourceResp,
        scope="Search",
        api="UpdateSearchDataSource",
        method="PATCH",
        url="https://open.feishu.cn/open-apis/search/v2/data_sources/:data_source_id",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
