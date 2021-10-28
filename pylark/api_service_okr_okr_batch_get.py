# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
from pylark import lark_type_enum, lark_type_sheet
import attr
import typing
import io


@attr.s
class BatchGetOKRReqUserIDType(object):
    pass


@attr.s
class BatchGetOKRReq(object):
    user_id_type: lark_type_enum.IDType = attr.ib(
        default=None, metadata={"req_type": "query", "key": "user_id_type"}
    )  # 用户 ID 类型, 示例值："open_id", 可选值有: `open_id`：用户的 open id, `union_id`：用户的 union id, `user_id`：用户的 user id, 默认值: `open_id`, 当值为 `user_id`, 字段权限要求: 获取用户 user ID
    okr_ids: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "query", "key": "okr_ids"}
    )  # OKR ID 列表，最多10个
    lang: str = attr.ib(
        default="", metadata={"req_type": "query", "key": "lang"}
    )  # 请求OKR的语言版本（比如@的人名），lang=en_us/zh_cn，请求 Query中, 示例值："zh_cn", 默认值: `zh_cn`


@attr.s
class BatchGetOKRRespOKRObjectiveAligningObjectiveOwner(object):
    open_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "open_id"}
    )  # 用户的 open_id


@attr.s
class BatchGetOKRRespOKRObjectiveAligningObjective(object):
    id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "id"}
    )  # Objective的ID
    okr_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "okr_id"}
    )  # OKR的ID
    owner: BatchGetOKRRespOKRObjectiveAligningObjectiveOwner = attr.ib(
        default=None, metadata={"req_type": "json", "key": "owner"}
    )  # 该Objective的Owner


@attr.s
class BatchGetOKRRespOKRObjectiveAlignedObjectiveOwner(object):
    open_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "open_id"}
    )  # 用户的 open_id


@attr.s
class BatchGetOKRRespOKRObjectiveAlignedObjective(object):
    id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "id"}
    )  # Objective的ID
    okr_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "okr_id"}
    )  # OKR的ID
    owner: BatchGetOKRRespOKRObjectiveAlignedObjectiveOwner = attr.ib(
        default=None, metadata={"req_type": "json", "key": "owner"}
    )  # 该Objective的Owner


@attr.s
class BatchGetOKRRespOKRObjectiveKrProgressRate(object):
    percent: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "percent"}
    )  # Objective 进度百分比 >= 0
    status: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "status"}
    )  # Objective 进度状态, 可选值有: `-1`：未更新, `0`：正常, `1`：有风险, `2`：已延期


@attr.s
class BatchGetOKRRespOKRObjectiveKrKrWeight(object):
    pass


@attr.s
class BatchGetOKRRespOKRObjectiveKr(object):
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
    progress_rate: BatchGetOKRRespOKRObjectiveKrProgressRate = attr.ib(
        default=None, metadata={"req_type": "json", "key": "progress_rate"}
    )  # KR进度


@attr.s
class BatchGetOKRRespOKRObjectiveProgressRate(object):
    percent: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "percent"}
    )  # Objective 进度百分比 >= 0
    status: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "status"}
    )  # Objective 进度状态, 可选值有: `-1`：未更新, `0`：正常, `1`：有风险, `2`：已延期


@attr.s
class BatchGetOKRRespOKRObjectiveWeight(object):
    pass


@attr.s
class BatchGetOKRRespOKRObjective(object):
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
    progress_rate: BatchGetOKRRespOKRObjectiveProgressRate = attr.ib(
        default=None, metadata={"req_type": "json", "key": "progress_rate"}
    )  # Objective进度
    kr_list: typing.List[BatchGetOKRRespOKRObjectiveKr] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "kr_list"}
    )  # Objective KeyResult 列表
    aligned_objective_list: typing.List[
        BatchGetOKRRespOKRObjectiveAlignedObjective
    ] = attr.ib(
        factory=lambda: [],
        metadata={"req_type": "json", "key": "aligned_objective_list"},
    )  # 对齐到该Objective的Objective列表
    aligning_objective_list: typing.List[
        BatchGetOKRRespOKRObjectiveAligningObjective
    ] = attr.ib(
        factory=lambda: [],
        metadata={"req_type": "json", "key": "aligning_objective_list"},
    )  # 该Objective对齐到的Objective列表


@attr.s
class BatchGetOKRRespOKR(object):
    id: str = attr.ib(default="", metadata={"req_type": "json", "key": "id"})  # id
    permission: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "permission"}
    )  # OKR的访问权限, 可选值有: `0`：此时OKR只返回id, `1`：返回OKR的其他具体字段
    name: str = attr.ib(default="", metadata={"req_type": "json", "key": "name"})  # 名称
    objective_list: typing.List[BatchGetOKRRespOKRObjective] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "objective_list"}
    )  # Objective列表


@attr.s
class BatchGetOKRResp(object):
    okr_list: typing.List[BatchGetOKRRespOKR] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "okr_list"}
    )  # OKR 列表


def _gen_batch_get_okr_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=BatchGetOKRResp,
        scope="OKR",
        api="BatchGetOKR",
        method="GET",
        url="https://open.feishu.cn/open-apis/okr/v1/okrs/batch_get",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        need_user_access_token=True,
    )
