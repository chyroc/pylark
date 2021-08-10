# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class DetectFaceAttributesReq(object):
    image: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 图片 base64 数据, 示例值："图片 base64 后的字符串"


@attr.s
class DetectFaceAttributesRespFaceInfoQualityOccludeRightEye(object):
    pass


@attr.s
class DetectFaceAttributesRespFaceInfoQualityOccludeLeftEye(object):
    pass


@attr.s
class DetectFaceAttributesRespFaceInfoQualityOccludeChin(object):
    pass


@attr.s
class DetectFaceAttributesRespFaceInfoQualityOccludeMouth(object):
    pass


@attr.s
class DetectFaceAttributesRespFaceInfoQualityOccludeCheek(object):
    pass


@attr.s
class DetectFaceAttributesRespFaceInfoQualityOccludeNose(object):
    pass


@attr.s
class DetectFaceAttributesRespFaceInfoQualityOccludeEyebrow(object):
    pass


@attr.s
class DetectFaceAttributesRespFaceInfoQualityOcclude(object):
    eyebrow: float = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 眉毛被遮挡情况：[0, 1] 值越大被遮挡的概率越高
    nose: float = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 鼻子被遮挡情况：[0, 1] 值越大被遮挡的概率越高
    cheek: float = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 脸颊被遮挡情况：[0, 1] 值越大被遮挡的概率越高
    mouth: float = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 嘴被遮挡情况：[0, 1] 值越大被遮挡的概率越高
    chin: float = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 下巴被遮挡情况：[0, 1] 值越大被遮挡的概率越高
    left_eye: float = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 左眼睛被遮挡情况：[0, 1] 值越大被遮挡的概率越高
    right_eye: float = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 右眼睛被遮挡情况：[0, 1] 值越大被遮挡的概率越高


@attr.s
class DetectFaceAttributesRespFaceInfoQualityBrightness(object):
    pass


@attr.s
class DetectFaceAttributesRespFaceInfoQualitySharpness(object):
    pass


@attr.s
class DetectFaceAttributesRespFaceInfoQuality(object):
    sharpness: float = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 清晰度，值越高越清晰
    brightness: float = attr.ib(default=None, metadata={"req_type": "json"})  # 亮度
    occlude: DetectFaceAttributesRespFaceInfoQualityOcclude = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 面部遮挡属性


@attr.s
class DetectFaceAttributesRespFaceInfoAttributeMaskProbability(object):
    pass


@attr.s
class DetectFaceAttributesRespFaceInfoAttributeMask(object):
    type: int = attr.ib(default=0, metadata={"req_type": "json"})  # 属性
    probability: float = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 识别置信度，[0, 1]，代表判断正确的概率


@attr.s
class DetectFaceAttributesRespFaceInfoAttributeGlassProbability(object):
    pass


@attr.s
class DetectFaceAttributesRespFaceInfoAttributeGlass(object):
    type: int = attr.ib(default=0, metadata={"req_type": "json"})  # 属性
    probability: float = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 识别置信度，[0, 1]，代表判断正确的概率


@attr.s
class DetectFaceAttributesRespFaceInfoAttributeHatProbability(object):
    pass


@attr.s
class DetectFaceAttributesRespFaceInfoAttributeHat(object):
    type: int = attr.ib(default=0, metadata={"req_type": "json"})  # 属性
    probability: float = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 识别置信度，[0, 1]，代表判断正确的概率


@attr.s
class DetectFaceAttributesRespFaceInfoAttributePose(object):
    pitch: int = attr.ib(default=0, metadata={"req_type": "json"})  # 脸部上下偏移 [-90, 90]
    yaw: int = attr.ib(default=0, metadata={"req_type": "json"})  # 脸部左右偏移 [-90, 90]
    roll: int = attr.ib(default=0, metadata={"req_type": "json"})  # 平面旋转 [-90, 90]


@attr.s
class DetectFaceAttributesRespFaceInfoAttributeEmotionProbability(object):
    pass


@attr.s
class DetectFaceAttributesRespFaceInfoAttributeEmotion(object):
    type: int = attr.ib(default=0, metadata={"req_type": "json"})  # 属性
    probability: float = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 识别置信度，[0, 1]，代表判断正确的概率


@attr.s
class DetectFaceAttributesRespFaceInfoAttributeGenderProbability(object):
    pass


@attr.s
class DetectFaceAttributesRespFaceInfoAttributeGender(object):
    type: int = attr.ib(default=0, metadata={"req_type": "json"})  # 属性
    probability: float = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 识别置信度，[0, 1]，代表判断正确的概率


@attr.s
class DetectFaceAttributesRespFaceInfoAttribute(object):
    gender: DetectFaceAttributesRespFaceInfoAttributeGender = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 性别信息：0 男性，1 女性
    age: int = attr.ib(default=0, metadata={"req_type": "json"})  # 年龄大小
    emotion: DetectFaceAttributesRespFaceInfoAttributeEmotion = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 情绪：0 自然, 1 高兴，2 惊讶，3 害怕，4 悲伤，5 生气, 6 厌恶
    beauty: int = attr.ib(default=0, metadata={"req_type": "json"})  # 颜值打分：[0, 100]
    pose: DetectFaceAttributesRespFaceInfoAttributePose = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 人脸姿态
    hat: DetectFaceAttributesRespFaceInfoAttributeHat = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 帽子：0 未戴帽子，1 戴帽子
    glass: DetectFaceAttributesRespFaceInfoAttributeGlass = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 眼镜：0 未戴眼镜，1 戴眼镜
    mask: DetectFaceAttributesRespFaceInfoAttributeMask = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 口罩：0 未戴口罩，1 戴口罩


@attr.s
class DetectFaceAttributesRespFaceInfoPositionLowerRightY(object):
    pass


@attr.s
class DetectFaceAttributesRespFaceInfoPositionLowerRightX(object):
    pass


@attr.s
class DetectFaceAttributesRespFaceInfoPositionLowerRight(object):
    x: float = attr.ib(default=None, metadata={"req_type": "json"})  # 横轴坐标
    y: float = attr.ib(default=None, metadata={"req_type": "json"})  # 纵轴坐标


@attr.s
class DetectFaceAttributesRespFaceInfoPositionUpperLeftY(object):
    pass


@attr.s
class DetectFaceAttributesRespFaceInfoPositionUpperLeftX(object):
    pass


@attr.s
class DetectFaceAttributesRespFaceInfoPositionUpperLeft(object):
    x: float = attr.ib(default=None, metadata={"req_type": "json"})  # 横轴坐标
    y: float = attr.ib(default=None, metadata={"req_type": "json"})  # 纵轴坐标


@attr.s
class DetectFaceAttributesRespFaceInfoPosition(object):
    upper_left: DetectFaceAttributesRespFaceInfoPositionUpperLeft = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 人脸框的左上角坐标
    lower_right: DetectFaceAttributesRespFaceInfoPositionLowerRight = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 人脸框的右下角坐标


@attr.s
class DetectFaceAttributesRespFaceInfo(object):
    position: DetectFaceAttributesRespFaceInfoPosition = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 人脸位置信息
    attribute: DetectFaceAttributesRespFaceInfoAttribute = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 人脸属性信息
    quality: DetectFaceAttributesRespFaceInfoQuality = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 人脸质量信息


@attr.s
class DetectFaceAttributesRespImageInfo(object):
    width: int = attr.ib(default=0, metadata={"req_type": "json"})  # 图片的宽度
    height: int = attr.ib(default=0, metadata={"req_type": "json"})  # 图片的高度


@attr.s
class DetectFaceAttributesResp(object):
    image_info: DetectFaceAttributesRespImageInfo = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 图片信息
    face_infos: typing.List[DetectFaceAttributesRespFaceInfo] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 人脸信息列表


def _gen_detect_face_attributes_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=DetectFaceAttributesResp,
        scope="AI",
        api="DetectFaceAttributes",
        method="POST",
        url="https://open.feishu.cn/open-apis/face_detection/v1/image/detect_face_attributes",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
