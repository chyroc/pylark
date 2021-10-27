# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class DeleteContactGroupMemberReqMemberIDType(object):
    pass


@attr.s
class DeleteContactGroupMemberReq(object):
    group_id: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 用户组ID, 示例值："g198123"
    member_type: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 用户组成员的类型，取值为 user, 示例值："user", 可选值有: `user`：user, 默认值: `user`
    member_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 操作移除的用户组成员ID, 示例值："xj82871k"
    member_id_type: DeleteContactGroupMemberReqMemberIDType = attr.ib(
        factory=lambda: DeleteContactGroupMemberReqMemberIDType(),
        metadata={"req_type": "json"},
    )  # 当member_type =user时候，member_id_type表示user_id_type，枚举值为open_id, union_id, user_id, 示例值："open_id", 可选值有: `open_id`：member_type =user时候，表示用户的open_id, `union_id`：member_type =user时候，表示用户的union_id, `user_id`：member_type =user时候，表示用户的user_id, 默认值: `open_id`


@attr.s
class DeleteContactGroupMemberResp(object):
    pass


def _gen_delete_contact_group_member_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=DeleteContactGroupMemberResp,
        scope="Contact",
        api="DeleteContactGroupMember",
        method="POST",
        url="https://open.feishu.cn/open-apis/contact/v3/group/:group_id/member/remove",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )