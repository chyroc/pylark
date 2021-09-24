# Code generated by lark_sdk_gen. DO NOT EDIT.

import unittest
import pylark
import pytest
from tests.test_conf import app_all_permission, app_no_permission
from tests.test_helper import mock_get_tenant_access_token_failed


def mock(*args, **kwargs):
    raise pylark.PyLarkError(scope="scope", func="func", code=1, msg="mock-failed")


def mock_raw_request(*args, **kwargs):
    raise pylark.PyLarkError(
        scope="scope", func="func", code=1, msg="mock-raw-request-failed"
    )


# mock get token
class TestContactSampleMockGetTokenFailed(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestContactSampleMockGetTokenFailed, self).__init__(*args, **kwargs)
        self.cli = app_all_permission.ins()
        self.cli.auth.get_tenant_access_token = mock_get_tenant_access_token_failed
        self.cli.auth.get_app_access_token = mock_get_tenant_access_token_failed
        self.module_cli = self.cli.contact

    def test_mock_get_token_create_user(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.create_user(pylark.CreateUserReq())

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_delete_user(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.delete_user(pylark.DeleteUserReq())

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_get_user(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_user(pylark.GetUserReq())

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_batch_get_user(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.batch_get_user(pylark.BatchGetUserReq())

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_batch_get_user_by_id(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.batch_get_user_by_id(pylark.BatchGetUserByIDReq())

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_get_user_list(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_user_list(pylark.GetUserListReq())

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_update_user_patch(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.update_user_patch(pylark.UpdateUserPatchReq())

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_update_user(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.update_user(pylark.UpdateUserReq())

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_create_department(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.create_department(pylark.CreateDepartmentReq())

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_get_department(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_department(pylark.GetDepartmentReq())

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_get_department_list(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_department_list(pylark.GetDepartmentListReq())

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_get_parent_department(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_parent_department(pylark.GetParentDepartmentReq())

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_update_department_patch(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.update_department_patch(pylark.UpdateDepartmentPatchReq())

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_update_department(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.update_department(pylark.UpdateDepartmentReq())

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_delete_department(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.delete_department(pylark.DeleteDepartmentReq())

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_create_contact_group(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.create_contact_group(pylark.CreateContactGroupReq())

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_update_contact_group(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.update_contact_group(pylark.UpdateContactGroupReq())

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_delete_contact_group(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.delete_contact_group(pylark.DeleteContactGroupReq())

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_get_contact_group(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_contact_group(pylark.GetContactGroupReq())

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_get_contact_group_list(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_contact_group_list(pylark.GetContactGroupListReq())

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_add_contact_group_member(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.add_contact_group_member(pylark.AddContactGroupMemberReq())

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_delete_contact_group_member(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.delete_contact_group_member(
                pylark.DeleteContactGroupMemberReq()
            )

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_get_contact_group_member(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_contact_group_member(pylark.GetContactGroupMemberReq())

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_get_employee_type_enum_list(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_employee_type_enum_list(
                pylark.GetEmployeeTypeEnumListReq()
            )

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_update_employee_type_enum_patch(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.update_employee_type_enum_patch(
                pylark.UpdateEmployeeTypeEnumPatchReq()
            )

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_delete_employee_type_enum(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.delete_employee_type_enum(
                pylark.DeleteEmployeeTypeEnumReq()
            )

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_create_employee_type_enum(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.create_employee_type_enum(
                pylark.CreateEmployeeTypeEnumReq()
            )

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_get_contact_custom_attr_list(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_contact_custom_attr_list(
                pylark.GetContactCustomAttrListReq()
            )

        assert "msg=failed" in f"{e}"


# mock mock self func
class TestContactSampleMockSelfFuncFailed(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestContactSampleMockSelfFuncFailed, self).__init__(*args, **kwargs)
        self.cli = app_all_permission.ins()
        self.module_cli = self.cli.contact

    def test_mock_self_func_create_user(self):
        origin_func = self.module_cli.create_user
        self.module_cli.create_user = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.create_user(pylark.CreateUserReq())

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.create_user = origin_func

    def test_mock_self_func_delete_user(self):
        origin_func = self.module_cli.delete_user
        self.module_cli.delete_user = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.delete_user(pylark.DeleteUserReq())

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.delete_user = origin_func

    def test_mock_self_func_get_user(self):
        origin_func = self.module_cli.get_user
        self.module_cli.get_user = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_user(pylark.GetUserReq())

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.get_user = origin_func

    def test_mock_self_func_batch_get_user(self):
        origin_func = self.module_cli.batch_get_user
        self.module_cli.batch_get_user = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.batch_get_user(pylark.BatchGetUserReq())

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.batch_get_user = origin_func

    def test_mock_self_func_batch_get_user_by_id(self):
        origin_func = self.module_cli.batch_get_user_by_id
        self.module_cli.batch_get_user_by_id = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.batch_get_user_by_id(pylark.BatchGetUserByIDReq())

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.batch_get_user_by_id = origin_func

    def test_mock_self_func_get_user_list(self):
        origin_func = self.module_cli.get_user_list
        self.module_cli.get_user_list = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_user_list(pylark.GetUserListReq())

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.get_user_list = origin_func

    def test_mock_self_func_update_user_patch(self):
        origin_func = self.module_cli.update_user_patch
        self.module_cli.update_user_patch = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.update_user_patch(pylark.UpdateUserPatchReq())

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.update_user_patch = origin_func

    def test_mock_self_func_update_user(self):
        origin_func = self.module_cli.update_user
        self.module_cli.update_user = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.update_user(pylark.UpdateUserReq())

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.update_user = origin_func

    def test_mock_self_func_create_department(self):
        origin_func = self.module_cli.create_department
        self.module_cli.create_department = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.create_department(pylark.CreateDepartmentReq())

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.create_department = origin_func

    def test_mock_self_func_get_department(self):
        origin_func = self.module_cli.get_department
        self.module_cli.get_department = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_department(pylark.GetDepartmentReq())

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.get_department = origin_func

    def test_mock_self_func_get_department_list(self):
        origin_func = self.module_cli.get_department_list
        self.module_cli.get_department_list = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_department_list(pylark.GetDepartmentListReq())

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.get_department_list = origin_func

    def test_mock_self_func_get_parent_department(self):
        origin_func = self.module_cli.get_parent_department
        self.module_cli.get_parent_department = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_parent_department(pylark.GetParentDepartmentReq())

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.get_parent_department = origin_func

    def test_mock_self_func_update_department_patch(self):
        origin_func = self.module_cli.update_department_patch
        self.module_cli.update_department_patch = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.update_department_patch(pylark.UpdateDepartmentPatchReq())

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.update_department_patch = origin_func

    def test_mock_self_func_update_department(self):
        origin_func = self.module_cli.update_department
        self.module_cli.update_department = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.update_department(pylark.UpdateDepartmentReq())

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.update_department = origin_func

    def test_mock_self_func_delete_department(self):
        origin_func = self.module_cli.delete_department
        self.module_cli.delete_department = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.delete_department(pylark.DeleteDepartmentReq())

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.delete_department = origin_func

    def test_mock_self_func_create_contact_group(self):
        origin_func = self.module_cli.create_contact_group
        self.module_cli.create_contact_group = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.create_contact_group(pylark.CreateContactGroupReq())

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.create_contact_group = origin_func

    def test_mock_self_func_update_contact_group(self):
        origin_func = self.module_cli.update_contact_group
        self.module_cli.update_contact_group = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.update_contact_group(pylark.UpdateContactGroupReq())

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.update_contact_group = origin_func

    def test_mock_self_func_delete_contact_group(self):
        origin_func = self.module_cli.delete_contact_group
        self.module_cli.delete_contact_group = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.delete_contact_group(pylark.DeleteContactGroupReq())

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.delete_contact_group = origin_func

    def test_mock_self_func_get_contact_group(self):
        origin_func = self.module_cli.get_contact_group
        self.module_cli.get_contact_group = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_contact_group(pylark.GetContactGroupReq())

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.get_contact_group = origin_func

    def test_mock_self_func_get_contact_group_list(self):
        origin_func = self.module_cli.get_contact_group_list
        self.module_cli.get_contact_group_list = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_contact_group_list(pylark.GetContactGroupListReq())

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.get_contact_group_list = origin_func

    def test_mock_self_func_add_contact_group_member(self):
        origin_func = self.module_cli.add_contact_group_member
        self.module_cli.add_contact_group_member = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.add_contact_group_member(pylark.AddContactGroupMemberReq())

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.add_contact_group_member = origin_func

    def test_mock_self_func_delete_contact_group_member(self):
        origin_func = self.module_cli.delete_contact_group_member
        self.module_cli.delete_contact_group_member = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.delete_contact_group_member(
                pylark.DeleteContactGroupMemberReq()
            )

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.delete_contact_group_member = origin_func

    def test_mock_self_func_get_contact_group_member(self):
        origin_func = self.module_cli.get_contact_group_member
        self.module_cli.get_contact_group_member = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_contact_group_member(pylark.GetContactGroupMemberReq())

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.get_contact_group_member = origin_func

    def test_mock_self_func_get_employee_type_enum_list(self):
        origin_func = self.module_cli.get_employee_type_enum_list
        self.module_cli.get_employee_type_enum_list = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_employee_type_enum_list(
                pylark.GetEmployeeTypeEnumListReq()
            )

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.get_employee_type_enum_list = origin_func

    def test_mock_self_func_update_employee_type_enum_patch(self):
        origin_func = self.module_cli.update_employee_type_enum_patch
        self.module_cli.update_employee_type_enum_patch = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.update_employee_type_enum_patch(
                pylark.UpdateEmployeeTypeEnumPatchReq()
            )

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.update_employee_type_enum_patch = origin_func

    def test_mock_self_func_delete_employee_type_enum(self):
        origin_func = self.module_cli.delete_employee_type_enum
        self.module_cli.delete_employee_type_enum = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.delete_employee_type_enum(
                pylark.DeleteEmployeeTypeEnumReq()
            )

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.delete_employee_type_enum = origin_func

    def test_mock_self_func_create_employee_type_enum(self):
        origin_func = self.module_cli.create_employee_type_enum
        self.module_cli.create_employee_type_enum = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.create_employee_type_enum(
                pylark.CreateEmployeeTypeEnumReq()
            )

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.create_employee_type_enum = origin_func

    def test_mock_self_func_get_contact_custom_attr_list(self):
        origin_func = self.module_cli.get_contact_custom_attr_list
        self.module_cli.get_contact_custom_attr_list = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_contact_custom_attr_list(
                pylark.GetContactCustomAttrListReq()
            )

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.get_contact_custom_attr_list = origin_func


# mock raw request
class TestContactSampleMockRawRequestFailed(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestContactSampleMockRawRequestFailed, self).__init__(*args, **kwargs)
        self.cli = app_all_permission.ins()
        self.module_cli = self.cli.contact
        self.cli.raw_request = mock_raw_request

    def test_mock_raw_request_create_user(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.create_user(pylark.CreateUserReq())

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_delete_user(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.delete_user(
                pylark.DeleteUserReq(
                    user_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_get_user(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_user(
                pylark.GetUserReq(
                    user_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_batch_get_user(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.batch_get_user(pylark.BatchGetUserReq())

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_batch_get_user_by_id(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.batch_get_user_by_id(pylark.BatchGetUserByIDReq())

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_get_user_list(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_user_list(pylark.GetUserListReq())

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_update_user_patch(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.update_user_patch(
                pylark.UpdateUserPatchReq(
                    user_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_update_user(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.update_user(
                pylark.UpdateUserReq(
                    user_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_create_department(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.create_department(pylark.CreateDepartmentReq())

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_get_department(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_department(
                pylark.GetDepartmentReq(
                    department_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_get_department_list(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_department_list(pylark.GetDepartmentListReq())

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_get_parent_department(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_parent_department(pylark.GetParentDepartmentReq())

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_update_department_patch(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.update_department_patch(
                pylark.UpdateDepartmentPatchReq(
                    department_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_update_department(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.update_department(
                pylark.UpdateDepartmentReq(
                    department_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_delete_department(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.delete_department(
                pylark.DeleteDepartmentReq(
                    department_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_create_contact_group(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.create_contact_group(pylark.CreateContactGroupReq())

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_update_contact_group(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.update_contact_group(
                pylark.UpdateContactGroupReq(
                    group_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_delete_contact_group(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.delete_contact_group(
                pylark.DeleteContactGroupReq(
                    group_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_get_contact_group(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_contact_group(
                pylark.GetContactGroupReq(
                    group_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_get_contact_group_list(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_contact_group_list(pylark.GetContactGroupListReq())

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_add_contact_group_member(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.add_contact_group_member(
                pylark.AddContactGroupMemberReq(
                    group_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_delete_contact_group_member(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.delete_contact_group_member(
                pylark.DeleteContactGroupMemberReq(
                    group_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_get_contact_group_member(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_contact_group_member(
                pylark.GetContactGroupMemberReq(
                    group_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_get_employee_type_enum_list(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_employee_type_enum_list(
                pylark.GetEmployeeTypeEnumListReq()
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_update_employee_type_enum_patch(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.update_employee_type_enum_patch(
                pylark.UpdateEmployeeTypeEnumPatchReq(
                    enum_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_delete_employee_type_enum(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.delete_employee_type_enum(
                pylark.DeleteEmployeeTypeEnumReq(
                    enum_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_create_employee_type_enum(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.create_employee_type_enum(
                pylark.CreateEmployeeTypeEnumReq()
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_get_contact_custom_attr_list(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_contact_custom_attr_list(
                pylark.GetContactCustomAttrListReq()
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg


# real request
class TestContactSampleRealRequestFailed(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestContactSampleRealRequestFailed, self).__init__(*args, **kwargs)
        self.cli = app_no_permission.ins()
        self.module_cli = self.cli.contact

    def test_real_request_create_user(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.create_user(pylark.CreateUserReq())

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_delete_user(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.delete_user(
                pylark.DeleteUserReq(
                    user_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_get_user(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_user(
                pylark.GetUserReq(
                    user_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_batch_get_user(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.batch_get_user(pylark.BatchGetUserReq())

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_batch_get_user_by_id(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.batch_get_user_by_id(pylark.BatchGetUserByIDReq())

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_get_user_list(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_user_list(pylark.GetUserListReq())

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_update_user_patch(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.update_user_patch(
                pylark.UpdateUserPatchReq(
                    user_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_update_user(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.update_user(
                pylark.UpdateUserReq(
                    user_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_create_department(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.create_department(pylark.CreateDepartmentReq())

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_get_department(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_department(
                pylark.GetDepartmentReq(
                    department_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_get_department_list(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_department_list(pylark.GetDepartmentListReq())

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_get_parent_department(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_parent_department(pylark.GetParentDepartmentReq())

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_update_department_patch(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.update_department_patch(
                pylark.UpdateDepartmentPatchReq(
                    department_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_update_department(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.update_department(
                pylark.UpdateDepartmentReq(
                    department_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_delete_department(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.delete_department(
                pylark.DeleteDepartmentReq(
                    department_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_create_contact_group(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.create_contact_group(pylark.CreateContactGroupReq())

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_update_contact_group(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.update_contact_group(
                pylark.UpdateContactGroupReq(
                    group_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_delete_contact_group(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.delete_contact_group(
                pylark.DeleteContactGroupReq(
                    group_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_get_contact_group(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_contact_group(
                pylark.GetContactGroupReq(
                    group_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_get_contact_group_list(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_contact_group_list(pylark.GetContactGroupListReq())

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_add_contact_group_member(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.add_contact_group_member(
                pylark.AddContactGroupMemberReq(
                    group_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_delete_contact_group_member(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.delete_contact_group_member(
                pylark.DeleteContactGroupMemberReq(
                    group_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_get_contact_group_member(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_contact_group_member(
                pylark.GetContactGroupMemberReq(
                    group_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_get_employee_type_enum_list(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_employee_type_enum_list(
                pylark.GetEmployeeTypeEnumListReq()
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_update_employee_type_enum_patch(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.update_employee_type_enum_patch(
                pylark.UpdateEmployeeTypeEnumPatchReq(
                    enum_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_delete_employee_type_enum(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.delete_employee_type_enum(
                pylark.DeleteEmployeeTypeEnumReq(
                    enum_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_create_employee_type_enum(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.create_employee_type_enum(
                pylark.CreateEmployeeTypeEnumReq()
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_get_contact_custom_attr_list(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_contact_custom_attr_list(
                pylark.GetContactCustomAttrListReq()
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
