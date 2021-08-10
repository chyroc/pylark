# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class GetHireApplicationReq(object):
    application_id: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 投递ID, 示例值："212121"


@attr.s
class GetHireApplicationRespApplicationStage(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # 阶段id
    zh_name: str = attr.ib(default="", metadata={"req_type": "json"})  # 阶段中文名字
    en_name: str = attr.ib(default="", metadata={"req_type": "json"})  # 英文名
    type: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 阶段类型, 可选值有: `1`：筛选型, `2`：评估型, `3`：笔试型, `4`：面试型, `5`：Offer型, `6`：待入职, `7`：已入职, `8`：其它类型, `255`：系统默认


@attr.s
class GetHireApplicationRespApplication(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # 投递id
    job_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 投递的职位id
    talent_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 候选人id
    resume_resource_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 简历来源id
    stage: GetHireApplicationRespApplicationStage = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 投递处于的阶段
    active_status: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 活跃状态, 可选值有: `1`：活跃, `2`：非活跃, `3`：全部


@attr.s
class GetHireApplicationResp(object):
    application: GetHireApplicationRespApplication = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 投递数据


def _gen_get_hire_application_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetHireApplicationResp,
        scope="Hire",
        api="GetHireApplication",
        method="GET",
        url="https://open.feishu.cn/open-apis/hire/v1/applications/:application_id",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
