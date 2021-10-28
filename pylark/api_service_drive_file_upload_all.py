# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
from pylark import lark_type_enum, lark_type_sheet
import attr
import typing
import io


@attr.s
class UploadDriveFileReqFile(object):
    pass


@attr.s
class UploadDriveFileReq(object):
    file_name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "file_name"}
    )  # 文件名, 示例值："test.txt", 最大长度：`250` 字符
    parent_type: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "parent_type"}
    )  # 上传点类型, 示例值："explorer", 可选值有: `explorer`：云空间
    parent_node: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "parent_node"}
    )  # 文件夹token, 示例值："fldcn77hdDT5"
    size: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "size"}
    )  # 文件大小,全量上传最大20M, 示例值：1024, 最大值：`20971520`
    checksum: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "checksum"}
    )  # 文件adler32校验和(可选), 示例值："123423882374238957235"
    file: typing.Union[str, bytes, io.BytesIO] = attr.ib(
        default=None, metadata={"req_type": "json", "key": "file"}
    )  # 文件数据, 示例值：file binary


@attr.s
class UploadDriveFileResp(object):
    file_token: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "file_token"}
    )  # 新创建文件的 token


def _gen_upload_drive_file_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=UploadDriveFileResp,
        scope="Drive",
        api="UploadDriveFile",
        method="POST",
        url="https://open.feishu.cn/open-apis/drive/v1/files/upload_all",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        need_user_access_token=True,
        is_file=True,
    )
