# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing


@attr.s
class UpdatePublicMailboxPatchReq(object):
    public_mailbox_id: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 公共邮箱唯一标识或公共邮箱地址, 示例值："xxxxxxxxxxxxxxx 或 test_public_mailbox@xxx.xx"
    name: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 公共邮箱名称, 示例值："test public mailbox"


@attr.s
class UpdatePublicMailboxPatchResp(object):
    public_mailbox_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 公共邮箱唯一标识
    email: str = attr.ib(default="", metadata={"req_type": "json"})  # 公共邮箱地址
    name: str = attr.ib(default="", metadata={"req_type": "json"})  # 公共邮箱名称


def _gen_update_public_mailbox_patch_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=UpdatePublicMailboxPatchResp,
        scope="Mail",
        api="UpdatePublicMailboxPatch",
        method="PATCH",
        url="https://open.feishu.cn/open-apis/mail/v1/public_mailboxes/:public_mailbox_id",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
