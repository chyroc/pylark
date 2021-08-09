# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing


@attr.s
class GetHireReferralByApplicationReqUserIDType(object):
    pass


@attr.s
class GetHireReferralByApplicationReq(object):
    application_id: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # 投递的id, 示例值："6134134355464633"
    user_id_type: IDType = attr.ib(
        default=None, metadata={"req_type": "query"}
    )  # 用户 ID 类型, 示例值："open_id", 可选值有: `open_id`：用户的 open id, `union_id`：用户的 union id, `user_id`：用户的 user id, 默认值: `open_id`, 当值为 `user_id`, 字段权限要求: 获取用户 userid


@attr.s
class GetHireReferralByApplicationRespReferral(object):
    application_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 投递id
    create_time: int = attr.ib(default=0, metadata={"req_type": "json"})  # 创建时间（ms）
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # 内推的id
    referral_user_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 内推人的id


@attr.s
class GetHireReferralByApplicationResp(object):
    referral: GetHireReferralByApplicationRespReferral = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 内推信息


def _gen_get_hire_referral_by_application_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetHireReferralByApplicationResp,
        scope="Hire",
        api="GetHireReferralByApplication",
        method="GET",
        url="https://open.feishu.cn/open-apis/hire/v1/referrals/get_by_application",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )