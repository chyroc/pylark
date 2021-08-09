# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing


@attr.s
class GetDriveCommentListReqUserIDType(object):
    pass


@attr.s
class GetDriveCommentListReqFileType(object):
    pass


@attr.s
class GetDriveCommentListReq(object):
    file_type: GetDriveCommentListReqFileType = attr.ib(
        factory=lambda: GetDriveCommentListReqFileType(), metadata={"req_type": "query"}
    )  # 文档类型, 示例值："doc", 可选值有: `doc`：文档, `sheet`：表格, `file`：文件
    user_id_type: IDType = attr.ib(
        default=None, metadata={"req_type": "query"}
    )  # 用户 ID 类型, 示例值："open_id", 可选值有: `open_id`：用户的 open id, `union_id`：用户的 union id, `user_id`：用户的 user id, 默认值: `open_id`, 当值为 `user_id`, 字段权限要求: 获取用户 userid
    is_solved: bool = attr.ib(
        default=None, metadata={"req_type": "query"}
    )  # 是否已解决（可选）, 示例值：false
    page_token: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果, 示例值："6916106822734578184"
    page_size: int = attr.ib(
        default=0, metadata={"req_type": "query"}
    )  # 分页大小, 示例值：10, 最大值：`100`
    file_token: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 文档token, 示例值："doccnHh7U87HOFpii5u5G*****"


@attr.s
class GetDriveCommentListRespItemReplyListReplyContentElementPerson(object):
    user_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 回复 at联系人


@attr.s
class GetDriveCommentListRespItemReplyListReplyContentElementDocsLink(object):
    url: str = attr.ib(default="", metadata={"req_type": "json"})  # 回复 at云文档


@attr.s
class GetDriveCommentListRespItemReplyListReplyContentElementTextRun(object):
    text: str = attr.ib(default="", metadata={"req_type": "json"})  # 回复 普通文本


@attr.s
class GetDriveCommentListRespItemReplyListReplyContentElement(object):
    type: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 回复的内容元素, 可选值有: `text_run`：普通文本, `docs_link`：at 云文档链接, `person`：at 联系人
    text_run: GetDriveCommentListRespItemReplyListReplyContentElementTextRun = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 文本内容
    docs_link: GetDriveCommentListRespItemReplyListReplyContentElementDocsLink = (
        attr.ib(default=None, metadata={"req_type": "json"})
    )  # 文本内容
    person: GetDriveCommentListRespItemReplyListReplyContentElementPerson = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 文本内容


@attr.s
class GetDriveCommentListRespItemReplyListReplyContent(object):
    elements: typing.List[
        GetDriveCommentListRespItemReplyListReplyContentElement
    ] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 回复的内容


@attr.s
class GetDriveCommentListRespItemReplyListReply(object):
    reply_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 回复ID
    user_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户ID
    create_time: int = attr.ib(default=0, metadata={"req_type": "json"})  # 创建时间
    update_time: int = attr.ib(default=0, metadata={"req_type": "json"})  # 更新时间
    content: GetDriveCommentListRespItemReplyListReplyContent = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 回复内容


@attr.s
class GetDriveCommentListRespItemReplyList(object):
    replies: typing.List[GetDriveCommentListRespItemReplyListReply] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 回复列表


@attr.s
class GetDriveCommentListRespItem(object):
    comment_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 评论ID
    user_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户ID
    create_time: int = attr.ib(default=0, metadata={"req_type": "json"})  # 创建时间
    update_time: int = attr.ib(default=0, metadata={"req_type": "json"})  # 更新时间
    is_solved: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 是否已解决
    solved_time: int = attr.ib(default=0, metadata={"req_type": "json"})  # 解决评论时间
    solver_user_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 解决评论者的用户ID
    reply_list: GetDriveCommentListRespItemReplyList = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 评论里的回复列表


@attr.s
class GetDriveCommentListResp(object):
    has_more: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 是否还有更多项
    page_token: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token
    items: typing.List[GetDriveCommentListRespItem] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 评论列表


def _gen_get_drive_comment_list_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetDriveCommentListResp,
        scope="Drive",
        api="GetDriveCommentList",
        method="GET",
        url="https://open.feishu.cn/open-apis/drive/v1/files/:file_token/comments",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )