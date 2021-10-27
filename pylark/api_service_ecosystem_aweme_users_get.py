# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class GetEcosystemBindAwemeUserReqUserIDType(object):
    pass


@attr.s
class GetEcosystemBindAwemeUserReq(object):
    user_id_type: GetEcosystemBindAwemeUserReqUserIDType = attr.ib(
        default=None, metadata={"req_type": "query"}
    )  # 用户 ID 类型, 示例值："open_id", 可选值有: `open_id`：用户的 open id, `union_id`：用户的 union id, `user_id`：用户的 user id, 默认值: `open_id`, 当值为 `user_id`, 字段权限要求:  获取用户 user ID
    user_id: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # 飞书用户id，由user_id_type决定类型, 示例值："ou_7d8a6e6df7621556ce0d21922b676706ccs"


@attr.s
class GetEcosystemBindAwemeUserRespAwemeUser(object):
    aweme_user_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 抖音用户id
    user_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 绑定的飞书用户id
    is_binded: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 飞书-抖音账号是否绑定


@attr.s
class GetEcosystemBindAwemeUserResp(object):
    aweme_user: GetEcosystemBindAwemeUserRespAwemeUser = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 用户绑定信息


def _gen_get_ecosystem_bind_aweme_user_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetEcosystemBindAwemeUserResp,
        scope="Ecosystem",
        api="GetEcosystemBindAwemeUser",
        method="POST",
        url="https://open.feishu.cn/open-apis/aweme_ecosystem/v1/aweme_users/get_bind_info",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )