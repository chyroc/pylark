# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class GetHelpdeskAgentSkillReq(object):
    agent_skill_id: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "agent_skill_id"}
    )  # agent skill id, 示例值："6941215891786825756"


@attr.s
class GetHelpdeskAgentSkillRespAgentSkillAgent(object):
    id: str = attr.ib(default="", metadata={"req_type": "json", "key": "id"})  # user id
    avatar_url: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "avatar_url"}
    )  # user avatar url
    name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "name"}
    )  # user name


@attr.s
class GetHelpdeskAgentSkillRespAgentSkillRule(object):
    id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "id"}
    )  # rule id, 看[获取客服技能rules](https://open.feishu.cn/document/ukTMukTMukTM/ucDOyYjL3gjM24yN4IjN/list-agent-skill-rules) 用于获取rules options
    selected_operator: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "selected_operator"}
    )  # 运算符compare, 看[客服技能运算符options](https://open.feishu.cn/document/ukTMukTMukTM/ucDOyYjL3gjM24yN4IjN/operator-options)
    operator_options: typing.List[int] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "operator_options"}
    )  # rule操作数value，[客服技能及运算符](https://open.feishu.cn/document/ukTMukTMukTM/ucDOyYjL3gjM24yN4IjN/operator-options)
    operand: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "operand"}
    )  # rule操作数value
    category: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "category"}
    )  # rule type，1-知识库，2-工单信息，3-用户飞书信息
    display_name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "display_name"}
    )  # rule 名


@attr.s
class GetHelpdeskAgentSkillRespAgentSkill(object):
    id: str = attr.ib(default="", metadata={"req_type": "json", "key": "id"})  # 技能id
    name: str = attr.ib(default="", metadata={"req_type": "json", "key": "name"})  # 技能名
    rules: typing.List[GetHelpdeskAgentSkillRespAgentSkillRule] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "rules"}
    )  # 技能rules
    agent_ids: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "agent_ids"}
    )  # 具有此技能的客服ids
    is_default: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json", "key": "is_default"}
    )  # 默认技能
    agents: typing.List[GetHelpdeskAgentSkillRespAgentSkillAgent] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "agents"}
    )  # 客服 info


@attr.s
class GetHelpdeskAgentSkillResp(object):
    agent_skill: GetHelpdeskAgentSkillRespAgentSkill = attr.ib(
        default=None, metadata={"req_type": "json", "key": "agent_skill"}
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
        need_helpdesk_auth=True,
    )
