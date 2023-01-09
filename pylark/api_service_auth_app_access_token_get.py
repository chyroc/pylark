from pylark.api_service_auth_tenant_access_token_get import TokenExpire
from pylark.lark_cache import get_access_token_cache, set_access_token_cache
from pylark.lark_request import RawRequestReq, _new_method_option, Request, Response
from typing import TYPE_CHECKING, Tuple
import attr

if TYPE_CHECKING:
    from pylark.lark import Lark


def __get_app_access_token(
        cli: "Lark",
        is_isv: bool,
):
    uri = "https://open.feishu.cn/open-apis/auth/v3/app_access_token/internal/"
    app_ticket = ""
    if is_isv:
        uri = "https://open.feishu.cn/open-apis/auth/v3/app_access_token/"
        app_ticket = cli.auth.get_app_ticket()

    req = RawRequestReq(
        scope="Auth",
        api="GetAppAccessToken",
        method="POST",
        url=uri,
        body={
            "app_id": cli.app_id,
            "app_secret": cli.app_secret,
            "app_ticket": app_ticket,
        },
        method_option=_new_method_option(),
    )

    return Request.raw_request(cli, req)


def _get_app_access_token(
        cli: "Lark",
        is_isv: bool,
        use_cache: bool,
):
    if use_cache:
        return _get_app_access_token_by_cache(
            cli=cli,
            is_isv=is_isv
        )

    return _get_app_access_token_common(
        cli=cli,
        is_isv=is_isv
    )


def _get_app_access_token_common(
        cli: "Lark",
        is_isv: bool,
) -> Tuple[TokenExpire, Response]:
    data, response = __get_app_access_token(
        cli=cli,
        is_isv=is_isv
    )

    return (
        TokenExpire(
            token=data.get("app_access_token") or "", expire=data.get("expire") or 0
        ),
        response,
    )


def _get_app_access_token_by_cache(
        cli: "Lark",
        is_isv: bool,
) -> Tuple[TokenExpire, Response]:
    # cache
    token_expire, response = get_access_token_cache(
        cli.last_get_app_access_token_time,
        cli.last_app_access_token_expire_time,
        cli.current_app_access_token,
    )

    if token_expire.token != "":
        return token_expire, response

    data, response = __get_app_access_token(
        cli=cli,
        is_isv=is_isv
    )

    # set cache
    cli.last_get_app_access_token_time, cli.last_app_access_token_expire_time, cli.current_app_access_token = set_access_token_cache(
        data
    )

    return (
        TokenExpire(
            token=data.get("app_access_token") or "", expire=data.get("expire") or 0
        ),
        response,
    )
