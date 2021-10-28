# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class PrependSheetValueReqValueRangeValues(object):
    pass


@attr.s
class PrependSheetValueReqValueRange(object):
    range_: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # ⁣插入范围，包含 sheetId 与单元格范围两部分，目前支持四种索引方式，详见 [在线表格开发指南](https://open.feishu.cn/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview)
    values: typing.List[typing.List[PrependSheetValueReqValueRangeValues]] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 需要写入的值，如要写入公式、超链接、email、@人等，可详看附录[sheet 支持写入数据类型](https://open.feishu.cn/document/ukTMukTMukTM/ugjN1UjL4YTN14CO2UTN)


@attr.s
class PrependSheetValueReq(object):
    spreadsheet_token: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # sheet的token，获取方式见 [在线表格开发指南](https://open.feishu.cn/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview)
    value_range: PrependSheetValueReqValueRange = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 值与范围


@attr.s
class PrependSheetValueRespUpdates(object):
    spreadsheet_token: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # spreadsheet 的 token
    updated_range: str = attr.ib(default="", metadata={"req_type": "json"})  # 写入的范围
    updated_rows: int = attr.ib(default=0, metadata={"req_type": "json"})  # 写入的行数
    updated_columns: int = attr.ib(default=0, metadata={"req_type": "json"})  # 写入的列数
    updated_cells: int = attr.ib(default=0, metadata={"req_type": "json"})  # 写入的单元格总数
    revision: int = attr.ib(default=0, metadata={"req_type": "json"})  # sheet 的版本号


@attr.s
class PrependSheetValueResp(object):
    spreadsheet_token: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # spreadsheet 的 token
    table_range: str = attr.ib(default="", metadata={"req_type": "json"})  # 写入的范围
    revision: int = attr.ib(default=0, metadata={"req_type": "json"})  # sheet 的版本号
    updates: PrependSheetValueRespUpdates = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 插入数据的范围、行列数等


def _gen_prepend_sheet_value_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=PrependSheetValueResp,
        scope="Drive",
        api="PrependSheetValue",
        method="POST",
        url="https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/:spreadsheetToken/values_prepend",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        need_user_access_token=True,
    )
