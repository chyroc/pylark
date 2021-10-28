# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
from pylark import lark_type_enum, lark_type_sheet
import attr
import typing
import io


@attr.s
class UploadImageReqImage(object):
    pass


@attr.s
class UploadImageReqImageType(object):
    pass


@attr.s
class UploadImageReq(object):
    image_type: UploadImageReqImageType = attr.ib(
        factory=lambda: UploadImageReqImageType(),
        metadata={"req_type": "json", "key": "image_type"},
    )  # 图片类型, 示例值："message", 可选值有: `message`：用于发送消息, `avatar`：用于设置头像
    image: typing.Union[str, bytes, io.BytesIO] = attr.ib(
        default=None, metadata={"req_type": "json", "key": "image"}
    )  # 图片内容, 示例值：二进制文件


@attr.s
class UploadImageResp(object):
    image_key: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "image_key"}
    )  # 图片的key


def _gen_upload_image_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=UploadImageResp,
        scope="File",
        api="UploadImage",
        method="POST",
        url="https://open.feishu.cn/open-apis/im/v1/images",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        is_file=True,
    )
