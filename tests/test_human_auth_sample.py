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
class TestHumanAuthSampleMockGetTokenFailed(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestHumanAuthSampleMockGetTokenFailed, self).__init__(*args, **kwargs)
        self.cli = app_all_permission.ins()
        self.cli.auth.get_tenant_access_token = mock_get_tenant_access_token_failed
        self.cli.auth.get_app_access_token = mock_get_tenant_access_token_failed
        self.module_cli = self.cli.human_auth

    def test_mock_get_token_get_face_verify_auth_result(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_face_verify_auth_result(
                pylark.GetFaceVerifyAuthResultReq()
            )

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_upload_face_verify_image(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.upload_face_verify_image(pylark.UploadFaceVerifyImageReq())

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_crop_face_verify_image(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.crop_face_verify_image(pylark.CropFaceVerifyImageReq())

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_create_identity(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.create_identity(pylark.CreateIdentityReq())

        assert "msg=failed" in f"{e}"


# mock mock self func
class TestHumanAuthSampleMockSelfFuncFailed(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestHumanAuthSampleMockSelfFuncFailed, self).__init__(*args, **kwargs)
        self.cli = app_all_permission.ins()
        self.module_cli = self.cli.human_auth

    def test_mock_self_func_get_face_verify_auth_result(self):
        origin_func = self.module_cli.get_face_verify_auth_result
        self.module_cli.get_face_verify_auth_result = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_face_verify_auth_result(
                pylark.GetFaceVerifyAuthResultReq()
            )

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.get_face_verify_auth_result = origin_func

    def test_mock_self_func_upload_face_verify_image(self):
        origin_func = self.module_cli.upload_face_verify_image
        self.module_cli.upload_face_verify_image = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.upload_face_verify_image(pylark.UploadFaceVerifyImageReq())

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.upload_face_verify_image = origin_func

    def test_mock_self_func_crop_face_verify_image(self):
        origin_func = self.module_cli.crop_face_verify_image
        self.module_cli.crop_face_verify_image = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.crop_face_verify_image(pylark.CropFaceVerifyImageReq())

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.crop_face_verify_image = origin_func

    def test_mock_self_func_create_identity(self):
        origin_func = self.module_cli.create_identity
        self.module_cli.create_identity = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.create_identity(pylark.CreateIdentityReq())

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.create_identity = origin_func


# mock raw request
class TestHumanAuthSampleMockRawRequestFailed(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestHumanAuthSampleMockRawRequestFailed, self).__init__(*args, **kwargs)
        self.cli = app_all_permission.ins()
        self.module_cli = self.cli.human_auth
        self.cli.raw_request = mock_raw_request

    def test_mock_raw_request_get_face_verify_auth_result(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_face_verify_auth_result(
                pylark.GetFaceVerifyAuthResultReq()
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_upload_face_verify_image(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.upload_face_verify_image(pylark.UploadFaceVerifyImageReq())

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_crop_face_verify_image(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.crop_face_verify_image(pylark.CropFaceVerifyImageReq())

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_create_identity(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.create_identity(pylark.CreateIdentityReq())

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg


# real request
class TestHumanAuthSampleRealRequestFailed(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestHumanAuthSampleRealRequestFailed, self).__init__(*args, **kwargs)
        self.cli = app_no_permission.ins()
        self.module_cli = self.cli.human_auth

    def test_real_request_get_face_verify_auth_result(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_face_verify_auth_result(
                pylark.GetFaceVerifyAuthResultReq()
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_upload_face_verify_image(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.upload_face_verify_image(pylark.UploadFaceVerifyImageReq())

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_crop_face_verify_image(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.crop_face_verify_image(pylark.CropFaceVerifyImageReq())

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_create_identity(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.create_identity(pylark.CreateIdentityReq())

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
