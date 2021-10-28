# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
from pylark import lark_type_enum, lark_type_sheet
import attr
import typing
import io


@attr.s
class DownloadFileReq(object):
    file_key: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "file_key"}
    )  # 文件的key, 示例值："file_456a92d6-c6ea-4de4-ac3f-7afcf44ac78g"


@attr.s
class DownloadFileRespFile(object):
    pass


@attr.s
class DownloadFileResp(object):
    file: typing.Union[str, bytes, io.BytesIO] = attr.ib(
        default=None, metadata={"req_type": "json", "key": "file"}
    )


@attr.s
class DownloadFileResp(object):
    is_file: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json", "key": "is_file"}
    )
    code: int = attr.ib(default=0, metadata={"req_type": "json", "key": "code"})
    msg: str = attr.ib(default="", metadata={"req_type": "json", "key": "msg"})
    data: DownloadFileResp = attr.ib(
        default=None, metadata={"req_type": "json", "key": "data"}
    )


def _gen_download_file_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=DownloadFileResp,
        scope="File",
        api="DownloadFile",
        method="GET",
        url="https://open.feishu.cn/open-apis/im/v1/files/:file_key",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
