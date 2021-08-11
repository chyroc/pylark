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
class TestOKRSampleMockGetTokenFailed(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestOKRSampleMockGetTokenFailed, self).__init__(*args, **kwargs)
        self.cli = app_all_permission.ins()
        self.cli.auth.get_tenant_access_token = mock_get_tenant_access_token_failed
        self.cli.auth.get_app_access_token = mock_get_tenant_access_token_failed
        self.module_cli = self.cli.okr

    def test_mock_get_token_get_okr_period_list(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_okr_period_list(pylark.GetOKRPeriodListReq())

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_batch_get_okr(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.batch_get_okr(pylark.BatchGetOKRReq())

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_get_user_okr_list(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_user_okr_list(pylark.GetUserOKRListReq())

        assert "msg=failed" in f"{e}"


# mock mock self func
class TestOKRSampleMockSelfFuncFailed(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestOKRSampleMockSelfFuncFailed, self).__init__(*args, **kwargs)
        self.cli = app_all_permission.ins()
        self.module_cli = self.cli.okr

    def test_mock_self_func_get_okr_period_list(self):
        origin_func = self.module_cli.get_okr_period_list
        self.module_cli.get_okr_period_list = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_okr_period_list(pylark.GetOKRPeriodListReq())

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.get_okr_period_list = origin_func

    def test_mock_self_func_batch_get_okr(self):
        origin_func = self.module_cli.batch_get_okr
        self.module_cli.batch_get_okr = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.batch_get_okr(pylark.BatchGetOKRReq())

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.batch_get_okr = origin_func

    def test_mock_self_func_get_user_okr_list(self):
        origin_func = self.module_cli.get_user_okr_list
        self.module_cli.get_user_okr_list = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_user_okr_list(pylark.GetUserOKRListReq())

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.get_user_okr_list = origin_func


# mock raw request
class TestOKRSampleMockRawRequestFailed(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestOKRSampleMockRawRequestFailed, self).__init__(*args, **kwargs)
        self.cli = app_all_permission.ins()
        self.module_cli = self.cli.okr
        self.cli.raw_request = mock_raw_request

    def test_mock_raw_request_get_okr_period_list(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_okr_period_list(pylark.GetOKRPeriodListReq())

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_batch_get_okr(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.batch_get_okr(pylark.BatchGetOKRReq())

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_get_user_okr_list(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_user_okr_list(
                pylark.GetUserOKRListReq(
                    user_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg


# real request
class TestOKRSampleRealRequestFailed(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestOKRSampleRealRequestFailed, self).__init__(*args, **kwargs)
        self.cli = app_no_permission.ins()
        self.module_cli = self.cli.okr

    def test_real_request_get_okr_period_list(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_okr_period_list(pylark.GetOKRPeriodListReq())

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_batch_get_okr(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.batch_get_okr(pylark.BatchGetOKRReq())

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_get_user_okr_list(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_user_okr_list(
                pylark.GetUserOKRListReq(
                    user_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
