# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class GetChatOldReq(object):
    chat_id: str = attr.ib(
        default="", metadata={"req_type": "query", "key": "chat_id"}
    )  # 群 ID


@attr.s
class GetChatOldRespLeaveMessageVisibility(object):
    pass


@attr.s
class GetChatOldRespJoinMessageVisibility(object):
    pass


@attr.s
class GetChatOldRespMember(object):
    open_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "open_id"}
    )  # 某成员的open_id
    user_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "user_id"}
    )  # 某成员的user_id


@attr.s
class GetChatOldRespI18nNames(object):
    pass


@attr.s
class GetChatOldResp(object):
    avatar: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "avatar"}
    )  # 群头像
    description: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "description"}
    )  # 群描述
    i18n_names: GetChatOldRespI18nNames = attr.ib(
        factory=lambda: GetChatOldRespI18nNames(),
        metadata={"req_type": "json", "key": "i18n_names"},
    )  # 群国际化名称（设置了国际化名称才会有这个字段）
    chat_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "chat_id"}
    )  # 群 ID
    members: typing.List[GetChatOldRespMember] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "members"}
    )  # 成员列表
    name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "name"}
    )  # 群名称，类型为group时有效
    type: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "type"}
    )  # 群类型，group表示群聊，p2p表示单聊
    owner_user_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "owner_user_id"}
    )  # 群主的 user_id（机器人是群主的时候没有这个字段）
    owner_open_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "owner_open_id"}
    )  # 群主的 open_id （机器人是群主的时候没有这个字段）
    only_owner_edit: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json", "key": "only_owner_edit"}
    )  # 是否仅群主可编辑群信息，群信息包括头像、名称、描述、公告
    only_owner_add: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json", "key": "only_owner_add"}
    )  # 是否仅群主可以添加人
    share_allowed: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json", "key": "share_allowed"}
    )  # 是否允许分享群
    add_member_verify: bool = attr.ib(
        factory=lambda: bool(),
        metadata={"req_type": "json", "key": "add_member_verify"},
    )  # 是否开启入群验证
    only_owner_at_all: bool = attr.ib(
        factory=lambda: bool(),
        metadata={"req_type": "json", "key": "only_owner_at_all"},
    )  # 是否仅群主@all
    send_message_permission: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "send_message_permission"}
    )  # 允许谁发送消息<br>all: 所有人<br>  owner： 仅群主<br>selected_member: 指定成员
    join_message_visibility: GetChatOldRespJoinMessageVisibility = attr.ib(
        factory=lambda: GetChatOldRespJoinMessageVisibility(),
        metadata={"req_type": "json", "key": "join_message_visibility"},
    )  # 成员入群通知<br>all：所有人 <br>owner：仅群主 <br>not_anyone：不通知任何人"
    leave_message_visibility: GetChatOldRespLeaveMessageVisibility = attr.ib(
        factory=lambda: GetChatOldRespLeaveMessageVisibility(),
        metadata={"req_type": "json", "key": "leave_message_visibility"},
    )  # 成员退群通知<br>all：所有人 <br>owner：仅群主 <br>not_anyone：不通知任何人
    group_email_enabled: bool = attr.ib(
        factory=lambda: bool(),
        metadata={"req_type": "json", "key": "group_email_enabled"},
    )  # 是否开启群邮件
    send_group_email_permission: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "send_group_email_permission"}
    )  # 发送群邮件的权限<br>owner：仅群主  <br>group_member：群组内成员<br>tenant_member：团队成员 <br>all：所有人


def _gen_get_chat_old_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetChatOldResp,
        scope="Chat",
        api="GetChatOld",
        method="GET",
        url="https://open.feishu.cn/open-apis/chat/v4/info",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
