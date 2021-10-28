# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class DeleteSheetFilterViewConditionReq(object):
    spreadsheet_token: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "spreadsheet_token"}
    )  # 表格 token, 示例值："shtcnmBA*****yGehy8"
    sheet_id: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "sheet_id"}
    )  # 子表 id, 示例值："0b**12"
    filter_view_id: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "filter_view_id"}
    )  # 筛选视图 id, 示例值："pH9hbVcCXA"
    condition_id: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "condition_id"}
    )  # 筛选范围内的某列字母号, 示例值："E"


@attr.s
class DeleteSheetFilterViewConditionResp(object):
    pass


def _gen_delete_sheet_filter_view_condition_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=DeleteSheetFilterViewConditionResp,
        scope="Drive",
        api="DeleteSheetFilterViewCondition",
        method="DELETE",
        url="https://open.feishu.cn/open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/:sheet_id/filter_views/:filter_view_id/conditions/:condition_id",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        need_user_access_token=True,
    )
