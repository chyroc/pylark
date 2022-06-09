# coding: utf-8

from __future__ import absolute_import, division, print_function, unicode_literals

import typing
from enum import EnumMeta, Enum
import attr


class DefaultEnumMeta(EnumMeta):
    default = object()

    def __call__(cls, value=default, *args, **kwargs):
        if value is DefaultEnumMeta.default:
            return next(iter(cls)) # type: ignore
        return super().__call__(value, *args, **kwargs) # type: ignore


class MsgType(Enum, metaclass=DefaultEnumMeta):
    """MsgType 消息类型"""

    text = "text"  # 文本
    post = "post"  # 富文本
    image = "image"  # 图片
    file = "file"  # 文件
    audio = "audio"  # 语音
    media = "media"  # 视频
    sticker = "sticker"  # 表情包
    interactive = "interactive"  # 卡片消息
    share_chat = "share_chat"  # 分享群卡片
    share_user = "share_user"  # 分享个人卡片


class ContainerIDType(Enum, metaclass=DefaultEnumMeta):
    """容器类型"""

    chat = "chat"


class IDType(Enum, metaclass=DefaultEnumMeta):
    """ID类型"""

    user_id = "user_id"  # 以 user_id 来识别成员
    union_id = "union_id"  # 以 union_id 来识别成员
    open_id = "open_id"  # 以 open_id 来识别成员
    app_id = "app_id"  # 以 app_id 来识别成员
    chat_id = "chat_id"  # 以 chat_id 来识别成员
    email = "email"  # 以 email 来识别成员


class DepartmentIDType(Enum, metaclass=DefaultEnumMeta):
    """ID类型"""

    department_id = "department_id"  # 以 department_id 来识别
    open_department_id = "open_department_id"  # open_department_id


class MailUserType(Enum, metaclass=DefaultEnumMeta):
    user = "USER"  # 内部用户
    department = "DEPARTMENT"  # 部门
    company = "COMPANY"  # 全员
    external_user = "EXTERNAL_USER"  # 外部用户
    mail_group = "MAIL_GROUP"  # 邮件组
    other_member = "OTHER_MEMBER"  # 内部成员


class EmployeeType(Enum, metaclass=DefaultEnumMeta):
    employee_id = "employee_id"  # 员工id
    employee_no = "employee_no"  # 员工工号


class ChatType(Enum, metaclass=DefaultEnumMeta):
    private = "private"
    public = "public"


class ImageType(Enum, metaclass=DefaultEnumMeta):
    message = "message"  # 用于发送消息
    avatar = "avatar"  # 用于设置头像


class FileType(Enum, metaclass=DefaultEnumMeta):
    opus = "opus"  # 上传opus音频文件；其他格式的音频文件，请转为opus格式后上传，转换方式可参考：ffmpeg -i SourceFile.mp3 -acodec libopus -ac 1 -ar 16000 TargetFile.opus
    mp4 = "mp4"  # 上传mp4视频文件
    pdf = "pdf"  # 上传pdf格式文件
    doc = "doc"  # 上传doc格式文件
    xls = "xls"  # 上传xls格式文件
    ppt = "ppt"  # 上传ppt格式文件
    stream = "stream"  # 上传stream格式文件


class CalendarRole(Enum, metaclass=DefaultEnumMeta):
    """CalendarRole 对日历的访问权限"""

    free_busy_reader = "free_busy_reader"  # 游客，只能看到忙碌/空闲信息
    reader = "reader"  # 订阅者，查看所有日程详情
    writer = "writer"  # 编辑者，创建及修改日程
    owner = "owner"  # 管理员，管理日历及共享设置


class CalendarEventAttendeeType(Enum, metaclass=DefaultEnumMeta):
    """参与人类型"""

    user = "user"  # 用户
    chat = "chat"  # 群组
    # user = "user"  # 会议室


class CalendarType(Enum, metaclass=DefaultEnumMeta):
    unknown = "unknown"  # 未知类型
    primary = "primary"  # 用户或应用的主日历
    shared = "shared"  # 由用户或应用创建的共享日历
    google = "google"  # 用户绑定的谷歌日历
    resource = "resource"  # 会议室日历
    exchange = "exchange"  # 用户绑定的Exchange日历


class CalendarPermission(Enum, metaclass=DefaultEnumMeta):
    private = "private"  # 私密
    show_only_free_busy = "show_only_free_busy"  # 仅展示忙闲信息
    public = "public"  # 他人可查看日程详情


class AddMemberPermission(Enum, metaclass=DefaultEnumMeta):
    """加 user/bot 入群权限"""

    all_members = "all_members"
    only_owner = "only_owner"


class MessageVisibility(Enum, metaclass=DefaultEnumMeta):
    """入群消息可见性"""

    only_owner = "only_owner"
    all_members = "all_members"
    not_anyone = "not_anyone"


class MembershipApproval(Enum, metaclass=DefaultEnumMeta):
    """加群审批"""

    no_approval_required = "no_approval_required"
    approval_required = "approval_required"


class ModerationPermission(Enum, metaclass=DefaultEnumMeta):
    """发言权限"""

    all_members = "all_members"
    only_owner = "only_owner"
    moderator_list = "moderator_list"


class ShareCardPermission(Enum, metaclass=DefaultEnumMeta):
    """群分享权限"""

    allowed = "allowed"
    not_allowed = "not_allowed"


class AtAllPermission(Enum, metaclass=DefaultEnumMeta):
    """at 所有人权限"""

    all_members = "all_members"
    only_owner = "only_owner"


class EditPermission(Enum, metaclass=DefaultEnumMeta):
    """群编辑权限"""

    all_members = "all_members"
    only_owner = "only_owner"


@attr.s
class HelpdeskDropdownOption(object):
    """下拉列表选项"""

    tag: str = attr.ib(default="", metadata={"req_type": "json", "key": "tag"})  # 选项ID
    display_name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "display_name"}
    )  # 展示名称
    children: typing.List["HelpdeskDropdownOption"] = attr.ib(
        factory=list, metadata={"req_type": "json", "key": "children"}
    )  # 同上：选项列表，只适用于多层下拉列表（最多可以设置三级下拉列表）

@attr.s
class I18nNames:
    # FIXME: inaccurate type name placeholder
    pass

@attr.s
class HelpdeskCategory:
    # FIXME: inaccurate type name placeholder
    pass

@attr.s
class MessageContentCard:
    # FIXME: inaccurate type name placeholder
    pass

@attr.s
class Sender:
    # FIXME: inaccurate type name placeholder
    pass

@attr.s
class MessageBody:
    # FIXME: inaccurate type name placeholder
    pass

@attr.s
class Mention:
    # FIXME: inaccurate type name placeholder
    pass
