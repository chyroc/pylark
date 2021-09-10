# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class AddApprovalInstanceSignReq(object):
    approval_code: str = attr.ib(default="", metadata={"req_type": "json"})  # 审批定义 Code
    instance_code: str = attr.ib(default="", metadata={"req_type": "json"})  # 审批实例 Code
    user_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 操作用户
    task_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 任务 ID
    comment: str = attr.ib(default="", metadata={"req_type": "json"})  # 意见
    add_sign_user_ids: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 被加签人id
    add_sign_type: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 1/2/3分别代表前加签/后加签/并加签
    approval_method: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 仅在前加签、后加签时需要填写，1/2 分别代表或签/会签


@attr.s
class AddApprovalInstanceSignResp(object):
    pass


def _gen_add_approval_instance_sign_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=AddApprovalInstanceSignResp,
        scope="Approval",
        api="AddApprovalInstanceSign",
        method="POST",
        url="https://open.feishu.cn/open-apis/approval/v4/instances/add_sign",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )