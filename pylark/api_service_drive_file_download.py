# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class DownloadDriveFileReqRange(object):
    pass


@attr.s
class DownloadDriveFileReq(object):
    file_token: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "file_token"}
    )  # 文件的 token，获取方式见 [概述](https://open.feishu.cn/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/files/guide/introduction), 示例值："boxcnabCdefg12345"
    range: DownloadDriveFileReqRange = attr.ib(
        factory=lambda: DownloadDriveFileReqRange(),
        metadata={"req_type": "header", "header": "range"},
    )  # 指定文件下载部分, 示例值："bytes=0-1024"


@attr.s
class DownloadDriveFileRespFile(object):
    pass


@attr.s
class DownloadDriveFileResp(object):
    file: typing.Union[str, bytes, io.BytesIO] = attr.ib(
        default=None, metadata={"resp_type": "header"}
    )
    filename: str = attr.ib(default="", metadata={"resp_type": "header"})  # 文件名


@attr.s
class DownloadDriveFileResp(object):
    is_file: bool = attr.ib(factory=lambda: bool(), metadata={"resp_type": "header"})
    code: int = attr.ib(default=0, metadata={"resp_type": "header"})
    msg: str = attr.ib(default="", metadata={"resp_type": "header"})
    data: DownloadDriveFileResp = attr.ib(
        default=None, metadata={"resp_type": "header"}
    )


def _gen_download_drive_file_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=DownloadDriveFileResp,
        scope="Drive",
        api="DownloadDriveFile",
        method="GET",
        url="https://open.feishu.cn/open-apis/drive/v1/files/:file_token/download",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        need_user_access_token=True,
    )
