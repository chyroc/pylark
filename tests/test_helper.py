import unittest

from pylark.api_service_ai_detect_face_attributes import (
    DetectFaceAttributesRespFaceInfoPositionUpperLeft,
)
from pylark.helper import _make_dataclass_from_dict


class MyTestCase(unittest.TestCase):
    def test_something(self):
        res = _make_dataclass_from_dict(
            DetectFaceAttributesRespFaceInfoPositionUpperLeft,
            {
                "x": 1,
                "y": 2,
            },
        )
        print(res)
        assert res == DetectFaceAttributesRespFaceInfoPositionUpperLeft(1, 2)
