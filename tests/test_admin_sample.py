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
class TestAdminSampleMockGetTokenFailed(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestAdminSampleMockGetTokenFailed, self).__init__(*args, **kwargs)
        self.cli = app_all_permission.ins()
        self.cli.auth.get_tenant_access_token = mock_get_tenant_access_token_failed
        self.cli.auth.get_app_access_token = mock_get_tenant_access_token_failed
        self.module_cli = self.cli.admin

    def test_mock_get_token_get_admin_dept_stats(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_admin_dept_stats(pylark.GetAdminDeptStatsReq())

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_get_admin_user_stats(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_admin_user_stats(pylark.GetAdminUserStatsReq())

        assert "msg=failed" in f"{e}"


# mock mock self func
class TestAdminSampleMockSelfFuncFailed(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestAdminSampleMockSelfFuncFailed, self).__init__(*args, **kwargs)
        self.cli = app_all_permission.ins()
        self.module_cli = self.cli.admin

    def test_mock_self_func_get_admin_dept_stats(self):
        origin_func = self.module_cli.get_admin_dept_stats
        self.module_cli.get_admin_dept_stats = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_admin_dept_stats(pylark.GetAdminDeptStatsReq())

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.get_admin_dept_stats = origin_func

    def test_mock_self_func_get_admin_user_stats(self):
        origin_func = self.module_cli.get_admin_user_stats
        self.module_cli.get_admin_user_stats = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_admin_user_stats(pylark.GetAdminUserStatsReq())

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.get_admin_user_stats = origin_func


# mock raw request
class TestAdminSampleMockRawRequestFailed(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestAdminSampleMockRawRequestFailed, self).__init__(*args, **kwargs)
        self.cli = app_all_permission.ins()
        self.module_cli = self.cli.admin
        self.cli.raw_request = mock_raw_request

    def test_mock_raw_request_get_admin_dept_stats(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_admin_dept_stats(pylark.GetAdminDeptStatsReq())

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_get_admin_user_stats(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_admin_user_stats(pylark.GetAdminUserStatsReq())

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg


# real request
class TestAdminSampleRealRequestFailed(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestAdminSampleRealRequestFailed, self).__init__(*args, **kwargs)
        self.cli = app_no_permission.ins()
        self.module_cli = self.cli.admin

    def test_real_request_get_admin_dept_stats(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_admin_dept_stats(pylark.GetAdminDeptStatsReq())

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_get_admin_user_stats(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_admin_user_stats(pylark.GetAdminUserStatsReq())

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
