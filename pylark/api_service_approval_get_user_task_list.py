# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class GetApprovalUserTaskListReqUserIDType(object):
    pass


@attr.s
class GetApprovalUserTaskListReq(object):
    page_size: int = attr.ib(
        default=0, metadata={"req_type": "query", "key": "page_size"}
    )  # 分页大小, 示例值：100, 最大值：`200`
    page_token: str = attr.ib(
        default="", metadata={"req_type": "query", "key": "page_token"}
    )  # 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果, 示例值："1"
    user_id: str = attr.ib(
        default="", metadata={"req_type": "query", "key": "user_id"}
    )  # 需要查询的 User ID, 示例值："example_user_id"
    topic: str = attr.ib(
        default="", metadata={"req_type": "query", "key": "topic"}
    )  # 需要查询的任务分组主题，如「待办」、「已办」等, 示例值："1", 可选值有: `1`：待办审批, `2`：已办审批, `3`：已发起审批, `17`：未读知会, `18`：已读知会
    user_id_type: GetApprovalUserTaskListReqUserIDType = attr.ib(
        default=None, metadata={"req_type": "query", "key": "user_id_type"}
    )  # 用户 ID 类型, 示例值："open_id", 可选值有: `open_id`：用户的 open id, `union_id`：用户的 union id, `user_id`：用户的 user id, 默认值: `open_id`,, 当值为 `user_id`, 字段权限要求: 获取用户 user ID


@attr.s
class GetApprovalUserTaskListRespCount(object):
    total: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "total"}
    )  # 总数，大于等于 1000 个项目时将返回 999
    has_more: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json", "key": "has_more"}
    )  # 还有更多，当大于等于 1000 时将返回 true


@attr.s
class GetApprovalUserTaskListRespTaskURLs(object):
    helpdesk: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "helpdesk"}
    )  # 帮助服务台 URL
    mobile: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "mobile"}
    )  # 移动端 URL
    pc: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "pc"}
    )  # PC 端 URL


@attr.s
class GetApprovalUserTaskListRespTask(object):
    topic: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "topic"}
    )  # 任务所属的任务分组，如「待办」、「已办」等, 可选值有: `1`：待办审批, `2`：已办审批, `3`：已发起审批, `17`：未读知会, `18`：已读知会
    user_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "user_id"}
    )  # 任务所属的用户 ID
    title: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "title"}
    )  # 任务题目
    urls: GetApprovalUserTaskListRespTaskURLs = attr.ib(
        default=None, metadata={"req_type": "json", "key": "urls"}
    )  # 任务相关 URL
    process_external_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "process_external_id"}
    )  # 流程三方 ID，仅第三方流程，需要在当前租户、当前 APP 内唯一
    task_external_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "task_external_id"}
    )  # 任务三方 ID，仅第三方流程，需要在当前流程实例内唯一
    status: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "status"}
    )  # 任务状态, 可选值有: `1`：待办, `2`：已办, `17`：未读, `18`：已读, `33`：处理中，标记完成用, `34`：撤回
    process_status: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "process_status"}
    )  # 流程实例状态, 可选值有: `0`：无流程状态，不展示对应标签, `1`：流程实例流转中, `2`：已通过, `3`：已拒绝, `4`：已撤销, `5`：已终止
    definition_code: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "definition_code"}
    )  # 流程定义 Code
    initiators: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "initiators"}
    )  # 发起人 ID 列表
    initiator_names: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "initiator_names"}
    )  # 发起人姓名列表
    task_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "task_id"}
    )  # 任务 ID，全局唯一
    process_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "process_id"}
    )  # 流程 ID，全局唯一
    process_code: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "process_code"}
    )  # 流程 Code
    definition_group_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "definition_group_id"}
    )  # 流程定义分组 ID
    definition_group_name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "definition_group_name"}
    )  # 流程定义分组名称
    definition_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "definition_id"}
    )  # 流程定义 ID
    definition_name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "definition_name"}
    )  # 流程定义名称


@attr.s
class GetApprovalUserTaskListResp(object):
    tasks: typing.List[GetApprovalUserTaskListRespTask] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "tasks"}
    )  # 任务列表
    page_token: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "page_token"}
    )  # 分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token
    has_more: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json", "key": "has_more"}
    )  # 是否还有更多项
    count: GetApprovalUserTaskListRespCount = attr.ib(
        default=None, metadata={"req_type": "json", "key": "count"}
    )  # 列表计数，只在分页第一页返回


def _gen_get_approval_user_task_list_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetApprovalUserTaskListResp,
        scope="Approval",
        api="GetApprovalUserTaskList",
        method="GET",
        url="https://open.feishu.cn/open-apis/approval/v4/tasks/query",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        need_user_access_token=True,
    )
