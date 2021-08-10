# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class GetSheetValueReqUserIDType(object):
    pass


@attr.s
class GetSheetValueReq(object):
    value_render_option: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # valueRenderOption=ToString 可返回纯文本的值；valueRenderOption=FormattedValue 计算并格式化单元格；valueRenderOption=Formula单元格中含有公式时返回公式本身；valueRenderOption=UnformattedValue计算但不对单元格进行格式化。
    date_time_render_option: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # dateTimeRenderOption=FormattedString 计算并对时间日期按照其格式进行格式化，但不会对数字进行格式化，返回格式化后的字符串。
    user_id_type: GetSheetValueReqUserIDType = attr.ib(
        default=None, metadata={"req_type": "query"}
    )  # 返回的用户id类型，可选open_id,union_id
    spreadsheet_token: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # spreadsheet 的 token，详见[在线表格开发指南](https://open.feishu.cn/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview)
    range_: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 查询范围，包含 sheetId 与单元格范围两部分，目前支持四种索引方式，详见[在线表格开发指南](https://open.feishu.cn/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview)


@attr.s
class GetSheetValueRespValueRangeValues(object):
    pass


@attr.s
class GetSheetValueRespValueRange(object):
    major_dimension: str = attr.ib(default="", metadata={"req_type": "json"})  # 插入维度
    range_: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 返回数据的范围，为空时表示查询范围没有数据
    revision: int = attr.ib(default=0, metadata={"req_type": "json"})  # sheet 的版本号
    values: typing.List[GetSheetValueRespValueRangeValues] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 查询得到的值


@attr.s
class GetSheetValueResp(object):
    revision: int = attr.ib(default=0, metadata={"req_type": "json"})  # sheet 的版本号
    spreadsheet_token: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # spreadsheet 的 token，详见 [对接前说明](https://open.feishu.cn/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN) 的第 4 项
    value_range: GetSheetValueRespValueRange = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 值与范围


def _gen_get_sheet_value_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetSheetValueResp,
        scope="Drive",
        api="GetSheetValue",
        method="GET",
        url="https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/:spreadsheetToken/values/:range",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        need_user_access_token=True,
    )
