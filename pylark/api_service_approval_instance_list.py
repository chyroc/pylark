# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing


@attr.s
class GetApprovalInstanceListReq(object):
    approval_code: str = attr.ib(default="", metadata={"req_type": "json"})  # 审批定义唯一标识
    start_time: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 审批实例创建时间区间（毫秒）
    end_time: int = attr.ib(default=0, metadata={"req_type": "json"})  # 审批实例创建时间区间（毫秒）
    offset: int = attr.ib(default=0, metadata={"req_type": "json"})  # 查询偏移量
    limit: int = attr.ib(default=0, metadata={"req_type": "json"})  # 查询限制量 注:不得大于100


@attr.s
class GetApprovalInstanceListResp(object):
    instance_code_list: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 审批实例 Code


def _gen_get_approval_instance_list_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetApprovalInstanceListResp,
        scope="Approval",
        api="GetApprovalInstanceList",
        method="POST",
        url="https://www.feishu.cn/approval/openapi/v2/instance/list",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
