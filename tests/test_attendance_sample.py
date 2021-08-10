# Code generated by lark_sdk_gen. DO NOT EDIT.

from tests.test_conf import app_all_permission
import unittest
import pylark
import pytest
from tests.test_helper import mock_get_tenant_access_token_failed


class TestAttendanceSampleRequestFailed(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestAttendanceSampleRequestFailed, self).__init__(*args, **kwargs)
        self.cli = app_all_permission.ins()
        self.cli.auth.get_tenant_access_token = mock_get_tenant_access_token_failed
        self.cli.auth.get_app_access_token = mock_get_tenant_access_token_failed
        self.module_cli = self.cli.attendance

    def test_request_failed_download_attendance_file(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.download_attendance_file(pylark.DownloadAttendanceFileReq())

        assert "msg=failed" in f"{e}"

    def test_request_failed_upload_attendance_file(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.upload_attendance_file(pylark.UploadAttendanceFileReq())

        assert "msg=failed" in f"{e}"

    def test_request_failed_query_attendance_user_settings(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.query_attendance_user_settings(
                pylark.QueryAttendanceUserSettingsReq()
            )

        assert "msg=failed" in f"{e}"

    def test_request_failed_update_attendance_user_settings(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.update_attendance_user_settings(
                pylark.UpdateAttendanceUserSettingsReq()
            )

        assert "msg=failed" in f"{e}"

    def test_request_failed_create_update_attendance_group(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.create_update_attendance_group(
                pylark.CreateUpdateAttendanceGroupReq()
            )

        assert "msg=failed" in f"{e}"

    def test_request_failed_delete_attendance_group(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.delete_attendance_group(pylark.DeleteAttendanceGroupReq())

        assert "msg=failed" in f"{e}"

    def test_request_failed_get_attendance_group(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_attendance_group(pylark.GetAttendanceGroupReq())

        assert "msg=failed" in f"{e}"

    def test_request_failed_create_attendance_shift(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.create_attendance_shift(pylark.CreateAttendanceShiftReq())

        assert "msg=failed" in f"{e}"

    def test_request_failed_delete_attendance_shift(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.delete_attendance_shift(pylark.DeleteAttendanceShiftReq())

        assert "msg=failed" in f"{e}"

    def test_request_failed_get_attendance_shift_by_id(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_attendance_shift_by_id(
                pylark.GetAttendanceShiftByIDReq()
            )

        assert "msg=failed" in f"{e}"

    def test_request_failed_get_attendance_shift_by_name(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_attendance_shift_by_name(
                pylark.GetAttendanceShiftByNameReq()
            )

        assert "msg=failed" in f"{e}"

    def test_request_failed_get_attendance_statistics_data(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_attendance_statistics_data(
                pylark.GetAttendanceStatisticsDataReq()
            )

        assert "msg=failed" in f"{e}"

    def test_request_failed_get_attendance_statistics_header(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_attendance_statistics_header(
                pylark.GetAttendanceStatisticsHeaderReq()
            )

        assert "msg=failed" in f"{e}"

    def test_request_failed_update_attendance_user_statistics_settings(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.update_attendance_user_statistics_settings(
                pylark.UpdateAttendanceUserStatisticsSettingsReq()
            )

        assert "msg=failed" in f"{e}"

    def test_request_failed_get_attendance_user_statistics_settings(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_attendance_user_statistics_settings(
                pylark.GetAttendanceUserStatisticsSettingsReq()
            )

        assert "msg=failed" in f"{e}"

    def test_request_failed_get_attendance_user_daily_shift(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_attendance_user_daily_shift(
                pylark.GetAttendanceUserDailyShiftReq()
            )

        assert "msg=failed" in f"{e}"

    def test_request_failed_get_attendance_user_task(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_attendance_user_task(pylark.GetAttendanceUserTaskReq())

        assert "msg=failed" in f"{e}"

    def test_request_failed_get_attendance_user_flow(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_attendance_user_flow(pylark.GetAttendanceUserFlowReq())

        assert "msg=failed" in f"{e}"

    def test_request_failed_batch_get_attendance_user_flow(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.batch_get_attendance_user_flow(
                pylark.BatchGetAttendanceUserFlowReq()
            )

        assert "msg=failed" in f"{e}"

    def test_request_failed_batch_create_attendance_user_flow(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.batch_create_attendance_user_flow(
                pylark.BatchCreateAttendanceUserFlowReq()
            )

        assert "msg=failed" in f"{e}"

    def test_request_failed_get_attendance_user_task_remedy(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_attendance_user_task_remedy(
                pylark.GetAttendanceUserTaskRemedyReq()
            )

        assert "msg=failed" in f"{e}"

    def test_request_failed_create_update_attendance_user_daily_shift(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.create_update_attendance_user_daily_shift(
                pylark.CreateUpdateAttendanceUserDailyShiftReq()
            )

        assert "msg=failed" in f"{e}"

    def test_request_failed_get_attendance_user_approval(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_attendance_user_approval(
                pylark.GetAttendanceUserApprovalReq()
            )

        assert "msg=failed" in f"{e}"

    def test_request_failed_create_attendance_user_approval(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.create_attendance_user_approval(
                pylark.CreateAttendanceUserApprovalReq()
            )

        assert "msg=failed" in f"{e}"

    def test_request_failed_get_attendance_user_allowed_remedy(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_attendance_user_allowed_remedy(
                pylark.GetAttendanceUserAllowedRemedyReq()
            )

        assert "msg=failed" in f"{e}"

    def test_request_failed_init_attendance_remedy_approval(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.init_attendance_remedy_approval(
                pylark.InitAttendanceRemedyApprovalReq()
            )

        assert "msg=failed" in f"{e}"

    def test_request_failed_update_attendance_remedy_approval(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.update_attendance_remedy_approval(
                pylark.UpdateAttendanceRemedyApprovalReq()
            )

        assert "msg=failed" in f"{e}"
