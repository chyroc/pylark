# pylark

[![codecov](https://codecov.io/gh/chyroc/pylark/branch/master/graph/badge.svg?token=Z73T6YFF80)](https://codecov.io/gh/chyroc/pylark)
[![test status](https://github.com/chyroc/pylark/actions/workflows/test.yml/badge.svg)](https://github.com/chyroc/pylark/actions)
[![Apache-2.0 license](https://img.shields.io/badge/License-Apache%202.0-brightgreen.svg)](https://opensource.org/licenses/Apache-2.0)
![PyPI - Downloads](https://img.shields.io/pypi/dm/pylark)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pylark)
![PyPI - Format](https://img.shields.io/pypi/format/pylark)
[![PyPI version](https://badge.fury.io/py/pylark.svg)](https://pypi.org/project/pylark)

[中文版 README](./README_CN.md)

Feishu/Lark Open API Python Sdk, Support ALL Open API and Event Callback.

Supported Features

- Many APIs and events
- Support mock to support test
- Support isv and self-built apps
- Support Logger interface
- Support UserAccessToken
- Use code generation to create, api and document update timely

## Chat

Click [Lark Chat Link](https://applink.feishu.cn/client/chat/chatter/add_by_link?link_token=985n4cf0-70d7-444c-909f-98885892c233) to discuss.

## Install

```shell
pip install pylark
```

## Docs

http://lark-sdk.github.io/

## Support APIs

API Count: 476, Event Count: 76

<details>
  <summary>
    Click This to See ALL
  </summary>

- Auth
  - ResendAppTicket
  - GetAccessToken
  - RefreshAccessToken
  - GetUserInfo
- Contact
  - SearchUserOld
  - CreateUser
  - DeleteUser
  - GetUser
  - BatchGetUser
  - BatchGetUserByID
  - GetUserList
  - UpdateUserPatch
  - UpdateUser
  - CreateDepartment
  - GetDepartment
  - GetDepartmentList
  - GetParentDepartment
  - SearchDepartment
  - UpdateDepartmentPatch
  - UpdateDepartment
  - DeleteDepartment
  - CreateContactGroup
  - UpdateContactGroup
  - DeleteContactGroup
  - GetContactGroup
  - GetContactGroupList
  - AddContactGroupMember
  - DeleteContactGroupMember
  - GetContactGroupMember
  - GetEmployeeTypeEnumList
  - UpdateEmployeeTypeEnumPatch
  - DeleteEmployeeTypeEnum
  - CreateEmployeeTypeEnum
  - GetContactCustomAttrList
- Message
  - SendEphemeralMessage
  - SendUrgentAppMessage
  - SendUrgentSmsMessage
  - SendUrgentPhoneMessage
  - SendRawMessage
  - SendRawMessageOld
  - BatchSendOldRawMessage
  - ReplyRawMessage
  - DeleteMessage
  - BatchDeleteMessage
  - UpdateMessage
  - GetMessageReadUserList
  - GetBatchSentMessageReadUser
  - GetMessageList
  - GetMessageFile
  - GetMessage
  - DeleteEphemeralMessage
- Chat
  - CreateChat
  - GetChatOld
  - GetChat
  - UpdateChat
  - DeleteChat
  - GetChatListOfSelf
  - SearchChat
  - GetChatMemberList
  - IsInChat
  - AddChatMember
  - DeleteChatMember
  - JoinChat
  - GetChatAnnouncement
  - UpdateChatAnnouncement
- Bot
  - GetBotInfo
  - AddBotToChat
- Calendar
  - CreateCalendarACL
  - DeleteCalendarACL
  - GetCalendarACLList
  - SubscribeCalendarACL
  - CreateCalendar
  - DeleteCalendar
  - GetCalendar
  - GetCalendarList
  - UpdateCalendar
  - SearchCalendar
  - SubscribeCalendar
  - UnsubscribeCalendar
  - SubscribeCalendarChangeEvent
  - CreateCalendarEvent
  - DeleteCalendarEvent
  - GetCalendarEvent
  - GetCalendarEventList
  - UpdateCalendarEvent
  - SearchCalendarEvent
  - SubscribeCalendarEvent
  - CreateCalendarEventAttendee
  - GetCalendarEventAttendeeList
  - DeleteCalendarEventAttendee
  - GetCalendarEventAttendeeChatMemberList
  - GetCalendarFreeBusyList
  - CreateCalendarTimeoffEvent
  - DeleteCalendarTimeoffEvent
  - GenerateCaldavConf
- Drive
  - SearchDriveFile
  - GetDriveFileMeta
  - CreateDriveFile
  - CopyDriveFile
  - DeleteDriveFile
  - DeleteDriveSheetFile
  - CreateDriveFolder
  - GetDriveFolderMeta
  - GetDriveRootFolderMeta
  - GetDriveFolderChildren
  - GetDriveFileStatistics
  - DownloadDriveFile
  - UploadDriveFile
  - PrepareUploadDriveFile
  - PartUploadDriveFile
  - FinishUploadDriveFile
  - DownloadDriveMedia
  - UploadDriveMedia
  - PrepareUploadDriveMedia
  - PartUploadDriveMedia
  - FinishUploadDriveMedia
  - CreateDriveMemberPermissionOld
  - TransferDriveMemberPermission
  - GetDriveMemberPermissionList
  - CreateDriveMemberPermission
  - DeleteDriveMemberPermissionOld
  - DeleteDriveMemberPermission
  - UpdateDriveMemberPermissionOld
  - UpdateDriveMemberPermission
  - CheckDriveMemberPermission
  - UpdateDrivePublicPermissionV1Old
  - UpdateDrivePublicPermissionV2Old
  - GetDrivePublicPermissionV2
  - UpdateDrivePublicPermission
  - BatchGetDriveMediaTmpDownloadURL
  - GetDriveCommentList
  - GetDriveComment
  - CreateDriveComment
  - UpdateDriveComment
  - DeleteDriveComment
  - UpdateDriveCommentPatch
  - CreateDriveDoc
  - GetDriveDocContent
  - GetDriveDocRawContent
  - GetDriveDocMeta
  - CreateSheet
  - GetSheetMeta
  - UpdateSheetProperty
  - BatchUpdateSheet
  - ImportSheet
  - CreateDriveImportTask
  - GetDriveImportTask
  - MoveSheetDimension
  - PrependSheetValue
  - AppendSheetValue
  - InsertSheetDimensionRange
  - AddSheetDimensionRange
  - UpdateSheetDimensionRange
  - DeleteSheetDimensionRange
  - GetSheetValue
  - BatchGetSheetValue
  - SetSheetValue
  - BatchSetSheetValue
  - SetSheetStyle
  - BatchSetSheetStyle
  - MergeSheetCell
  - UnmergeSheetCell
  - SetSheetValueImage
  - FindSheet
  - ReplaceSheet
  - CreateSheetConditionFormat
  - GetSheetConditionFormat
  - UpdateSheetConditionFormat
  - DeleteSheetConditionFormat
  - CreateSheetProtectedDimension
  - GetSheetProtectedDimension
  - UpdateSheetProtectedDimension
  - DeleteSheetProtectedDimension
  - CreateSheetDataValidationDropdown
  - DeleteSheetDataValidationDropdown
  - UpdateSheetDataValidationDropdown
  - GetSheetDataValidationDropdown
  - CreateSheetFilter
  - DeleteSheetFilter
  - UpdateSheetFilter
  - GetSheetFilter
  - CreateSheetFilterView
  - DeleteSheetFilterView
  - UpdateSheetFilterView
  - GetSheetFilterView
  - QuerySheetFilterView
  - CreateSheetFilterViewCondition
  - DeleteSheetFilterViewCondition
  - UpdateSheetFilterViewCondition
  - GetSheetFilterViewCondition
  - QuerySheetFilterViewCondition
  - CreateSheetFloatImage
  - DeleteSheetFloatImage
  - UpdateSheetFloatImage
  - GetSheetFloatImage
  - QuerySheetFloatImage
- Bitable
  - GetBitableViewList
  - CreateBitableView
  - DeleteBitableView
  - GetBitableRecordList
  - GetBitableRecord
  - CreateBitableRecord
  - BatchCreateBitableRecord
  - UpdateBitableRecord
  - BatchUpdateBitableRecord
  - DeleteBitableRecord
  - BatchDeleteBitableRecord
  - GetBitableFieldList
  - CreateBitableField
  - UpdateBitableField
  - DeleteBitableField
  - GetBitableTableList
  - CreateBitableTable
  - BatchCreateBitableTable
  - DeleteBitableTable
  - BatchDeleteBitableTable
  - GetBitableMeta
- MeetingRoom
  - BatchGetMeetingRoomSummary
  - GetMeetingRoomBuildingList
  - BatchGetMeetingRoomBuilding
  - GetMeetingRoomRoomList
  - BatchGetMeetingRoomRoom
  - BatchGetMeetingRoomFreebusy
  - ReplyMeetingRoomInstance
  - CreateMeetingRoomBuilding
  - UpdateMeetingRoomBuilding
  - DeleteMeetingRoomBuilding
  - BatchGetMeetingRoomBuildingID
  - CreateMeetingRoomRoom
  - UpdateMeetingRoomRoom
  - DeleteMeetingRoomRoom
  - BatchGetMeetingRoomRoomID
  - GetMeetingRoomCountryList
  - GetMeetingRoomDistrictList
- Jssdk
  - GetJssdkTicket
- VC
  - ApplyVCReserve
  - UpdateVCReserve
  - DeleteVCReserve
  - GetVCReserve
  - GetVCReserveActiveMeeting
  - GetVCMeeting
  - InviteVCMeeting
  - KickoutVCMeeting
  - SetVCHostMeeting
  - EndVCMeeting
  - StartVCMeetingRecording
  - StopVCMeetingRecording
  - GetVCMeetingRecording
  - SetVCPermissionMeetingRecording
  - GetVCDailyReport
  - GetVCTopUserReport
  - GetVCRoomConfig
  - SetVCRoomConfig
- Application
  - IsApplicationUserAdmin
  - GetApplicationUserAdminScope
  - GetApplicationAppVisibility
  - GetApplicationUserVisibleApp
  - GetApplicationAppList
  - UpdateApplicationAppVisibility
  - GetApplicationAppAdminUserList
  - CheckUserIsInApplicationPaidScope
  - GetApplicationOrderList
  - GetApplicationOrder
  - GetApplicationUsageOverview
  - GetApplicationUsageTrend
  - GetApplicationUsageDetail
  - GetApplicationMessageOverview
  - GetApplicationMessageTrend
  - GetApplicationMessageDetail
- Mail
  - CreateMailGroup
  - GetMailGroup
  - GetMailGroupList
  - UpdateMailGroupPatch
  - UpdateMailGroup
  - DeleteMailGroup
  - CreateMailGroupMember
  - GetMailGroupMember
  - GetMailGroupMemberList
  - DeleteMailGroupMember
  - CreateMailGroupPermissionMember
  - GetMailGroupPermissionMember
  - GetMailGroupPermissionMemberList
  - DeleteMailGroupPermissionMember
  - CreatePublicMailbox
  - GetPublicMailbox
  - GetPublicMailboxList
  - UpdatePublicMailboxPatch
  - UpdatePublicMailbox
  - CreatePublicMailboxMember
  - GetPublicMailboxMember
  - GetPublicMailboxMemberList
  - DeletePublicMailboxMember
  - ClearPublicMailboxMember
- Approval
  - GetApproval
  - GetApprovalInstanceList
  - GetApprovalInstance
  - CreateApprovalInstance
  - ApproveApprovalInstance
  - RejectApprovalInstance
  - TransferApprovalInstance
  - CancelApprovalInstance
  - SearchApprovalInstance
  - AddApprovalInstanceSign
  - UploadApprovalFile
  - SearchApprovalTask
  - GetApprovalUserTaskList
  - SearchApprovalCarbonCopy
  - CreateApprovalCarbonCopy
  - PreviewApprovalInstance
  - UpdateApprovalMessage
- Helpdesk
  - StartHelpdeskService
  - GetHelpdeskTicket
  - UpdateHelpdeskTicket
  - GetHelpdeskTicketList
  - DownloadHelpdeskTicketImage
  - AnswerHelpdeskTicketUserQuery
  - GetHelpdeskTicketMessageList
  - SendHelpdeskTicketMessage
  - GetHelpdeskTicketCustomizedFieldList
  - DeleteHelpdeskTicketCustomizedField
  - UpdateHelpdeskTicketCustomizedField
  - CreateHelpdeskTicketCustomizedField
  - GetHelpdeskTicketCustomizedField
  - CreateHelpdeskCategory
  - GetHelpdeskCategory
  - UpdateHelpdeskCategory
  - DeleteHelpdeskCategory
  - GetHelpdeskCategoryList
  - CreateHelpdeskFAQ
  - GetHelpdeskFAQ
  - UpdateHelpdeskFAQ
  - DeleteHelpdeskFAQ
  - GetHelpdeskFAQList
  - GetHelpdeskFAQImage
  - SearchHelpdeskFAQ
  - UpdateHelpdeskAgent
  - GetHelpdeskAgentEmail
  - CreateHelpdeskAgentSchedule
  - DeleteHelpdeskAgentSchedule
  - UpdateHelpdeskAgentSchedule
  - GetHelpdeskAgentSchedule
  - GetHelpdeskAgentScheduleList
  - CreateHelpdeskAgentSkill
  - GetHelpdeskAgentSkill
  - UpdateHelpdeskAgentSkill
  - DeleteHelpdeskAgentSkill
  - GetHelpdeskAgentSkillList
  - GetHelpdeskAgentSkillRuleList
  - SubscribeHelpdeskEvent
  - UnsubscribeHelpdeskEvent
- Admin
  - GetAdminDeptStats
  - GetAdminUserStats
- HumanAuth
  - GetFaceVerifyAuthResult
  - UploadFaceVerifyImage
  - CropFaceVerifyImage
  - CreateIdentity
- AI
  - RecognizeBasicImage
  - RecognizeSpeechStream
  - RecognizeSpeechFile
  - TranslateText
  - DetectTextLanguage
  - DetectFaceAttributes
- Attendance
  - DownloadAttendanceFile
  - UploadAttendanceFile
  - QueryAttendanceUserSettings
  - UpdateAttendanceUserSettings
  - CreateUpdateAttendanceGroup
  - DeleteAttendanceGroup
  - GetAttendanceGroup
  - CreateAttendanceShift
  - DeleteAttendanceShift
  - GetAttendanceShiftByID
  - GetAttendanceShiftByName
  - GetAttendanceStatisticsData
  - GetAttendanceStatisticsHeader
  - UpdateAttendanceUserStatisticsSettings
  - GetAttendanceUserStatisticsSettings
  - GetAttendanceUserDailyShift
  - GetAttendanceUserTask
  - GetAttendanceUserFlow
  - BatchGetAttendanceUserFlow
  - BatchCreateAttendanceUserFlow
  - GetAttendanceUserTaskRemedy
  - CreateUpdateAttendanceUserDailyShift
  - GetAttendanceUserApproval
  - CreateAttendanceUserApproval
  - GetAttendanceUserAllowedRemedy
  - InitAttendanceRemedyApproval
  - UpdateAttendanceRemedyApproval
- File
  - UploadImage
  - DownloadImage
  - UploadFile
  - DownloadFile
- OKR
  - GetOKRPeriodList
  - BatchGetOKR
  - GetUserOKRList
- EHR
  - GetEHREmployeeList
  - DownloadEHRAttachments
- Tenant
  - GetTenant
- Search
  - CreateSearchDataSourceItem
  - GetSearchDataSourceItem
  - DeleteSearchDataSourceItem
  - CreateSearchDataSource
  - GetSearchDataSource
  - UpdateSearchDataSource
  - GetSearchDataSourceList
  - DeleteSearchDataSource
- Hire
  - GetHireJob
  - GetHireJobManager
  - GetHireTalent
  - GetHireAttachment
  - GetHireAttachmentPreview
  - GetHireResumeSource
  - CreateHireNote
  - UpdateHireNote
  - GetHireNote
  - GetHireNoteList
  - GetHireReferralByApplication
  - GetHireJobProcessList
  - CreateHireApplication
  - TerminateHireApplication
  - GetHireApplication
  - GetHireApplicationList
  - GetHireApplicationInterviewList
  - GetHireOfferByApplication
  - GetHireOfferSchema
  - MakeHireTransferOnboardByApplication
  - UpdateHireEmployee
  - GetHireEmployeeByApplication
  - GetHireEmployee
- Task
  - CreateTaskCollaborator
  - GetTaskCollaboratorList
  - DeleteTaskCollaborator
  - CreateTaskFollower
  - GetTaskFollowerList
  - DeleteTaskFollower
  - CreateTaskReminder
  - GetTaskReminderList
  - DeleteTaskReminder
  - CreateTask
  - GetTask
  - DeleteTask
  - UpdateTask
  - CompleteTask
  - UncompleteTask
  - CreateTaskComment
  - GetTaskComment
  - DeleteTaskComment
  - UpdateTaskComment
- ACS
  - GetACSAccessRecordPhoto
  - GetACSAccessRecordList
  - GetACSDeviceList
  - GetACSUserFace
  - UpdateACSUserFace
  - GetACSUser
  - UpdateACSUser
  - GetACSUserList
- Ecosystem
  - GetEcosystemBindAwemeUser
- EventCallback
  - EventV2DriveFileTitleUpdatedV1
  - EventV2DriveFileReadV1
  - EventV2DriveFileEditV1
  - EventV1AppOpen
  - EventV1ShiftApproval
  - EventV1LeaveApprovalV2
  - EventV1OutApproval
  - EventV1WorkApproval
  - EventV2DriveFilePermissionMemberAddedV1
  - EventV2DriveFileTrashedV1
  - EventV2DriveFileDeletedV1
  - EventV2DriveFilePermissionMemberRemovedV1
  - EventV2ApprovalApprovalUpdatedV4
  - EventV1TripApproval
  - EventV1RemedyApproval
  - EventV2MeetingRoomMeetingRoomUpdatedV1
  - EventV2MeetingRoomMeetingRoomStatusChangedV1
  - EventV2MeetingRoomMeetingRoomDeletedV1
  - EventV2MeetingRoomMeetingRoomCreatedV1
  - EventV1OrderPaid
  - EventV1AppTicket
  - EventV1AppUninstalled
  - EventV1AppStatusChange
  - EventV2ApplicationApplicationVisibilityAddedV6
  - EventV2AttendanceUserTaskUpdatedV1
  - EventV2AttendanceUserFlowCreatedV1
  - EventV2AwemeEcosystemAwemeUserBindedAccountV1
  - EventV2TaskTaskUpdatedV1
  - EventV2TaskTaskCommentUpdatedV1
  - EventV2HelpdeskTicketMessageCreatedV1
  - EventV2HelpdeskTicketCreatedV1
  - EventV2HelpdeskTicketMessageUpdatedV1
  - EventV2ContactDepartmentCreatedV3
  - EventV2ContactDepartmentDeletedV3
  - EventV2ContactDepartmentUpdatedV3
  - EventV2ContactUserUpdatedV3
  - EventV2ContactUserCreatedV3
  - EventV2ContactUserDeletedV3
  - EventV2ContactScopeUpdatedV3
  - EventV2ContactEmployeeTypeEnumCreatedV3
  - EventV2ContactEmployeeTypeEnumActivedV3
  - EventV2ContactEmployeeTypeEnumDeactivatedV3
  - EventV2ContactEmployeeTypeEnumUpdatedV3
  - EventV2ContactEmployeeTypeEnumDeletedV3
  - EventV2IMMessageReceiveV1
  - EventV2IMMessageReadV1
  - EventV2IMChatDisbandedV1
  - EventV2IMChatUpdatedV1
  - EventV2IMChatMemberBotAddedV1
  - EventV2IMChatMemberBotDeletedV1
  - EventV2IMChatMemberUserAddedV1
  - EventV2IMChatMemberUserWithdrawnV1
  - EventV2IMChatMemberUserDeletedV1
  - EventV2VCMeetingMeetingStartedV1
  - EventV2VCMeetingMeetingEndedV1
  - EventV2VCMeetingJoinMeetingV1
  - EventV2VCMeetingLeaveMeetingV1
  - EventV2VCMeetingRecordingStartedV1
  - EventV2VCMeetingRecordingEndedV1
  - EventV2VCMeetingRecordingReadyV1
  - EventV2VCMeetingShareStartedV1
  - EventV2VCMeetingShareEndedV1
  - EventV2ACSAccessRecordCreatedV1
  - EventV2ACSUserUpdatedV1
  - EventV2CalendarCalendarACLCreatedV4
  - EventV2CalendarCalendarACLDeletedV4
  - EventV2CalendarCalendarEventChangedV4
  - EventV2CalendarCalendarChangedV4
  - EventV1AddBot
  - EventV1RemoveBot
  - EventV1P2PChatCreate
  - EventV1ReceiveMessage
  - EventV1AddUserToChat
  - EventV1RemoveUserFromChat
  - EventV1RevokeAddUserFromChat
  - EventV1ChatDisband
- AppLink
  - OpenLark
  - OpenMiniProgram
  - OpenWebApp
  - OpenChat
  - OpenCalender
  - OpenCalenderView
  - OpenCalenderEventCreate
  - OpenCalenderAccount
  - OpenDocs
  - OpenBot
  - OpenSSOLogin
  - OpenWebURL


</details>

## Usage


