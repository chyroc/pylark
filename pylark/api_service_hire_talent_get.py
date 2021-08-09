# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing


@attr.s
class GetHireTalentReq(object):
    talent_id: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 人才ID, 示例值："6891560630172518670"


@attr.s
class GetHireTalentRespTalentInterviewRegistration(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # ID
    registration_time: int = attr.ib(default=0, metadata={"req_type": "json"})  # 创建时间


@attr.s
class GetHireTalentRespTalentResumeSource(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # ID
    zh_name: str = attr.ib(default="", metadata={"req_type": "json"})  # 中文名
    en_name: str = attr.ib(default="", metadata={"req_type": "json"})  # 英文名


@attr.s
class GetHireTalentRespTalentSns(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # ID
    sns_type: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # SNS类型, 可选值有: `1`：领英, `2`：脉脉, `3`：微信, `4`：微博, `5`：Github, `6`：知乎, `7`：脸书, `8`：推特, `9`：Whatsapp, `10`：个人网站, `11`：QQ
    link: str = attr.ib(default="", metadata={"req_type": "json"})  # SNS链接


@attr.s
class GetHireTalentRespTalentLanguage(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # ID
    language: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 语言, 可选值有: `1`：英语, `2`：法语, `3`：日语, `4`：韩语, `5`：德语, `6`：俄语, `7`：西班牙语, `8`：葡萄牙语, `9`：阿拉伯语, `10`：印地语, `11`：印度斯坦语, `12`：孟加拉语, `13`：豪萨语, `14`：旁遮普语, `15`：波斯语, `16`：斯瓦西里语, `17`：泰卢固语, `18`：土耳其语, `19`：意大利语, `20`：爪哇语, `21`：泰米尔语, `22`：马拉地语, `23`：越南语, `24`：普通话, `25`：粤语
    proficiency: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 熟练程度, 可选值有: `1`：入门, `2`：日常会话, `3`：商务会话, `4`：无障碍沟通, `5`：母语


@attr.s
class GetHireTalentRespTalentCertificate(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # ID
    name: str = attr.ib(default="", metadata={"req_type": "json"})  # 证件名称
    desc: str = attr.ib(default="", metadata={"req_type": "json"})  # 证件描述


@attr.s
class GetHireTalentRespTalentCompetition(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # ID
    name: str = attr.ib(default="", metadata={"req_type": "json"})  # 竞赛名称
    desc: str = attr.ib(default="", metadata={"req_type": "json"})  # 竞赛描述


@attr.s
class GetHireTalentRespTalentAward(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # ID
    title: str = attr.ib(default="", metadata={"req_type": "json"})  # 名称
    award_time: str = attr.ib(default="", metadata={"req_type": "json"})  # 获奖时间
    desc: str = attr.ib(default="", metadata={"req_type": "json"})  # 描述


@attr.s
class GetHireTalentRespTalentWorks(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # ID
    link: str = attr.ib(default="", metadata={"req_type": "json"})  # 链接
    desc: str = attr.ib(default="", metadata={"req_type": "json"})  # 描述
    name: str = attr.ib(default="", metadata={"req_type": "json"})  # 名字


@attr.s
class GetHireTalentRespTalentProject(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # ID
    name: str = attr.ib(default="", metadata={"req_type": "json"})  # 项目名称
    role: str = attr.ib(default="", metadata={"req_type": "json"})  # 项目角色
    link: str = attr.ib(default="", metadata={"req_type": "json"})  # 项目链接
    desc: str = attr.ib(default="", metadata={"req_type": "json"})  # 描述
    start_time: str = attr.ib(default="", metadata={"req_type": "json"})  # 开始时间
    end_time: str = attr.ib(default="", metadata={"req_type": "json"})  # 结束时间


@attr.s
class GetHireTalentRespTalentCareer(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # ID
    company: str = attr.ib(default="", metadata={"req_type": "json"})  # 公司
    title: str = attr.ib(default="", metadata={"req_type": "json"})  # 职位
    desc: str = attr.ib(default="", metadata={"req_type": "json"})  # 描述
    start_time: str = attr.ib(default="", metadata={"req_type": "json"})  # 开始时间
    end_time: str = attr.ib(default="", metadata={"req_type": "json"})  # 结束时间
    tag_list: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 标签, 可选值有: `1`：985学校, `2`：211学校, `3`：一本, `4`：国外院校QS200, `5`：百度 阿里 腾讯, `6`：头条, 美团, 滴滴, `7`：其它大厂, `8`：猎头渠道, `9`：内推渠道, `10`：互联网大厂（包含 BAT/TMD）, `11`：熟人内推, `100`：email, `101`：mobile, `102`：猎头保护中, `103`：已入职, `104`：已离职


@attr.s
class GetHireTalentRespTalentEducation(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # ID
    degree: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 学位, 可选值有: `1`：小学, `2`：初中, `3`：专职, `4`：高中, `5`：大专, `6`：本科, `7`：硕士, `8`：博士, `9`：其他
    school: str = attr.ib(default="", metadata={"req_type": "json"})  # 学校
    field_of_study: str = attr.ib(default="", metadata={"req_type": "json"})  # 专业
    start_time: int = attr.ib(default=0, metadata={"req_type": "json"})  # 开始时间
    end_time: int = attr.ib(default=0, metadata={"req_type": "json"})  # 结束时间
    education_type: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 学历类型, 可选值有: `1`：非中国大陆, `2`：统招全日制, `3`：非全日制, `4`：自考, `5`：其他
    academic_ranking: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 成绩排名, 可选值有: `5`：前 5 %, `10`：前 10 %, `20`：前 20 %, `30`：前 30 %, `50`：前 50 %, `-1`：其他
    tag_list: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 标记, 可选值有: `1`：985学校, `2`：211学校, `3`：一本, `4`：国外院校QS200, `5`：百度 阿里 腾讯, `6`：头条, 美团, 滴滴, `7`：其它大厂, `8`：猎头渠道, `9`：内推渠道, `10`：互联网大厂（包含 BAT/TMD）, `11`：熟人内推, `100`：email, `101`：mobile, `102`：猎头保护中, `103`：已入职, `104`：已离职


@attr.s
class GetHireTalentRespTalentBasicInfoPreferredCity(object):
    city_code: str = attr.ib(default="", metadata={"req_type": "json"})  # 城市码
    zh_name: str = attr.ib(default="", metadata={"req_type": "json"})  # 名字
    en_name: str = attr.ib(default="", metadata={"req_type": "json"})  # 英文名


@attr.s
class GetHireTalentRespTalentBasicInfoHometownCity(object):
    city_code: str = attr.ib(default="", metadata={"req_type": "json"})  # 城市码
    zh_name: str = attr.ib(default="", metadata={"req_type": "json"})  # 名字
    en_name: str = attr.ib(default="", metadata={"req_type": "json"})  # 英文名


@attr.s
class GetHireTalentRespTalentBasicInfoCurrentCity(object):
    city_code: str = attr.ib(default="", metadata={"req_type": "json"})  # 城市码
    zh_name: str = attr.ib(default="", metadata={"req_type": "json"})  # 名字
    en_name: str = attr.ib(default="", metadata={"req_type": "json"})  # 英文名


@attr.s
class GetHireTalentRespTalentBasicInfoNationality(object):
    nationality_code: str = attr.ib(default="", metadata={"req_type": "json"})  # 国家编码
    zh_name: str = attr.ib(default="", metadata={"req_type": "json"})  # 名字
    en_name: str = attr.ib(default="", metadata={"req_type": "json"})  # 英文名


@attr.s
class GetHireTalentRespTalentBasicInfo(object):
    name: str = attr.ib(default="", metadata={"req_type": "json"})  # 名字
    mobile: str = attr.ib(default="", metadata={"req_type": "json"})  # 手机
    mobile_country_code: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 手机国家代码
    email: str = attr.ib(default="", metadata={"req_type": "json"})  # 邮箱
    experience_years: int = attr.ib(default=0, metadata={"req_type": "json"})  # 工作年限
    age: int = attr.ib(default=0, metadata={"req_type": "json"})  # 年龄
    nationality: GetHireTalentRespTalentBasicInfoNationality = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 国籍
    gender: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 性别, 可选值有: `1`：男, `2`：女, `3`：其他
    current_city: GetHireTalentRespTalentBasicInfoCurrentCity = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 当前所在城市信息
    hometown_city: GetHireTalentRespTalentBasicInfoHometownCity = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 家乡
    preferred_city_list: typing.List[
        GetHireTalentRespTalentBasicInfoPreferredCity
    ] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 偏好城市
    identification_type: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 证件类型, 可选值有: `1`：中国 - 居民身份证, `2`：护照, `3`：中国 - 港澳居民居住证, `4`：中国 - 台湾居民来往大陆通行证, `5`：其他, `6`：中国 - 港澳居民来往内地通行证, `9`：中国 - 台湾居民居住证
    identification_number: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 证件号
    birthday: int = attr.ib(default=0, metadata={"req_type": "json"})  # 生日


@attr.s
class GetHireTalentRespTalent(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # ID
    basic_info: GetHireTalentRespTalentBasicInfo = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 基础信息
    education_list: typing.List[GetHireTalentRespTalentEducation] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 教育经历
    career_list: typing.List[GetHireTalentRespTalentCareer] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 工作经历
    project_list: typing.List[GetHireTalentRespTalentProject] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 项目经历
    works_list: typing.List[GetHireTalentRespTalentWorks] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 作品集
    award_list: typing.List[GetHireTalentRespTalentAward] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 获奖列表
    competition_list: typing.List[GetHireTalentRespTalentCompetition] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 竞赛列表
    certificate_list: typing.List[GetHireTalentRespTalentCertificate] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 证书列表
    language_list: typing.List[GetHireTalentRespTalentLanguage] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 语言列表
    sns_list: typing.List[GetHireTalentRespTalentSns] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # SNS列表
    resume_source_list: typing.List[GetHireTalentRespTalentResumeSource] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 简历来源
    interview_registration_list: typing.List[
        GetHireTalentRespTalentInterviewRegistration
    ] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 面试登记表
    resume_attachment_id_list: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 简历附件id列表（按照简历创建时间降序）


@attr.s
class GetHireTalentResp(object):
    talent: GetHireTalentRespTalent = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 人才信息


def _gen_get_hire_talent_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetHireTalentResp,
        scope="Hire",
        api="GetHireTalent",
        method="GET",
        url="https://open.feishu.cn/open-apis/hire/v1/talents/:talent_id",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )