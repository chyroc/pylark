# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
from pylark import lark_type_enum, lark_type_sheet
import attr
import typing
import io


@attr.s
class DeleteMailGroupPermissionMemberReq(object):
    mailgroup_id: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "mailgroup_id"}
    )  # The unique ID or email address of a mail group, 示例值："xxxxxxxxxxxxxxx or test_mail_group@xxx.xx"
    permission_member_id: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "permission_member_id"}
    )  # The unique ID of a member in this permission group, 示例值："xxxxxxxxxxxxxxx"


@attr.s
class DeleteMailGroupPermissionMemberResp(object):
    pass


def _gen_delete_mail_group_permission_member_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=DeleteMailGroupPermissionMemberResp,
        scope="Mail",
        api="DeleteMailGroupPermissionMember",
        method="DELETE",
        url="https://open.feishu.cn/open-apis/mail/v1/mailgroups/:mailgroup_id/permission_members/:permission_member_id",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
