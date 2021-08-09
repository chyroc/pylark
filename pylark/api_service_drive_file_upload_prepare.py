# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing


@attr.s
class PrepareUploadDriveFileReq(object):
    file_name: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 文件名, 示例值："test.txt", 最大长度：`250` 字符
    parent_type: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 上传点类型, 示例值："explorer", 可选值有: `explorer`：云空间
    parent_node: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 文件夹的token, 示例值："fldcnaBcdEfghdis"
    size: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 文件大小, 示例值：1024, 最小值：`0`


@attr.s
class PrepareUploadDriveFileResp(object):
    upload_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 分片上传事务ID
    block_size: int = attr.ib(default=0, metadata={"req_type": "json"})  # 分片大小策略
    block_num: int = attr.ib(default=0, metadata={"req_type": "json"})  # 分片数量


def _gen_prepare_upload_drive_file_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=PrepareUploadDriveFileResp,
        scope="Drive",
        api="PrepareUploadDriveFile",
        method="POST",
        url="https://open.feishu.cn/open-apis/drive/v1/files/upload_prepare",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
