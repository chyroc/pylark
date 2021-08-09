# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing


@attr.s
class DeleteSheetDimensionRangeReqDimension(object):
    sheet_id: str = attr.ib(default="", metadata={"req_type": "json"})  # sheetId
    major_dimension: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 默认 ROWS ，可选 ROWS、COLUMNS
    start_index: int = attr.ib(default=0, metadata={"req_type": "json"})  # 开始的位置
    end_index: int = attr.ib(default=0, metadata={"req_type": "json"})  # 结束的位置


@attr.s
class DeleteSheetDimensionRangeReq(object):
    spreadsheet_token: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # spreadsheet的token，详见 [在线表格开发指南](https://open.feishu.cn/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview)
    dimension: DeleteSheetDimensionRangeReqDimension = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 需要删除行列的维度信息


@attr.s
class DeleteSheetDimensionRangeResp(object):
    del_count: int = attr.ib(default=0, metadata={"req_type": "json"})  # 删除的行/列数
    major_dimension: str = attr.ib(default="", metadata={"req_type": "json"})  # 插入维度


def _gen_delete_sheet_dimension_range_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=DeleteSheetDimensionRangeResp,
        scope="Drive",
        api="DeleteSheetDimensionRange",
        method="DELETE",
        url="https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/:spreadsheetToken/dimension_range",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
