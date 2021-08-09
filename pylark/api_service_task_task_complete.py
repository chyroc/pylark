# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing


@attr.s
class CompleteTaskReq(object):
    task_id: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 任务 ID, 示例值："bb54ab99-d360-434f-bcaa-a4cc4c05840e"


@attr.s
class CompleteTaskResp(object):
    pass


def _gen_complete_task_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=CompleteTaskResp,
        scope="Task",
        api="CompleteTask",
        method="POST",
        url="https://open.feishu.cn/open-apis/task/v1/tasks/:task_id/complete",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )