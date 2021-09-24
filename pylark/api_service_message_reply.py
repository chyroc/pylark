# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class ReplyRawMessageReqMsgType(object):
    pass


@attr.s
class ReplyRawMessageReq(object):
    message_id: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 待回复的消息的ID, 示例值："om_dc13264520392913993dd051dba21dcf"
    content: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 消息内容 json 格式，格式说明参考: [发送消息content说明](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/im-v1/message/create_json), 示例值："{\"text\":\"<at user_id=\"ou_155184d1e73cbfb8973e5a9e698e74f2\">Tom</at> test content\"}"
    msg_type: ReplyRawMessageReqMsgType = attr.ib(
        factory=lambda: ReplyRawMessageReqMsgType(), metadata={"req_type": "json"}
    )  # 消息类型，包括：text、post、image、file、audio、media、sticker、interactive、share_card、share_user, 示例值："text"


@attr.s
class ReplyRawMessageRespMentionIDType(object):
    pass


@attr.s
class ReplyRawMessageRespMention(object):
    key: str = attr.ib(default="", metadata={"req_type": "json"})  # mention key
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户open id
    id_type: ReplyRawMessageRespMentionIDType = attr.ib(
        factory=lambda: ReplyRawMessageRespMentionIDType(),
        metadata={"req_type": "json"},
    )  # id 可以是open_id，user_id或者union_id
    name: str = attr.ib(default="", metadata={"req_type": "json"})  # 被at用户的姓名
    tenant_key: str = attr.ib(default="", metadata={"req_type": "json"})  # tenant key


@attr.s
class ReplyRawMessageRespBody(object):
    content: str = attr.ib(default="", metadata={"req_type": "json"})  # 消息jsonContent


@attr.s
class ReplyRawMessageRespSenderIDType(object):
    pass


@attr.s
class ReplyRawMessageRespSender(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # 该字段标识发送者的id
    id_type: ReplyRawMessageRespSenderIDType = attr.ib(
        factory=lambda: ReplyRawMessageRespSenderIDType(), metadata={"req_type": "json"}
    )  # 该字段标识发送者的id类型
    sender_type: str = attr.ib(default="", metadata={"req_type": "json"})  # 该字段标识发送者的类型
    tenant_key: str = attr.ib(default="", metadata={"req_type": "json"})  # tenant key


@attr.s
class ReplyRawMessageRespMsgType(object):
    pass


@attr.s
class ReplyRawMessageResp(object):
    message_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 消息id open_message_id
    root_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 根消息id open_message_id
    parent_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 父消息的id open_message_id
    msg_type: ReplyRawMessageRespMsgType = attr.ib(
        factory=lambda: ReplyRawMessageRespMsgType(), metadata={"req_type": "json"}
    )  # 消息类型 text post card image等等
    create_time: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 消息生成的时间戳（毫秒）
    update_time: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 消息更新的时间戳（毫秒）
    deleted: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 消息是否被撤回
    updated: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 消息是否被更新
    chat_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 所属的群
    sender: ReplyRawMessageRespSender = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 发送者，可以是用户或应用
    body: ReplyRawMessageRespBody = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 消息内容，json结构，格式说明参考： [消息content说明](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/im-v1/message/events/message_content)
    mentions: typing.List[ReplyRawMessageRespMention] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 被艾特的人或应用的id
    upper_message_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 上一层级的消息id open_message_id


def _gen_reply_raw_message_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=ReplyRawMessageResp,
        scope="Message",
        api="ReplyRawMessage",
        method="POST",
        url="https://open.feishu.cn/open-apis/im/v1/messages/:message_id/reply",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
