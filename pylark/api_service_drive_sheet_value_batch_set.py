# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class BatchSetSheetValueReqValueRangeValue(object):
    pass


@attr.s
class BatchSetSheetValueReqValueRange(object):
    range_: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 更新范围，包含 sheetId 与单元格范围两部分，目前支持四种索引方式，详见[在线表格开发指南](https://open.feishu.cn/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview)
    values: typing.List[typing.List[BatchSetSheetValueReqValueRangeValue]] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 需要写入的值，如要写入公式、超链接、emial、@人等，可详看附录[sheet 支持写入数据类型](https://open.feishu.cn/document/ukTMukTMukTM/ugjN1UjL4YTN14CO2UTN)


@attr.s
class BatchSetSheetValueReq(object):
    spreadsheet_token: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # spreadsheet 的 token，获取方式见[在线表格开发指南](https://open.feishu.cn/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview)
    value_ranges: BatchSetSheetValueReqValueRange = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 需要更新的多个范围


@attr.s
class BatchSetSheetValueRespResponse(object):
    spreadsheet_token: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # spreadsheet 的 token
    updated_range: str = attr.ib(default="", metadata={"req_type": "json"})  # 写入的范围
    updated_rows: int = attr.ib(default=0, metadata={"req_type": "json"})  # 写入的行数
    updated_columns: int = attr.ib(default=0, metadata={"req_type": "json"})  # 写入的列数
    updated_cells: int = attr.ib(default=0, metadata={"req_type": "json"})  # 写入的单元格总数


@attr.s
class BatchSetSheetValueResp(object):
    responses: typing.List[BatchSetSheetValueRespResponse] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 响应
    revision: int = attr.ib(default=0, metadata={"req_type": "json"})  # sheet 的版本号
    spreadsheet_token: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # spreadsheet 的 token


def _gen_batch_set_sheet_value_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=BatchSetSheetValueResp,
        scope="Drive",
        api="BatchSetSheetValue",
        method="POST",
        url="https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/:spreadsheetToken/values_batch_update",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        need_user_access_token=True,
    )
