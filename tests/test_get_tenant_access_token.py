from unittest import TestCase
from pylark.log import logger
from tests.test_conf import app_all_permission


class TestToken(TestCase):
    def test_get_tenant_access_token(self):
        res, response = app_all_permission.ins().auth.get_tenant_access_token()
        assert response.request_id
        assert res.token
        assert res.expire

        logger.debug("res: %s", res)
        print(res)
