# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class SearchUserOldReq(object):
    query: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # 要执行搜索的字符串，一般为用户名。
    page_size: int = attr.ib(
        default=0, metadata={"req_type": "query"}
    )  # 分页大小，最小为 1，最大为 200，默认为 20。
    page_token: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # 分页标识，获取首页不需要填写，获取下一页时传入上一页返回的分页标识值。<br>请注意此字段的值并没有特殊含义，请使用每次请求所返回的标识值。


@attr.s
class SearchUserOldRespUserAvatar(object):
    avatar_72: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 用户的头像图片 URL，72×72px。
    avatar_240: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 用户的头像图片 URL，240×240px。
    avatar_640: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 用户的头像图片 URL，640×640px。
    avatar_origin: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 用户的头像图片 URL，原始大小。


@attr.s
class SearchUserOldRespUser(object):
    avatar: SearchUserOldRespUserAvatar = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 用户的头像信息。
    department_ids: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 用户所在的部门 ID。
    name: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户名。
    open_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户的 open_id。
    user_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 用户的 user_id，只有已申请 `获取用户UserID` 权限的企业自建应用返回此字段。


@attr.s
class SearchUserOldResp(object):
    has_more: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 是否还有更多用户，值为 true 表示存在下一页。
    page_token: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 分页标识，存在下一页的时候返回。下次请求带上此标识可以获取下一页的用户。
    users: typing.List[SearchUserOldRespUser] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 搜索到的用户列表。


def _gen_search_user_old_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=SearchUserOldResp,
        scope="Contact",
        api="SearchUserOld",
        method="GET",
        url="https://open.feishu.cn/open-apis/search/v1/user",
        body=request,
        method_option=_new_method_option(options),
        need_user_access_token=True,
    )