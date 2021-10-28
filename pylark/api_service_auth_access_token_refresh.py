# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class RefreshAccessTokenReq(object):
    grant_type: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "grant_type"}
    )  # 授权类型，本流程中，此值为："refresh_token", 示例值："refresh_token"
    refresh_token: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "refresh_token"}
    )  # 来自[获取登录用户身份](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/authen-v1/authen/access_token) 或 本接口返回值, 示例值："ur-t9HHgRCsMqGqIU9vw5Zhof"


@attr.s
class RefreshAccessTokenResp(object):
    access_token: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "access_token"}
    )  # user_access_token，用于获取用户资源
    token_type: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "token_type"}
    )  # token 类型
    expires_in: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "expires_in"}
    )  # access_token 的有效期，单位: 秒
    name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "name"}
    )  # 用户姓名
    en_name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "en_name"}
    )  # 用户英文名称
    avatar_url: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "avatar_url"}
    )  # 用户头像
    avatar_thumb: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "avatar_thumb"}
    )  # 用户头像 72x72
    avatar_middle: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "avatar_middle"}
    )  # 用户头像 240x240
    avatar_big: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "avatar_big"}
    )  # 用户头像 640x640
    open_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "open_id"}
    )  # 用户在应用内的唯一标识
    union_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "union_id"}
    )  # 用户统一ID
    email: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "email"}
    )  # 用户邮箱, 字段权限要求:  获取用户邮箱信息
    user_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "user_id"}
    )  # 用户 user_id, 字段权限要求:  获取用户 user ID
    mobile: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "mobile"}
    )  # 用户手机号, 字段权限要求:  获取用户手机号
    tenant_key: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "tenant_key"}
    )  # 当前企业标识
    refresh_expires_in: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "refresh_expires_in"}
    )  # refresh_token 的有效期，单位: 秒
    refresh_token: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "refresh_token"}
    )  # 刷新用户 access_token 时使用的 token


def _gen_refresh_access_token_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=RefreshAccessTokenResp,
        scope="Auth",
        api="RefreshAccessToken",
        method="POST",
        url="https://open.feishu.cn/open-apis/authen/v1/refresh_access_token",
        body=request,
        method_option=_new_method_option(options),
        need_app_access_token=True,
        need_user_access_token=True,
    )
