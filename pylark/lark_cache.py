import time
from typing import Tuple

from pylark import Response
from pylark.api_service_auth_tenant_access_token_get import TokenExpire


def get_current_sec():
    return int(round(time.time()))


def get_access_token_cache(
        last_get_access_token_time: int,
        last_access_token_expire_time: int,
        current_access_token: int,

) -> Tuple[TokenExpire, Response]:

    if last_get_access_token_time != 0 and current_access_token != "":
        cur_time = get_current_sec()
        if cur_time - last_get_access_token_time < last_access_token_expire_time:
            return (
                TokenExpire(
                    token=current_access_token,
                    expire=last_access_token_expire_time - (cur_time - last_get_access_token_time)
                ),
                Response(),
            )
        return TokenExpire(), Response()


def set_access_token_cache(
    resp_data
):
    get_current_sec(), resp_data.get("expire") or 0, resp_data.get("tenant_access_token") or ""
