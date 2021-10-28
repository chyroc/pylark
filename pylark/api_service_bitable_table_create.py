# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class CreateBitableTableReqTable(object):
    name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "name"}
    )  # 数据表 名字, 示例值："table1"


@attr.s
class CreateBitableTableReqUserIDType(object):
    pass


@attr.s
class CreateBitableTableReq(object):
    user_id_type: CreateBitableTableReqUserIDType = attr.ib(
        default=None, metadata={"req_type": "query", "key": "user_id_type"}
    )  # 用户 ID 类型, 示例值："open_id", 可选值有: `open_id`：用户的 open id, `union_id`：用户的 union id, `user_id`：用户的 user id, 默认值: `open_id`, 当值为 `user_id`, 字段权限要求: 获取用户 user ID
    app_token: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "app_token"}
    )  # bitable app token, 示例值："appbcbWCzen6D8dezhoCH2RpMAh"
    table: CreateBitableTableReqTable = attr.ib(
        default=None, metadata={"req_type": "json", "key": "table"}
    )  # 数据表


@attr.s
class CreateBitableTableResp(object):
    table_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "table_id"}
    )  # table id


def _gen_create_bitable_table_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=CreateBitableTableResp,
        scope="Bitable",
        api="CreateBitableTable",
        method="POST",
        url="https://open.feishu.cn/open-apis/bitable/v1/apps/:app_token/tables",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        need_user_access_token=True,
    )
