from pylark.lark_request import RawRequestReq, _new_method_option, Request, Response
from typing import TYPE_CHECKING, Tuple
import attr

if TYPE_CHECKING:
    from pylark.lark import Lark


@attr.s
class GetTenantAccessTokenReq(object):
    app_id = attr.ib(metadata={"req_type": "json"})  # 应用唯一标识，创建应用后获得
    app_secret = attr.ib(metadata={"req_type": "json"})  # 应用秘钥，创建应用后获得


@attr.s
class TokenExpire(object):
    token = attr.ib(default="")
    expire = attr.ib(default=0)


def _get_tenant_access_token(
    cli: "Lark",
    is_isv: bool,
    app_id: str,
    app_secret: str,
    tenant_key: str,
) -> Tuple[TokenExpire, Response]:
    # mock

    # cache

    uri = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal/"
    body = {
        "app_id": app_id,
        "app_secret": app_secret,
    }
    if is_isv:
        # TODO
        app_access_token = ""
        uri = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/"
        body = {
            "app_access_token": app_access_token,
            "tenant_key": tenant_key,
        }

    req = RawRequestReq(
        # dataclass=GetTenantAccessTokenResp,
        scope="Auth",
        api="GetTenantAccessToken",
        method="POST",
        url=uri,
        body=body,
        method_option=_new_method_option(),
    )

    data, response = Request.raw_request(cli, req)

    # set cache

    return (
        TokenExpire(
            token=data.get("tenant_access_token") or "", expire=data.get("expire") or 0
        ),
        response,
    )
