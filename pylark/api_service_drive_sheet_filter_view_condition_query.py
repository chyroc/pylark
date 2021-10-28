# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class QuerySheetFilterViewConditionReq(object):
    spreadsheet_token: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "spreadsheet_token"}
    )  # 表格 token, 示例值："shtcnmBA*****yGehy8"
    sheet_id: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "sheet_id"}
    )  # 子表 id, 示例值："0b**12"
    filter_view_id: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "filter_view_id"}
    )  # 筛选视图 id, 示例值："pH9hbVcCXA"


@attr.s
class QuerySheetFilterViewConditionRespItem(object):
    condition_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "condition_id"}
    )  # 设置筛选条件的列，使用字母号
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
class QuerySheetFilterViewConditionResp(object):
    items: typing.List[QuerySheetFilterViewConditionRespItem] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "items"}
    )  # 筛选视图设置的所有筛选条件


def _gen_query_sheet_filter_view_condition_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=QuerySheetFilterViewConditionResp,
        scope="Drive",
        api="QuerySheetFilterViewCondition",
        method="GET",
        url="https://open.feishu.cn/open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/:sheet_id/filter_views/:filter_view_id/conditions/query",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        need_user_access_token=True,
    )
