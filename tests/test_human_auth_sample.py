# Code generated by lark_sdk_gen. DO NOT EDIT.

from tests.test_conf import app_all_permission
import unittest
import pylark
import pytest
from tests.test_helper import mock_get_tenant_access_token_failed


class TestHumanAuthSampleRequestFailed(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestHumanAuthSampleRequestFailed, self).__init__(*args, **kwargs)
        self.cli = app_all_permission.ins()
        self.cli.auth.get_tenant_access_token = mock_get_tenant_access_token_failed
        self.cli.auth.get_app_access_token = mock_get_tenant_access_token_failed
        self.module_cli = self.cli.human_auth

    def test_request_failed_get_face_verify_auth_result(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_face_verify_auth_result(
                pylark.GetFaceVerifyAuthResultReq()
            )

        assert "msg=failed" in f"{e}"

    def test_request_failed_upload_face_verify_image(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.upload_face_verify_image(pylark.UploadFaceVerifyImageReq())

        assert "msg=failed" in f"{e}"

    def test_request_failed_crop_face_verify_image(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.crop_face_verify_image(pylark.CropFaceVerifyImageReq())

        assert "msg=failed" in f"{e}"

    def test_request_failed_create_identity(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.create_identity(pylark.CreateIdentityReq())

        assert "msg=failed" in f"{e}"
