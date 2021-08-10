# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class CreateSheetFilterReqCondition(object):
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
class CreateSheetFilterReq(object):
    spreadsheet_token: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 表格 token, 示例值："shtcnmBA\*****yGehy8"
    sheet_id: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 子表 id, 示例值："0b\**12"
    range_: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 筛选应用范围, 示例值："xxxxxx!C1:H14"
    col: str = attr.ib(default="", metadata={"req_type": "json"})  # 设置筛选条件的列, 示例值："E"
    condition: CreateSheetFilterReqCondition = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 筛选的条件


@attr.s
class CreateSheetFilterResp(object):
    pass


def _gen_create_sheet_filter_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=CreateSheetFilterResp,
        scope="Drive",
        api="CreateSheetFilter",
        method="POST",
        url="https://open.feishu.cn/open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/:sheet_id/filter",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        need_user_access_token=True,
    )
