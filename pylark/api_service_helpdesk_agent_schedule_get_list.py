# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing


@attr.s
class GetHelpdeskAgentScheduleListReq(object):
    status: typing.List[int] = attr.ib(
        factory=lambda: [], metadata={"req_type": "query"}
    )  # 筛选条件, 1 - online客服, 2 - offline(手动)客服, 3 - off duty(下班)客服, 4 - 移除客服


@attr.s
class GetHelpdeskAgentScheduleListRespAgentScheduleAgentSkill(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # 客服技能 id
    name: str = attr.ib(default="", metadata={"req_type": "json"})  # 客服技能名
    is_default: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 是默认技能


@attr.s
class GetHelpdeskAgentScheduleListRespAgentScheduleSchedule(object):
    start_time: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 开始时间, format 00:00 - 23:59
    end_time: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 结束时间, format 00:00 - 23:59
    weekday: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 星期几, 1 - Monday, 2 - Tuesday, 3 - Wednesday, 4 - Thursday, 5 - Friday, 6 - Saturday, 7 - Sunday, 9 - Everday, 10 - Weekday, 11 - Weekend


@attr.s
class GetHelpdeskAgentScheduleListRespAgentScheduleAgent(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # 客服 id
    avatar_url: str = attr.ib(default="", metadata={"req_type": "json"})  # avatar url
    name: str = attr.ib(default="", metadata={"req_type": "json"})  # 客服名字
    email: str = attr.ib(default="", metadata={"req_type": "json"})  # email
    department: str = attr.ib(default="", metadata={"req_type": "json"})  # 部门
    company_name: str = attr.ib(default="", metadata={"req_type": "json"})  # 公司名


@attr.s
class GetHelpdeskAgentScheduleListRespAgentSchedule(object):
    status: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 客服状态, 1 - online客服, 2 - offline(手动)客服, 3 - off duty(下班)自动处于非服务时间段
    agent: GetHelpdeskAgentScheduleListRespAgentScheduleAgent = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 客服信息
    schedule: GetHelpdeskAgentScheduleListRespAgentScheduleSchedule = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 工作日程列表
    agent_skills: typing.List[
        GetHelpdeskAgentScheduleListRespAgentScheduleAgentSkill
    ] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 客服技能


@attr.s
class GetHelpdeskAgentScheduleListResp(object):
    agent_schedules: typing.List[
        GetHelpdeskAgentScheduleListRespAgentSchedule
    ] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 客服列表


def _gen_get_helpdesk_agent_schedule_list_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetHelpdeskAgentScheduleListResp,
        scope="Helpdesk",
        api="GetHelpdeskAgentScheduleList",
        method="GET",
        url="https://open.feishu.cn/open-apis/helpdesk/v1/agent_schedules",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
