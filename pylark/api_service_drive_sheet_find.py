# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing


@attr.s
class FindSheetReqFindCondition(object):
    range_: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 查找范围, 示例值："0b**12!A1:H10"
    match_case: bool = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 是否忽略大小写, 示例值：true
    match_entire_cell: bool = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 是否匹配整个单元格, 示例值：false
    search_by_regex: bool = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 是否为正则匹配, 示例值：false
    include_formulas: bool = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 是否搜索公式内容, 示例值：false


@attr.s
class FindSheetReq(object):
    spreadsheet_token: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 表格的 token, 示例值："shtcnmBA*****yGehy8"
    sheet_id: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 子表的 id, 示例值："0b**12"
    find_condition: FindSheetReqFindCondition = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 查找条件
    find: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 查找的字符串, 示例值："hello"


@attr.s
class FindSheetRespFindResult(object):
    matched_cells: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 符合查找条件的单元格数组，不包含公式，例如["A1", "A2"...]
    matched_formula_cells: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 符合查找条件的含有公式的单元格数组，例如["B3", "H7"...]
    rows_count: int = attr.ib(default=0, metadata={"req_type": "json"})  # 符合查找条件的总行数


@attr.s
class FindSheetResp(object):
    find_result: FindSheetRespFindResult = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 查找返回符合条件的信息


def _gen_find_sheet_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=FindSheetResp,
        scope="Drive",
        api="FindSheet",
        method="POST",
        url="https://open.feishu.cn/open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/:sheet_id/find",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
