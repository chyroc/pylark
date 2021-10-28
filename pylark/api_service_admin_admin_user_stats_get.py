# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class GetAdminUserStatsReqDepartmentIDType(object):
    pass


@attr.s
class GetAdminUserStatsReqUserIDType(object):
    pass


@attr.s
class GetAdminUserStatsReq(object):
    user_id_type: GetAdminUserStatsReqUserIDType = attr.ib(
        default=None, metadata={"req_type": "query", "key": "user_id_type"}
    )  # 用户 ID 类型, 示例值："open_id", 可选值有: `open_id`：用户的 open id, `union_id`：用户的 union id, `user_id`：用户的 user id, 默认值: `open_id`, 当值为 `user_id`, 字段权限要求: 获取用户 user ID
    department_id_type: GetAdminUserStatsReqDepartmentIDType = attr.ib(
        default=None, metadata={"req_type": "query", "key": "department_id_type"}
    )  # 部门ID类型, 示例值："open_department_id", 可选值有: `department_id`：部门的 ID, `open_department_id`：部门的 Open ID
    start_date: str = attr.ib(
        default="", metadata={"req_type": "query", "key": "start_date"}
    )  # 起始日期（包含），格式是YYYY-mm-dd, 示例值："2020-02-15"
    end_date: str = attr.ib(
        default="", metadata={"req_type": "query", "key": "end_date"}
    )  # 终止日期（包含），格式是YYYY-mm-dd。起止日期之间相差不能超过31天（包含31天）, 示例值："2020-02-15"
    department_id: str = attr.ib(
        default="", metadata={"req_type": "query", "key": "department_id"}
    )  # 部门的 ID，取决于department_id_type, 示例值："od-382e2793cfc9471f892e8a672987654c"
    user_id: str = attr.ib(
        default="", metadata={"req_type": "query", "key": "user_id"}
    )  # 用户的open_id，user_id或者union_id，取决于user_id_type, 示例值："ou_7dab8a3d3cdcc9da365777c7ad535d62"
    page_size: int = attr.ib(
        default=0, metadata={"req_type": "query", "key": "page_size"}
    )  # 分页大小，默认是10, 示例值：10, 取值范围：`1` ～ `20`
    page_token: str = attr.ib(
        default="", metadata={"req_type": "query", "key": "page_token"}
    )  # 分页标记，第一次请求不填，表示从头开始遍历；当返回的has_more为true时，会返回新的page_token，再次调用接口，传入这个page_token，将获得下一页数据, 示例值："2"


@attr.s
class GetAdminUserStatsRespItem(object):
    date: str = attr.ib(default="", metadata={"req_type": "json", "key": "date"})  # 日期
    user_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "user_id"}
    )  # 用户ID
    user_name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "user_name"}
    )  # 用户名
    department_name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "department_name"}
    )  # 部门名
    department_path: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "department_path"}
    )  # 部门路径
    create_time: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "create_time"}
    )  # 添加时间
    user_active_flag: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "user_active_flag"}
    )  # 用户激活状态, 可选值有: `0`：未激活, `1`：已激活
    register_time: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "register_time"}
    )  # 激活时间
    suite_active_flag: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "suite_active_flag"}
    )  # 用户活跃状态, 可选值有: `0`：无活跃, `1`：活跃
    last_active_time: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "last_active_time"}
    )  # 最近活跃时间
    im_active_flag: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "im_active_flag"}
    )  # 用户消息活跃状态, 可选值有: `0`：无活跃, `1`：活跃
    send_messenger_num: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "send_messenger_num"}
    )  # 发送消息数
    docs_active_flag: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "docs_active_flag"}
    )  # 用户云文档活跃状态, 可选值有: `0`：无活跃, `1`：活跃
    create_docs_num: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "create_docs_num"}
    )  # 创建文件数
    cal_active_flag: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "cal_active_flag"}
    )  # 用户日历活跃状态, 可选值有: `0`：无活跃, `1`：活跃
    create_cal_num: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "create_cal_num"}
    )  # 创建日程数
    vc_active_flag: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "vc_active_flag"}
    )  # 用户音视频会议活跃状态, 可选值有: `0`：无活跃, `1`：活跃
    vc_duration: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "vc_duration"}
    )  # 会议时长
    active_os: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "active_os"}
    )  # 活跃设备


@attr.s
class GetAdminUserStatsResp(object):
    has_more: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json", "key": "has_more"}
    )  # 是否有下一页数据
    page_token: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "page_token"}
    )  # 下一页分页的token
    items: typing.List[GetAdminUserStatsRespItem] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "items"}
    )  # 数据报表


def _gen_get_admin_user_stats_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetAdminUserStatsResp,
        scope="Admin",
        api="GetAdminUserStats",
        method="GET",
        url="https://open.feishu.cn/open-apis/admin/v1/admin_user_stats",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
