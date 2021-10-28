# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
from pylark import lark_type_enum, lark_type_sheet
import attr
import typing
import io


@attr.s
class GetHireOfferByApplicationReqUserIDType(object):
    pass


@attr.s
class GetHireOfferByApplicationReq(object):
    user_id_type: lark_type_enum.IDType = attr.ib(
        default=None, metadata={"req_type": "query", "key": "user_id_type"}
    )  # 用户 ID 类型, 示例值："open_id", 可选值有: `open_id`：用户的 open id, `union_id`：用户的 union id, `user_id`：用户的 user id, 默认值: `open_id`, 当值为 `user_id`, 字段权限要求: 获取用户 user ID
    application_id: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "application_id"}
    )  # 投递ID, 示例值："12312312312"


@attr.s
class GetHireOfferByApplicationRespOfferSalaryPlanCustomizeInfo(object):
    object_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "object_id"}
    )  # 自定义字段ID
    customize_value: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "customize_value"}
    )  # 自定义字段Value


@attr.s
class GetHireOfferByApplicationRespOfferSalaryPlan(object):
    currency: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "currency"}
    )  # 币种
    basic_salary: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "basic_salary"}
    )  # 基本薪资, 注意是json
    probation_salary_percentage: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "probation_salary_percentage"}
    )  # 试用期百分比
    award_salary_multiple: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "award_salary_multiple"}
    )  # 年终奖月数
    option_shares: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "option_shares"}
    )  # 期权股数
    quarterly_bonus: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "quarterly_bonus"}
    )  # 季度奖金额
    half_year_bonus: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "half_year_bonus"}
    )  # 半年奖金额
    total_annual_cash: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "total_annual_cash"}
    )  # 年度现金总额(数量，非公式)
    customize_info_list: typing.List[
        GetHireOfferByApplicationRespOfferSalaryPlanCustomizeInfo
    ] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "customize_info_list"}
    )  # 自定义字段的value信息


@attr.s
class GetHireOfferByApplicationRespOfferBasicInfoCustomizeInfo(object):
    object_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "object_id"}
    )  # 自定义字段ID
    customize_value: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "customize_value"}
    )  # 自定义字段Value


@attr.s
class GetHireOfferByApplicationRespOfferBasicInfoWorkAddressCountry(object):
    zh_name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "zh_name"}
    )  # 中文名称
    en_name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "en_name"}
    )  # 英文名称
    code: str = attr.ib(default="", metadata={"req_type": "json", "key": "code"})  # 编码
    location_type: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "location_type"}
    )  # 地址类型 1=COUNTRY, 2=STATE, 3=CITY, 4=DISTRICT, 5=ADDRESS,, 可选值有: `1`：COUNTRY, `2`：STATE, `3`：CITY, `4`：DISTRICT, `5`：ADDRESS


@attr.s
class GetHireOfferByApplicationRespOfferBasicInfoWorkAddressState(object):
    zh_name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "zh_name"}
    )  # 中文名称
    en_name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "en_name"}
    )  # 英文名称
    code: str = attr.ib(default="", metadata={"req_type": "json", "key": "code"})  # 编码
    location_type: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "location_type"}
    )  # 地址类型 1=COUNTRY, 2=STATE, 3=CITY, 4=DISTRICT, 5=ADDRESS,, 可选值有: `1`：COUNTRY, `2`：STATE, `3`：CITY, `4`：DISTRICT, `5`：ADDRESS


@attr.s
class GetHireOfferByApplicationRespOfferBasicInfoWorkAddressCity(object):
    zh_name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "zh_name"}
    )  # 中文名称
    en_name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "en_name"}
    )  # 英文名称
    code: str = attr.ib(default="", metadata={"req_type": "json", "key": "code"})  # 编码
    location_type: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "location_type"}
    )  # 地址类型 1=COUNTRY, 2=STATE, 3=CITY, 4=DISTRICT, 5=ADDRESS,, 可选值有: `1`：COUNTRY, `2`：STATE, `3`：CITY, `4`：DISTRICT, `5`：ADDRESS


@attr.s
class GetHireOfferByApplicationRespOfferBasicInfoWorkAddressDistrict(object):
    zh_name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "zh_name"}
    )  # 中文名称
    en_name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "en_name"}
    )  # 英文名称
    code: str = attr.ib(default="", metadata={"req_type": "json", "key": "code"})  # 编码
    location_type: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "location_type"}
    )  # 地址类型 1=COUNTRY, 2=STATE, 3=CITY, 4=DISTRICT, 5=ADDRESS,


@attr.s
class GetHireOfferByApplicationRespOfferBasicInfoWorkAddress(object):
    id: str = attr.ib(default="", metadata={"req_type": "json", "key": "id"})  # ID
    zh_name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "zh_name"}
    )  # 中文名称
    en_name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "en_name"}
    )  # 英文名称
    district: GetHireOfferByApplicationRespOfferBasicInfoWorkAddressDistrict = attr.ib(
        default=None, metadata={"req_type": "json", "key": "district"}
    )  # 区域信息
    city: GetHireOfferByApplicationRespOfferBasicInfoWorkAddressCity = attr.ib(
        default=None, metadata={"req_type": "json", "key": "city"}
    )  # 城市信息
    state: GetHireOfferByApplicationRespOfferBasicInfoWorkAddressState = attr.ib(
        default=None, metadata={"req_type": "json", "key": "state"}
    )  # 省信息
    country: GetHireOfferByApplicationRespOfferBasicInfoWorkAddressCountry = attr.ib(
        default=None, metadata={"req_type": "json", "key": "country"}
    )  # 国家信息


@attr.s
class GetHireOfferByApplicationRespOfferBasicInfoOnboardAddressCountry(object):
    zh_name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "zh_name"}
    )  # 中文名称
    en_name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "en_name"}
    )  # 英文名称
    code: str = attr.ib(default="", metadata={"req_type": "json", "key": "code"})  # 编码
    location_type: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "location_type"}
    )  # 地址类型 1=COUNTRY, 2=STATE, 3=CITY, 4=DISTRICT, 5=ADDRESS,, 可选值有: `1`：COUNTRY, `2`：STATE, `3`：CITY, `4`：DISTRICT, `5`：ADDRESS


@attr.s
class GetHireOfferByApplicationRespOfferBasicInfoOnboardAddressState(object):
    zh_name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "zh_name"}
    )  # 中文名称
    en_name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "en_name"}
    )  # 英文名称
    code: str = attr.ib(default="", metadata={"req_type": "json", "key": "code"})  # 编码
    location_type: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "location_type"}
    )  # 地址类型 1=COUNTRY, 2=STATE, 3=CITY, 4=DISTRICT, 5=ADDRESS,, 可选值有: `1`：COUNTRY, `2`：STATE, `3`：CITY, `4`：DISTRICT, `5`：ADDRESS


@attr.s
class GetHireOfferByApplicationRespOfferBasicInfoOnboardAddressCity(object):
    zh_name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "zh_name"}
    )  # 中文名称
    en_name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "en_name"}
    )  # 英文名称
    code: str = attr.ib(default="", metadata={"req_type": "json", "key": "code"})  # 编码
    location_type: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "location_type"}
    )  # 地址类型 1=COUNTRY, 2=STATE, 3=CITY, 4=DISTRICT, 5=ADDRESS,, 可选值有: `1`：COUNTRY, `2`：STATE, `3`：CITY, `4`：DISTRICT, `5`：ADDRESS


@attr.s
class GetHireOfferByApplicationRespOfferBasicInfoOnboardAddressDistrict(object):
    zh_name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "zh_name"}
    )  # 中文名称
    en_name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "en_name"}
    )  # 英文名称
    code: str = attr.ib(default="", metadata={"req_type": "json", "key": "code"})  # 编码
    location_type: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "location_type"}
    )  # 地址类型 1=COUNTRY, 2=STATE, 3=CITY, 4=DISTRICT, 5=ADDRESS,


@attr.s
class GetHireOfferByApplicationRespOfferBasicInfoOnboardAddress(object):
    id: str = attr.ib(default="", metadata={"req_type": "json", "key": "id"})  # ID
    zh_name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "zh_name"}
    )  # 中文名称
    en_name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "en_name"}
    )  # 英文名称
    district: GetHireOfferByApplicationRespOfferBasicInfoOnboardAddressDistrict = (
        attr.ib(default=None, metadata={"req_type": "json", "key": "district"})
    )  # 区域信息
    city: GetHireOfferByApplicationRespOfferBasicInfoOnboardAddressCity = attr.ib(
        default=None, metadata={"req_type": "json", "key": "city"}
    )  # 城市信息
    state: GetHireOfferByApplicationRespOfferBasicInfoOnboardAddressState = attr.ib(
        default=None, metadata={"req_type": "json", "key": "state"}
    )  # 省信息
    country: GetHireOfferByApplicationRespOfferBasicInfoOnboardAddressCountry = attr.ib(
        default=None, metadata={"req_type": "json", "key": "country"}
    )  # 国家信息


@attr.s
class GetHireOfferByApplicationRespOfferBasicInfoLevel(object):
    id: str = attr.ib(default="", metadata={"req_type": "json", "key": "id"})  # ID
    zh_name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "zh_name"}
    )  # 中文名称
    en_name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "en_name"}
    )  # 英文名称


@attr.s
class GetHireOfferByApplicationRespOfferBasicInfoSequence(object):
    id: str = attr.ib(default="", metadata={"req_type": "json", "key": "id"})  # ID
    zh_name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "zh_name"}
    )  # 中文名称
    en_name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "en_name"}
    )  # 英文名称


@attr.s
class GetHireOfferByApplicationRespOfferBasicInfoRecruitmentType(object):
    id: str = attr.ib(default="", metadata={"req_type": "json", "key": "id"})  # ID
    zh_name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "zh_name"}
    )  # 中文名称
    en_name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "en_name"}
    )  # 英文名称


@attr.s
class GetHireOfferByApplicationRespOfferBasicInfo(object):
    offer_type: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "offer_type"}
    )  # Offer类型 1=Social, 2=Campus, 3=Intern, 4=InternTransfer, 可选值有: `1`：Social, `2`：Campus, `3`：Intern, `4`：InternTransfer
    remark: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "remark"}
    )  # 备注
    expire_time: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "expire_time"}
    )  # Offer过期时间
    owner_user_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "owner_user_id"}
    )  # offer 负责人 ID
    leader_user_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "leader_user_id"}
    )  # 直属上级 ID
    onboard_date: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "onboard_date"}
    )  # 入职日期
    department_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "department_id"}
    )  # 入职部门
    probation_month: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "probation_month"}
    )  # 试用期, 比如试用期6个月
    contract_year: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "contract_year"}
    )  # 合同期, 比如3年
    recruitment_type: GetHireOfferByApplicationRespOfferBasicInfoRecruitmentType = (
        attr.ib(default=None, metadata={"req_type": "json", "key": "recruitment_type"})
    )  # 雇员类型
    sequence: GetHireOfferByApplicationRespOfferBasicInfoSequence = attr.ib(
        default=None, metadata={"req_type": "json", "key": "sequence"}
    )  # 序列
    level: GetHireOfferByApplicationRespOfferBasicInfoLevel = attr.ib(
        default=None, metadata={"req_type": "json", "key": "level"}
    )  # 级别
    onboard_address: GetHireOfferByApplicationRespOfferBasicInfoOnboardAddress = (
        attr.ib(default=None, metadata={"req_type": "json", "key": "onboard_address"})
    )  # 入职地点
    work_address: GetHireOfferByApplicationRespOfferBasicInfoWorkAddress = attr.ib(
        default=None, metadata={"req_type": "json", "key": "work_address"}
    )  # 工作地点
    customize_info_list: typing.List[
        GetHireOfferByApplicationRespOfferBasicInfoCustomizeInfo
    ] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "customize_info_list"}
    )  # 自定义字段的value信息


@attr.s
class GetHireOfferByApplicationRespOffer(object):
    id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "id"}
    )  # Offer id
    application_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "application_id"}
    )  # 投递id
    basic_info: GetHireOfferByApplicationRespOfferBasicInfo = attr.ib(
        default=None, metadata={"req_type": "json", "key": "basic_info"}
    )  # 基础信息
    salary_plan: GetHireOfferByApplicationRespOfferSalaryPlan = attr.ib(
        default=None, metadata={"req_type": "json", "key": "salary_plan"}
    )  # 薪酬计划
    schema_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "schema_id"}
    )  # 当前offer使用的schema
    offer_status: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "offer_status"}
    )  # Offer状态, 可选值有: `0`：所有, `1`：未申请, `2`：审批中, `3`：审批已撤回, `4`：审批通过, `5`：审批不通过, `6`：Offer 已发出, `7`：候选人已接受, `8`：候选人已拒绝, `9`：Offer 已失效


@attr.s
class GetHireOfferByApplicationResp(object):
    offer: GetHireOfferByApplicationRespOffer = attr.ib(
        default=None, metadata={"req_type": "json", "key": "offer"}
    )  # Offer数据


def _gen_get_hire_offer_by_application_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetHireOfferByApplicationResp,
        scope="Hire",
        api="GetHireOfferByApplication",
        method="GET",
        url="https://open.feishu.cn/open-apis/hire/v1/applications/:application_id/offer",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
