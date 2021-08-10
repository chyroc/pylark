# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class DeleteDriveFileReq(object):
    doc_token: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # doc 的 token，获取方式见 [概述](https://open.feishu.cn/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/files/guide/introduction)


@attr.s
class DeleteDriveFileResp(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # doc 的 id「字符串类型」
    result: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 删除结果


def _gen_delete_drive_file_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=DeleteDriveFileResp,
        scope="Drive",
        api="DeleteDriveFile",
        method="DELETE",
        url="https://open.feishu.cn/open-apis/drive/explorer/v2/file/docs/:docToken",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        need_user_access_token=True,
    )
