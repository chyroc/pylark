# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
from pylark import lark_type_enum, lark_type_sheet
import attr
import typing
import io


@attr.s
class GetPublicMailboxMemberReqUserIDType(object):
    pass


@attr.s
class GetPublicMailboxMemberReq(object):
    user_id_type: lark_type_enum.IDType = attr.ib(
        default=None, metadata={"req_type": "query", "key": "user_id_type"}
    )  # 用户 ID 类型, 示例值："open_id", 可选值有: `open_id`：用户的 open id, `union_id`：用户的 union id, `user_id`：用户的 user id, 默认值: `open_id`, 当值为 `user_id`, 字段权限要求: 获取用户 user ID
    public_mailbox_id: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "public_mailbox_id"}
    )  # 公共邮箱唯一标识或公共邮箱地址, 示例值："xxxxxxxxxxxxxxx 或 test_public_mailbox@xxx.xx"
    member_id: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "member_id"}
    )  # 公共邮箱内成员唯一标识, 示例值："xxxxxxxxxxxxxxx"


@attr.s
class GetPublicMailboxMemberRespType(object):
    pass


@attr.s
class GetPublicMailboxMemberResp(object):
    member_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "member_id"}
    )  # 公共邮箱内成员唯一标识
    user_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "user_id"}
    )  # 租户内用户的唯一标识（当成员类型是USER时有值）
    type: GetPublicMailboxMemberRespType = attr.ib(
        factory=lambda: GetPublicMailboxMemberRespType(),
        metadata={"req_type": "json", "key": "type"},
    )  # 成员类型, 可选值有: `USER`：内部用户


def _gen_get_public_mailbox_member_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetPublicMailboxMemberResp,
        scope="Mail",
        api="GetPublicMailboxMember",
        method="GET",
        url="https://open.feishu.cn/open-apis/mail/v1/public_mailboxes/:public_mailbox_id/members/:member_id",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
