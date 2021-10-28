# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class GetSheetFilterReq(object):
    spreadsheet_token: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "spreadsheet_token"}
    )  # 表格 token, 示例值："shtcnmBA\*****yGehy8"
    sheet_id: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "sheet_id"}
    )  # 子表 id, 示例值："0b\**12"


@attr.s
class GetSheetFilterRespSheetFilterInfoFilterInfoCondition(object):
    filter_type: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "filter_type"}
    )  # 筛选类型
    compare_type: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "compare_type"}
    )  # 比较类型
    expected: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "expected"}
    )  # 筛选参数


@attr.s
class GetSheetFilterRespSheetFilterInfoFilterInfo(object):
    col: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "col"}
    )  # 设置了筛选条件的列
    conditions: typing.List[
        GetSheetFilterRespSheetFilterInfoFilterInfoCondition
    ] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "conditions"}
    )  # 筛选条件


@attr.s
class GetSheetFilterRespSheetFilterInfo(object):
    range_: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "range"}
    )  # 筛选应用范围
    filtered_out_rows: typing.List[int] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "filtered_out_rows"}
    )  # 筛选出来隐藏的行
    filter_infos: typing.List[GetSheetFilterRespSheetFilterInfoFilterInfo] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "filter_infos"}
    )  # sheet的筛选条件


@attr.s
class GetSheetFilterResp(object):
    sheet_filter_info: GetSheetFilterRespSheetFilterInfo = attr.ib(
        default=None, metadata={"req_type": "json", "key": "sheet_filter_info"}
    )  # 筛选信息


def _gen_get_sheet_filter_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetSheetFilterResp,
        scope="Drive",
        api="GetSheetFilter",
        method="GET",
        url="https://open.feishu.cn/open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/:sheet_id/filter",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        need_user_access_token=True,
    )
