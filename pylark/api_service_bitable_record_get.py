# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class GetBitableRecordReq(object):
    app_token: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # bitable app token, 示例值："bascnCMII2ORej2RItqpZZUNMIe"
    table_id: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # table id, 示例值："tblxI2tWaxP5dG7p"
    record_id: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 单条记录的 id, 示例值："recn0hoyXL"


@attr.s
class GetBitableRecordRespRecordFieldsValue(object):
    pass


@attr.s
class GetBitableRecordRespRecordFields(object):
    key: str = attr.ib(default="", metadata={"req_type": "json"})  # 字段名
    value: typing.Any = attr.ib(default=None, metadata={"req_type": "json"})  # 内容


@attr.s
class GetBitableRecordRespRecord(object):
    record_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 记录 id
    fields: GetBitableRecordRespRecordFields = attr.ib(
        factory=lambda: GetBitableRecordRespRecordFields(),
        metadata={"req_type": "json"},
    )  # 记录字段


@attr.s
class GetBitableRecordResp(object):
    record: GetBitableRecordRespRecord = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 记录


def _gen_get_bitable_record_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetBitableRecordResp,
        scope="Bitable",
        api="GetBitableRecord",
        method="GET",
        url="https://open.feishu.cn/open-apis/bitable/v1/apps/:app_token/tables/:table_id/records/:record_id",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        need_user_access_token=True,
    )
