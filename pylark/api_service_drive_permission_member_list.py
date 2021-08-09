# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing


@attr.s
class GetDriveMemberPermissionListReq(object):
    token: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 文件的 token，获取方式见 [对接前说明](https://open.feishu.cn/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN)的第 4 项
    type: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 文档类型   "doc"  or  "sheet" or "bitable"  or "file"


@attr.s
class GetDriveMemberPermissionListRespMember(object):
    member_type: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 协作者类型 "user" or "chat"
    member_open_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 协作者openid
    member_user_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 协作者userid(仅当member_type="user"时有效)
    perm: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 协作者权限 (注意: **有"edit"权限的协作者一定有"view"权限**)


@attr.s
class GetDriveMemberPermissionListResp(object):
    members: typing.List[GetDriveMemberPermissionListRespMember] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 协作者列表


def _gen_get_drive_member_permission_list_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetDriveMemberPermissionListResp,
        scope="Drive",
        api="GetDriveMemberPermissionList",
        method="POST",
        url="https://open.feishu.cn/open-apis/drive/permission/member/list",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
