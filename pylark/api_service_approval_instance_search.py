# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing


@attr.s
class SearchApprovalInstanceReq(object):
    user_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户 id
    approval_code: str = attr.ib(default="", metadata={"req_type": "json"})  # 审批定义 code
    instance_code: str = attr.ib(default="", metadata={"req_type": "json"})  # 审批实例 code
    instance_external_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 审批实例第三方 id <br>注：和 approval_code 取并集
    group_external_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 审批定义分组第三方 id <br>注：和 instance_code 取并集
    instance_title: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 审批实例标题（只有第三方审批有）
    instance_status: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 审批实例状态<br>REJECT：拒绝<br>PENDING：审批中<br>RECALL：撤回<br>DELETED： 已删除<br>APPROVED：通过<br>注：若不设置，查询全部状态<br>若不在集合中，报错
    instance_start_time_from: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 实例查询开始时间（unix毫秒时间戳）
    instance_start_time_to: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 实例查询结束时间  (unix毫秒时间戳)
    locale: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 地区 （zh-CN、en-US、ja-JP）
    offset: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 查询偏移量 <br>注：不得超过10000
    limit: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 查询限制量 <br>注：不得超过200<br>不设置默认查询10条数据


@attr.s
class SearchApprovalInstanceRespInstanceInstanceLink(object):
    pc_link: str = attr.ib(default="", metadata={"req_type": "json"})  # 审批实例 pc 端链接
    mobile_link: str = attr.ib(default="", metadata={"req_type": "json"})  # 审批实例移动端链接


@attr.s
class SearchApprovalInstanceRespInstanceInstance(object):
    code: str = attr.ib(default="", metadata={"req_type": "json"})  # 审批实例 code
    external_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 审批实例外部 id
    user_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 审批实例发起人 id
    start_time: int = attr.ib(default=0, metadata={"req_type": "json"})  # 审批实例开始时间
    end_time: int = attr.ib(default=0, metadata={"req_type": "json"})  # 审批实例结束时间
    status: str = attr.ib(default="", metadata={"req_type": "json"})  # 审批实例状态
    title: str = attr.ib(default="", metadata={"req_type": "json"})  # 审批实例名称（只有第三方审批有）
    extra: str = attr.ib(default="", metadata={"req_type": "json"})  # 审批实例扩展字段
    serial_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 审批流水号
    link: SearchApprovalInstanceRespInstanceInstanceLink = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 审批实例链接（只有第三方审批有）


@attr.s
class SearchApprovalInstanceRespInstanceApprovalGroup(object):
    external_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 审批定义分组外部 id
    name: str = attr.ib(default="", metadata={"req_type": "json"})  # 审批定义分组名称


@attr.s
class SearchApprovalInstanceRespInstanceApprovalExternal(object):
    batch_cc_read: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 是否支持批量读


@attr.s
class SearchApprovalInstanceRespInstanceApproval(object):
    code: str = attr.ib(default="", metadata={"req_type": "json"})  # 审批定义 code
    name: str = attr.ib(default="", metadata={"req_type": "json"})  # 审批定义名称
    is_external: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 是否为第三方审批
    external: SearchApprovalInstanceRespInstanceApprovalExternal = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 第三方审批信息
    group: SearchApprovalInstanceRespInstanceApprovalGroup = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 审批定义分组


@attr.s
class SearchApprovalInstanceRespInstance(object):
    approval: SearchApprovalInstanceRespInstanceApproval = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 审批定义
    instance: SearchApprovalInstanceRespInstanceInstance = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 审批实例信息


@attr.s
class SearchApprovalInstanceResp(object):
    count: int = attr.ib(default=0, metadata={"req_type": "json"})  # 查询返回条数
    instance_list: typing.List[SearchApprovalInstanceRespInstance] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 审批实例列表


def _gen_search_approval_instance_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=SearchApprovalInstanceResp,
        scope="Approval",
        api="SearchApprovalInstance",
        method="POST",
        url="https://www.feishu.cn/approval/openapi/v2/instance/search",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
