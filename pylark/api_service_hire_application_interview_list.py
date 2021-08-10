# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class GetHireApplicationInterviewListReqUserIDType(object):
    pass


@attr.s
class GetHireApplicationInterviewListReq(object):
    page_size: int = attr.ib(default=0, metadata={"req_type": "query"})  # 分页大小, 示例值：10
    page_token: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果, 示例值："xx"
    user_id_type: GetHireApplicationInterviewListReqUserIDType = attr.ib(
        default=None, metadata={"req_type": "query"}
    )  # 用户 ID 类型, 示例值："open_id", 可选值有: `open_id`：用户的 open id, `union_id`：用户的 union id, `user_id`：用户的 user id, 默认值: `open_id`, 当值为 `user_id`, 字段权限要求: 获取用户 userid
    application_id: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 投递ID, 示例值："6949805467799537964"


@attr.s
class GetHireApplicationInterviewListRespItemInterviewRecordInterviewScore(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # 面试评分id
    level: int = attr.ib(default=0, metadata={"req_type": "json"})  # 分数级别
    zh_name: str = attr.ib(default="", metadata={"req_type": "json"})  # 中文名称
    zh_description: str = attr.ib(default="", metadata={"req_type": "json"})  # 中文描述
    en_name: str = attr.ib(default="", metadata={"req_type": "json"})  # 英文名称
    en_description: str = attr.ib(default="", metadata={"req_type": "json"})  # 英文描述


@attr.s
class GetHireApplicationInterviewListRespItemInterviewRecord(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # 面试记录id
    user_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 面试官用户id
    content: str = attr.ib(default="", metadata={"req_type": "json"})  # 面试评价
    min_job_level_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 建议定级下限的职级id
    max_job_level_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 建议定级上限的职级id
    commit_status: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 提交状态, 可选值有: `1`：已提交, `2`：未提交
    conclusion: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 面试结论, 可选值有: `1`：通过, `2`：未通过, `3`：未开始, `4`：未提交, `5`：未到场
    interview_score: GetHireApplicationInterviewListRespItemInterviewRecordInterviewScore = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 面试评分


@attr.s
class GetHireApplicationInterviewListRespItem(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # 面试id
    begin_time: int = attr.ib(default=0, metadata={"req_type": "json"})  # 面试开始时间（ms）
    end_time: int = attr.ib(default=0, metadata={"req_type": "json"})  # 面试结束时间（ms）
    round: int = attr.ib(default=0, metadata={"req_type": "json"})  # 面试轮次（从0开始计数）
    stage_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 面试关联的投递阶段
    interview_record_list: typing.List[
        GetHireApplicationInterviewListRespItemInterviewRecord
    ] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 面试官记录列表


@attr.s
class GetHireApplicationInterviewListResp(object):
    page_token: str = attr.ib(default="", metadata={"req_type": "json"})  # 分页标志
    has_more: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 是否有更多
    items: typing.List[GetHireApplicationInterviewListRespItem] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 面试列表


def _gen_get_hire_application_interview_list_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetHireApplicationInterviewListResp,
        scope="Hire",
        api="GetHireApplicationInterviewList",
        method="GET",
        url="https://open.feishu.cn/open-apis/hire/v1/applications/:application_id/interviews",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
