# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing


@attr.s
class GetBitableTableListReq(object):
    page_token: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果, 示例值："tblsRc9GRRXKqhvW"
    page_size: int = attr.ib(
        default=0, metadata={"req_type": "query"}
    )  # 分页大小, 示例值：10, 最大值：`100`
    app_token: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # bitable app token, 示例值："appbcbWCzen6D8dezhoCH2RpMAh"


@attr.s
class GetBitableTableListRespItem(object):
    table_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 表格表 id
    revision: int = attr.ib(default=0, metadata={"req_type": "json"})  # 数据表的版本号
    name: str = attr.ib(default="", metadata={"req_type": "json"})  # 数据表 名字


@attr.s
class GetBitableTableListResp(object):
    has_more: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 是否还有更多项
    page_token: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token
    items: typing.List[GetBitableTableListRespItem] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 数据表信息


def _gen_get_bitable_table_list_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetBitableTableListResp,
        scope="Bitable",
        api="GetBitableTableList",
        method="GET",
        url="https://open.feishu.cn/open-apis/bitable/v1/apps/:app_token/tables",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )