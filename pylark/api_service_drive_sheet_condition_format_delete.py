# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class DeleteSheetConditionFormatReqSheetCfIDs(object):
    sheet_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "sheet_id"}
    )  # sheet的id
    cf_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "cf_id"}
    )  # 条件格式id


@attr.s
class DeleteSheetConditionFormatReq(object):
    spreadsheet_token: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "spreadsheetToken"}
    )  # sheet 的 token，获取方式见 [在线表格开发指南](https://open.feishu.cn/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview)
    sheet_cf_ids: DeleteSheetConditionFormatReqSheetCfIDs = attr.ib(
        default=None, metadata={"req_type": "json", "key": "sheet_cf_ids"}
    )  # 表格条件格式id


@attr.s
class DeleteSheetConditionFormatRespResponse(object):
    sheet_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "sheet_id"}
    )  # sheet的Id
    cf_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "cf_id"}
    )  # 条件格式id
    res_code: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "res_code"}
    )  # 条件格式删除状态码，0表示成功，非0表示失败
    res_msg: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "res_msg"}
    )  # 条件格式删除返回的状态信息，空表示成功，非空表示失败原因


@attr.s
class DeleteSheetConditionFormatResp(object):
    responses: typing.List[DeleteSheetConditionFormatRespResponse] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "responses"}
    )  # 响应


def _gen_delete_sheet_condition_format_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=DeleteSheetConditionFormatResp,
        scope="Drive",
        api="DeleteSheetConditionFormat",
        method="DELETE",
        url="https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/:spreadsheetToken/condition_formats/batch_delete",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        need_user_access_token=True,
    )
