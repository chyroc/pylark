import logging
import os
from unittest import TestCase

import attr

from pylark import Lark, logger

logger.setLevel(logging.DEBUG)


@attr.s
class App(object):
    app_id = attr.ib(default="")
    app_secret = attr.ib(default="")
    custom_url = attr.ib(default="")
    custom_secret = attr.ib(default="")

    def ins(self) -> Lark:
        return Lark(
            app_id=self.app_id,
            app_secret=self.app_secret,
        )

    def custom_bot(self) -> Lark:
        return Lark(
            custom_url=self.custom_url,
            custom_secret=self.custom_secret,
        )


# type Helpdesk struct {
# 	AppID     string
# 	AppSecret string
# 	ID        string
# 	Token     string
# }
#
# func (r *Helpdesk) Ins() *lark.Lark {
# 	return lark.New(
# 		lark.WithAppCredential(r.AppID, r.AppSecret),
# 		lark.WithHelpdeskCredential(r.ID, r.Token),
# 		lark.WithTimeout(time.Second*20),
# 	)
# }
#
# var HelpdeskAllPermission = Helpdesk{
# 	AppID:     os.Getenv("LARK_APP_ALL_PERMISSION_APP_ID"),
# 	AppSecret: os.Getenv("LARK_APP_ALL_PERMISSION_APP_SECRET"),
# 	ID:        os.Getenv("LARK_HELPDESK_ALL_PERMISSION_ID"),
# 	Token:     os.Getenv("LARK_HELPDESK_ALL_PERMISSION_TOKEN"),
# }


@attr.s
class User(object):
    user_id = attr.ib(default="")
    open_id = attr.ib(default="")
    name = attr.ib(default="")
    access_token = attr.ib(default=dict)
    refresh_token = attr.ib(default=dict)

    # def ins(self) -> Lark:
    #     return Lark(
    #         app_id=self.app_id,
    #         app_secret=self.app_secret,
    #     )
    #
    # def custom_bot(self) -> Lark:
    #     return Lark(
    #         custom_url=self.custom_url,
    #         custom_secret=self.custom_secret,
    #     )


# func (r User) OneAccessToken() string {
# 	for _, v := range r.AccessToken {
# 		return v
# 	}
# 	return ""
# }
#
# type Chat struct {
# 	ChatID string
# 	Name   string
# }

app_no_permission = App(
    app_id=os.getenv("LARK_APP_NO_PERMISSION_APP_ID"),
    app_secret=os.getenv("LARK_APP_NO_PERMISSION_APP_SECRET"),
)

app_all_permission = App(
    app_id=os.getenv("LARK_APP_ALL_PERMISSION_APP_ID"),
    app_secret=os.getenv("LARK_APP_ALL_PERMISSION_APP_SECRET"),
)

# var AppCustomBotNoValid = App{
# 	CustomURL: os.Getenv("LARK_APP_CUSTOM_BOT_NO_VALID_WEBHOOK_URL"),
# }
#
# var AppCustomBotCheckCanSendWord = App{
# 	CustomURL: os.Getenv("LARK_APP_CUSTOM_BOT_CHECK_CAN_SEND_WEBHOOK_URL"),
# }
#
# var AppCustomBotCheckSign = App{
# 	CustomURL:    os.Getenv("LARK_APP_CUSTOM_BOT_CHECK_SIGN_WEBHOOK_URL"),
# 	CustomSecret: os.Getenv("LARK_APP_CUSTOM_BOT_CHECK_SIGN_SIGN"),
# }

user_admin = User(
    user_id=os.getenv("LARK_USER_ADMIN_USER_ID"),
    open_id=os.getenv("LARK_USER_ADMIN_OPEN_ID"),
    name=os.getenv("LARK_USER_ADMIN_NAME"),
    access_token={
        os.getenv("LARK_APP_ALL_PERMISSION_APP_ID"): os.getenv(
            "LARK_ACCESS_TOKEN_ALL_PERMISSION_APP"
        ),
    },
    refresh_token={
        os.getenv("LARK_APP_ALL_PERMISSION_APP_ID"): os.getenv(
            "LARK_REFRESH_TOKEN_ALL_PERMISSION_APP"
        )
    },
)


# // 这个群公共，必须设置「群公共」三个字
# var ChatContainALLPermissionApp = Chat{
# 	ChatID: os.Getenv("LARK_CHAT_CONTAINS_APP_PERMISSION_APP_CHAT_ID"),
# 	Name:   "包含「lark-sdk」的群",
# }
#
# var ChatNotContainALLPermissionApp = Chat{
# 	ChatID: os.Getenv("LARK_CHAT_NOT_CONTAINS_APP_PERMISSION_APP_CHAT_ID"),
# 	Name:   "不包含「lark-sdk」的群",
# }
#
# var ChatForSendMessage = Chat{
# 	ChatID: os.Getenv("LARK_CHAT_FOR_SEND_MSG_CHAT_ID"),
# 	Name:   "for-send-message",
# }
#
# type File struct {
# 	Key string
# }
#
# var File1 = File{
# 	Key: os.Getenv("LARK_FILE_KEY_TEST_FILE_1_PNG"), // this is file of ./test/file_1.png
# }
#
# var File2 = File{
# 	Key: os.Getenv("LARK_FILE_KEY_TEST_FILE_2_DOC"), // ./test/file_2.docx
# }
#
# type Message struct {
# 	MessageID string
# 	ChatID    string
# }
#
# var MessageAdminSendTextInChatContainAllPermissionApp = Message{
# 	MessageID: os.Getenv("LARK_MESSAGE_ADMIN_SEND_TEST_IN_CHAT_CONTAINS_ALL_PERMISSION_APP"),
# 	ChatID:    os.Getenv("LARK_CHAT_CONTAINS_APP_PERMISSION_APP_CHAT_ID"),
# }
#
# var MessageAdminSendImageInChatContainAllPermissionApp = Message{
# 	MessageID: os.Getenv("LARK_MESSAGE_ADMIN_SEND_IMAGE_IN_CHAT_CONTAINS_ALL_PERMISSION_APP"),
# 	ChatID:    os.Getenv("LARK_CHAT_CONTAINS_APP_PERMISSION_APP_CHAT_ID"),
# }
#
# var MessageAllPermissionAppSendTextInChatContainAllPermissionApp = Message{
# 	MessageID: os.Getenv("LARK_MESSAGE_ALL_PERMISSION_APP_SEND_TEXT_IN_CHAT_CONTAINS_ALL_PERMISSION_APP"),
# 	ChatID:    os.Getenv("LARK_CHAT_CONTAINS_APP_PERMISSION_APP_CHAT_ID"),
# }
#
# type Approval struct {
# 	Code string `json:"code"`
# }
#
# var ApprovalALLField = Approval{
# 	Code: os.Getenv("LARK_APPROVAL_ALL_FIELD"),
# }


class TestConfig(TestCase):
    def test_config(self):
        assert app_no_permission.app_id
        assert app_no_permission.app_secret

        assert app_all_permission.app_id
        assert app_all_permission.app_secret


# 	as.NotEmpty(UserAdmin.UserID)
# 	as.NotEmpty(UserAdmin.OpenID)
# 	as.NotEmpty(ChatContainALLPermissionApp.ChatID)
# 	as.NotEmpty(ChatNotContainALLPermissionApp.ChatID)
# 	as.NotEmpty(ChatForSendMessage.ChatID)
# 	as.NotEmpty(File1.Key)
# 	as.NotEmpty(File2.Key)
# 	as.NotEmpty(MessageAdminSendTextInChatContainAllPermissionApp.ChatID)
# 	as.NotEmpty(MessageAdminSendTextInChatContainAllPermissionApp.MessageID)
# 	as.NotEmpty(MessageAdminSendImageInChatContainAllPermissionApp.ChatID)
# 	as.NotEmpty(MessageAdminSendImageInChatContainAllPermissionApp.MessageID)
# 	as.NotEmpty(MessageAllPermissionAppSendTextInChatContainAllPermissionApp.ChatID)
# 	as.NotEmpty(MessageAllPermissionAppSendTextInChatContainAllPermissionApp.MessageID)
# }
