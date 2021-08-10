# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class GetVCTopUserReportReq(object):
    start_time: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # 开始时间（unix时间，单位sec）, 示例值："1608888867"
    end_time: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # 结束时间（unix时间，单位sec）, 示例值："1608889966"
    limit: int = attr.ib(default=0, metadata={"req_type": "query"})  # 取前多少位, 示例值：10
    order_by: int = attr.ib(
        default=0, metadata={"req_type": "query"}
    )  # 排序依据（降序）, 示例值：1, 可选值有: `1`：会议数量, `2`：会议时长


@attr.s
class GetVCTopUserReportRespTopUserReport(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户ID
    name: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户名
    user_type: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 用户类型, 可选值有: `1`：lark用户, `2`：rooms用户, `3`：文档用户, `4`：neo单品用户, `5`：neo单品游客用户, `6`：pstn用户, `7`：sip用户
    meeting_count: str = attr.ib(default="", metadata={"req_type": "json"})  # 会议数量
    meeting_duration: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 会议时长（单位sec）


@attr.s
class GetVCTopUserReportResp(object):
    top_user_report: GetVCTopUserReportRespTopUserReport = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # top用户列表


def _gen_get_vc_top_user_report_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetVCTopUserReportResp,
        scope="VC",
        api="GetVCTopUserReport",
        method="GET",
        url="https://open.feishu.cn/open-apis/vc/v1/reports/get_top_user",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
