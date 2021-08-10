# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class CreateSheetProtectedDimensionReqAddProtectedDimensionDimension(object):
    sheet_id: str = attr.ib(default="", metadata={"req_type": "json"})  # sheetId
    major_dimension: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 默认 ROWS ，可选 ROWS、COLUMNS
    start_index: int = attr.ib(default=0, metadata={"req_type": "json"})  # 开始的位置
    end_index: int = attr.ib(default=0, metadata={"req_type": "json"})  # 结束的位置


@attr.s
class CreateSheetProtectedDimensionReqAddProtectedDimension(object):
    dimension: CreateSheetProtectedDimensionReqAddProtectedDimensionDimension = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 需要保护行列的维度信息
    editors: typing.List[int] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 允许编辑保护范围的用户的 userID
    users: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 允许编辑保护范围的用户的id，id类型取决于user_id_type
    lock_info: str = attr.ib(default="", metadata={"req_type": "json"})  # 保护范围的信息


@attr.s
class CreateSheetProtectedDimensionReqUserIDType(object):
    pass


@attr.s
class CreateSheetProtectedDimensionReq(object):
    user_id_type: CreateSheetProtectedDimensionReqUserIDType = attr.ib(
        default=None, metadata={"req_type": "query"}
    )  # 请求的用户id类型，可选open_id,union_id
    spreadsheet_token: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # spreadsheet 的 token，获取方式见 [在线表格开发指南](https://open.feishu.cn/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview)
    add_protected_dimension: CreateSheetProtectedDimensionReqAddProtectedDimension = (
        attr.ib(default=None, metadata={"req_type": "json"})
    )  # 需要增加保护范围的维度信息，可多个范围


@attr.s
class CreateSheetProtectedDimensionRespAddProtectedDimensionDimension(object):
    sheet_id: str = attr.ib(default="", metadata={"req_type": "json"})  # sheetId
    major_dimension: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 默认 ROWS ，可选 ROWS、COLUMNS
    start_index: int = attr.ib(default=0, metadata={"req_type": "json"})  # 开始的位置
    end_index: int = attr.ib(default=0, metadata={"req_type": "json"})  # 结束的位置


@attr.s
class CreateSheetProtectedDimensionRespAddProtectedDimension(object):
    dimension: CreateSheetProtectedDimensionRespAddProtectedDimensionDimension = (
        attr.ib(default=None, metadata={"req_type": "json"})
    )  # 需要保护行列的维度信息
    editors: typing.List[int] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 允许编辑保护范围的用户的 userID
    users: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 允许编辑保护范围的用户的id，id类型取决于user_id_type
    lock_info: str = attr.ib(default="", metadata={"req_type": "json"})  # 保护范围的信息
    protect_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 保护区域的唯一 uid ，可用做后续解除保护


@attr.s
class CreateSheetProtectedDimensionResp(object):
    add_protected_dimension: CreateSheetProtectedDimensionRespAddProtectedDimension = (
        attr.ib(default=None, metadata={"req_type": "json"})
    )  # 需要增加保护范围的维度信息，可多个范围


def _gen_create_sheet_protected_dimension_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=CreateSheetProtectedDimensionResp,
        scope="Drive",
        api="CreateSheetProtectedDimension",
        method="POST",
        url="https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/:spreadsheetToken/protected_dimension",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        need_user_access_token=True,
    )
