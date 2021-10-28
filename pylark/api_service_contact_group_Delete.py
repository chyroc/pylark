# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
from pylark import lark_type_enum, lark_type_sheet
import attr
import typing
import io


@attr.s
class DeleteContactGroupReq(object):
    group_id: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "group_id"}
    )  # 需删除的用户组ID, 示例值："g1837191"


@attr.s
class DeleteContactGroupResp(object):
    pass


def _gen_delete_contact_group_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=DeleteContactGroupResp,
        scope="Contact",
        api="DeleteContactGroup",
        method="DELETE",
        url="https://open.feishu.cn/open-apis/contact/v3/group/:group_id",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
