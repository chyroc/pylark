# import logging
# from dataclasses import dataclass, field
# import pytest
# from pylark.api_service_auth_app_ticket_resend import ResendAppTicketReq
# from pylark.lark import Lark
# from pylark.lark_request import Request, RawRequestReq
# from urllib.parse import urlparse, parse_qsl, parse_qs, urlencode, urlunparse
# from requests.models import PreparedRequest
#
#
# def f(msg: str, *args):
#     logging.getLogger("test").error(msg, *args)
#
#
# @dataclass
# class SomeReq(object):
#     a: str = field(metadata={"req_type": "json"})
#     b: str = field(metadata={"req_type": "query"})
#     c: str = field(metadata={"req_type": "path"})
#
#
# class TestRequest(unittest.TestCase):
#     def test_url(self):
#         # prepared_request = PreparedRequest()
#         # prepared_request.prepare_url('https://docs.python.org/3?a=b', {})
#         # print(prepared_request.url)
#         # prepared_request.prepare_body()
#         pass
#
#     # q = dict(parse_qsl(r.query))
#     # print(r)
#     # print(q)
#     # q.update({'c': 'd'})
#     # r.query = urlencode(q)
#     # print(urlunparse(r))
#
#     def test_parse_request(self):
#         body = SomeReq(a="a", b="b", c="c")
#         req_ins = Request()
#         res = req_ins._parse_request_param(
#             RawRequestReq(
#                 url="https://a.com/:c/id",
#                 body=body,
#             )
#         )
#
#         assert res["query"]
#         assert "b" == res["query"]["b"]
#         assert "https://a.com/c/id" == res["url"]
#         print(res)
