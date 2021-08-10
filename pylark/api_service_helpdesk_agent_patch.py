# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class UpdateHelpdeskAgentReq(object):
    agent_id: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 客服id, 示例值："ou_14777d82ffef0f707de5a8c7ff2c5ebe"
    status: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # agent status, 示例值：1：在线；2：离线


@attr.s
class UpdateHelpdeskAgentResp(object):
    pass


def _gen_update_helpdesk_agent_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=UpdateHelpdeskAgentResp,
        scope="Helpdesk",
        api="UpdateHelpdeskAgent",
        method="PATCH",
        url="https://open.feishu.cn/open-apis/helpdesk/v1/agents/:agent_id",
        body=request,
        method_option=_new_method_option(options),
        need_user_access_token=True,
        need_helpdesk_auth=True,
    )
