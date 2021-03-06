# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
from pylark import lark_type, lark_type_sheet, lark_type_approval
import attr
import typing
import io


@attr.s
class CreateBitableRecordReq(object):
    user_id_type: lark_type.IDType = attr.ib(
        default=None, metadata={"req_type": "query", "key": "user_id_type"}
    )  # 用户 ID 类型, 示例值："open_id", 可选值有: `open_id`：用户的 open id, `union_id`：用户的 union id, `user_id`：用户的 user id, 默认值: `open_id`, 当值为 `user_id`, 字段权限要求:  获取用户 user ID
    app_token: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "app_token"}
    )  # bitable app token, 示例值："bascng7vrxcxpig7geggXiCtadY"
    table_id: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "table_id"}
    )  # table id, 示例值："tblUa9vcYjWQYJCj"
    record_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "record_id"}
    )  # 记录 id, 示例值："recqwIwhc6"
    fields: typing.Dict = attr.ib(
        default=None, metadata={"req_type": "json", "key": "fields"}
    )  # 记录字段


@attr.s
class CreateBitableRecordRespRecord(object):
    record_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "record_id"}
    )  # 记录 id
    fields: typing.Dict = attr.ib(
        default=None, metadata={"req_type": "json", "key": "fields"}
    )  # 记录字段


@attr.s
class CreateBitableRecordResp(object):
    record: CreateBitableRecordRespRecord = attr.ib(
        default=None, metadata={"req_type": "json", "key": "record"}
    )  # 记录


def _gen_create_bitable_record_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=CreateBitableRecordResp,
        scope="Bitable",
        api="CreateBitableRecord",
        method="POST",
        url="https://open.feishu.cn/open-apis/bitable/v1/apps/:app_token/tables/:table_id/records",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        need_user_access_token=True,
    )
