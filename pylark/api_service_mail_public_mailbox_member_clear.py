# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing


@attr.s
class ClearPublicMailboxMemberReq(object):
    public_mailbox_id: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 公共邮箱唯一标识或公共邮箱地址, 示例值："xxxxxxxxxxxxxxx 或 test_public_mailbox@xxx.xx"


@attr.s
class ClearPublicMailboxMemberResp(object):
    pass


def _gen_clear_public_mailbox_member_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=ClearPublicMailboxMemberResp,
        scope="Mail",
        api="ClearPublicMailboxMember",
        method="POST",
        url="https://open.feishu.cn/open-apis/mail/v1/public_mailboxes/:public_mailbox_id/members/clear",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
