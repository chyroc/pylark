# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class DeleteTaskReminderReq(object):
    task_id: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 任务 ID, 示例值："83912691-2e43-47fc-94a4-d512e03984fa"
    reminder_id: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 任务提醒时间设置的 ID（即 reminder.id）, 示例值："1"


@attr.s
class DeleteTaskReminderResp(object):
    pass


def _gen_delete_task_reminder_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=DeleteTaskReminderResp,
        scope="Task",
        api="DeleteTaskReminder",
        method="DELETE",
        url="https://open.feishu.cn/open-apis/task/v1/tasks/:task_id/reminders/:reminder_id",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
