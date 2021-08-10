# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class CreateTaskReminderReq(object):
    task_id: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 任务 ID, 示例值："83912691-2e43-47fc-94a4-d512e03984fa"
    relative_fire_minute: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 相对于截止时间的提醒时间（如提前 30 分钟，截止时间后 30 分钟，则为 -30）, 示例值：30


@attr.s
class CreateTaskReminderRespReminder(object):
    id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 提醒时间设置的 ID（在删除时候需要使用这个）
    relative_fire_minute: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 相对于截止时间的提醒时间（如提前 30 分钟，截止时间后 30 分钟，则为 -30）


@attr.s
class CreateTaskReminderResp(object):
    reminder: CreateTaskReminderRespReminder = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 返回创建成功的提醒时间


def _gen_create_task_reminder_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=CreateTaskReminderResp,
        scope="Task",
        api="CreateTaskReminder",
        method="POST",
        url="https://open.feishu.cn/open-apis/task/v1/tasks/:task_id/reminders",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
