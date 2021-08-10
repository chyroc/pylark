# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class UploadDriveMediaReqFile(object):
    pass


@attr.s
class UploadDriveMediaReq(object):
    file_name: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 文件名, 示例值："test.txt", 最大长度：`250` 字符
    parent_type: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 上传点类型, 示例值："doc_image", 可选值有: `doc_image`：docs图片, `sheet_image`：sheet图片, `doc_file`：doc文件, `sheet_file`：sheet文件, `vc_virtual_background`：vc虚拟背景(灰度中，暂未开放), `bitable_image`：bitable图片, `bitable_file`：bitable文件, `moments`：同事圈(灰度中，暂未开放), `ccm_import_open`：云文档导入文件
    parent_node: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 上传点的token, 示例值："doccn123456"
    size: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 文件大小,全量上传最大20M, 示例值：1024, 最大值：`20971520`
    checksum: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 文件adler32校验和(可选), 示例值："12345678"
    extra: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 扩展信息(可选), 示例值："{"test":"test"}"
    file: typing.Union[str, bytes, io.BytesIO] = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 文件内容, 示例值：file binary


@attr.s
class UploadDriveMediaResp(object):
    file_token: str = attr.ib(default="", metadata={"req_type": "json"})  # 新创建文件的 token


def _gen_upload_drive_media_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=UploadDriveMediaResp,
        scope="Drive",
        api="UploadDriveMedia",
        method="POST",
        url="https://open.feishu.cn/open-apis/drive/v1/medias/upload_all",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        need_user_access_token=True,
        is_file=True,
    )
