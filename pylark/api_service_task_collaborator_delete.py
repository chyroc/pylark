# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
from pylark import lark_type_enum, lark_type_sheet
import attr
import typing
import io


@attr.s
class DeleteTaskCollaboratorReq(object):
    task_id: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "task_id"}
    )  # 任务 ID, 示例值："83912691-2e43-47fc-94a4-d512e03984fa"
    collaborator_id: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "collaborator_id"}
    )  # 任务协作者 ID（Open ID）, 示例值："ou_99e1a581b36ecc4862cbfbce123f346a"


@attr.s
class DeleteTaskCollaboratorResp(object):
    pass


def _gen_delete_task_collaborator_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=DeleteTaskCollaboratorResp,
        scope="Task",
        api="DeleteTaskCollaborator",
        method="DELETE",
        url="https://open.feishu.cn/open-apis/task/v1/tasks/:task_id/collaborators/:collaborator_id",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
