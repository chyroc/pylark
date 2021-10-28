# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class GetUserOKRListReqUserIDType(object):
    pass


@attr.s
class GetUserOKRListReq(object):
    user_id_type: GetUserOKRListReqUserIDType = attr.ib(
        default=None, metadata={"req_type": "query", "key": "user_id_type"}
    )  # 用户 ID 类型, 示例值："open_id", 可选值有: `open_id`：用户的 open id, `union_id`：用户的 union id, `user_id`：用户的 user id, `people_admin_id`：以people_admin_id来识别用户, 默认值: `open_id`, 当值为 `user_id`, 字段权限要求:  获取用户 user ID
    offset: str = attr.ib(
        default="", metadata={"req_type": "query", "key": "offset"}
    )  # 请求列表的偏移，offset>=0，请求Query中, 示例值："0"
    limit: str = attr.ib(
        default="", metadata={"req_type": "query", "key": "limit"}
    )  # 请求列表的长度，0<limit<=10，请求Query中, 示例值："0"
    lang: str = attr.ib(
        default="", metadata={"req_type": "query", "key": "lang"}
    )  # 请求OKR的语言版本（比如@的人名），lang=en_us/zh_cn，请求 Query中, 示例值："zh_cn", 默认值: `zh_cn`
    period_ids: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "query", "key": "period_ids"}
    )  # period_id列表，最多10个, 示例值：["6951461264858777132"], 最大长度：`10`
    user_id: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "user_id"}
    )  # 目标用户id, 示例值："ou-asdasdasdasdasd"


@attr.s
class GetUserOKRListRespOKRObjectiveAligningObjectiveOwner(object):
    open_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "open_id"}
    )  # 用户的 open_id
    user_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "user_id"}
    )  # 用户的 user_id


@attr.s
class GetUserOKRListRespOKRObjectiveAligningObjective(object):
    id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "id"}
    )  # Objective的ID
    okr_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "okr_id"}
    )  # OKR的ID
    owner: GetUserOKRListRespOKRObjectiveAligningObjectiveOwner = attr.ib(
        default=None, metadata={"req_type": "json", "key": "owner"}
    )  # 该Objective的Owner


@attr.s
class GetUserOKRListRespOKRObjectiveAlignedObjectiveOwner(object):
    open_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "open_id"}
    )  # 用户的 open_id
    user_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "user_id"}
    )  # 用户的 user_id


@attr.s
class GetUserOKRListRespOKRObjectiveAlignedObjective(object):
    id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "id"}
    )  # Objective的ID
    okr_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "okr_id"}
    )  # OKR的ID
    owner: GetUserOKRListRespOKRObjectiveAlignedObjectiveOwner = attr.ib(
        default=None, metadata={"req_type": "json", "key": "owner"}
    )  # 该Objective的Owner


@attr.s
class GetUserOKRListRespOKRObjectiveKrProgressRate(object):
    percent: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "percent"}
    )  # Objective 进度百分比 >= 0
    status: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "status"}
    )  # Objective 进度状态, 可选值有: `-1`：未更新, `0`：正常, `1`：有风险, `2`：已延期


@attr.s
class GetUserOKRListRespOKRObjectiveKrKrWeight(object):
    pass


@attr.s
class GetUserOKRListRespOKRObjectiveKr(object):
    id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "id"}
    )  # Key Result ID
    content: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "content"}
    )  # KeyResult 内容
    score: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "score"}
    )  # KeyResult打分（0 - 100）
    weight: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "weight"}
    )  # KeyResult权重（0 - 100）（废弃）
    kr_weight: float = attr.ib(
        default=None, metadata={"req_type": "json", "key": "kr_weight"}
    )  # KeyResult的权重（0 - 100）
    progress_rate: GetUserOKRListRespOKRObjectiveKrProgressRate = attr.ib(
        default=None, metadata={"req_type": "json", "key": "progress_rate"}
    )  # KR进度


@attr.s
class GetUserOKRListRespOKRObjectiveProgressRate(object):
    percent: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "percent"}
    )  # Objective 进度百分比 >= 0
    status: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "status"}
    )  # Objective 进度状态, 可选值有: `-1`：未更新, `0`：正常, `1`：有风险, `2`：已延期


@attr.s
class GetUserOKRListRespOKRObjectiveWeight(object):
    pass


@attr.s
class GetUserOKRListRespOKRObjective(object):
    id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "id"}
    )  # Objective ID
    permission: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "permission"}
    )  # 权限, 可选值有: `0`：此时OKR只返回id, `1`：返回OKR的其他具体字段
    content: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "content"}
    )  # Objective 内容
    progress_report: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "progress_report"}
    )  # Objective 进度记录内容
    score: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "score"}
    )  # Objective 分数（0 - 100）
    weight: float = attr.ib(
        default=None, metadata={"req_type": "json", "key": "weight"}
    )  # Objective的权重（0 - 100）
    progress_rate: GetUserOKRListRespOKRObjectiveProgressRate = attr.ib(
        default=None, metadata={"req_type": "json", "key": "progress_rate"}
    )  # Objective进度
    kr_list: typing.List[GetUserOKRListRespOKRObjectiveKr] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "kr_list"}
    )  # Objective KeyResult 列表
    aligned_objective_list: typing.List[
        GetUserOKRListRespOKRObjectiveAlignedObjective
    ] = attr.ib(
        factory=lambda: [],
        metadata={"req_type": "json", "key": "aligned_objective_list"},
    )  # 对齐到该Objective的Objective列表
    aligning_objective_list: typing.List[
        GetUserOKRListRespOKRObjectiveAligningObjective
    ] = attr.ib(
        factory=lambda: [],
        metadata={"req_type": "json", "key": "aligning_objective_list"},
    )  # 该Objective对齐到的Objective列表


@attr.s
class GetUserOKRListRespOKR(object):
    id: str = attr.ib(default="", metadata={"req_type": "json", "key": "id"})  # id
    permission: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "permission"}
    )  # OKR的访问权限, 可选值有: `0`：此时OKR只返回id, `1`：返回OKR的其他具体字段
    period_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "period_id"}
    )  # period_id
    name: str = attr.ib(default="", metadata={"req_type": "json", "key": "name"})  # 名称
    objective_list: typing.List[GetUserOKRListRespOKRObjective] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "objective_list"}
    )  # Objective列表


@attr.s
class GetUserOKRListResp(object):
    total: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "total"}
    )  # OKR周期总数
    okr_list: typing.List[GetUserOKRListRespOKR] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "okr_list"}
    )  # OKR 列表


def _gen_get_user_okr_list_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetUserOKRListResp,
        scope="OKR",
        api="GetUserOKRList",
        method="GET",
        url="https://open.feishu.cn/open-apis/okr/v1/users/:user_id/okrs",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        need_user_access_token=True,
    )
