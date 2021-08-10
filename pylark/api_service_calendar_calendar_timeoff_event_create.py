# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class CreateCalendarTimeoffEventReqUserIDType(object):
    pass


@attr.s
class CreateCalendarTimeoffEventReq(object):
    user_id_type: CreateCalendarTimeoffEventReqUserIDType = attr.ib(
        default=None, metadata={"req_type": "query"}
    )  # 用户 ID 类型, 示例值："open_id", 可选值有: `open_id`：用户的 open id, `union_id`：用户的 union id, `user_id`：用户的 user id, 默认值: `open_id`, 当值为 `user_id`, 字段权限要求: 获取用户 userid
    user_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 用户id, 示例值："ou_XXXXXXXXXX"
    timezone: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 时区, 示例值："Asia/Shanghai"
    start_time: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 休假开始时间: 有时间戳(1609430400)和日期(2021-01-01)两种格式，其它格式无效；,时间戳格式是按小时休假日程，日期格式是全天休假日程；,start_time与end_time格式需保持一致，否则无效。, 示例值："2021-01-01"
    end_time: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 休假结束时间：,有时间戳(1609430400)和日期(2021-01-01)两种格式，其它格式无效；,时间戳格式是按小时休假日程，日期格式是全天休假日程；,start_time与end_time格式需保持一致，否则无效。, 示例值："2021-01-01"
    title: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 自定义请假日程标题，没有设置则为默认日程标题, 示例值："请假中(全天) / 1-Day Time Off"
    description: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 自定义请假日程描述，没有设置则为默认日程描述, 示例值："若删除此日程，飞书中相应的“请假”标签将自动消失，而请假系统中的休假申请不会被撤销。"


@attr.s
class CreateCalendarTimeoffEventResp(object):
    timeoff_event_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 请假日程ID
    user_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户id
    timezone: str = attr.ib(default="", metadata={"req_type": "json"})  # 时区
    start_time: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 休假开始时间: 有时间戳(1609430400)和日期(2021-01-01)两种格式，其它格式无效；,时间戳格式是按小时休假日程，日期格式是全天休假日程；,start_time与end_time格式需保持一致，否则无效。
    end_time: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 休假结束时间：,有时间戳(1609430400)和日期(2021-01-01)两种格式，其它格式无效；,时间戳格式是按小时休假日程，日期格式是全天休假日程；,start_time与end_time格式需保持一致，否则无效。
    title: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 自定义请假日程标题，没有设置则为默认日程标题
    description: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 自定义请假日程描述，没有设置则为默认日程描述


def _gen_create_calendar_timeoff_event_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=CreateCalendarTimeoffEventResp,
        scope="Calendar",
        api="CreateCalendarTimeoffEvent",
        method="POST",
        url="https://open.feishu.cn/open-apis/calendar/v4/timeoff_events",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
