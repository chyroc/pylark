import logging
import unittest
import pylark
import pytest

from pylark import logger
from tests.test_conf import app_all_permission, app_no_permission, user_admin


class TestSheet(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestSheet, self).__init__(*args, **kwargs)
        self.cli = app_all_permission.ins()
        self.module_cli = self.cli.drive

        self.to_delete_sheet = []

    def setUp(self):
        pass

    def tearDown(self):
        for sheet_token in self.to_delete_sheet:
            self.module_cli.delete_drive_sheet_file(
                pylark.DeleteDriveSheetFileReq(spreadsheet_token=sheet_token)
            )

    def create_sheet(self):
        resp, _ = self.module_cli.create_sheet(pylark.CreateSheetReq(title="debug"))
        assert resp.spreadsheet.spreadsheet_token
        sheet_token = resp.spreadsheet.spreadsheet_token

        resp2, _ = self.module_cli.update_drive_member_permission(
            pylark.UpdateDriveMemberPermissionReq(
                need_notification=True,
                type="sheet",
                token=sheet_token,
                member_id=user_admin.open_id,
                member_type="openid",
                perm="full_access",
            )
        )
        assert resp2.member

        return sheet_token

    def test_sheet(self):
        sheet_token = self.create_sheet()
        self.to_delete_sheet.append(sheet_token)

        resp, _ = self.module_cli.get_sheet_meta(
            pylark.GetSheetMetaReq(spreadsheet_token=sheet_token)
        )
        assert resp.sheets
        assert 1 == len(resp.sheets)
        assert resp.sheets[0].sheet_id
