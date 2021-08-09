# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing


@attr.s
class GetUserInfoReq(object):
    pass


@attr.s
class GetUserInfoResp(object):
    name: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户姓名
    en_name: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户英文名称
    avatar_url: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户头像
    avatar_thumb: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户头像 72x72
    avatar_middle: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 用户头像 240x240
    avatar_big: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户头像 640x640
    email: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 用户邮箱，拥有"获取用户邮箱"权限时返回
    user_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 用户的 user_id，申请了"获取用户user_id"权限的应用返回该字段
    mobile: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 用户手机号，申请了"获取用户手机号"权限的应用返回该字段
    open_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户在应用内的唯一标识
    union_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 用户对ISV的唯一标识，对于同一个ISV，用户在其名下所有应用的union_id相同
    tenant_key: str = attr.ib(default="", metadata={"req_type": "json"})  # 用于企业标识


def _gen_get_user_info_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetUserInfoResp,
        scope="Auth",
        api="GetUserInfo",
        method="GET",
        url="https://open.feishu.cn/open-apis/authen/v1/user_info",
        body=request,
        method_option=_new_method_option(options),
    )