# Code generated by lark_sdk_gen. DO NOT EDIT.

import typing
from pylark.lark_request import Response

from pylark.api_service_mail_mail_group_create import (
    CreateMailGroupReq,
    CreateMailGroupResp,
    _gen_create_mailgroup_req,
)
from pylark.api_service_mail_mail_group_get import (
    GetMailGroupReq,
    GetMailGroupResp,
    _gen_get_mailgroup_req,
)
from pylark.api_service_mail_mail_group_get_list import (
    GetMailGroupListReq,
    GetMailGroupListResp,
    _gen_get_mail_group_list_req,
)
from pylark.api_service_mail_mail_group_patch import (
    UpdateMailGroupPatchReq,
    UpdateMailGroupPatchResp,
    _gen_update_mail_group_patch_req,
)
from pylark.api_service_mail_mail_group_update import (
    UpdateMailGroupReq,
    UpdateMailGroupResp,
    _gen_update_mailgroup_req,
)
from pylark.api_service_mail_mail_group_delete import (
    DeleteMailGroupReq,
    DeleteMailGroupResp,
    _gen_delete_mailgroup_req,
)
from pylark.api_service_mail_mail_group_member_create import (
    CreateMailGroupMemberReq,
    CreateMailGroupMemberResp,
    _gen_create_mail_group_member_req,
)
from pylark.api_service_mail_mail_group_member_get import (
    GetMailGroupMemberReq,
    GetMailGroupMemberResp,
    _gen_get_mail_group_member_req,
)
from pylark.api_service_mail_mail_group_member_get_list import (
    GetMailGroupMemberListReq,
    GetMailGroupMemberListResp,
    _gen_get_mail_group_member_list_req,
)
from pylark.api_service_mail_mail_group_member_delete import (
    DeleteMailGroupMemberReq,
    DeleteMailGroupMemberResp,
    _gen_delete_mail_group_member_req,
)
from pylark.api_service_mail_mail_group_permission_member_create import (
    CreateMailGroupPermissionMemberReq,
    CreateMailGroupPermissionMemberResp,
    _gen_create_mail_group_permission_member_req,
)
from pylark.api_service_mail_mail_group_permission_member_get import (
    GetMailGroupPermissionMemberReq,
    GetMailGroupPermissionMemberResp,
    _gen_get_mail_group_permission_member_req,
)
from pylark.api_service_mail_mail_group_permission_member_get_list import (
    GetMailGroupPermissionMemberListReq,
    GetMailGroupPermissionMemberListResp,
    _gen_get_mail_group_permission_member_list_req,
)
from pylark.api_service_mail_mail_group_permission_member_delete import (
    DeleteMailGroupPermissionMemberReq,
    DeleteMailGroupPermissionMemberResp,
    _gen_delete_mail_group_permission_member_req,
)
from pylark.api_service_mail_public_mailbox_create import (
    CreatePublicMailboxReq,
    CreatePublicMailboxResp,
    _gen_create_public_mailbox_req,
)
from pylark.api_service_mail_public_mailbox_get import (
    GetPublicMailboxReq,
    GetPublicMailboxResp,
    _gen_get_public_mailbox_req,
)
from pylark.api_service_mail_public_mailbox_get_list import (
    GetPublicMailboxListReq,
    GetPublicMailboxListResp,
    _gen_get_public_mailbox_list_req,
)
from pylark.api_service_mail_public_mailbox_patch import (
    UpdatePublicMailboxPatchReq,
    UpdatePublicMailboxPatchResp,
    _gen_update_public_mailbox_patch_req,
)
from pylark.api_service_mail_public_mailbox_update import (
    UpdatePublicMailboxReq,
    UpdatePublicMailboxResp,
    _gen_update_public_mailbox_req,
)
from pylark.api_service_mail_public_mailbox_delete import (
    DeletePublicMailboxReq,
    DeletePublicMailboxResp,
    _gen_delete_public_mailbox_req,
)
from pylark.api_service_mail_public_mailbox_member_create import (
    CreatePublicMailboxMemberReq,
    CreatePublicMailboxMemberResp,
    _gen_create_public_mailbox_member_req,
)
from pylark.api_service_mail_public_mailbox_member_get import (
    GetPublicMailboxMemberReq,
    GetPublicMailboxMemberResp,
    _gen_get_public_mailbox_member_req,
)
from pylark.api_service_mail_public_mailbox_member_get_list import (
    GetPublicMailboxMemberListReq,
    GetPublicMailboxMemberListResp,
    _gen_get_public_mailbox_member_list_req,
)
from pylark.api_service_mail_public_mailbox_member_delete import (
    DeletePublicMailboxMemberReq,
    DeletePublicMailboxMemberResp,
    _gen_delete_public_mailbox_member_req,
)
from pylark.api_service_mail_public_mailbox_member_clear import (
    ClearPublicMailboxMemberReq,
    ClearPublicMailboxMemberResp,
    _gen_clear_public_mailbox_member_req,
)


if typing.TYPE_CHECKING:
    from lark import Lark


class LarkMailService(object):
    cli: "Lark"

    def __init__(self, cli: "Lark"):
        self.cli = cli

    def create_mailgroup(
        self, request: CreateMailGroupReq, options: typing.List[str] = None
    ) -> typing.Tuple[CreateMailGroupResp, Response]:
        return self.cli.raw_request(_gen_create_mailgroup_req(request, options))

    def get_mailgroup(
        self, request: GetMailGroupReq, options: typing.List[str] = None
    ) -> typing.Tuple[GetMailGroupResp, Response]:
        return self.cli.raw_request(_gen_get_mailgroup_req(request, options))

    def get_mail_group_list(
        self, request: GetMailGroupListReq, options: typing.List[str] = None
    ) -> typing.Tuple[GetMailGroupListResp, Response]:
        return self.cli.raw_request(_gen_get_mail_group_list_req(request, options))

    def update_mail_group_patch(
        self, request: UpdateMailGroupPatchReq, options: typing.List[str] = None
    ) -> typing.Tuple[UpdateMailGroupPatchResp, Response]:
        return self.cli.raw_request(_gen_update_mail_group_patch_req(request, options))

    def update_mailgroup(
        self, request: UpdateMailGroupReq, options: typing.List[str] = None
    ) -> typing.Tuple[UpdateMailGroupResp, Response]:
        return self.cli.raw_request(_gen_update_mailgroup_req(request, options))

    def delete_mailgroup(
        self, request: DeleteMailGroupReq, options: typing.List[str] = None
    ) -> typing.Tuple[DeleteMailGroupResp, Response]:
        return self.cli.raw_request(_gen_delete_mailgroup_req(request, options))

    def create_mail_group_member(
        self, request: CreateMailGroupMemberReq, options: typing.List[str] = None
    ) -> typing.Tuple[CreateMailGroupMemberResp, Response]:
        return self.cli.raw_request(_gen_create_mail_group_member_req(request, options))

    def get_mail_group_member(
        self, request: GetMailGroupMemberReq, options: typing.List[str] = None
    ) -> typing.Tuple[GetMailGroupMemberResp, Response]:
        return self.cli.raw_request(_gen_get_mail_group_member_req(request, options))

    def get_mail_group_member_list(
        self, request: GetMailGroupMemberListReq, options: typing.List[str] = None
    ) -> typing.Tuple[GetMailGroupMemberListResp, Response]:
        return self.cli.raw_request(
            _gen_get_mail_group_member_list_req(request, options)
        )

    def delete_mail_group_member(
        self, request: DeleteMailGroupMemberReq, options: typing.List[str] = None
    ) -> typing.Tuple[DeleteMailGroupMemberResp, Response]:
        return self.cli.raw_request(_gen_delete_mail_group_member_req(request, options))

    def create_mail_group_permission_member(
        self,
        request: CreateMailGroupPermissionMemberReq,
        options: typing.List[str] = None,
    ) -> typing.Tuple[CreateMailGroupPermissionMemberResp, Response]:
        return self.cli.raw_request(
            _gen_create_mail_group_permission_member_req(request, options)
        )

    def get_mail_group_permission_member(
        self, request: GetMailGroupPermissionMemberReq, options: typing.List[str] = None
    ) -> typing.Tuple[GetMailGroupPermissionMemberResp, Response]:
        return self.cli.raw_request(
            _gen_get_mail_group_permission_member_req(request, options)
        )

    def get_mail_group_permission_member_list(
        self,
        request: GetMailGroupPermissionMemberListReq,
        options: typing.List[str] = None,
    ) -> typing.Tuple[GetMailGroupPermissionMemberListResp, Response]:
        return self.cli.raw_request(
            _gen_get_mail_group_permission_member_list_req(request, options)
        )

    def delete_mail_group_permission_member(
        self,
        request: DeleteMailGroupPermissionMemberReq,
        options: typing.List[str] = None,
    ) -> typing.Tuple[DeleteMailGroupPermissionMemberResp, Response]:
        return self.cli.raw_request(
            _gen_delete_mail_group_permission_member_req(request, options)
        )

    def create_public_mailbox(
        self, request: CreatePublicMailboxReq, options: typing.List[str] = None
    ) -> typing.Tuple[CreatePublicMailboxResp, Response]:
        return self.cli.raw_request(_gen_create_public_mailbox_req(request, options))

    def get_public_mailbox(
        self, request: GetPublicMailboxReq, options: typing.List[str] = None
    ) -> typing.Tuple[GetPublicMailboxResp, Response]:
        return self.cli.raw_request(_gen_get_public_mailbox_req(request, options))

    def get_public_mailbox_list(
        self, request: GetPublicMailboxListReq, options: typing.List[str] = None
    ) -> typing.Tuple[GetPublicMailboxListResp, Response]:
        return self.cli.raw_request(_gen_get_public_mailbox_list_req(request, options))

    def update_public_mailbox_patch(
        self, request: UpdatePublicMailboxPatchReq, options: typing.List[str] = None
    ) -> typing.Tuple[UpdatePublicMailboxPatchResp, Response]:
        return self.cli.raw_request(
            _gen_update_public_mailbox_patch_req(request, options)
        )

    def update_public_mailbox(
        self, request: UpdatePublicMailboxReq, options: typing.List[str] = None
    ) -> typing.Tuple[UpdatePublicMailboxResp, Response]:
        return self.cli.raw_request(_gen_update_public_mailbox_req(request, options))

    def delete_public_mailbox(
        self, request: DeletePublicMailboxReq, options: typing.List[str] = None
    ) -> typing.Tuple[DeletePublicMailboxResp, Response]:
        return self.cli.raw_request(_gen_delete_public_mailbox_req(request, options))

    def create_public_mailbox_member(
        self, request: CreatePublicMailboxMemberReq, options: typing.List[str] = None
    ) -> typing.Tuple[CreatePublicMailboxMemberResp, Response]:
        return self.cli.raw_request(
            _gen_create_public_mailbox_member_req(request, options)
        )

    def get_public_mailbox_member(
        self, request: GetPublicMailboxMemberReq, options: typing.List[str] = None
    ) -> typing.Tuple[GetPublicMailboxMemberResp, Response]:
        return self.cli.raw_request(
            _gen_get_public_mailbox_member_req(request, options)
        )

    def get_public_mailbox_member_list(
        self, request: GetPublicMailboxMemberListReq, options: typing.List[str] = None
    ) -> typing.Tuple[GetPublicMailboxMemberListResp, Response]:
        return self.cli.raw_request(
            _gen_get_public_mailbox_member_list_req(request, options)
        )

    def delete_public_mailbox_member(
        self, request: DeletePublicMailboxMemberReq, options: typing.List[str] = None
    ) -> typing.Tuple[DeletePublicMailboxMemberResp, Response]:
        return self.cli.raw_request(
            _gen_delete_public_mailbox_member_req(request, options)
        )

    def clear_public_mailbox_member(
        self, request: ClearPublicMailboxMemberReq, options: typing.List[str] = None
    ) -> typing.Tuple[ClearPublicMailboxMemberResp, Response]:
        return self.cli.raw_request(
            _gen_clear_public_mailbox_member_req(request, options)
        )
