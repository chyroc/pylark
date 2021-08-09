# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing


@attr.s
class RejectApprovalInstanceReq(object):
    approval_code: str = attr.ib(default="", metadata={"req_type": "json"})  # 审批定义 Code
    instance_code: str = attr.ib(default="", metadata={"req_type": "json"})  # 审批实例 Code
    open_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 用户open_id，如果没有user_id，必须要有open_id
    user_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 操作用户
    task_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 任务 ID
    comment: str = attr.ib(default="", metadata={"req_type": "json"})  # 意见


@attr.s
class RejectApprovalInstanceResp(object):
    pass


def _gen_reject_approval_instance_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=RejectApprovalInstanceResp,
        scope="Approval",
        api="RejectApprovalInstance",
        method="POST",
        url="https://www.feishu.cn/approval/openapi/v2/instance/reject",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
