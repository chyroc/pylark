# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing


@attr.s
class GetUserOKRListReqUserIDType(object):
    pass


@attr.s
class GetUserOKRListReq(object):
    user_id_type: IDType = attr.ib(
        default=None, metadata={"req_type": "query"}
    )  # 用户 ID 类型, 示例值："open_id", 可选值有: `open_id`：用户的 open id, `union_id`：用户的 union id, `user_id`：用户的 user id, 默认值: `open_id`, 当值为 `user_id`, 字段权限要求: 获取用户 userid
    offset: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # 请求列表的偏移，offset>=0，请求Query中, 示例值："0"
    limit: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # 请求列表的长度，0<limit<=10，请求Query中, 示例值："0"
    lang: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # 请求OKR的语言版本（比如@的人名），lang=en_us/zh_cn，请求 Query中, 示例值："zh_cn", 默认值: `zh_cn`
    user_id: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 目标用户id, 示例值："ou-asdasdasdasdasd"


@attr.s
class GetUserOKRListRespOKRObjectiveAligningObjectiveOwner(object):
    open_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户的 open_id


@attr.s
class GetUserOKRListRespOKRObjectiveAligningObjective(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # Objective的ID
    okr_id: str = attr.ib(default="", metadata={"req_type": "json"})  # OKR的ID
    owner: GetUserOKRListRespOKRObjectiveAligningObjectiveOwner = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 该Objective的Owner


@attr.s
class GetUserOKRListRespOKRObjectiveAlignedObjectiveOwner(object):
    open_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户的 open_id


@attr.s
class GetUserOKRListRespOKRObjectiveAlignedObjective(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # Objective的ID
    okr_id: str = attr.ib(default="", metadata={"req_type": "json"})  # OKR的ID
    owner: GetUserOKRListRespOKRObjectiveAlignedObjectiveOwner = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 该Objective的Owner


@attr.s
class GetUserOKRListRespOKRObjectiveKrProgressRate(object):
    percent: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # Objective 进度百分比 >= 0
    status: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # Objective 进度状态, 可选值有: `-1`：未更新, `0`：正常, `1`：有风险, `2`：已延期


@attr.s
class GetUserOKRListRespOKRObjectiveKrKrWeight(object):
    pass


@attr.s
class GetUserOKRListRespOKRObjectiveKr(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # Key Result ID
    content: str = attr.ib(default="", metadata={"req_type": "json"})  # KeyResult 内容
    score: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # KeyResult打分（0 - 100）
    weight: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # KeyResult权重（0 - 100）（废弃）
    kr_weight: float = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # KeyResult的权重（0 - 100）
    progress_rate: GetUserOKRListRespOKRObjectiveKrProgressRate = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # KR进度


@attr.s
class GetUserOKRListRespOKRObjectiveProgressRate(object):
    percent: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # Objective 进度百分比 >= 0
    status: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # Objective 进度状态, 可选值有: `-1`：未更新, `0`：正常, `1`：有风险, `2`：已延期


@attr.s
class GetUserOKRListRespOKRObjectiveWeight(object):
    pass


@attr.s
class GetUserOKRListRespOKRObjective(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # Objective ID
    permission: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 权限, 可选值有: `0`：此时OKR只返回id, `1`：返回OKR的其他具体字段
    content: str = attr.ib(default="", metadata={"req_type": "json"})  # Objective 内容
    progress_report: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # Objective 进度记录内容
    score: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # Objective 分数（0 - 100）
    weight: float = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # Objective的权重（0 - 100）
    progress_rate: GetUserOKRListRespOKRObjectiveProgressRate = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # Objective进度
    kr_list: typing.List[GetUserOKRListRespOKRObjectiveKr] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # Objective KeyResult 列表
    aligned_objective_list: typing.List[
        GetUserOKRListRespOKRObjectiveAlignedObjective
    ] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 对齐到该Objective的Objective列表
    aligning_objective_list: typing.List[
        GetUserOKRListRespOKRObjectiveAligningObjective
    ] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 该Objective对齐到的Objective列表


@attr.s
class GetUserOKRListRespOKR(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # id
    permission: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # OKR的访问权限, 可选值有: `0`：此时OKR只返回id, `1`：返回OKR的其他具体字段
    name: str = attr.ib(default="", metadata={"req_type": "json"})  # 名称
    objective_list: typing.List[GetUserOKRListRespOKRObjective] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # Objective列表


@attr.s
class GetUserOKRListResp(object):
    total: int = attr.ib(default=0, metadata={"req_type": "json"})  # OKR周期总数
    okr_list: typing.List[GetUserOKRListRespOKR] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
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
    )
