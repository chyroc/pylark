# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class GetSearchDataSourceReq(object):
    data_source_id: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "data_source_id"}
    )  # 数据源的唯一标识, 示例值："service_ticket"


@attr.s
class GetSearchDataSourceRespDataSource(object):
    id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "id"}
    )  # 数据源的唯一标识
    name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "name"}
    )  # data_source的展示名称
    state: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "state"}
    )  # 数据源状态，0-未上线，1-已上线, 可选值有: `0`：未上线, `1`：已上线
    description: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "description"}
    )  # 对于数据源的描述
    create_time: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "create_time"}
    )  # 创建时间，使用Unix时间戳，单位为“秒”
    update_time: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "update_time"}
    )  # 更新时间，使用Unix时间戳，单位为“秒”
    is_exceed_quota: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json", "key": "is_exceed_quota"}
    )  # 是否超限


@attr.s
class GetSearchDataSourceResp(object):
    data_source: GetSearchDataSourceRespDataSource = attr.ib(
        default=None, metadata={"req_type": "json", "key": "data_source"}
    )  # 数据源实例


def _gen_get_search_data_source_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetSearchDataSourceResp,
        scope="Search",
        api="GetSearchDataSource",
        method="GET",
        url="https://open.feishu.cn/open-apis/search/v2/data_sources/:data_source_id",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
