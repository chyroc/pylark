import logging
import unittest

import pylark
from tests.test_conf import app_all_permission


class TestBot(unittest.TestCase):
    def test_get_bot(self):
        res, response = app_all_permission.ins().bot.get_bot_info(
            pylark.GetBotInfoReq()
        )
        print(res, response)
        pylark.logger.debug("x")
        assert "lark-sdk" == res.app_name
