# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class BatchGetUserByIDReq(object):
    emails: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "query"}
    )  # 要查询的用户邮箱，最多 50 条。
    mobiles: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "query"}
    )  # 要查询的用户手机号，最多 50 条。<br>非中国大陆地区的手机号需要添加以 “+” 开头的国家 / 地区代码，并且需要进行 URL 转义。<br>


@attr.s
class BatchGetUserByIDRespEmailUser(object):
    open_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户的 open_id。
    user_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 用户的 user_id。<br>只有已申请 `获取用户UserID` 权限的企业自建应用返回此字段。


@attr.s
class BatchGetUserByIDRespEmailUser(object):
    open_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户的 open_id。
    user_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 用户的 user_id。<br>只有已申请 `获取用户UserID` 权限的企业自建应用返回此字段。


@attr.s
class BatchGetUserByIDResp(object):
    email_users: BatchGetUserByIDRespEmailUser = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 根据邮箱查询到的用户，key 为邮箱，value 为查询到用户的 array。<br>目前同一个邮箱最多只能查询到一个用户。
    emails_not_exist: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 没有匹配记录的邮箱。
    mobile_users: BatchGetUserByIDRespEmailUser = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 根据手机号查询到的用户，key 为手机号，value 为查询到用户的 array。<br>目前同一个手机号最多只能查询到一个用户。
    mobiles_not_exist: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 没有匹配记录的手机号。


def _gen_batch_get_user_by_id_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=BatchGetUserByIDResp,
        scope="Contact",
        api="BatchGetUserByID",
        method="GET",
        url="https://open.feishu.cn/open-apis/user/v1/batch_get_id",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
