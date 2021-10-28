# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
from pylark import lark_type_enum, lark_type_sheet
import attr
import typing
import io


@attr.s
class UpdateSheetDimensionRangeReqDimensionProperties(object):
    visible: bool = attr.ib(
        default=None, metadata={"req_type": "json", "key": "visible"}
    )  # true 为显示，false 为隐藏行列
    fixed_size: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "fixedSize"}
    )  # 行/列的大小


@attr.s
class UpdateSheetDimensionRangeReqDimension(object):
    sheet_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "sheetId"}
    )  # sheetId
    major_dimension: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "majorDimension"}
    )  # 默认 ROWS ，可选 ROWS、COLUMNS
    start_index: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "startIndex"}
    )  # 开始的位置
    end_index: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "endIndex"}
    )  # 结束的位置


@attr.s
class UpdateSheetDimensionRangeReq(object):
    spreadsheet_token: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "spreadsheetToken"}
    )  # spreadsheet 的 token，获取方式见[在线表格开发指南](https://open.feishu.cn/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview)
    dimension: UpdateSheetDimensionRangeReqDimension = attr.ib(
        default=None, metadata={"req_type": "json", "key": "dimension"}
    )  # 需要更新行列的维度信息
    dimension_properties: UpdateSheetDimensionRangeReqDimensionProperties = attr.ib(
        default=None, metadata={"req_type": "json", "key": "dimensionProperties"}
    )  # 需要更新行列的属性


@attr.s
class UpdateSheetDimensionRangeResp(object):
    pass


def _gen_update_sheet_dimension_range_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=UpdateSheetDimensionRangeResp,
        scope="Drive",
        api="UpdateSheetDimensionRange",
        method="PUT",
        url="https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/:spreadsheetToken/dimension_range",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        need_user_access_token=True,
    )
