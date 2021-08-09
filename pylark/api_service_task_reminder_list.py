# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing


@attr.s
class GetTaskReminderListReq(object):
    page_size: int = attr.ib(
        default=0, metadata={"req_type": "query"}
    )  # 分页大小, 示例值：50, 最大值：`50`
    page_token: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果, 示例值："「填写上次返回的page_token」"
    task_id: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 任务 ID, 示例值："0d38e26e-190a-49e9-93a2-35067763ed1f"


@attr.s
class GetTaskReminderListRespItem(object):
    id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 提醒时间设置的 ID（在删除时候需要使用这个）
    relative_fire_minute: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 相对于截止时间的提醒时间（如提前 30 分钟，截止时间后 30 分钟，则为 -30）


@attr.s
class GetTaskReminderListResp(object):
    items: typing.List[GetTaskReminderListRespItem] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 返回提醒时间设置列表
    page_token: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token
    has_more: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 是否还有更多项


def _gen_get_task_reminder_list_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetTaskReminderListResp,
        scope="Task",
        api="GetTaskReminderList",
        method="GET",
        url="https://open.feishu.cn/open-apis/task/v1/tasks/:task_id/reminders",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
