# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class UpdateSheetConditionFormatReqSheetConditionFormatsConditionFormatStyleFont(
    object
):
    bold: bool = attr.ib(
        default=None, metadata={"req_type": "json", "key": "bold"}
    )  # 加粗
    italic: bool = attr.ib(
        default=None, metadata={"req_type": "json", "key": "italic"}
    )  # 斜体


@attr.s
class UpdateSheetConditionFormatReqSheetConditionFormatsConditionFormatStyle(object):
    font: UpdateSheetConditionFormatReqSheetConditionFormatsConditionFormatStyleFont = (
        attr.ib(default=None, metadata={"req_type": "json", "key": "font"})
    )  # 字体样式
    text_decoration: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "text_decoration"}
    )  # 文本装饰 ，0 默认，1 下划线，2 删除线 ，3 下划线和删除线
    fore_color: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "fore_color"}
    )  # 字体颜色
    back_color: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "back_color"}
    )  # 背景颜色


@attr.s
class UpdateSheetConditionFormatReqSheetConditionFormatsConditionFormatAttr(object):
    operator: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "operator"}
    )  # 操作方法
    time_period: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "time_period"}
    )  # 时间范围
    formula: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "formula"}
    )  # 格式
    text: str = attr.ib(default="", metadata={"req_type": "json", "key": "text"})  # 文本


@attr.s
class UpdateSheetConditionFormatReqSheetConditionFormatsConditionFormat(object):
    cf_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "cf_id"}
    )  # 需要更新的条件格式id，会校验id是否存在
    ranges: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "ranges"}
    )  # 条件格式应用的范围，支持：sheetId（整表）；sheetId!1:2（整行）；sheetId!A:B（整列）；sheetId!A1:B2（普通范围）；sheetId!A1:C（应用至最后一行）。应用范围不能超过表格的行总数和列总数，sheetId要与参数的sheetId一致
    rule_type: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "rule_type"}
    )  # 条件格式规则类型，目前只有7种：***containsBlanks（为空）、notContainsBlanks（不为空）、duplicateValues（重复值）、uniqueValues（唯一值）、cellIs（限定值范围）、containsText（包含内容）、timePeriod（日期）***
    attrs: typing.List[
        UpdateSheetConditionFormatReqSheetConditionFormatsConditionFormatAttr
    ] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "attrs"}
    )  # rule_type对应的具体属性信息，详见 [条件格式指南](https://open.feishu.cn/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/conditionformat/condition-format-guide)
    style: UpdateSheetConditionFormatReqSheetConditionFormatsConditionFormatStyle = (
        attr.ib(default=None, metadata={"req_type": "json", "key": "style"})
    )  # 条件格式样式，只支持以下样式，以下样式每个参数都可选，但是不能设置空的style


@attr.s
class UpdateSheetConditionFormatReqSheetConditionFormats(object):
    sheet_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "sheet_id"}
    )  # sheet的id
    condition_format: UpdateSheetConditionFormatReqSheetConditionFormatsConditionFormat = attr.ib(
        default=None, metadata={"req_type": "json", "key": "condition_format"}
    )  # 一个条件格式的详细信息


@attr.s
class UpdateSheetConditionFormatReq(object):
    spreadsheet_token: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "spreadsheetToken"}
    )  # sheet 的 token，获取方式见 [在线表格开发指南](https://open.feishu.cn/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview)
    sheet_condition_formats: UpdateSheetConditionFormatReqSheetConditionFormats = (
        attr.ib(
            default=None,
            metadata={"req_type": "json", "key": "sheet_condition_formats"},
        )
    )  # 表格的条件格式信息


@attr.s
class UpdateSheetConditionFormatRespResponse(object):
    sheet_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "sheet_id"}
    )  # sheet的Id
    cf_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "cf_id"}
    )  # 更新的条件格式id
    res_code: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "res_code"}
    )  # 条件格式更新状态码，0表示成功，非0表示失败
    res_msg: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "res_msg"}
    )  # 条件格式更新返回的状态信息，空表示成功，不空表示失败原因


@attr.s
class UpdateSheetConditionFormatResp(object):
    responses: typing.List[UpdateSheetConditionFormatRespResponse] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "responses"}
    )  # 响应


def _gen_update_sheet_condition_format_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=UpdateSheetConditionFormatResp,
        scope="Drive",
        api="UpdateSheetConditionFormat",
        method="POST",
        url="https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/:spreadsheetToken/condition_formats/batch_update",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        need_user_access_token=True,
    )
