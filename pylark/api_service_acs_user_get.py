# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing


@attr.s
class GetACSUserReqUserIDType(object):
    pass


@attr.s
class GetACSUserReq(object):
    user_id_type: IDType = attr.ib(
        default=None, metadata={"req_type": "query"}
    )  # 用户 ID 类型, 示例值："open_id", 可选值有: `open_id`：用户的 open id, `union_id`：用户的 union id, `user_id`：用户的 user id, 默认值: `open_id`,, 当值为 `user_id`, 字段权限要求: 获取用户 userid
    user_id: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 用户 ID, 示例值："ou_7dab8a3d3cdcc9da365777c7ad535d62"


@attr.s
class GetACSUserRespUserFeature(object):
    card: int = attr.ib(default=0, metadata={"req_type": "json"})  # 卡号
    face_uploaded: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 是否已上传人脸图片


@attr.s
class GetACSUserRespUser(object):
    feature: GetACSUserRespUserFeature = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 用户特征
    user_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户 ID


@attr.s
class GetACSUserResp(object):
    user: GetACSUserRespUser = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 门禁用户信息


def _gen_get_acs_user_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetACSUserResp,
        scope="ACS",
        api="GetACSUser",
        method="GET",
        url="https://open.feishu.cn/open-apis/acs/v1/users/:user_id",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )