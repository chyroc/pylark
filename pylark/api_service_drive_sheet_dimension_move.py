# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing


@attr.s
class MoveSheetDimensionReqSource(object):
    major_dimension: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 操作行还是列，取值：ROWS、COLUMNS, 示例值："ROWS"
    start_index: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 起始行或者列号, 示例值：0
    end_index: int = attr.ib(default=0, metadata={"req_type": "json"})  # 结束行或者列号, 示例值：1


@attr.s
class MoveSheetDimensionReq(object):
    spreadsheet_token: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 表格 token, 示例值："shtcnmBA\*****yGehy8"
    sheet_id: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 子表 id, 示例值："0b\**12"
    source: MoveSheetDimensionReqSource = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 移动源位置参数
    destination_index: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 移动的目标位置行或者列号, 示例值：4


@attr.s
class MoveSheetDimensionResp(object):
    pass


def _gen_move_sheet_dimension_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=MoveSheetDimensionResp,
        scope="Drive",
        api="MoveSheetDimension",
        method="POST",
        url="https://open.feishu.cn/open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/:sheet_id/move_dimension",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )