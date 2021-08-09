# Code generated by lark_sdk_gen. DO NOT EDIT.

import typing
from pylark.lark_request import Response
from pylark.api_service_contact_user_create import (
    CreateUserReq,
    CreateUserResp,
    _gen_create_user_req,
)
from pylark.api_service_contact_user_delete import (
    DeleteUserReq,
    DeleteUserResp,
    _gen_delete_user_req,
)
from pylark.api_service_contact_user_get import (
    GetUserReq,
    GetUserResp,
    _gen_get_user_req,
)
from pylark.api_service_contact_user_get_batch import (
    BatchGetUserReq,
    BatchGetUserResp,
    _gen_batch_get_user_req,
)
from pylark.api_service_contact_user_get_batch_by_id import (
    BatchGetUserByIDReq,
    BatchGetUserByIDResp,
    _gen_batch_get_user_by_id_req,
)
from pylark.api_service_contact_user_get_list import (
    GetUserListReq,
    GetUserListResp,
    _gen_get_user_list_req,
)
from pylark.api_service_contact_user_update_patch import (
    UpdateUserPatchReq,
    UpdateUserPatchResp,
    _gen_update_user_patch_req,
)
from pylark.api_service_contact_user_update import (
    UpdateUserReq,
    UpdateUserResp,
    _gen_update_user_req,
)
from pylark.api_service_contact_department_create import (
    CreateDepartmentReq,
    CreateDepartmentResp,
    _gen_create_department_req,
)
from pylark.api_service_contact_department_get import (
    GetDepartmentReq,
    GetDepartmentResp,
    _gen_get_department_req,
)
from pylark.api_service_contact_department_get_list import (
    GetDepartmentListReq,
    GetDepartmentListResp,
    _gen_get_department_list_req,
)
from pylark.api_service_contact_department_get_parent import (
    GetParentDepartmentReq,
    GetParentDepartmentResp,
    _gen_get_parent_department_req,
)
from pylark.api_service_contact_department_search import (
    SearchDepartmentReq,
    SearchDepartmentResp,
    _gen_search_department_req,
)
from pylark.api_service_contact_department_update_patch import (
    UpdateDepartmentPatchReq,
    UpdateDepartmentPatchResp,
    _gen_update_department_patch_req,
)
from pylark.api_service_contact_department_update import (
    UpdateDepartmentReq,
    UpdateDepartmentResp,
    _gen_update_department_req,
)
from pylark.api_service_contact_department_delete import (
    DeleteDepartmentReq,
    DeleteDepartmentResp,
    _gen_delete_department_req,
)
from pylark.api_service_contact_employee_type_enums_list import (
    GetEmployeeTypeEnumListReq,
    GetEmployeeTypeEnumListResp,
    _gen_get_employee_type_enum_list_req,
)
from pylark.api_service_contact_employee_type_enums_update import (
    UpdateEmployeeTypeEnumPatchReq,
    UpdateEmployeeTypeEnumPatchResp,
    _gen_update_employee_type_enum_patch_req,
)
from pylark.api_service_contact_employee_type_enums_delete import (
    DeleteEmployeeTypeEnumReq,
    DeleteEmployeeTypeEnumResp,
    _gen_delete_employee_type_enum_req,
)
from pylark.api_service_contact_employee_type_enums_create import (
    CreateEmployeeTypeEnumReq,
    CreateEmployeeTypeEnumResp,
    _gen_create_employee_type_enum_req,
)
from pylark.api_service_contact_custom_attr_list import (
    GetContactCustomAttrListReq,
    GetContactCustomAttrListResp,
    _gen_get_contact_custom_attr_list_req,
)


if typing.TYPE_CHECKING:
    from lark import Lark


class LarkContactService(object):
    cli: "Lark"

    def __init__(self, cli: "Lark"):
        self.cli = cli

    def create_user(
        self, request: CreateUserReq, options: typing.List[str] = None
    ) -> typing.Tuple[CreateUserResp, Response]:
        return self.cli.raw_request(_gen_create_user_req(request, options))

    def delete_user(
        self, request: DeleteUserReq, options: typing.List[str] = None
    ) -> typing.Tuple[DeleteUserResp, Response]:
        return self.cli.raw_request(_gen_delete_user_req(request, options))

    def get_user(
        self, request: GetUserReq, options: typing.List[str] = None
    ) -> typing.Tuple[GetUserResp, Response]:
        return self.cli.raw_request(_gen_get_user_req(request, options))

    def batch_get_user(
        self, request: BatchGetUserReq, options: typing.List[str] = None
    ) -> typing.Tuple[BatchGetUserResp, Response]:
        return self.cli.raw_request(_gen_batch_get_user_req(request, options))

    def batch_get_user_by_id(
        self, request: BatchGetUserByIDReq, options: typing.List[str] = None
    ) -> typing.Tuple[BatchGetUserByIDResp, Response]:
        return self.cli.raw_request(_gen_batch_get_user_by_id_req(request, options))

    def get_user_list(
        self, request: GetUserListReq, options: typing.List[str] = None
    ) -> typing.Tuple[GetUserListResp, Response]:
        return self.cli.raw_request(_gen_get_user_list_req(request, options))

    def update_user_patch(
        self, request: UpdateUserPatchReq, options: typing.List[str] = None
    ) -> typing.Tuple[UpdateUserPatchResp, Response]:
        return self.cli.raw_request(_gen_update_user_patch_req(request, options))

    def update_user(
        self, request: UpdateUserReq, options: typing.List[str] = None
    ) -> typing.Tuple[UpdateUserResp, Response]:
        return self.cli.raw_request(_gen_update_user_req(request, options))

    def create_department(
        self, request: CreateDepartmentReq, options: typing.List[str] = None
    ) -> typing.Tuple[CreateDepartmentResp, Response]:
        return self.cli.raw_request(_gen_create_department_req(request, options))

    def get_department(
        self, request: GetDepartmentReq, options: typing.List[str] = None
    ) -> typing.Tuple[GetDepartmentResp, Response]:
        return self.cli.raw_request(_gen_get_department_req(request, options))

    def get_department_list(
        self, request: GetDepartmentListReq, options: typing.List[str] = None
    ) -> typing.Tuple[GetDepartmentListResp, Response]:
        return self.cli.raw_request(_gen_get_department_list_req(request, options))

    def get_parent_department(
        self, request: GetParentDepartmentReq, options: typing.List[str] = None
    ) -> typing.Tuple[GetParentDepartmentResp, Response]:
        return self.cli.raw_request(_gen_get_parent_department_req(request, options))

    def search_department(
        self, request: SearchDepartmentReq, options: typing.List[str] = None
    ) -> typing.Tuple[SearchDepartmentResp, Response]:
        return self.cli.raw_request(_gen_search_department_req(request, options))

    def update_department_patch(
        self, request: UpdateDepartmentPatchReq, options: typing.List[str] = None
    ) -> typing.Tuple[UpdateDepartmentPatchResp, Response]:
        return self.cli.raw_request(_gen_update_department_patch_req(request, options))

    def update_department(
        self, request: UpdateDepartmentReq, options: typing.List[str] = None
    ) -> typing.Tuple[UpdateDepartmentResp, Response]:
        return self.cli.raw_request(_gen_update_department_req(request, options))

    def delete_department(
        self, request: DeleteDepartmentReq, options: typing.List[str] = None
    ) -> typing.Tuple[DeleteDepartmentResp, Response]:
        return self.cli.raw_request(_gen_delete_department_req(request, options))

    def get_employee_type_enum_list(
        self, request: GetEmployeeTypeEnumListReq, options: typing.List[str] = None
    ) -> typing.Tuple[GetEmployeeTypeEnumListResp, Response]:
        return self.cli.raw_request(
            _gen_get_employee_type_enum_list_req(request, options)
        )

    def update_employee_type_enum_patch(
        self, request: UpdateEmployeeTypeEnumPatchReq, options: typing.List[str] = None
    ) -> typing.Tuple[UpdateEmployeeTypeEnumPatchResp, Response]:
        return self.cli.raw_request(
            _gen_update_employee_type_enum_patch_req(request, options)
        )

    def delete_employee_type_enum(
        self, request: DeleteEmployeeTypeEnumReq, options: typing.List[str] = None
    ) -> typing.Tuple[DeleteEmployeeTypeEnumResp, Response]:
        return self.cli.raw_request(
            _gen_delete_employee_type_enum_req(request, options)
        )

    def create_employee_type_enum(
        self, request: CreateEmployeeTypeEnumReq, options: typing.List[str] = None
    ) -> typing.Tuple[CreateEmployeeTypeEnumResp, Response]:
        return self.cli.raw_request(
            _gen_create_employee_type_enum_req(request, options)
        )

    def get_contact_custom_attr_list(
        self, request: GetContactCustomAttrListReq, options: typing.List[str] = None
    ) -> typing.Tuple[GetContactCustomAttrListResp, Response]:
        return self.cli.raw_request(
            _gen_get_contact_custom_attr_list_req(request, options)
        )
