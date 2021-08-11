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
class TestAuthSampleMockGetTokenFailed(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestAuthSampleMockGetTokenFailed, self).__init__(*args, **kwargs)
        self.cli = app_all_permission.ins()
        self.cli.auth.get_tenant_access_token = mock_get_tenant_access_token_failed
        self.cli.auth.get_app_access_token = mock_get_tenant_access_token_failed
        self.module_cli = self.cli.auth

    def test_mock_get_token_get_access_token(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_access_token(pylark.GetAccessTokenReq())

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_refresh_access_token(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.refresh_access_token(pylark.RefreshAccessTokenReq())

        assert "msg=failed" in f"{e}"


# mock mock self func
class TestAuthSampleMockSelfFuncFailed(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestAuthSampleMockSelfFuncFailed, self).__init__(*args, **kwargs)
        self.cli = app_all_permission.ins()
        self.module_cli = self.cli.auth

    def test_mock_self_func_get_access_token(self):
        origin_func = self.module_cli.get_access_token
        self.module_cli.get_access_token = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_access_token(pylark.GetAccessTokenReq())

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.get_access_token = origin_func

    def test_mock_self_func_refresh_access_token(self):
        origin_func = self.module_cli.refresh_access_token
        self.module_cli.refresh_access_token = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.refresh_access_token(pylark.RefreshAccessTokenReq())

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.refresh_access_token = origin_func


# mock raw request
class TestAuthSampleMockRawRequestFailed(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestAuthSampleMockRawRequestFailed, self).__init__(*args, **kwargs)
        self.cli = app_all_permission.ins()
        self.module_cli = self.cli.auth
        self.cli.raw_request = mock_raw_request

    def test_mock_raw_request_get_access_token(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_access_token(pylark.GetAccessTokenReq())

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_refresh_access_token(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.refresh_access_token(pylark.RefreshAccessTokenReq())

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg


# real request
class TestAuthSampleRealRequestFailed(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestAuthSampleRealRequestFailed, self).__init__(*args, **kwargs)
        self.cli = app_no_permission.ins()
        self.module_cli = self.cli.auth

    def test_real_request_get_access_token(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_access_token(pylark.GetAccessTokenReq())

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_refresh_access_token(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.refresh_access_token(pylark.RefreshAccessTokenReq())

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
