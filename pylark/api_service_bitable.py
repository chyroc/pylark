# Code generated by lark_sdk_gen. DO NOT EDIT.

import typing
from pylark.lark_request import Response
from pylark.api_service_bitable_view_list import (
    GetBitableViewListReq,
    GetBitableViewListResp,
    _gen_get_bitable_view_list_req,
)
from pylark.api_service_bitable_view_create import (
    CreateBitableViewReq,
    CreateBitableViewResp,
    _gen_create_bitable_view_req,
)
from pylark.api_service_bitable_view_delete import (
    DeleteBitableViewReq,
    DeleteBitableViewResp,
    _gen_delete_bitable_view_req,
)
from pylark.api_service_bitable_record_list import (
    GetBitableRecordListReq,
    GetBitableRecordListResp,
    _gen_get_bitable_record_list_req,
)
from pylark.api_service_bitable_record_get import (
    GetBitableRecordReq,
    GetBitableRecordResp,
    _gen_get_bitable_record_req,
)
from pylark.api_service_bitable_record_create import (
    CreateBitableRecordReq,
    CreateBitableRecordResp,
    _gen_create_bitable_record_req,
)
from pylark.api_service_bitable_record_batch_create import (
    BatchCreateBitableRecordReq,
    BatchCreateBitableRecordResp,
    _gen_batch_create_bitable_record_req,
)
from pylark.api_service_bitable_record_update import (
    UpdateBitableRecordReq,
    UpdateBitableRecordResp,
    _gen_update_bitable_record_req,
)
from pylark.api_service_bitable_record_batch_update import (
    BatchUpdateBitableRecordReq,
    BatchUpdateBitableRecordResp,
    _gen_batch_update_bitable_record_req,
)
from pylark.api_service_bitable_record_delete import (
    DeleteBitableRecordReq,
    DeleteBitableRecordResp,
    _gen_delete_bitable_record_req,
)
from pylark.api_service_bitable_record_batch_delete import (
    BatchDeleteBitableRecordReq,
    BatchDeleteBitableRecordResp,
    _gen_batch_delete_bitable_record_req,
)
from pylark.api_service_bitable_field_list import (
    GetBitableFieldListReq,
    GetBitableFieldListResp,
    _gen_get_bitable_field_list_req,
)
from pylark.api_service_bitable_field_create import (
    CreateBitableFieldReq,
    CreateBitableFieldResp,
    _gen_create_bitable_field_req,
)
from pylark.api_service_bitable_field_update import (
    UpdateBitableFieldReq,
    UpdateBitableFieldResp,
    _gen_update_bitable_field_req,
)
from pylark.api_service_bitable_field_delete import (
    DeleteBitableFieldReq,
    DeleteBitableFieldResp,
    _gen_delete_bitable_field_req,
)
from pylark.api_service_bitable_table_list import (
    GetBitableTableListReq,
    GetBitableTableListResp,
    _gen_get_bitable_table_list_req,
)
from pylark.api_service_bitable_table_create import (
    CreateBitableTableReq,
    CreateBitableTableResp,
    _gen_create_bitable_table_req,
)
from pylark.api_service_bitable_table_batch_create import (
    BatchCreateBitableTableReq,
    BatchCreateBitableTableResp,
    _gen_batch_create_bitable_table_req,
)
from pylark.api_service_bitable_table_delete import (
    DeleteBitableTableReq,
    DeleteBitableTableResp,
    _gen_delete_bitable_table_req,
)
from pylark.api_service_bitable_table_batch_delete import (
    BatchDeleteBitableTableReq,
    BatchDeleteBitableTableResp,
    _gen_batch_delete_bitable_table_req,
)
from pylark.api_service_bitable_meta_get import (
    GetBitableMetaReq,
    GetBitableMetaResp,
    _gen_get_bitable_meta_req,
)


if typing.TYPE_CHECKING:
    from lark import Lark


class LarkBitableService(object):
    cli: "Lark"

    def __init__(self, cli: "Lark"):
        self.cli = cli

    def get_bitable_view_list(
        self, request: GetBitableViewListReq, options: typing.List[str] = None
    ) -> typing.Tuple[GetBitableViewListResp, Response]:
        return self.cli.raw_request(_gen_get_bitable_view_list_req(request, options))

    def create_bitable_view(
        self, request: CreateBitableViewReq, options: typing.List[str] = None
    ) -> typing.Tuple[CreateBitableViewResp, Response]:
        return self.cli.raw_request(_gen_create_bitable_view_req(request, options))

    def delete_bitable_view(
        self, request: DeleteBitableViewReq, options: typing.List[str] = None
    ) -> typing.Tuple[DeleteBitableViewResp, Response]:
        return self.cli.raw_request(_gen_delete_bitable_view_req(request, options))

    def get_bitable_record_list(
        self, request: GetBitableRecordListReq, options: typing.List[str] = None
    ) -> typing.Tuple[GetBitableRecordListResp, Response]:
        return self.cli.raw_request(_gen_get_bitable_record_list_req(request, options))

    def get_bitable_record(
        self, request: GetBitableRecordReq, options: typing.List[str] = None
    ) -> typing.Tuple[GetBitableRecordResp, Response]:
        return self.cli.raw_request(_gen_get_bitable_record_req(request, options))

    def create_bitable_record(
        self, request: CreateBitableRecordReq, options: typing.List[str] = None
    ) -> typing.Tuple[CreateBitableRecordResp, Response]:
        return self.cli.raw_request(_gen_create_bitable_record_req(request, options))

    def batch_create_bitable_record(
        self, request: BatchCreateBitableRecordReq, options: typing.List[str] = None
    ) -> typing.Tuple[BatchCreateBitableRecordResp, Response]:
        return self.cli.raw_request(
            _gen_batch_create_bitable_record_req(request, options)
        )

    def update_bitable_record(
        self, request: UpdateBitableRecordReq, options: typing.List[str] = None
    ) -> typing.Tuple[UpdateBitableRecordResp, Response]:
        return self.cli.raw_request(_gen_update_bitable_record_req(request, options))

    def batch_update_bitable_record(
        self, request: BatchUpdateBitableRecordReq, options: typing.List[str] = None
    ) -> typing.Tuple[BatchUpdateBitableRecordResp, Response]:
        return self.cli.raw_request(
            _gen_batch_update_bitable_record_req(request, options)
        )

    def delete_bitable_record(
        self, request: DeleteBitableRecordReq, options: typing.List[str] = None
    ) -> typing.Tuple[DeleteBitableRecordResp, Response]:
        return self.cli.raw_request(_gen_delete_bitable_record_req(request, options))

    def batch_delete_bitable_record(
        self, request: BatchDeleteBitableRecordReq, options: typing.List[str] = None
    ) -> typing.Tuple[BatchDeleteBitableRecordResp, Response]:
        return self.cli.raw_request(
            _gen_batch_delete_bitable_record_req(request, options)
        )

    def get_bitable_field_list(
        self, request: GetBitableFieldListReq, options: typing.List[str] = None
    ) -> typing.Tuple[GetBitableFieldListResp, Response]:
        return self.cli.raw_request(_gen_get_bitable_field_list_req(request, options))

    def create_bitable_field(
        self, request: CreateBitableFieldReq, options: typing.List[str] = None
    ) -> typing.Tuple[CreateBitableFieldResp, Response]:
        return self.cli.raw_request(_gen_create_bitable_field_req(request, options))

    def update_bitable_field(
        self, request: UpdateBitableFieldReq, options: typing.List[str] = None
    ) -> typing.Tuple[UpdateBitableFieldResp, Response]:
        return self.cli.raw_request(_gen_update_bitable_field_req(request, options))

    def delete_bitable_field(
        self, request: DeleteBitableFieldReq, options: typing.List[str] = None
    ) -> typing.Tuple[DeleteBitableFieldResp, Response]:
        return self.cli.raw_request(_gen_delete_bitable_field_req(request, options))

    def get_bitable_table_list(
        self, request: GetBitableTableListReq, options: typing.List[str] = None
    ) -> typing.Tuple[GetBitableTableListResp, Response]:
        return self.cli.raw_request(_gen_get_bitable_table_list_req(request, options))

    def create_bitable_table(
        self, request: CreateBitableTableReq, options: typing.List[str] = None
    ) -> typing.Tuple[CreateBitableTableResp, Response]:
        return self.cli.raw_request(_gen_create_bitable_table_req(request, options))

    def batch_create_bitable_table(
        self, request: BatchCreateBitableTableReq, options: typing.List[str] = None
    ) -> typing.Tuple[BatchCreateBitableTableResp, Response]:
        return self.cli.raw_request(
            _gen_batch_create_bitable_table_req(request, options)
        )

    def delete_bitable_table(
        self, request: DeleteBitableTableReq, options: typing.List[str] = None
    ) -> typing.Tuple[DeleteBitableTableResp, Response]:
        return self.cli.raw_request(_gen_delete_bitable_table_req(request, options))

    def batch_delete_bitable_table(
        self, request: BatchDeleteBitableTableReq, options: typing.List[str] = None
    ) -> typing.Tuple[BatchDeleteBitableTableResp, Response]:
        return self.cli.raw_request(
            _gen_batch_delete_bitable_table_req(request, options)
        )

    def get_bitable_meta(
        self, request: GetBitableMetaReq, options: typing.List[str] = None
    ) -> typing.Tuple[GetBitableMetaResp, Response]:
        return self.cli.raw_request(_gen_get_bitable_meta_req(request, options))