# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing


@attr.s
class AddSheetDimensionRangeReqDimension(object):
    sheet_id: str = attr.ib(default="", metadata={"req_type": "json"})  # sheetId
    major_dimension: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 默认 ROWS ，可选 ROWS、COLUMNS
    length: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 要增加的行/列数,0<length<5000


@attr.s
class AddSheetDimensionRangeReq(object):
    spreadsheet_token: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # spreadsheet 的 token，详见 [在线表格开发指南](https://open.feishu.cn/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview)
    dimension: AddSheetDimensionRangeReqDimension = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 需要增加行列的维度信息


@attr.s
class AddSheetDimensionRangeResp(object):
    add_count: int = attr.ib(default=0, metadata={"req_type": "json"})  # 增加的行/列数
    major_dimension: str = attr.ib(default="", metadata={"req_type": "json"})  # 插入维度


def _gen_add_sheet_dimension_range_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=AddSheetDimensionRangeResp,
        scope="Drive",
        api="AddSheetDimensionRange",
        method="POST",
        url="https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/:spreadsheetToken/dimension_range",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )