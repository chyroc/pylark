# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class UpdateAttendanceRemedyApprovalReq(object):
    approval_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 审批实例 ID
    approval_type: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 审批类型，leave：请假，out：外出，overtime：加班，trip：出差，remedy：补卡
    status: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 审批状态，1：不通过，2：通过，4：撤销


@attr.s
class UpdateAttendanceRemedyApprovalRespApprovalInfo(object):
    approval_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 审批实例 ID
    approval_type: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 审批类型，leave：请假，out：外出，overtime：加班，trip：出差，remedy：补卡
    status: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 审批状态，1：不通过，2：通过，4：已撤销


@attr.s
class UpdateAttendanceRemedyApprovalResp(object):
    approval_info: UpdateAttendanceRemedyApprovalRespApprovalInfo = attr.ib(
        default=None, metadata={"req_type": "json"}
    )


def _gen_update_attendance_remedy_approval_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=UpdateAttendanceRemedyApprovalResp,
        scope="Attendance",
        api="UpdateAttendanceRemedyApproval",
        method="POST",
        url="https://open.feishu.cn/open-apis/attendance/v1/approval_infos/process",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
