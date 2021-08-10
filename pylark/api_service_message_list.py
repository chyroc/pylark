# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class GetMessageListReqContainerIDType(object):
    pass


@attr.s
class GetMessageListReq(object):
    container_id_type: GetMessageListReqContainerIDType = attr.ib(
        factory=lambda: GetMessageListReqContainerIDType(),
        metadata={"req_type": "query"},
    )  # 容器类型 ，目前可选值仅有"chat", 示例值："chat"
    container_id: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # 容器的id，即chat的id, 示例值："oc_234jsi43d3ssi993d43545f"
    start_time: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # 历史信息的起始时间, 示例值："1609296809"
    end_time: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # 历史信息的结束时间, 示例值："1608594809"
    page_token: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果, 示例值："GxmvlNRvP0NdQZpa7yIqf_Lv_QuBwTQ8tXkX7w-irAghVD_TvuYd1aoJ1LQph86O-XImC4X9j9FhUPhXQDvtrQ=="
    page_size: int = attr.ib(
        default=0, metadata={"req_type": "query"}
    )  # 分页大小, 示例值：10, 最大值：`50`


@attr.s
class GetMessageListRespItemMentionIDType(object):
    pass


@attr.s
class GetMessageListRespItemMention(object):
    key: str = attr.ib(default="", metadata={"req_type": "json"})  # mention key
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户open id
    id_type: GetMessageListRespItemMentionIDType = attr.ib(
        factory=lambda: GetMessageListRespItemMentionIDType(),
        metadata={"req_type": "json"},
    )  # id 可以是open_id，user_id或者union_id
    name: str = attr.ib(default="", metadata={"req_type": "json"})  # 被at用户的姓名


@attr.s
class GetMessageListRespItemBody(object):
    content: str = attr.ib(default="", metadata={"req_type": "json"})  # 消息jsonContent


@attr.s
class GetMessageListRespItemSenderIDType(object):
    pass


@attr.s
class GetMessageListRespItemSender(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # 该字段标识发送者的id
    id_type: GetMessageListRespItemSenderIDType = attr.ib(
        factory=lambda: GetMessageListRespItemSenderIDType(),
        metadata={"req_type": "json"},
    )  # 该字段标识发送者的id类型
    sender_type: str = attr.ib(default="", metadata={"req_type": "json"})  # 该字段标识发送者的类型


@attr.s
class GetMessageListRespItemMsgType(object):
    pass


@attr.s
class GetMessageListRespItem(object):
    message_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 消息id open_message_id
    root_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 根消息id open_message_id
    parent_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 父消息的id open_message_id
    msg_type: GetMessageListRespItemMsgType = attr.ib(
        factory=lambda: GetMessageListRespItemMsgType(), metadata={"req_type": "json"}
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
    sender: GetMessageListRespItemSender = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 发送者，可以是用户或应用
    body: GetMessageListRespItemBody = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 消息内容，json结构，格式说明参考： [消息content说明](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/im-v1/message/events/message_content)
    mentions: typing.List[GetMessageListRespItemMention] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 被艾特的人或应用的id
    upper_message_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 上一层级的消息id open_message_id


@attr.s
class GetMessageListResp(object):
    has_more: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 是否还有更多项
    page_token: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token
    items: typing.List[GetMessageListRespItem] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # message[]


def _gen_get_message_list_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetMessageListResp,
        scope="Message",
        api="GetMessageList",
        method="GET",
        url="https://open.feishu.cn/open-apis/im/v1/messages",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
