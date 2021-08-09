# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing


@attr.s
class UploadApprovalFileReqContent(object):
    pass


@attr.s
class UploadApprovalFileReq(object):
    name: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 文件名（需包含文件扩展名，如“文件.doc”
    type: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 文件类型（image 或 attachment）
    content: UploadApprovalFileReqContent = attr.ib(
        factory=lambda: UploadApprovalFileReqContent(), metadata={"req_type": "json"}
    )  # 文件


@attr.s
class UploadApprovalFileResp(object):
    code: str = attr.ib(default="", metadata={"req_type": "json"})  # 文件标识码（用于创建审批实例）
    url: str = attr.ib(default="", metadata={"req_type": "json"})  # 文件 url


def _gen_upload_approval_file_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=UploadApprovalFileResp,
        scope="Approval",
        api="UploadApprovalFile",
        method="POST",
        url="https://www.feishu.cn/approval/openapi/v2/file/upload",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
