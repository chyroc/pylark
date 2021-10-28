# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class SetSheetStyleReqAppendStyleStyleFont(object):
    bold: bool = attr.ib(
        default=None, metadata={"req_type": "json", "key": "bold"}
    )  # 是否加粗
    italic: bool = attr.ib(
        default=None, metadata={"req_type": "json", "key": "italic"}
    )  # 是否斜体
    font_size: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "fontSize"}
    )  # 字体大小 字号大小为9~36 行距固定为1.5，如:10pt/1.5
    clean: bool = attr.ib(
        default=None, metadata={"req_type": "json", "key": "clean"}
    )  # 清除 font 格式,默认 false


@attr.s
class SetSheetStyleReqAppendStyleStyle(object):
    font: SetSheetStyleReqAppendStyleStyleFont = attr.ib(
        default=None, metadata={"req_type": "json", "key": "font"}
    )  # 字体相关样式
    text_decoration: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "textDecoration"}
    )  # 文本装饰 ，0 默认，1 下划线，2 删除线 ，3 下划线和删除线
    formatter: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "formatter"}
    )  # 数字格式，详见附录 [sheet支持数字格式类型](https://open.feishu.cn/document/ukTMukTMukTM/uMjM2UjLzIjN14yMyYTN)
    h_align: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "hAlign"}
    )  # 水平对齐，0 左对齐，1 中对齐，2 右对齐
    v_align: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "vAlign"}
    )  # 垂直对齐, 0 上对齐，1 中对齐, 2 下对齐
    fore_color: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "foreColor"}
    )  # 字体颜色
    back_color: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "backColor"}
    )  # 背景颜色
    border_type: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "borderType"}
    )  # 边框类型，可选 "FULL_BORDER"，"OUTER_BORDER"，"INNER_BORDER"，"NO_BORDER"，"LEFT_BORDER"，"RIGHT_BORDER"，"TOP_BORDER"，"BOTTOM_BORDER"
    border_color: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "borderColor"}
    )  # 边框颜色
    clean: bool = attr.ib(
        default=None, metadata={"req_type": "json", "key": "clean"}
    )  # 是否清除所有格式,默认 false


@attr.s
class SetSheetStyleReqAppendStyle(object):
    range_: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "range"}
    )  # 查询范围，包含 sheetId 与单元格范围两部分，目前支持四种索引方式，详见[在线表格开发指南](https://open.feishu.cn/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview)
    style: SetSheetStyleReqAppendStyleStyle = attr.ib(
        default=None, metadata={"req_type": "json", "key": "style"}
    )  # 需要更新的样式


@attr.s
class SetSheetStyleReq(object):
    spreadsheet_token: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "spreadsheetToken"}
    )  # spreadsheet 的 token，详见 [在线表格开发指南](https://open.feishu.cn/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview)
    append_style: SetSheetStyleReqAppendStyle = attr.ib(
        default=None, metadata={"req_type": "json", "key": "appendStyle"}
    )  # 设置单元格样式


@attr.s
class SetSheetStyleResp(object):
    spreadsheet_token: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "spreadsheetToken"}
    )  # spreadsheet 的 token
    updated_range: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "updatedRange"}
    )  # 设置样式的范围
    updated_rows: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "updatedRows"}
    )  # 设置样式的行数
    updated_columns: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "updatedColumns"}
    )  # 设置样式的列数
    updated_cells: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "updatedCells"}
    )  # 设置样式的单元格总数
    revision: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "revision"}
    )  # sheet 的版本号


def _gen_set_sheet_style_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=SetSheetStyleResp,
        scope="Drive",
        api="SetSheetStyle",
        method="PUT",
        url="https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/:spreadsheetToken/style",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        need_user_access_token=True,
    )
