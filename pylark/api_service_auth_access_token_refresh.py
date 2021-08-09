# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing


@attr.s
class RefreshAccessTokenReq(object):
    grant_type: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 本流程中，此值为 refresh_token
    refresh_token: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 来自[获取登录用户身份(新)](https://open.feishu.cn/document/ukTMukTMukTM/uEDO4UjLxgDO14SM4gTN) 或 本接口返回值


@attr.s
class RefreshAccessTokenResp(object):
    access_token: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # user_access_token，用于获取用户资源
    avatar_url: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户头像
    avatar_thumb: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户头像 72x72
    avatar_middle: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 用户头像 240x240
    avatar_big: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户头像 640x640
    expires_in: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # access_token 的有效期，单位: 秒
    name: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户姓名
    en_name: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户英文名称
    open_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户在应用内的唯一标识
    union_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户统一ID
    email: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 申请了"获取用户邮箱"权限的应用返回该字段
    user_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 申请了"获取用户 user_id"权限的应用返回该字段
    mobile: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 申请了"获取用户手机号"权限的应用返回该字段
    tenant_key: str = attr.ib(default="", metadata={"req_type": "json"})  # 当前企业标识
    refresh_expires_in: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # refresh_token 的有效期，单位: 秒
    refresh_token: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 刷新用户 access_token 时使用的 token
    token_type: str = attr.ib(default="", metadata={"req_type": "json"})  # 此处为 Bearer


def _gen_refresh_access_token_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=RefreshAccessTokenResp,
        scope="Auth",
        api="RefreshAccessToken",
        method="POST",
        url="https://open.feishu.cn/open-apis/authen/v1/refresh_access_token",
        body=request,
        method_option=_new_method_option(options),
    )