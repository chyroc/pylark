from unittest import TestCase

from pylark import DetectTextLanguageReq
from tests.test_conf import app_all_permission


class TestAI(TestCase):
    def test_detect_text_language(self):
        res, response = app_all_permission.ins().ai.detect_text_language(
            DetectTextLanguageReq(text="你好")
        )
        print(res)
        print(response)
        assert response.request_id
        assert "zh" == res.language
