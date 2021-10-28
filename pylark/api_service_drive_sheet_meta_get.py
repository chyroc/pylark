# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
from pylark import lark_type_enum, lark_type_sheet
import attr
import typing
import io


@attr.s
class GetSheetMetaReqUserIDType(object):
    pass


@attr.s
class GetSheetMetaReq(object):
    ext_fields: str = attr.ib(
        default="", metadata={"req_type": "query", "key": "extFields"}
    )  # 额外返回的字段，extFields=protectedRange时返回保护行列信息
    user_id_type: lark_type_enum.IDType = attr.ib(
        default=None, metadata={"req_type": "query", "key": "user_id_type"}
    )  # 返回的用户id类型，可选open_id,union_id
    spreadsheet_token: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "spreadsheetToken"}
    )  # spreadsheet 的 token；获取方式见[在线表格开发指南](https://open.feishu.cn/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview)


@attr.s
class GetSheetMetaRespSheetBlockInfo(object):
    block_token: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "blockToken"}
    )  # block的token
    block_type: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "blockType"}
    )  # block的类型


@attr.s
class GetSheetMetaRespSheetProtectedRangeDimension(object):
    start_index: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "startIndex"}
    )  # 保护行列的起始位置，位置从1开始
    end_index: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "endIndex"}
    )  # 保护行列的结束位置，位置从1开始
    major_dimension: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "majorDimension"}
    )  # 若为ROWS，则为保护行；为COLUMNS，则为保护列
    sheet_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "sheetId"}
    )  # 保护范围所在工作表 ID


@attr.s
class GetSheetMetaRespSheetProtectedRange(object):
    dimension: GetSheetMetaRespSheetProtectedRangeDimension = attr.ib(
        default=None, metadata={"req_type": "json", "key": "dimension"}
    )  # 保护行列的信息，如果为保护工作表，则该字段为空
    protect_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "protectId"}
    )  # 保护范围ID
    lock_info: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "lockInfo"}
    )  # 保护说明
    sheet_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "sheetId"}
    )  # 保护工作表 ID


@attr.s
class GetSheetMetaRespSheetMerge(object):
    start_row_index: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "startRowIndex"}
    )  # 合并单元格范围的开始行下标，index 从 0 开始
    start_column_index: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "startColumnIndex"}
    )  # 合并单元格范围的开始列下标，index 从 0 开始
    row_count: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "rowCount"}
    )  # 合并单元格范围的行数量
    column_count: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "columnCount"}
    )  # 合并单元格范围的列数量


@attr.s
class GetSheetMetaRespSheet(object):
    sheet_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "sheetId"}
    )  # sheet 的 id
    title: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "title"}
    )  # sheet 的标题
    index: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "index"}
    )  # sheet 的位置
    row_count: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "rowCount"}
    )  # sheet 的最大行数
    column_count: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "columnCount"}
    )  # sheet 的最大列数
    frozen_row_count: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "frozenRowCount"}
    )  # 该 sheet 的冻结行数，小于等于 sheet 的最大行数，0表示未设置冻结
    frozen_col_count: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "frozenColCount"}
    )  # 该 sheet 的冻结列数，小于等于 sheet 的最大列数，0表示未设置冻结
    merges: typing.List[GetSheetMetaRespSheetMerge] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "merges"}
    )  # 该 sheet 中合并单元格的范围
    protected_range: GetSheetMetaRespSheetProtectedRange = attr.ib(
        default=None, metadata={"req_type": "json", "key": "protectedRange"}
    )  # 该 sheet 中保护范围
    block_info: GetSheetMetaRespSheetBlockInfo = attr.ib(
        default=None, metadata={"req_type": "json", "key": "blockInfo"}
    )  # 若含有该字段，则此工作表不为表格


@attr.s
class GetSheetMetaRespProperties(object):
    title: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "title"}
    )  # spreadsheet 的标题
    owner_user: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "ownerUser"}
    )  # 所有者的 id
    owner_user_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "ownerUserID"}
    )  # 所有者的 id，取决于user_id_type的值，仅user_id_type不为空是返回该值
    sheet_count: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "sheetCount"}
    )  # spreadsheet 下的 sheet 数
    revision: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "revision"}
    )  # 该 sheet 的版本


@attr.s
class GetSheetMetaResp(object):
    spreadsheet_token: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "spreadsheetToken"}
    )  # spreadsheet 的 token
    properties: GetSheetMetaRespProperties = attr.ib(
        default=None, metadata={"req_type": "json", "key": "properties"}
    )  # spreadsheet 的属性
    sheets: typing.List[GetSheetMetaRespSheet] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "sheets"}
    )  # spreadsheet 下的sheet列表


def _gen_get_sheet_meta_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetSheetMetaResp,
        scope="Drive",
        api="GetSheetMeta",
        method="GET",
        url="https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/:spreadsheetToken/metainfo",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        need_user_access_token=True,
    )
