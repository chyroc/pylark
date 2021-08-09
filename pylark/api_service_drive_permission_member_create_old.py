# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing


@attr.s
class CreateDriveMemberPermissionOldReqMembers(object):
    member_type: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 用户类型，可选 **email 、openid、openchat、userid**
    member_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户类型下的值
    perm: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 需要增加的权限，权限值："view"，"edit"


@attr.s
class CreateDriveMemberPermissionOldReq(object):
    token: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 文件的 token，获取方式见 [对接前说明](https://open.feishu.cn/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN)的第 4 项
    type: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 文档类型  "doc" 、"sheet" 、 "bitable" or "file"
    members: CreateDriveMemberPermissionOldReqMembers = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 用户
    notify_lark: bool = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 添加权限后是否飞书/lark通知对方<br>true 通知 or false 不通知


@attr.s
class CreateDriveMemberPermissionOldRespFailMembers(object):
    member_type: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户类型
    member_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户类型下的值
    perm: str = attr.ib(default="", metadata={"req_type": "json"})  # 需要增加的权限


@attr.s
class CreateDriveMemberPermissionOldResp(object):
    is_all_success: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 是否全部成功
    fail_members: CreateDriveMemberPermissionOldRespFailMembers = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 添加权限失败的用户信息


def _gen_create_drive_member_permission_old_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=CreateDriveMemberPermissionOldResp,
        scope="Drive",
        api="CreateDriveMemberPermissionOld",
        method="POST",
        url="https://open.feishu.cn/open-apis/drive/permission/member/create",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
