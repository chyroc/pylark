# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class CreateDriveCommentReqReplyListReplyContentElementPerson(object):
    user_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 回复 at联系人, 示例值："ou_cc19b2bfb93f8a44db4b4d6eab*****"


@attr.s
class CreateDriveCommentReqReplyListReplyContentElementDocsLink(object):
    url: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 回复 at云文档, 示例值："https://bytedance.feishu.cn/docs/doccnHh7U87HOFpii5u5G*****"


@attr.s
class CreateDriveCommentReqReplyListReplyContentElementTextRun(object):
    text: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 回复 普通文本, 示例值："comment text"


@attr.s
class CreateDriveCommentReqReplyListReplyContentElement(object):
    type: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 回复的内容元素, 示例值："text_run", 可选值有: `text_run`：普通文本, `docs_link`：at 云文档链接, `person`：at 联系人
    text_run: CreateDriveCommentReqReplyListReplyContentElementTextRun = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 文本内容
    docs_link: CreateDriveCommentReqReplyListReplyContentElementDocsLink = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 文本内容
    person: CreateDriveCommentReqReplyListReplyContentElementPerson = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 文本内容


@attr.s
class CreateDriveCommentReqReplyListReplyContent(object):
    elements: typing.List[CreateDriveCommentReqReplyListReplyContentElement] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 回复的内容


@attr.s
class CreateDriveCommentReqReplyListReply(object):
    reply_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 回复ID, 示例值："6916106822734594568"
    user_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 用户ID, 示例值："ou_cc19b2bfb93f8a44db4b4d6eab2*****"
    create_time: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 创建时间, 示例值：1610281603
    update_time: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 更新时间, 示例值：1610281603
    content: CreateDriveCommentReqReplyListReplyContent = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 回复内容


@attr.s
class CreateDriveCommentReqReplyList(object):
    replies: typing.List[CreateDriveCommentReqReplyListReply] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 回复列表


@attr.s
class CreateDriveCommentReqUserIDType(object):
    pass


@attr.s
class CreateDriveCommentReqFileType(object):
    pass


@attr.s
class CreateDriveCommentReq(object):
    file_type: CreateDriveCommentReqFileType = attr.ib(
        factory=lambda: CreateDriveCommentReqFileType(), metadata={"req_type": "query"}
    )  # 文档类型, 示例值："doc", 可选值有: `doc`：文档, `sheet`：表格, `file`：文件
    user_id_type: CreateDriveCommentReqUserIDType = attr.ib(
        default=None, metadata={"req_type": "query"}
    )  # 用户 ID 类型, 示例值："open_id", 可选值有: `open_id`：用户的 open id, `union_id`：用户的 union id, `user_id`：用户的 user id, 默认值: `open_id`, 当值为 `user_id`, 字段权限要求: 获取用户 userid
    file_token: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 文档token, 示例值："doccnGp4UK1UskrOEJwBXd3****"
    comment_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 评论ID, 示例值："6916106822734578184"
    user_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 用户ID, 示例值："ou_cc19b2bfb93f8a44db4b4d6eab*****"
    create_time: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 创建时间, 示例值：1610281603
    update_time: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 更新时间, 示例值：1610281603
    is_solved: bool = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 是否已解决, 示例值：false
    solved_time: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 解决评论时间, 示例值：1610281603
    solver_user_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 解决评论者的用户ID, 示例值："null"
    reply_list: CreateDriveCommentReqReplyList = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 评论里的回复列表


@attr.s
class CreateDriveCommentRespReplyListReplyContentElementPerson(object):
    user_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 回复 at联系人


@attr.s
class CreateDriveCommentRespReplyListReplyContentElementDocsLink(object):
    url: str = attr.ib(default="", metadata={"req_type": "json"})  # 回复 at云文档


@attr.s
class CreateDriveCommentRespReplyListReplyContentElementTextRun(object):
    text: str = attr.ib(default="", metadata={"req_type": "json"})  # 回复 普通文本


@attr.s
class CreateDriveCommentRespReplyListReplyContentElement(object):
    type: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 回复的内容元素, 可选值有: `text_run`：普通文本, `docs_link`：at 云文档链接, `person`：at 联系人
    text_run: CreateDriveCommentRespReplyListReplyContentElementTextRun = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 文本内容
    docs_link: CreateDriveCommentRespReplyListReplyContentElementDocsLink = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 文本内容
    person: CreateDriveCommentRespReplyListReplyContentElementPerson = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 文本内容


@attr.s
class CreateDriveCommentRespReplyListReplyContent(object):
    elements: typing.List[CreateDriveCommentRespReplyListReplyContentElement] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 回复的内容


@attr.s
class CreateDriveCommentRespReplyListReply(object):
    reply_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 回复ID
    user_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户ID
    create_time: int = attr.ib(default=0, metadata={"req_type": "json"})  # 创建时间
    update_time: int = attr.ib(default=0, metadata={"req_type": "json"})  # 更新时间
    content: CreateDriveCommentRespReplyListReplyContent = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 回复内容


@attr.s
class CreateDriveCommentRespReplyList(object):
    replies: typing.List[CreateDriveCommentRespReplyListReply] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 回复列表


@attr.s
class CreateDriveCommentResp(object):
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
    reply_list: CreateDriveCommentRespReplyList = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 评论里的回复列表


def _gen_create_drive_comment_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=CreateDriveCommentResp,
        scope="Drive",
        api="CreateDriveComment",
        method="POST",
        url="https://open.feishu.cn/open-apis/drive/v1/files/:file_token/comments",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        need_user_access_token=True,
    )
