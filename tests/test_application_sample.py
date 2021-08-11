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
class TestApplicationSampleMockGetTokenFailed(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestApplicationSampleMockGetTokenFailed, self).__init__(*args, **kwargs)
        self.cli = app_all_permission.ins()
        self.cli.auth.get_tenant_access_token = mock_get_tenant_access_token_failed
        self.cli.auth.get_app_access_token = mock_get_tenant_access_token_failed
        self.module_cli = self.cli.application

    def test_mock_get_token_is_application_user_admin(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.is_application_user_admin(
                pylark.IsApplicationUserAdminReq()
            )

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_get_application_user_admin_scope(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_application_user_admin_scope(
                pylark.GetApplicationUserAdminScopeReq()
            )

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_get_application_app_visibility(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_application_app_visibility(
                pylark.GetApplicationAppVisibilityReq()
            )

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_get_application_user_visible_app(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_application_user_visible_app(
                pylark.GetApplicationUserVisibleAppReq()
            )

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_get_application_app_list(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_application_app_list(pylark.GetApplicationAppListReq())

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_update_application_app_visibility(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.update_application_app_visibility(
                pylark.UpdateApplicationAppVisibilityReq()
            )

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_get_application_app_admin_user_list(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_application_app_admin_user_list(
                pylark.GetApplicationAppAdminUserListReq()
            )

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_check_user_is_in_application_paid_scope(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.check_user_is_in_application_paid_scope(
                pylark.CheckUserIsInApplicationPaidScopeReq()
            )

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_get_application_order_list(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_application_order_list(
                pylark.GetApplicationOrderListReq()
            )

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_get_application_order(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_application_order(pylark.GetApplicationOrderReq())

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_get_application_usage_overview(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_application_usage_overview(
                pylark.GetApplicationUsageOverviewReq()
            )

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_get_application_usage_trend(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_application_usage_trend(
                pylark.GetApplicationUsageTrendReq()
            )

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_get_application_usage_detail(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_application_usage_detail(
                pylark.GetApplicationUsageDetailReq()
            )

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_get_application_message_overview(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_application_message_overview(
                pylark.GetApplicationMessageOverviewReq()
            )

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_get_application_message_trend(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_application_message_trend(
                pylark.GetApplicationMessageTrendReq()
            )

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_get_application_message_detail(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_application_message_detail(
                pylark.GetApplicationMessageDetailReq()
            )

        assert "msg=failed" in f"{e}"


# mock mock self func
class TestApplicationSampleMockSelfFuncFailed(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestApplicationSampleMockSelfFuncFailed, self).__init__(*args, **kwargs)
        self.cli = app_all_permission.ins()
        self.module_cli = self.cli.application

    def test_mock_self_func_is_application_user_admin(self):
        origin_func = self.module_cli.is_application_user_admin
        self.module_cli.is_application_user_admin = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.is_application_user_admin(
                pylark.IsApplicationUserAdminReq()
            )

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.is_application_user_admin = origin_func

    def test_mock_self_func_get_application_user_admin_scope(self):
        origin_func = self.module_cli.get_application_user_admin_scope
        self.module_cli.get_application_user_admin_scope = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_application_user_admin_scope(
                pylark.GetApplicationUserAdminScopeReq()
            )

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.get_application_user_admin_scope = origin_func

    def test_mock_self_func_get_application_app_visibility(self):
        origin_func = self.module_cli.get_application_app_visibility
        self.module_cli.get_application_app_visibility = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_application_app_visibility(
                pylark.GetApplicationAppVisibilityReq()
            )

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.get_application_app_visibility = origin_func

    def test_mock_self_func_get_application_user_visible_app(self):
        origin_func = self.module_cli.get_application_user_visible_app
        self.module_cli.get_application_user_visible_app = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_application_user_visible_app(
                pylark.GetApplicationUserVisibleAppReq()
            )

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.get_application_user_visible_app = origin_func

    def test_mock_self_func_get_application_app_list(self):
        origin_func = self.module_cli.get_application_app_list
        self.module_cli.get_application_app_list = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_application_app_list(pylark.GetApplicationAppListReq())

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.get_application_app_list = origin_func

    def test_mock_self_func_update_application_app_visibility(self):
        origin_func = self.module_cli.update_application_app_visibility
        self.module_cli.update_application_app_visibility = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.update_application_app_visibility(
                pylark.UpdateApplicationAppVisibilityReq()
            )

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.update_application_app_visibility = origin_func

    def test_mock_self_func_get_application_app_admin_user_list(self):
        origin_func = self.module_cli.get_application_app_admin_user_list
        self.module_cli.get_application_app_admin_user_list = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_application_app_admin_user_list(
                pylark.GetApplicationAppAdminUserListReq()
            )

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.get_application_app_admin_user_list = origin_func

    def test_mock_self_func_check_user_is_in_application_paid_scope(self):
        origin_func = self.module_cli.check_user_is_in_application_paid_scope
        self.module_cli.check_user_is_in_application_paid_scope = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.check_user_is_in_application_paid_scope(
                pylark.CheckUserIsInApplicationPaidScopeReq()
            )

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.check_user_is_in_application_paid_scope = origin_func

    def test_mock_self_func_get_application_order_list(self):
        origin_func = self.module_cli.get_application_order_list
        self.module_cli.get_application_order_list = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_application_order_list(
                pylark.GetApplicationOrderListReq()
            )

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.get_application_order_list = origin_func

    def test_mock_self_func_get_application_order(self):
        origin_func = self.module_cli.get_application_order
        self.module_cli.get_application_order = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_application_order(pylark.GetApplicationOrderReq())

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.get_application_order = origin_func

    def test_mock_self_func_get_application_usage_overview(self):
        origin_func = self.module_cli.get_application_usage_overview
        self.module_cli.get_application_usage_overview = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_application_usage_overview(
                pylark.GetApplicationUsageOverviewReq()
            )

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.get_application_usage_overview = origin_func

    def test_mock_self_func_get_application_usage_trend(self):
        origin_func = self.module_cli.get_application_usage_trend
        self.module_cli.get_application_usage_trend = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_application_usage_trend(
                pylark.GetApplicationUsageTrendReq()
            )

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.get_application_usage_trend = origin_func

    def test_mock_self_func_get_application_usage_detail(self):
        origin_func = self.module_cli.get_application_usage_detail
        self.module_cli.get_application_usage_detail = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_application_usage_detail(
                pylark.GetApplicationUsageDetailReq()
            )

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.get_application_usage_detail = origin_func

    def test_mock_self_func_get_application_message_overview(self):
        origin_func = self.module_cli.get_application_message_overview
        self.module_cli.get_application_message_overview = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_application_message_overview(
                pylark.GetApplicationMessageOverviewReq()
            )

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.get_application_message_overview = origin_func

    def test_mock_self_func_get_application_message_trend(self):
        origin_func = self.module_cli.get_application_message_trend
        self.module_cli.get_application_message_trend = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_application_message_trend(
                pylark.GetApplicationMessageTrendReq()
            )

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.get_application_message_trend = origin_func

    def test_mock_self_func_get_application_message_detail(self):
        origin_func = self.module_cli.get_application_message_detail
        self.module_cli.get_application_message_detail = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_application_message_detail(
                pylark.GetApplicationMessageDetailReq()
            )

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.get_application_message_detail = origin_func


# mock raw request
class TestApplicationSampleMockRawRequestFailed(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestApplicationSampleMockRawRequestFailed, self).__init__(*args, **kwargs)
        self.cli = app_all_permission.ins()
        self.module_cli = self.cli.application
        self.cli.raw_request = mock_raw_request

    def test_mock_raw_request_is_application_user_admin(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.is_application_user_admin(
                pylark.IsApplicationUserAdminReq()
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_get_application_user_admin_scope(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_application_user_admin_scope(
                pylark.GetApplicationUserAdminScopeReq()
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_get_application_app_visibility(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_application_app_visibility(
                pylark.GetApplicationAppVisibilityReq()
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_get_application_user_visible_app(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_application_user_visible_app(
                pylark.GetApplicationUserVisibleAppReq()
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_get_application_app_list(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_application_app_list(pylark.GetApplicationAppListReq())

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_update_application_app_visibility(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.update_application_app_visibility(
                pylark.UpdateApplicationAppVisibilityReq()
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_get_application_app_admin_user_list(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_application_app_admin_user_list(
                pylark.GetApplicationAppAdminUserListReq()
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_check_user_is_in_application_paid_scope(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.check_user_is_in_application_paid_scope(
                pylark.CheckUserIsInApplicationPaidScopeReq()
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_get_application_order_list(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_application_order_list(
                pylark.GetApplicationOrderListReq()
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_get_application_order(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_application_order(pylark.GetApplicationOrderReq())

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_get_application_usage_overview(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_application_usage_overview(
                pylark.GetApplicationUsageOverviewReq()
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_get_application_usage_trend(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_application_usage_trend(
                pylark.GetApplicationUsageTrendReq()
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_get_application_usage_detail(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_application_usage_detail(
                pylark.GetApplicationUsageDetailReq()
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_get_application_message_overview(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_application_message_overview(
                pylark.GetApplicationMessageOverviewReq()
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_get_application_message_trend(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_application_message_trend(
                pylark.GetApplicationMessageTrendReq()
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_get_application_message_detail(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_application_message_detail(
                pylark.GetApplicationMessageDetailReq()
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg


# real request
class TestApplicationSampleRealRequestFailed(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestApplicationSampleRealRequestFailed, self).__init__(*args, **kwargs)
        self.cli = app_no_permission.ins()
        self.module_cli = self.cli.application

    def test_real_request_is_application_user_admin(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.is_application_user_admin(
                pylark.IsApplicationUserAdminReq()
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_get_application_user_admin_scope(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_application_user_admin_scope(
                pylark.GetApplicationUserAdminScopeReq()
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_get_application_app_visibility(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_application_app_visibility(
                pylark.GetApplicationAppVisibilityReq()
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_get_application_user_visible_app(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_application_user_visible_app(
                pylark.GetApplicationUserVisibleAppReq()
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_get_application_app_list(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_application_app_list(pylark.GetApplicationAppListReq())

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_update_application_app_visibility(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.update_application_app_visibility(
                pylark.UpdateApplicationAppVisibilityReq()
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_get_application_app_admin_user_list(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_application_app_admin_user_list(
                pylark.GetApplicationAppAdminUserListReq()
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_check_user_is_in_application_paid_scope(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.check_user_is_in_application_paid_scope(
                pylark.CheckUserIsInApplicationPaidScopeReq()
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_get_application_order_list(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_application_order_list(
                pylark.GetApplicationOrderListReq()
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_get_application_order(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_application_order(pylark.GetApplicationOrderReq())

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_get_application_usage_overview(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_application_usage_overview(
                pylark.GetApplicationUsageOverviewReq()
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_get_application_usage_trend(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_application_usage_trend(
                pylark.GetApplicationUsageTrendReq()
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_get_application_usage_detail(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_application_usage_detail(
                pylark.GetApplicationUsageDetailReq()
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_get_application_message_overview(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_application_message_overview(
                pylark.GetApplicationMessageOverviewReq()
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_get_application_message_trend(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_application_message_trend(
                pylark.GetApplicationMessageTrendReq()
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_get_application_message_detail(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_application_message_detail(
                pylark.GetApplicationMessageDetailReq()
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
