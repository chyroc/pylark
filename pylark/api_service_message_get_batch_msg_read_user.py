# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class GetBatchSentMessageReadUserReq(object):
    batch_message_id: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "batch_message_id"}
    )  # 待查询的批量消息的ID, 示例值："bm_dc13264520392913993dd051dba21dcf"


@attr.s
class GetBatchSentMessageReadUserRespReadUser(object):
    read_count: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "read_count"}
    )  # 已读的人数
    total_count: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "total_count"}
    )  # 推送的总人数


@attr.s
class GetBatchSentMessageReadUserResp(object):
    read_user: GetBatchSentMessageReadUserRespReadUser = attr.ib(
        default=None, metadata={"req_type": "json", "key": "read_user"}
    )  # 批量发送消息的用户阅读情况


def _gen_get_batch_sent_message_read_user_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetBatchSentMessageReadUserResp,
        scope="Message",
        api="GetBatchSentMessageReadUser",
        method="GET",
        url="https://open.feishu.cn/open-apis/im/v1/batch_messages/:batch_message_id/read_user",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
