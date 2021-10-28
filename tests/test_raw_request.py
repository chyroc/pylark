import logging
import unittest
import pylark
import pytest

from pylark import (
    logger,
    Request,
    RawRequestReq,
    DeleteDriveSheetFileReq,
    DeleteDriveSheetFileResp,
    GetSheetMetaResp,
)
from pylark._internal_helper import _make_dataclass_from_dict
from pylark.lark_request import RawRequestReq, _new_method_option


class TestRawRequest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestRawRequest, self).__init__(*args, **kwargs)

    def test_foo(self):
        resp = Request._parse_request_param(
            RawRequestReq(
                dataclass=DeleteDriveSheetFileResp,
                scope="Drive",
                api="DeleteDriveSheetFile",
                method="DELETE",
                url="https://open.feishu.cn/open-apis/drive/explorer/v2/file/spreadsheets/:spreadsheetToken",
                body=DeleteDriveSheetFileReq(spreadsheet_token="token"),
                method_option=_new_method_option(None),
                need_tenant_access_token=True,
                need_user_access_token=True,
            )
        )

        assert (
            "https://open.feishu.cn/open-apis/drive/explorer/v2/file/spreadsheets/token"
            == resp["url"]
        )

    def test_make_class(self):
        data = {
            "properties": {
                "ownerUser": 12345,
                "revision": 0,
                "sheetCount": 1,
                "title": "debug",
            },
            "sheets": [
                {
                    "columnCount": 20,
                    "frozenColCount": 0,
                    "frozenRowCount": 0,
                    "index": 0,
                    "rowCount": 200,
                    "sheetId": "123",
                    "title": "Sheet1",
                }
            ],
            "spreadsheetToken": "sht123",
        }
        resp = _make_dataclass_from_dict(GetSheetMetaResp, data)
        assert "sht123" == resp.spreadsheet_token
        assert 12345 == resp.properties.owner_user
        assert "123" == resp.sheets[0].sheet_id
