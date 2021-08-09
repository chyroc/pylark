# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing


@attr.s
class GetVCDailyReportReq(object):
    start_time: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # 开始时间（unix时间，单位sec）, 示例值："1608888867"
    end_time: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # 结束时间（unix时间，单位sec）, 示例值："1608888966"


@attr.s
class GetVCDailyReportRespMeetingReportDailyReport(object):
    date: str = attr.ib(default="", metadata={"req_type": "json"})  # 日期（unix时间，单位sec）
    meeting_count: str = attr.ib(default="", metadata={"req_type": "json"})  # 会议数量
    meeting_duration: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 会议时长（单位sec）
    participant_count: str = attr.ib(default="", metadata={"req_type": "json"})  # 参会人数


@attr.s
class GetVCDailyReportRespMeetingReport(object):
    total_meeting_count: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 总会议数量
    total_meeting_duration: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 总会议时长（单位sec）
    total_participant_count: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 总参会人数
    daily_report: GetVCDailyReportRespMeetingReportDailyReport = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 每日会议报告列表


@attr.s
class GetVCDailyReportResp(object):
    meeting_report: GetVCDailyReportRespMeetingReport = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 会议报告


def _gen_get_vc_daily_report_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetVCDailyReportResp,
        scope="VC",
        api="GetVCDailyReport",
        method="GET",
        url="https://open.feishu.cn/open-apis/vc/v1/reports/get_daily",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )