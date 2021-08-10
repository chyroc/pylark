# Code generated by lark_sdk_gen. DO NOT EDIT.

from tests.test_conf import app_all_permission
import unittest
import pylark
import pytest
from tests.test_helper import mock_get_tenant_access_token_failed


class TestOKRSampleRequestFailed(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestOKRSampleRequestFailed, self).__init__(*args, **kwargs)
        self.cli = app_all_permission.ins()
        self.cli.auth.get_tenant_access_token = mock_get_tenant_access_token_failed
        self.cli.auth.get_app_access_token = mock_get_tenant_access_token_failed
        self.module_cli = self.cli.okr

    def test_request_failed_get_okr_period_list(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_okr_period_list(pylark.GetOKRPeriodListReq())

        assert "msg=failed" in f"{e}"

    def test_request_failed_batch_get_okr(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.batch_get_okr(pylark.BatchGetOKRReq())

        assert "msg=failed" in f"{e}"

    def test_request_failed_get_user_okr_list(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_user_okr_list(pylark.GetUserOKRListReq())

        assert "msg=failed" in f"{e}"
