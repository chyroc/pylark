# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing


@attr.s
class CreateCalendarACLReqScope(object):
    type: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 权限类型，当type为User时，值为open_id/user_id/union_id, 示例值："user", 可选值有: `user`：用户
    user_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 用户ID, 示例值："ou_xxxxxx"


@attr.s
class CreateCalendarACLReqRole(object):
    pass


@attr.s
class CreateCalendarACLReqUserIDType(object):
    pass


@attr.s
class CreateCalendarACLReq(object):
    user_id_type: IDType = attr.ib(
        default=None, metadata={"req_type": "query"}
    )  # 用户 ID 类型, 示例值："open_id", 可选值有: `open_id`：用户的 open id, `union_id`：用户的 union id, `user_id`：用户的 user id, 默认值: `open_id`, 当值为 `user_id`, 字段权限要求: 获取用户 userid
    calendar_id: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 日历ID, 示例值："feishu.cn_xxxxxxxxxx@group.calendar.feishu.cn"
    role: CreateCalendarACLReqRole = attr.ib(
        factory=lambda: CreateCalendarACLReqRole(), metadata={"req_type": "json"}
    )  # 对日历的访问权限, 示例值："writer", 可选值有: `unknown`：未知权限, `free_busy_reader`：游客，只能看到忙碌/空闲信息, `reader`：订阅者，查看所有日程详情, `writer`：编辑者，创建及修改日程, `owner`：管理员，管理日历及共享设置
    scope: CreateCalendarACLReqScope = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 权限范围


@attr.s
class CreateCalendarACLRespScope(object):
    type: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 权限类型，当type为User时，值为open_id/user_id/union_id, 可选值有: `user`：用户
    user_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户ID


@attr.s
class CreateCalendarACLRespRole(object):
    pass


@attr.s
class CreateCalendarACLResp(object):
    acl_id: str = attr.ib(default="", metadata={"req_type": "json"})  # acl资源ID
    role: CreateCalendarACLRespRole = attr.ib(
        factory=lambda: CreateCalendarACLRespRole(), metadata={"req_type": "json"}
    )  # 对日历的访问权限, 可选值有: `unknown`：未知权限, `free_busy_reader`：游客，只能看到忙碌/空闲信息, `reader`：订阅者，查看所有日程详情, `writer`：编辑者，创建及修改日程, `owner`：管理员，管理日历及共享设置
    scope: CreateCalendarACLRespScope = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 权限范围


def _gen_create_calendar_acl_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=CreateCalendarACLResp,
        scope="Calendar",
        api="CreateCalendarACL",
        method="POST",
        url="https://open.feishu.cn/open-apis/calendar/v4/calendars/:calendar_id/acls",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
