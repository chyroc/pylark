# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing


@attr.s
class GetTenantReq(object):
    pass


@attr.s
class GetTenantRespTenantAvatar(object):
    avatar_origin: str = attr.ib(default="", metadata={"req_type": "json"})  # 企业头像
    avatar_72: str = attr.ib(default="", metadata={"req_type": "json"})  # 企业头像 72x72
    avatar_240: str = attr.ib(default="", metadata={"req_type": "json"})  # 企业头像 240x240
    avatar_640: str = attr.ib(default="", metadata={"req_type": "json"})  # 企业头像 640x640


@attr.s
class GetTenantRespTenant(object):
    name: str = attr.ib(default="", metadata={"req_type": "json"})  # 企业名称
    display_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 企业编号
    tenant_tag: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 个人版/团队版标志, 可选值有: `0`：团队版, `2`：个人版
    tenant_key: str = attr.ib(default="", metadata={"req_type": "json"})  # 企业标识
    avatar: GetTenantRespTenantAvatar = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 企业头像


@attr.s
class GetTenantResp(object):
    tenant: GetTenantRespTenant = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 企业信息


def _gen_get_tenant_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetTenantResp,
        scope="Tenant",
        api="GetTenant",
        method="GET",
        url="https://open.feishu.cn/open-apis/tenant/v2/tenant/query",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )