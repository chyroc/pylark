import typing
import unittest

import attr

from pylark import (
    DetectFaceAttributesRespFaceInfoPositionUpperLeft,
    TokenExpire,
    Response,
    PyLarkError,
)
from pylark.helper import _make_dataclass_from_dict


# mockGetTenantAccessTokenFailed
def mock_get_tenant_access_token_failed() -> typing.Tuple[TokenExpire, Response]:
    raise PyLarkError(scope="scope", func="func", code=1, msg="failed")


class MyTestCase(unittest.TestCase):
    def test_make_dataclass(self):
        res = _make_dataclass_from_dict(
            DetectFaceAttributesRespFaceInfoPositionUpperLeft,
            {
                "x": 1,
                "y": 2,
            },
        )
        print(res)
        assert res == DetectFaceAttributesRespFaceInfoPositionUpperLeft(1, 2)

    def test_field(self):
        res = attr.fields(DetectFaceAttributesRespFaceInfoPositionUpperLeft)
        for field in res:
            assert "json" == field.metadata["req_type"]
