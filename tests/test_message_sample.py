# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.log import logger
from tests.test_conf import app_all_permission
import unittest
import pylark
import pytest


class Test_Message_Sample_RequestFailed(unittest.TestCase):
    def __init__(self):
        super().__init__()
        self.cli = app_all_permission.ins()
        # self.cli.mock().MockGetTenantAccessToken(mockGetTenantAccessTokenFailed)
        # self.cli.mock().MockGetAppAccessToken(mockGetTenantAccessTokenFailed)
        self.module_cli = self.cli.message

    def test_request_failed_send_raw_message(self):
        with pytest.raises(ZeroDivisionError) as e:
            res, response = self.module_cli.SendRawMessage(pylark.SendRawMessageReq())
            print("e", e)

            # as.NotNil(err)
            # as.Equal(err.Error(), "failed")

    def test_request_failed_send_raw_message_old(self):
        with pytest.raises(ZeroDivisionError) as e:
            res, response = self.module_cli.SendRawMessageOld(
                pylark.SendRawMessageOldReq()
            )
            print("e", e)

            # as.NotNil(err)
            # as.Equal(err.Error(), "failed")

    def test_request_failed_reply_raw_message(self):
        with pytest.raises(ZeroDivisionError) as e:
            res, response = self.module_cli.ReplyRawMessage(pylark.ReplyRawMessageReq())
            print("e", e)

            # as.NotNil(err)
            # as.Equal(err.Error(), "failed")

    def test_request_failed_delete_message(self):
        with pytest.raises(ZeroDivisionError) as e:
            res, response = self.module_cli.DeleteMessage(pylark.DeleteMessageReq())
            print("e", e)

            # as.NotNil(err)
            # as.Equal(err.Error(), "failed")

    def test_request_failed_update_message(self):
        with pytest.raises(ZeroDivisionError) as e:
            res, response = self.module_cli.UpdateMessage(pylark.UpdateMessageReq())
            print("e", e)

            # as.NotNil(err)
            # as.Equal(err.Error(), "failed")

    def test_request_failed_get_message_read_user_list(self):
        with pytest.raises(ZeroDivisionError) as e:
            res, response = self.module_cli.GetMessageReadUserList(
                pylark.GetMessageReadUserListReq()
            )
            print("e", e)

            # as.NotNil(err)
            # as.Equal(err.Error(), "failed")

    def test_request_failed_get_message_list(self):
        with pytest.raises(ZeroDivisionError) as e:
            res, response = self.module_cli.GetMessageList(pylark.GetMessageListReq())
            print("e", e)

            # as.NotNil(err)
            # as.Equal(err.Error(), "failed")

    def test_request_failed_get_message_file(self):
        with pytest.raises(ZeroDivisionError) as e:
            res, response = self.module_cli.GetMessageFile(pylark.GetMessageFileReq())
            print("e", e)

            # as.NotNil(err)
            # as.Equal(err.Error(), "failed")

    def test_request_failed_get_message(self):
        with pytest.raises(ZeroDivisionError) as e:
            res, response = self.module_cli.GetMessage(pylark.GetMessageReq())
            print("e", e)

            # as.NotNil(err)
            # as.Equal(err.Error(), "failed")

    def test_request_failed_delete_ephemeral_message(self):
        with pytest.raises(ZeroDivisionError) as e:
            res, response = self.module_cli.DeleteEphemeralMessage(
                pylark.DeleteEphemeralMessageReq()
            )
            print("e", e)

            # as.NotNil(err)
            # as.Equal(err.Error(), "failed")