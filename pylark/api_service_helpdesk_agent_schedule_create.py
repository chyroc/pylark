# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class CreateHelpdeskAgentScheduleReqAgentScheduleSchedule(object):
    start_time: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "start_time"}
    )  # 开始时间, format 00:00 - 23:59, 示例值："00:00"
    end_time: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "end_time"}
    )  # 结束时间, format 00:00 - 23:59, 示例值："24:00"
    weekday: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "weekday"}
    )  # 星期几, 1 - Monday, 2 - Tuesday, 3 - Wednesday, 4 - Thursday, 5 - Friday, 6 - Saturday, 7 - Sunday, 9 - Everday, 10 - Weekday, 11 - Weekend, 示例值：9


@attr.s
class CreateHelpdeskAgentScheduleReqAgentSchedule(object):
    agent_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "agent_id"}
    )  # 客服id, 示例值："agent-id"
    schedule: CreateHelpdeskAgentScheduleReqAgentScheduleSchedule = attr.ib(
        default=None, metadata={"req_type": "json", "key": "schedule"}
    )  # 工作日程列表
    agent_skill_ids: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "agent_skill_ids"}
    )  # 客服技能 ids


@attr.s
class CreateHelpdeskAgentScheduleReq(object):
    agent_schedules: typing.List[CreateHelpdeskAgentScheduleReqAgentSchedule] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "agent_schedules"}
    )  # 新客服日程


@attr.s
class CreateHelpdeskAgentScheduleResp(object):
    pass


def _gen_create_helpdesk_agent_schedule_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=CreateHelpdeskAgentScheduleResp,
        scope="Helpdesk",
        api="CreateHelpdeskAgentSchedule",
        method="POST",
        url="https://open.feishu.cn/open-apis/helpdesk/v1/agent_schedules",
        body=request,
        method_option=_new_method_option(options),
        need_user_access_token=True,
        need_helpdesk_auth=True,
    )
