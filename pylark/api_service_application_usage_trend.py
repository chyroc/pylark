# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing


@attr.s
class GetApplicationUsageTrendReqFilter(object):
    key: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 过滤字段，支持`department_id`
    op: str = attr.ib(default="", metadata={"req_type": "json"})  # 过滤操作，支持`in`、`=`
    value: str = attr.ib(default="", metadata={"req_type": "json"})  # 过滤字段值，多个使用英文逗号分隔


@attr.s
class GetApplicationUsageTrendReq(object):
    app_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 目标应用的 ID，支持自建应用
    ability: str = attr.ib(default="", metadata={"req_type": "json"})  # 应用能力，mp：小程序
    time_start: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 起始时间戳（秒），时间跨度最长支持180天
    time_end: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 截止时间戳（秒），时间跨度最长支持180天
    time_interval: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 步长（秒），最小步长为60秒，需满足(${time_end} - ${time_start}) / ${time_interval} <= 2*24*60
    filters: typing.List[GetApplicationUsageTrendReqFilter] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 过滤条件


@attr.s
class GetApplicationUsageTrendRespItemTrend(object):
    timestamp: int = attr.ib(default=0, metadata={"req_type": "json"})  # 时间戳
    pv: int = attr.ib(default=0, metadata={"req_type": "json"})  # 应用使用pv
    uv: int = attr.ib(default=0, metadata={"req_type": "json"})  # 应用使用uv


@attr.s
class GetApplicationUsageTrendRespItem(object):
    trends: typing.List[GetApplicationUsageTrendRespItemTrend] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 趋势数据


@attr.s
class GetApplicationUsageTrendResp(object):
    item: GetApplicationUsageTrendRespItem = attr.ib(
        factory=lambda: GetApplicationUsageTrendRespItem(),
        metadata={"req_type": "json"},
    )  # 返回项


def _gen_get_application_usage_trend_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetApplicationUsageTrendResp,
        scope="Application",
        api="GetApplicationUsageTrend",
        method="POST",
        url="https://open.feishu.cn/open-apis/application/v1/app_usage_trend",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
