# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class SearchCalendarReq(object):
    page_token: str = attr.ib(
        default="", metadata={"req_type": "query", "key": "page_token"}
    )  # 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果, 示例值："xxxxx"
    page_size: int = attr.ib(
        default=0, metadata={"req_type": "query", "key": "page_size"}
    )  # 分页大小, 示例值：10, 最大值：`50`
    query: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "query"}
    )  # 搜索关键字, 示例值："query words", 长度范围：`1` ～ `200` 字符


@attr.s
class SearchCalendarRespItemRole(object):
    pass


@attr.s
class SearchCalendarRespItemType(object):
    pass


@attr.s
class SearchCalendarRespItemPermissions(object):
    pass


@attr.s
class SearchCalendarRespItem(object):
    calendar_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "calendar_id"}
    )  # 日历ID
    summary: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "summary"}
    )  # 日历标题, 最大长度：`255` 字符
    description: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "description"}
    )  # 日历描述, 最大长度：`255` 字符
    permissions: SearchCalendarRespItemPermissions = attr.ib(
        factory=lambda: SearchCalendarRespItemPermissions(),
        metadata={"req_type": "json", "key": "permissions"},
    )  # 日历公开范围, 可选值有: `private`：私密, `show_only_free_busy`：仅展示忙闲信息, `public`：他人可查看日程详情
    color: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "color"}
    )  # 日历颜色，颜色RGB值的int32表示。客户端展示时会映射到色板上最接近的一种颜色。仅对当前身份生效
    type: SearchCalendarRespItemType = attr.ib(
        factory=lambda: SearchCalendarRespItemType(),
        metadata={"req_type": "json", "key": "type"},
    )  # 日历类型, 可选值有: `unknown`：未知类型, `primary`：用户或应用的主日历, `shared`：由用户或应用创建的共享日历, `google`：用户绑定的谷歌日历, `resource`：会议室日历, `exchange`：用户绑定的Exchange日历
    summary_alias: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "summary_alias"}
    )  # 日历备注名，修改或添加后仅对当前身份生效, 最大长度：`255` 字符
    is_deleted: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json", "key": "is_deleted"}
    )  # 对于当前身份，日历是否已经被标记为删除, 默认值: `false`
    is_third_party: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json", "key": "is_third_party"}
    )  # 当前日历是否是第三方数据；三方日历及日程只支持读，不支持写入, 默认值: `false`
    role: SearchCalendarRespItemRole = attr.ib(
        factory=lambda: SearchCalendarRespItemRole(),
        metadata={"req_type": "json", "key": "role"},
    )  # 当前身份对于该日历的访问权限, 可选值有: `unknown`：未知权限, `free_busy_reader`：游客，只能看到忙碌/空闲信息, `reader`：订阅者，查看所有日程详情, `writer`：编辑者，创建及修改日程, `owner`：管理员，管理日历及共享设置


@attr.s
class SearchCalendarResp(object):
    items: typing.List[SearchCalendarRespItem] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "items"}
    )  # 搜索命中的日历列表
    page_token: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "page_token"}
    )  # 分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token


def _gen_search_calendar_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=SearchCalendarResp,
        scope="Calendar",
        api="SearchCalendar",
        method="POST",
        url="https://open.feishu.cn/open-apis/calendar/v4/calendars/search",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
