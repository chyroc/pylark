# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing


@attr.s
class DeleteBitableViewReq(object):
    app_token: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # bitable app token, 示例值："appbcbWCzen6D8dezhoCH2RpMAh"
    table_id: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # table id, 示例值："tblsRc9GRRXKqhvW"
    view_id: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 视图Id, 示例值："vewTpR1urY"


@attr.s
class DeleteBitableViewResp(object):
    pass


def _gen_delete_bitable_view_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=DeleteBitableViewResp,
        scope="Bitable",
        api="DeleteBitableView",
        method="DELETE",
        url="https://open.feishu.cn/open-apis/bitable/v1/apps/:app_token/tables/:table_id/views/:view_id",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )