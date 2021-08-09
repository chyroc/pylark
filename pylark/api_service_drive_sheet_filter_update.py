# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing


@attr.s
class UpdateSheetFilterReqCondition(object):
    filter_type: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 筛选类型, 示例值："number"
    compare_type: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 比较类型, 示例值："less"
    expected: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 筛选参数, 示例值：6


@attr.s
class UpdateSheetFilterReq(object):
    spreadsheet_token: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 表格 token, 示例值："shtcnmBA\*****yGehy8"
    sheet_id: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 子表 id, 示例值："0b\**12"
    col: str = attr.ib(default="", metadata={"req_type": "json"})  # 更新筛选条件的列, 示例值："E"
    condition: UpdateSheetFilterReqCondition = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 筛选条件


@attr.s
class UpdateSheetFilterResp(object):
    pass


def _gen_update_sheet_filter_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=UpdateSheetFilterResp,
        scope="Drive",
        api="UpdateSheetFilter",
        method="PUT",
        url="https://open.feishu.cn/open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/:sheet_id/filter",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
