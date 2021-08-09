# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing


@attr.s
class GetHelpdeskAgentSkillReq(object):
    agent_skill_id: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # agent skill id, 示例值："6941215891786825756"


@attr.s
class GetHelpdeskAgentSkillRespAgentSkillAgent(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # user id
    avatar_url: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # user avatar url
    name: str = attr.ib(default="", metadata={"req_type": "json"})  # user name


@attr.s
class GetHelpdeskAgentSkillRespAgentSkillRule(object):
    id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # rule id, 看[获取客服技能rules](https://open.feishu.cn/document/ukTMukTMukTM/ucDOyYjL3gjM24yN4IjN/list-agent-skill-rules) 用于获取rules options
    selected_operator: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 运算符compare, 看[客服技能运算符options](https://open.feishu.cn/document/ukTMukTMukTM/ucDOyYjL3gjM24yN4IjN/operator-options)
    operator_options: typing.List[int] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # rule操作数value，[客服技能及运算符](https://open.feishu.cn/document/ukTMukTMukTM/ucDOyYjL3gjM24yN4IjN/operator-options)
    operand: str = attr.ib(default="", metadata={"req_type": "json"})  # rule操作数value
    category: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # rule type，1-知识库，2-工单信息，3-用户飞书信息
    display_name: str = attr.ib(default="", metadata={"req_type": "json"})  # rule 名


@attr.s
class GetHelpdeskAgentSkillRespAgentSkill(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # 技能id
    name: str = attr.ib(default="", metadata={"req_type": "json"})  # 技能名
    rules: typing.List[GetHelpdeskAgentSkillRespAgentSkillRule] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 技能rules
    agent_ids: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 具有此技能的客服ids
    is_default: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 默认技能
    agents: typing.List[GetHelpdeskAgentSkillRespAgentSkillAgent] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 客服 info


@attr.s
class GetHelpdeskAgentSkillResp(object):
    agent_skill: GetHelpdeskAgentSkillRespAgentSkill = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 技能


def _gen_get_helpdesk_agent_skill_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetHelpdeskAgentSkillResp,
        scope="Helpdesk",
        api="GetHelpdeskAgentSkill",
        method="GET",
        url="https://open.feishu.cn/open-apis/helpdesk/v1/agent_skills/:agent_skill_id",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )