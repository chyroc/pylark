# Code generated by lark_sdk_gen. DO NOT EDIT.

import unittest
import pylark
import pytest
from tests.test_conf import app_all_permission, app_no_permission
from tests.test_helper import mock_get_tenant_access_token_failed


def mock(*args, **kwargs):
    raise pylark.PyLarkError(scope="scope", func="func", code=1, msg="mock-failed")


def mock_raw_request(*args, **kwargs):
    raise pylark.PyLarkError(
        scope="scope", func="func", code=1, msg="mock-raw-request-failed"
    )


# mock get token
class TestHelpdeskSampleMockGetTokenFailed(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestHelpdeskSampleMockGetTokenFailed, self).__init__(*args, **kwargs)
        self.cli = app_all_permission.ins()
        self.cli.auth.get_tenant_access_token = mock_get_tenant_access_token_failed
        self.cli.auth.get_app_access_token = mock_get_tenant_access_token_failed
        self.module_cli = self.cli.helpdesk

    def test_mock_get_token_start_helpdesk_service(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.start_helpdesk_service(pylark.StartHelpdeskServiceReq())

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_get_helpdesk_ticket(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_ticket(pylark.GetHelpdeskTicketReq())

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_get_helpdesk_ticket_list(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_ticket_list(pylark.GetHelpdeskTicketListReq())

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_download_helpdesk_ticket_image(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.download_helpdesk_ticket_image(
                pylark.DownloadHelpdeskTicketImageReq()
            )

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_answer_helpdesk_ticket_user_query(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.answer_helpdesk_ticket_user_query(
                pylark.AnswerHelpdeskTicketUserQueryReq()
            )

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_get_helpdesk_ticket_message_list(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_ticket_message_list(
                pylark.GetHelpdeskTicketMessageListReq()
            )

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_send_helpdesk_ticket_message(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.send_helpdesk_ticket_message(
                pylark.SendHelpdeskTicketMessageReq()
            )

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_get_helpdesk_ticket_customized_field_list(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_ticket_customized_field_list(
                pylark.GetHelpdeskTicketCustomizedFieldListReq()
            )

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_get_helpdesk_ticket_customized_field(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_ticket_customized_field(
                pylark.GetHelpdeskTicketCustomizedFieldReq()
            )

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_get_helpdesk_category(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_category(pylark.GetHelpdeskCategoryReq())

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_get_helpdesk_category_list(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_category_list(
                pylark.GetHelpdeskCategoryListReq()
            )

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_get_helpdesk_faq(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_faq(pylark.GetHelpdeskFAQReq())

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_get_helpdesk_faq_list(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_faq_list(pylark.GetHelpdeskFAQListReq())

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_get_helpdesk_faq_image(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_faq_image(pylark.GetHelpdeskFAQImageReq())

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_search_helpdesk_faq(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.search_helpdesk_faq(pylark.SearchHelpdeskFAQReq())

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_get_helpdesk_agent_email(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_agent_email(pylark.GetHelpdeskAgentEmailReq())

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_get_helpdesk_agent_schedule(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_agent_schedule(
                pylark.GetHelpdeskAgentScheduleReq()
            )

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_get_helpdesk_agent_schedule_list(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_agent_schedule_list(
                pylark.GetHelpdeskAgentScheduleListReq()
            )

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_get_helpdesk_agent_skill(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_agent_skill(pylark.GetHelpdeskAgentSkillReq())

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_get_helpdesk_agent_skill_list(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_agent_skill_list(
                pylark.GetHelpdeskAgentSkillListReq()
            )

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_get_helpdesk_agent_skill_rule_list(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_agent_skill_rule_list(
                pylark.GetHelpdeskAgentSkillRuleListReq()
            )

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_subscribe_helpdesk_event(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.subscribe_helpdesk_event(pylark.SubscribeHelpdeskEventReq())

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_unsubscribe_helpdesk_event(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.unsubscribe_helpdesk_event(
                pylark.UnsubscribeHelpdeskEventReq()
            )

        assert "msg=failed" in f"{e}"


# mock mock self func
class TestHelpdeskSampleMockSelfFuncFailed(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestHelpdeskSampleMockSelfFuncFailed, self).__init__(*args, **kwargs)
        self.cli = app_all_permission.ins()
        self.module_cli = self.cli.helpdesk

    def test_mock_self_func_start_helpdesk_service(self):
        origin_func = self.module_cli.start_helpdesk_service
        self.module_cli.start_helpdesk_service = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.start_helpdesk_service(pylark.StartHelpdeskServiceReq())

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.start_helpdesk_service = origin_func

    def test_mock_self_func_get_helpdesk_ticket(self):
        origin_func = self.module_cli.get_helpdesk_ticket
        self.module_cli.get_helpdesk_ticket = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_ticket(pylark.GetHelpdeskTicketReq())

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.get_helpdesk_ticket = origin_func

    def test_mock_self_func_get_helpdesk_ticket_list(self):
        origin_func = self.module_cli.get_helpdesk_ticket_list
        self.module_cli.get_helpdesk_ticket_list = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_ticket_list(pylark.GetHelpdeskTicketListReq())

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.get_helpdesk_ticket_list = origin_func

    def test_mock_self_func_download_helpdesk_ticket_image(self):
        origin_func = self.module_cli.download_helpdesk_ticket_image
        self.module_cli.download_helpdesk_ticket_image = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.download_helpdesk_ticket_image(
                pylark.DownloadHelpdeskTicketImageReq()
            )

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.download_helpdesk_ticket_image = origin_func

    def test_mock_self_func_answer_helpdesk_ticket_user_query(self):
        origin_func = self.module_cli.answer_helpdesk_ticket_user_query
        self.module_cli.answer_helpdesk_ticket_user_query = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.answer_helpdesk_ticket_user_query(
                pylark.AnswerHelpdeskTicketUserQueryReq()
            )

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.answer_helpdesk_ticket_user_query = origin_func

    def test_mock_self_func_get_helpdesk_ticket_message_list(self):
        origin_func = self.module_cli.get_helpdesk_ticket_message_list
        self.module_cli.get_helpdesk_ticket_message_list = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_ticket_message_list(
                pylark.GetHelpdeskTicketMessageListReq()
            )

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.get_helpdesk_ticket_message_list = origin_func

    def test_mock_self_func_send_helpdesk_ticket_message(self):
        origin_func = self.module_cli.send_helpdesk_ticket_message
        self.module_cli.send_helpdesk_ticket_message = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.send_helpdesk_ticket_message(
                pylark.SendHelpdeskTicketMessageReq()
            )

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.send_helpdesk_ticket_message = origin_func

    def test_mock_self_func_get_helpdesk_ticket_customized_field_list(self):
        origin_func = self.module_cli.get_helpdesk_ticket_customized_field_list
        self.module_cli.get_helpdesk_ticket_customized_field_list = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_ticket_customized_field_list(
                pylark.GetHelpdeskTicketCustomizedFieldListReq()
            )

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.get_helpdesk_ticket_customized_field_list = origin_func

    def test_mock_self_func_get_helpdesk_ticket_customized_field(self):
        origin_func = self.module_cli.get_helpdesk_ticket_customized_field
        self.module_cli.get_helpdesk_ticket_customized_field = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_ticket_customized_field(
                pylark.GetHelpdeskTicketCustomizedFieldReq()
            )

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.get_helpdesk_ticket_customized_field = origin_func

    def test_mock_self_func_get_helpdesk_category(self):
        origin_func = self.module_cli.get_helpdesk_category
        self.module_cli.get_helpdesk_category = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_category(pylark.GetHelpdeskCategoryReq())

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.get_helpdesk_category = origin_func

    def test_mock_self_func_get_helpdesk_category_list(self):
        origin_func = self.module_cli.get_helpdesk_category_list
        self.module_cli.get_helpdesk_category_list = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_category_list(
                pylark.GetHelpdeskCategoryListReq()
            )

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.get_helpdesk_category_list = origin_func

    def test_mock_self_func_get_helpdesk_faq(self):
        origin_func = self.module_cli.get_helpdesk_faq
        self.module_cli.get_helpdesk_faq = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_faq(pylark.GetHelpdeskFAQReq())

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.get_helpdesk_faq = origin_func

    def test_mock_self_func_get_helpdesk_faq_list(self):
        origin_func = self.module_cli.get_helpdesk_faq_list
        self.module_cli.get_helpdesk_faq_list = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_faq_list(pylark.GetHelpdeskFAQListReq())

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.get_helpdesk_faq_list = origin_func

    def test_mock_self_func_get_helpdesk_faq_image(self):
        origin_func = self.module_cli.get_helpdesk_faq_image
        self.module_cli.get_helpdesk_faq_image = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_faq_image(pylark.GetHelpdeskFAQImageReq())

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.get_helpdesk_faq_image = origin_func

    def test_mock_self_func_search_helpdesk_faq(self):
        origin_func = self.module_cli.search_helpdesk_faq
        self.module_cli.search_helpdesk_faq = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.search_helpdesk_faq(pylark.SearchHelpdeskFAQReq())

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.search_helpdesk_faq = origin_func

    def test_mock_self_func_get_helpdesk_agent_email(self):
        origin_func = self.module_cli.get_helpdesk_agent_email
        self.module_cli.get_helpdesk_agent_email = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_agent_email(pylark.GetHelpdeskAgentEmailReq())

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.get_helpdesk_agent_email = origin_func

    def test_mock_self_func_get_helpdesk_agent_schedule(self):
        origin_func = self.module_cli.get_helpdesk_agent_schedule
        self.module_cli.get_helpdesk_agent_schedule = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_agent_schedule(
                pylark.GetHelpdeskAgentScheduleReq()
            )

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.get_helpdesk_agent_schedule = origin_func

    def test_mock_self_func_get_helpdesk_agent_schedule_list(self):
        origin_func = self.module_cli.get_helpdesk_agent_schedule_list
        self.module_cli.get_helpdesk_agent_schedule_list = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_agent_schedule_list(
                pylark.GetHelpdeskAgentScheduleListReq()
            )

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.get_helpdesk_agent_schedule_list = origin_func

    def test_mock_self_func_get_helpdesk_agent_skill(self):
        origin_func = self.module_cli.get_helpdesk_agent_skill
        self.module_cli.get_helpdesk_agent_skill = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_agent_skill(pylark.GetHelpdeskAgentSkillReq())

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.get_helpdesk_agent_skill = origin_func

    def test_mock_self_func_get_helpdesk_agent_skill_list(self):
        origin_func = self.module_cli.get_helpdesk_agent_skill_list
        self.module_cli.get_helpdesk_agent_skill_list = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_agent_skill_list(
                pylark.GetHelpdeskAgentSkillListReq()
            )

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.get_helpdesk_agent_skill_list = origin_func

    def test_mock_self_func_get_helpdesk_agent_skill_rule_list(self):
        origin_func = self.module_cli.get_helpdesk_agent_skill_rule_list
        self.module_cli.get_helpdesk_agent_skill_rule_list = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_agent_skill_rule_list(
                pylark.GetHelpdeskAgentSkillRuleListReq()
            )

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.get_helpdesk_agent_skill_rule_list = origin_func

    def test_mock_self_func_subscribe_helpdesk_event(self):
        origin_func = self.module_cli.subscribe_helpdesk_event
        self.module_cli.subscribe_helpdesk_event = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.subscribe_helpdesk_event(pylark.SubscribeHelpdeskEventReq())

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.subscribe_helpdesk_event = origin_func

    def test_mock_self_func_unsubscribe_helpdesk_event(self):
        origin_func = self.module_cli.unsubscribe_helpdesk_event
        self.module_cli.unsubscribe_helpdesk_event = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.unsubscribe_helpdesk_event(
                pylark.UnsubscribeHelpdeskEventReq()
            )

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.unsubscribe_helpdesk_event = origin_func


# mock raw request
class TestHelpdeskSampleMockRawRequestFailed(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestHelpdeskSampleMockRawRequestFailed, self).__init__(*args, **kwargs)
        self.cli = app_all_permission.ins()
        self.module_cli = self.cli.helpdesk
        self.cli.raw_request = mock_raw_request

    def test_mock_raw_request_start_helpdesk_service(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.start_helpdesk_service(pylark.StartHelpdeskServiceReq())

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_get_helpdesk_ticket(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_ticket(
                pylark.GetHelpdeskTicketReq(
                    ticket_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_get_helpdesk_ticket_list(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_ticket_list(pylark.GetHelpdeskTicketListReq())

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_download_helpdesk_ticket_image(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.download_helpdesk_ticket_image(
                pylark.DownloadHelpdeskTicketImageReq()
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_answer_helpdesk_ticket_user_query(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.answer_helpdesk_ticket_user_query(
                pylark.AnswerHelpdeskTicketUserQueryReq(
                    ticket_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_get_helpdesk_ticket_message_list(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_ticket_message_list(
                pylark.GetHelpdeskTicketMessageListReq(
                    ticket_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_send_helpdesk_ticket_message(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.send_helpdesk_ticket_message(
                pylark.SendHelpdeskTicketMessageReq(
                    ticket_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_get_helpdesk_ticket_customized_field_list(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_ticket_customized_field_list(
                pylark.GetHelpdeskTicketCustomizedFieldListReq()
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_get_helpdesk_ticket_customized_field(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_ticket_customized_field(
                pylark.GetHelpdeskTicketCustomizedFieldReq(
                    ticket_customized_field_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_get_helpdesk_category(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_category(
                pylark.GetHelpdeskCategoryReq(
                    id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_get_helpdesk_category_list(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_category_list(
                pylark.GetHelpdeskCategoryListReq()
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_get_helpdesk_faq(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_faq(
                pylark.GetHelpdeskFAQReq(
                    id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_get_helpdesk_faq_list(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_faq_list(pylark.GetHelpdeskFAQListReq())

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_get_helpdesk_faq_image(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_faq_image(
                pylark.GetHelpdeskFAQImageReq(
                    id="x",
                    image_key="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_search_helpdesk_faq(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.search_helpdesk_faq(pylark.SearchHelpdeskFAQReq())

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_get_helpdesk_agent_email(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_agent_email(pylark.GetHelpdeskAgentEmailReq())

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_get_helpdesk_agent_schedule(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_agent_schedule(
                pylark.GetHelpdeskAgentScheduleReq(
                    agent_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_get_helpdesk_agent_schedule_list(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_agent_schedule_list(
                pylark.GetHelpdeskAgentScheduleListReq()
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_get_helpdesk_agent_skill(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_agent_skill(
                pylark.GetHelpdeskAgentSkillReq(
                    agent_skill_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_get_helpdesk_agent_skill_list(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_agent_skill_list(
                pylark.GetHelpdeskAgentSkillListReq()
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_get_helpdesk_agent_skill_rule_list(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_agent_skill_rule_list(
                pylark.GetHelpdeskAgentSkillRuleListReq()
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_subscribe_helpdesk_event(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.subscribe_helpdesk_event(pylark.SubscribeHelpdeskEventReq())

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_unsubscribe_helpdesk_event(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.unsubscribe_helpdesk_event(
                pylark.UnsubscribeHelpdeskEventReq()
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg


# real request
class TestHelpdeskSampleRealRequestFailed(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestHelpdeskSampleRealRequestFailed, self).__init__(*args, **kwargs)
        self.cli = app_no_permission.ins()
        self.module_cli = self.cli.helpdesk

    def test_real_request_start_helpdesk_service(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.start_helpdesk_service(pylark.StartHelpdeskServiceReq())

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_get_helpdesk_ticket(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_ticket(
                pylark.GetHelpdeskTicketReq(
                    ticket_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_get_helpdesk_ticket_list(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_ticket_list(pylark.GetHelpdeskTicketListReq())

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_download_helpdesk_ticket_image(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.download_helpdesk_ticket_image(
                pylark.DownloadHelpdeskTicketImageReq()
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_answer_helpdesk_ticket_user_query(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.answer_helpdesk_ticket_user_query(
                pylark.AnswerHelpdeskTicketUserQueryReq(
                    ticket_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_get_helpdesk_ticket_message_list(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_ticket_message_list(
                pylark.GetHelpdeskTicketMessageListReq(
                    ticket_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_send_helpdesk_ticket_message(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.send_helpdesk_ticket_message(
                pylark.SendHelpdeskTicketMessageReq(
                    ticket_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_get_helpdesk_ticket_customized_field_list(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_ticket_customized_field_list(
                pylark.GetHelpdeskTicketCustomizedFieldListReq()
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_get_helpdesk_ticket_customized_field(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_ticket_customized_field(
                pylark.GetHelpdeskTicketCustomizedFieldReq(
                    ticket_customized_field_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_get_helpdesk_category(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_category(
                pylark.GetHelpdeskCategoryReq(
                    id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_get_helpdesk_category_list(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_category_list(
                pylark.GetHelpdeskCategoryListReq()
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_get_helpdesk_faq(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_faq(
                pylark.GetHelpdeskFAQReq(
                    id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_get_helpdesk_faq_list(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_faq_list(pylark.GetHelpdeskFAQListReq())

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_get_helpdesk_faq_image(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_faq_image(
                pylark.GetHelpdeskFAQImageReq(
                    id="x",
                    image_key="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_search_helpdesk_faq(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.search_helpdesk_faq(pylark.SearchHelpdeskFAQReq())

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_get_helpdesk_agent_email(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_agent_email(pylark.GetHelpdeskAgentEmailReq())

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_get_helpdesk_agent_schedule(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_agent_schedule(
                pylark.GetHelpdeskAgentScheduleReq(
                    agent_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_get_helpdesk_agent_schedule_list(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_agent_schedule_list(
                pylark.GetHelpdeskAgentScheduleListReq()
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_get_helpdesk_agent_skill(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_agent_skill(
                pylark.GetHelpdeskAgentSkillReq(
                    agent_skill_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_get_helpdesk_agent_skill_list(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_agent_skill_list(
                pylark.GetHelpdeskAgentSkillListReq()
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_get_helpdesk_agent_skill_rule_list(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_helpdesk_agent_skill_rule_list(
                pylark.GetHelpdeskAgentSkillRuleListReq()
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_subscribe_helpdesk_event(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.subscribe_helpdesk_event(pylark.SubscribeHelpdeskEventReq())

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_unsubscribe_helpdesk_event(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.unsubscribe_helpdesk_event(
                pylark.UnsubscribeHelpdeskEventReq()
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
