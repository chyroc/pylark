# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class BatchDeleteBitableTableReq(object):
    app_token: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "app_token"}
    )  # bitable app token, 示例值："appbcbWCzen6D8dezhoCH2RpMAh"
    table_ids: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "table_ids"}
    )  # 删除的多条tableid列表


@attr.s
class BatchDeleteBitableTableResp(object):
    pass


def _gen_batch_delete_bitable_table_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=BatchDeleteBitableTableResp,
        scope="Bitable",
        api="BatchDeleteBitableTable",
        method="POST",
        url="https://open.feishu.cn/open-apis/bitable/v1/apps/:app_token/tables/batch_delete",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        need_user_access_token=True,
    )
