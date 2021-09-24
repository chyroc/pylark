# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class PreviewApprovalInstanceReqForm(object):
    id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 控件ID，也可以使用自定义 ID custom_id 的值
    type: str = attr.ib(default="", metadata={"req_type": "json"})  # 控件类型
    value: str = attr.ib(default="", metadata={"req_type": "json"})  # 控件值，不同类型的值格式不一样


@attr.s
class PreviewApprovalInstanceReqUserIDType(object):
    pass


@attr.s
class PreviewApprovalInstanceReq(object):
    user_id_type: PreviewApprovalInstanceReqUserIDType = attr.ib(
        default=None, metadata={"req_type": "query"}
    )  # 默认为open_id, 对于open_id(ou_开头)类型，user_id_type为open_id, 对于employeeID(8位字符串，如f7cb567e)类型，user_id_type为user_id
    approval_code: str = attr.ib(default="", metadata={"req_type": "json"})  # 审批定义 Code
    user_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 发起审批用户，employeid或者openid
    department_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 发起审批用户部门，如果用户只属于一个部门，可以不填，如果属于多个部门，必须填其中一个部门
    form: PreviewApprovalInstanceReqForm = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # JSON字符串，控件值。提交审批之前，查看预览流程时，该字段必填
    instance_code: str = attr.ib(default="", metadata={"req_type": "json"})  # 审批实例code
    task_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 若审批实例已存在，则传递当前审批任务对应的task_id


@attr.s
class PreviewApprovalInstanceResp(object):
    preview_nodes: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 预览节点信息
    user_id_list: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 审批人id列表
    end_cc_id_list: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 审批结束抄送人id列表
    node_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 节点id
    node_name: str = attr.ib(default="", metadata={"req_type": "json"})  # 节点名称
    node_type: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 节点类型：<br>AND：会签<br>OR: 或签
    custom_node_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 用户自定义节点id
    comments: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 节点的说明信息


def _gen_preview_approval_instance_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=PreviewApprovalInstanceResp,
        scope="Approval",
        api="PreviewApprovalInstance",
        method="POST",
        url="https://open.feishu.cn/open-apis/approval/v4/instances/preview",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
