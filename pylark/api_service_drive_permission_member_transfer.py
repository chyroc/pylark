# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class TransferDriveMemberPermissionReqOwner(object):
    member_type: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 用户类型，可选 **email、openid、userid**
    member_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户类型下的值


@attr.s
class TransferDriveMemberPermissionReq(object):
    token: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 文件的 token，获取方式见 [对接前说明](https://open.feishu.cn/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN)的第 4 项
    type: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 文档类型  "doc"  or  "sheet" or "bitable"  or "file"
    owner: TransferDriveMemberPermissionReqOwner = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 要转移到的新的文档所有者
    remove_old_owner: bool = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # true 为转移后删除旧 owner 的权限，默认为false
    cancel_notify: bool = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # true为不通知新owner，默认为false


@attr.s
class TransferDriveMemberPermissionRespOwner(object):
    member_type: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 用户类型，有 email 、openid、userid
    member_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户类型下的值


@attr.s
class TransferDriveMemberPermissionResp(object):
    is_success: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 请求是否成功
    type: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 文档类型 "doc" or "sheet" or "file"
    token: str = attr.ib(default="", metadata={"req_type": "json"})  # 文档的 token
    owner: TransferDriveMemberPermissionRespOwner = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 文档当前所有者


def _gen_transfer_drive_member_permission_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=TransferDriveMemberPermissionResp,
        scope="Drive",
        api="TransferDriveMemberPermission",
        method="POST",
        url="https://open.feishu.cn/open-apis/drive/permission/member/transfer",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        need_user_access_token=True,
    )
