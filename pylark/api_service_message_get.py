# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing


@attr.s
class GetMessageReq(object):
    message_id: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 待获取消息内容的消息的ID, 示例值："om_dc13264520392913993dd051dba21dcf"


@attr.s
class GetMessageRespItemMentionIDType(object):
    pass


@attr.s
class GetMessageRespItemMention(object):
    key: str = attr.ib(default="", metadata={"req_type": "json"})  # mention key
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户open id
    id_type: GetMessageRespItemMentionIDType = attr.ib(
        factory=lambda: GetMessageRespItemMentionIDType(), metadata={"req_type": "json"}
    )  # id 可以是open_id，user_id或者union_id
    name: str = attr.ib(default="", metadata={"req_type": "json"})  # 被at用户的姓名


@attr.s
class GetMessageRespItemBody(object):
    content: str = attr.ib(default="", metadata={"req_type": "json"})  # 消息jsonContent


@attr.s
class GetMessageRespItemSenderIDType(object):
    pass


@attr.s
class GetMessageRespItemSender(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # 该字段标识发送者的id
    id_type: GetMessageRespItemSenderIDType = attr.ib(
        factory=lambda: GetMessageRespItemSenderIDType(), metadata={"req_type": "json"}
    )  # 该字段标识发送者的id类型
    sender_type: str = attr.ib(default="", metadata={"req_type": "json"})  # 该字段标识发送者的类型


@attr.s
class GetMessageRespItemMsgType(object):
    pass


@attr.s
class GetMessageRespItem(object):
    message_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 消息id open_message_id
    root_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 根消息id open_message_id
    parent_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 父消息的id open_message_id
    msg_type: GetMessageRespItemMsgType = attr.ib(
        factory=lambda: GetMessageRespItemMsgType(), metadata={"req_type": "json"}
    )  # 消息类型 text post card image等等
    create_time: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 消息生成的时间戳(毫秒)
    update_time: str = attr.ib(default="", metadata={"req_type": "json"})  # 消息更新的时间戳
    deleted: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 消息是否被撤回
    updated: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 消息是否被更新
    chat_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 所属的群
    sender: Sender = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 发送者，可以是用户或应用
    body: MessageBody = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 消息内容，json结构，格式说明参考： [消息content说明](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/im-v1/message/events/message_content)
    mentions: typing.List[Mention] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 被艾特的人或应用的id
    upper_message_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 上一层级的消息id open_message_id


@attr.s
class GetMessageResp(object):
    items: typing.List[GetMessageRespItem] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # -


def _gen_get_message_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetMessageResp,
        scope="Message",
        api="GetMessage",
        method="GET",
        url="https://open.feishu.cn/open-apis/im/v1/messages/:message_id",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
