# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/automl_v1/proto/operations.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.cloud.automl_v1.proto import (
    dataset_pb2 as google_dot_cloud_dot_automl__v1_dot_proto_dot_dataset__pb2,
)
from google.cloud.automl_v1.proto import (
    io_pb2 as google_dot_cloud_dot_automl__v1_dot_proto_dot_io__pb2,
)
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/automl_v1/proto/operations.proto",
    package="google.cloud.automl.v1",
    syntax="proto3",
    serialized_options=b"\n\032com.google.cloud.automl.v1P\001Z<google.golang.org/genproto/googleapis/cloud/automl/v1;automl\252\002\026Google.Cloud.AutoML.V1\312\002\026Google\\Cloud\\AutoMl\\V1\352\002\031Google::Cloud::AutoML::V1",
    serialized_pb=b'\n-google/cloud/automl_v1/proto/operations.proto\x12\x16google.cloud.automl.v1\x1a*google/cloud/automl_v1/proto/dataset.proto\x1a%google/cloud/automl_v1/proto/io.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto\x1a\x1cgoogle/api/annotations.proto"\xc9\x07\n\x11OperationMetadata\x12I\n\x0e\x64\x65lete_details\x18\x08 \x01(\x0b\x32/.google.cloud.automl.v1.DeleteOperationMetadataH\x00\x12T\n\x14\x64\x65ploy_model_details\x18\x18 \x01(\x0b\x32\x34.google.cloud.automl.v1.DeployModelOperationMetadataH\x00\x12X\n\x16undeploy_model_details\x18\x19 \x01(\x0b\x32\x36.google.cloud.automl.v1.UndeployModelOperationMetadataH\x00\x12T\n\x14\x63reate_model_details\x18\n \x01(\x0b\x32\x34.google.cloud.automl.v1.CreateModelOperationMetadataH\x00\x12X\n\x16\x63reate_dataset_details\x18\x1e \x01(\x0b\x32\x36.google.cloud.automl.v1.CreateDatasetOperationMetadataH\x00\x12R\n\x13import_data_details\x18\x0f \x01(\x0b\x32\x33.google.cloud.automl.v1.ImportDataOperationMetadataH\x00\x12V\n\x15\x62\x61tch_predict_details\x18\x10 \x01(\x0b\x32\x35.google.cloud.automl.v1.BatchPredictOperationMetadataH\x00\x12R\n\x13\x65xport_data_details\x18\x15 \x01(\x0b\x32\x33.google.cloud.automl.v1.ExportDataOperationMetadataH\x00\x12T\n\x14\x65xport_model_details\x18\x16 \x01(\x0b\x32\x34.google.cloud.automl.v1.ExportModelOperationMetadataH\x00\x12\x18\n\x10progress_percent\x18\r \x01(\x05\x12,\n\x10partial_failures\x18\x02 \x03(\x0b\x32\x12.google.rpc.Status\x12/\n\x0b\x63reate_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\t\n\x07\x64\x65tails"\x19\n\x17\x44\x65leteOperationMetadata"\x1e\n\x1c\x44\x65ployModelOperationMetadata" \n\x1eUndeployModelOperationMetadata" \n\x1e\x43reateDatasetOperationMetadata"\x1e\n\x1c\x43reateModelOperationMetadata"\x1d\n\x1bImportDataOperationMetadata"\xc7\x01\n\x1b\x45xportDataOperationMetadata\x12]\n\x0boutput_info\x18\x01 \x01(\x0b\x32H.google.cloud.automl.v1.ExportDataOperationMetadata.ExportDataOutputInfo\x1aI\n\x14\x45xportDataOutputInfo\x12\x1e\n\x14gcs_output_directory\x18\x01 \x01(\tH\x00\x42\x11\n\x0foutput_location"\x96\x02\n\x1d\x42\x61tchPredictOperationMetadata\x12\x45\n\x0cinput_config\x18\x01 \x01(\x0b\x32/.google.cloud.automl.v1.BatchPredictInputConfig\x12\x61\n\x0boutput_info\x18\x02 \x01(\x0b\x32L.google.cloud.automl.v1.BatchPredictOperationMetadata.BatchPredictOutputInfo\x1aK\n\x16\x42\x61tchPredictOutputInfo\x12\x1e\n\x14gcs_output_directory\x18\x01 \x01(\tH\x00\x42\x11\n\x0foutput_location"\xb6\x01\n\x1c\x45xportModelOperationMetadata\x12_\n\x0boutput_info\x18\x02 \x01(\x0b\x32J.google.cloud.automl.v1.ExportModelOperationMetadata.ExportModelOutputInfo\x1a\x35\n\x15\x45xportModelOutputInfo\x12\x1c\n\x14gcs_output_directory\x18\x01 \x01(\tB\xaa\x01\n\x1a\x63om.google.cloud.automl.v1P\x01Z<google.golang.org/genproto/googleapis/cloud/automl/v1;automl\xaa\x02\x16Google.Cloud.AutoML.V1\xca\x02\x16Google\\Cloud\\AutoMl\\V1\xea\x02\x19Google::Cloud::AutoML::V1b\x06proto3',
    dependencies=[
        google_dot_cloud_dot_automl__v1_dot_proto_dot_dataset__pb2.DESCRIPTOR,
        google_dot_cloud_dot_automl__v1_dot_proto_dot_io__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,
        google_dot_rpc_dot_status__pb2.DESCRIPTOR,
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
    ],
)


_OPERATIONMETADATA = _descriptor.Descriptor(
    name="OperationMetadata",
    full_name="google.cloud.automl.v1.OperationMetadata",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="delete_details",
            full_name="google.cloud.automl.v1.OperationMetadata.delete_details",
            index=0,
            number=8,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="deploy_model_details",
            full_name="google.cloud.automl.v1.OperationMetadata.deploy_model_details",
            index=1,
            number=24,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="undeploy_model_details",
            full_name="google.cloud.automl.v1.OperationMetadata.undeploy_model_details",
            index=2,
            number=25,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="create_model_details",
            full_name="google.cloud.automl.v1.OperationMetadata.create_model_details",
            index=3,
            number=10,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="create_dataset_details",
            full_name="google.cloud.automl.v1.OperationMetadata.create_dataset_details",
            index=4,
            number=30,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="import_data_details",
            full_name="google.cloud.automl.v1.OperationMetadata.import_data_details",
            index=5,
            number=15,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="batch_predict_details",
            full_name="google.cloud.automl.v1.OperationMetadata.batch_predict_details",
            index=6,
            number=16,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="export_data_details",
            full_name="google.cloud.automl.v1.OperationMetadata.export_data_details",
            index=7,
            number=21,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="export_model_details",
            full_name="google.cloud.automl.v1.OperationMetadata.export_model_details",
            index=8,
            number=22,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="progress_percent",
            full_name="google.cloud.automl.v1.OperationMetadata.progress_percent",
            index=9,
            number=13,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="partial_failures",
            full_name="google.cloud.automl.v1.OperationMetadata.partial_failures",
            index=10,
            number=2,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="create_time",
            full_name="google.cloud.automl.v1.OperationMetadata.create_time",
            index=11,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="update_time",
            full_name="google.cloud.automl.v1.OperationMetadata.update_time",
            index=12,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="details",
            full_name="google.cloud.automl.v1.OperationMetadata.details",
            index=0,
            containing_type=None,
            fields=[],
        )
    ],
    serialized_start=245,
    serialized_end=1214,
)


_DELETEOPERATIONMETADATA = _descriptor.Descriptor(
    name="DeleteOperationMetadata",
    full_name="google.cloud.automl.v1.DeleteOperationMetadata",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1216,
    serialized_end=1241,
)


_DEPLOYMODELOPERATIONMETADATA = _descriptor.Descriptor(
    name="DeployModelOperationMetadata",
    full_name="google.cloud.automl.v1.DeployModelOperationMetadata",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1243,
    serialized_end=1273,
)


_UNDEPLOYMODELOPERATIONMETADATA = _descriptor.Descriptor(
    name="UndeployModelOperationMetadata",
    full_name="google.cloud.automl.v1.UndeployModelOperationMetadata",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1275,
    serialized_end=1307,
)


_CREATEDATASETOPERATIONMETADATA = _descriptor.Descriptor(
    name="CreateDatasetOperationMetadata",
    full_name="google.cloud.automl.v1.CreateDatasetOperationMetadata",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1309,
    serialized_end=1341,
)


_CREATEMODELOPERATIONMETADATA = _descriptor.Descriptor(
    name="CreateModelOperationMetadata",
    full_name="google.cloud.automl.v1.CreateModelOperationMetadata",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1343,
    serialized_end=1373,
)


_IMPORTDATAOPERATIONMETADATA = _descriptor.Descriptor(
    name="ImportDataOperationMetadata",
    full_name="google.cloud.automl.v1.ImportDataOperationMetadata",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1375,
    serialized_end=1404,
)


_EXPORTDATAOPERATIONMETADATA_EXPORTDATAOUTPUTINFO = _descriptor.Descriptor(
    name="ExportDataOutputInfo",
    full_name="google.cloud.automl.v1.ExportDataOperationMetadata.ExportDataOutputInfo",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="gcs_output_directory",
            full_name="google.cloud.automl.v1.ExportDataOperationMetadata.ExportDataOutputInfo.gcs_output_directory",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="output_location",
            full_name="google.cloud.automl.v1.ExportDataOperationMetadata.ExportDataOutputInfo.output_location",
            index=0,
            containing_type=None,
            fields=[],
        )
    ],
    serialized_start=1533,
    serialized_end=1606,
)

_EXPORTDATAOPERATIONMETADATA = _descriptor.Descriptor(
    name="ExportDataOperationMetadata",
    full_name="google.cloud.automl.v1.ExportDataOperationMetadata",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="output_info",
            full_name="google.cloud.automl.v1.ExportDataOperationMetadata.output_info",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[_EXPORTDATAOPERATIONMETADATA_EXPORTDATAOUTPUTINFO],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1407,
    serialized_end=1606,
)


_BATCHPREDICTOPERATIONMETADATA_BATCHPREDICTOUTPUTINFO = _descriptor.Descriptor(
    name="BatchPredictOutputInfo",
    full_name="google.cloud.automl.v1.BatchPredictOperationMetadata.BatchPredictOutputInfo",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="gcs_output_directory",
            full_name="google.cloud.automl.v1.BatchPredictOperationMetadata.BatchPredictOutputInfo.gcs_output_directory",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="output_location",
            full_name="google.cloud.automl.v1.BatchPredictOperationMetadata.BatchPredictOutputInfo.output_location",
            index=0,
            containing_type=None,
            fields=[],
        )
    ],
    serialized_start=1812,
    serialized_end=1887,
)

_BATCHPREDICTOPERATIONMETADATA = _descriptor.Descriptor(
    name="BatchPredictOperationMetadata",
    full_name="google.cloud.automl.v1.BatchPredictOperationMetadata",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="input_config",
            full_name="google.cloud.automl.v1.BatchPredictOperationMetadata.input_config",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="output_info",
            full_name="google.cloud.automl.v1.BatchPredictOperationMetadata.output_info",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[_BATCHPREDICTOPERATIONMETADATA_BATCHPREDICTOUTPUTINFO],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1609,
    serialized_end=1887,
)


_EXPORTMODELOPERATIONMETADATA_EXPORTMODELOUTPUTINFO = _descriptor.Descriptor(
    name="ExportModelOutputInfo",
    full_name="google.cloud.automl.v1.ExportModelOperationMetadata.ExportModelOutputInfo",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="gcs_output_directory",
            full_name="google.cloud.automl.v1.ExportModelOperationMetadata.ExportModelOutputInfo.gcs_output_directory",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=2019,
    serialized_end=2072,
)

_EXPORTMODELOPERATIONMETADATA = _descriptor.Descriptor(
    name="ExportModelOperationMetadata",
    full_name="google.cloud.automl.v1.ExportModelOperationMetadata",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="output_info",
            full_name="google.cloud.automl.v1.ExportModelOperationMetadata.output_info",
            index=0,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[_EXPORTMODELOPERATIONMETADATA_EXPORTMODELOUTPUTINFO],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1890,
    serialized_end=2072,
)

_OPERATIONMETADATA.fields_by_name[
    "delete_details"
].message_type = _DELETEOPERATIONMETADATA
_OPERATIONMETADATA.fields_by_name[
    "deploy_model_details"
].message_type = _DEPLOYMODELOPERATIONMETADATA
_OPERATIONMETADATA.fields_by_name[
    "undeploy_model_details"
].message_type = _UNDEPLOYMODELOPERATIONMETADATA
_OPERATIONMETADATA.fields_by_name[
    "create_model_details"
].message_type = _CREATEMODELOPERATIONMETADATA
_OPERATIONMETADATA.fields_by_name[
    "create_dataset_details"
].message_type = _CREATEDATASETOPERATIONMETADATA
_OPERATIONMETADATA.fields_by_name[
    "import_data_details"
].message_type = _IMPORTDATAOPERATIONMETADATA
_OPERATIONMETADATA.fields_by_name[
    "batch_predict_details"
].message_type = _BATCHPREDICTOPERATIONMETADATA
_OPERATIONMETADATA.fields_by_name[
    "export_data_details"
].message_type = _EXPORTDATAOPERATIONMETADATA
_OPERATIONMETADATA.fields_by_name[
    "export_model_details"
].message_type = _EXPORTMODELOPERATIONMETADATA
_OPERATIONMETADATA.fields_by_name[
    "partial_failures"
].message_type = google_dot_rpc_dot_status__pb2._STATUS
_OPERATIONMETADATA.fields_by_name[
    "create_time"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_OPERATIONMETADATA.fields_by_name[
    "update_time"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_OPERATIONMETADATA.oneofs_by_name["details"].fields.append(
    _OPERATIONMETADATA.fields_by_name["delete_details"]
)
_OPERATIONMETADATA.fields_by_name[
    "delete_details"
].containing_oneof = _OPERATIONMETADATA.oneofs_by_name["details"]
_OPERATIONMETADATA.oneofs_by_name["details"].fields.append(
    _OPERATIONMETADATA.fields_by_name["deploy_model_details"]
)
_OPERATIONMETADATA.fields_by_name[
    "deploy_model_details"
].containing_oneof = _OPERATIONMETADATA.oneofs_by_name["details"]
_OPERATIONMETADATA.oneofs_by_name["details"].fields.append(
    _OPERATIONMETADATA.fields_by_name["undeploy_model_details"]
)
_OPERATIONMETADATA.fields_by_name[
    "undeploy_model_details"
].containing_oneof = _OPERATIONMETADATA.oneofs_by_name["details"]
_OPERATIONMETADATA.oneofs_by_name["details"].fields.append(
    _OPERATIONMETADATA.fields_by_name["create_model_details"]
)
_OPERATIONMETADATA.fields_by_name[
    "create_model_details"
].containing_oneof = _OPERATIONMETADATA.oneofs_by_name["details"]
_OPERATIONMETADATA.oneofs_by_name["details"].fields.append(
    _OPERATIONMETADATA.fields_by_name["create_dataset_details"]
)
_OPERATIONMETADATA.fields_by_name[
    "create_dataset_details"
].containing_oneof = _OPERATIONMETADATA.oneofs_by_name["details"]
_OPERATIONMETADATA.oneofs_by_name["details"].fields.append(
    _OPERATIONMETADATA.fields_by_name["import_data_details"]
)
_OPERATIONMETADATA.fields_by_name[
    "import_data_details"
].containing_oneof = _OPERATIONMETADATA.oneofs_by_name["details"]
_OPERATIONMETADATA.oneofs_by_name["details"].fields.append(
    _OPERATIONMETADATA.fields_by_name["batch_predict_details"]
)
_OPERATIONMETADATA.fields_by_name[
    "batch_predict_details"
].containing_oneof = _OPERATIONMETADATA.oneofs_by_name["details"]
_OPERATIONMETADATA.oneofs_by_name["details"].fields.append(
    _OPERATIONMETADATA.fields_by_name["export_data_details"]
)
_OPERATIONMETADATA.fields_by_name[
    "export_data_details"
].containing_oneof = _OPERATIONMETADATA.oneofs_by_name["details"]
_OPERATIONMETADATA.oneofs_by_name["details"].fields.append(
    _OPERATIONMETADATA.fields_by_name["export_model_details"]
)
_OPERATIONMETADATA.fields_by_name[
    "export_model_details"
].containing_oneof = _OPERATIONMETADATA.oneofs_by_name["details"]
_EXPORTDATAOPERATIONMETADATA_EXPORTDATAOUTPUTINFO.containing_type = (
    _EXPORTDATAOPERATIONMETADATA
)
_EXPORTDATAOPERATIONMETADATA_EXPORTDATAOUTPUTINFO.oneofs_by_name[
    "output_location"
].fields.append(
    _EXPORTDATAOPERATIONMETADATA_EXPORTDATAOUTPUTINFO.fields_by_name[
        "gcs_output_directory"
    ]
)
_EXPORTDATAOPERATIONMETADATA_EXPORTDATAOUTPUTINFO.fields_by_name[
    "gcs_output_directory"
].containing_oneof = _EXPORTDATAOPERATIONMETADATA_EXPORTDATAOUTPUTINFO.oneofs_by_name[
    "output_location"
]
_EXPORTDATAOPERATIONMETADATA.fields_by_name[
    "output_info"
].message_type = _EXPORTDATAOPERATIONMETADATA_EXPORTDATAOUTPUTINFO
_BATCHPREDICTOPERATIONMETADATA_BATCHPREDICTOUTPUTINFO.containing_type = (
    _BATCHPREDICTOPERATIONMETADATA
)
_BATCHPREDICTOPERATIONMETADATA_BATCHPREDICTOUTPUTINFO.oneofs_by_name[
    "output_location"
].fields.append(
    _BATCHPREDICTOPERATIONMETADATA_BATCHPREDICTOUTPUTINFO.fields_by_name[
        "gcs_output_directory"
    ]
)
_BATCHPREDICTOPERATIONMETADATA_BATCHPREDICTOUTPUTINFO.fields_by_name[
    "gcs_output_directory"
].containing_oneof = _BATCHPREDICTOPERATIONMETADATA_BATCHPREDICTOUTPUTINFO.oneofs_by_name[
    "output_location"
]
_BATCHPREDICTOPERATIONMETADATA.fields_by_name[
    "input_config"
].message_type = (
    google_dot_cloud_dot_automl__v1_dot_proto_dot_io__pb2._BATCHPREDICTINPUTCONFIG
)
_BATCHPREDICTOPERATIONMETADATA.fields_by_name[
    "output_info"
].message_type = _BATCHPREDICTOPERATIONMETADATA_BATCHPREDICTOUTPUTINFO
_EXPORTMODELOPERATIONMETADATA_EXPORTMODELOUTPUTINFO.containing_type = (
    _EXPORTMODELOPERATIONMETADATA
)
_EXPORTMODELOPERATIONMETADATA.fields_by_name[
    "output_info"
].message_type = _EXPORTMODELOPERATIONMETADATA_EXPORTMODELOUTPUTINFO
DESCRIPTOR.message_types_by_name["OperationMetadata"] = _OPERATIONMETADATA
DESCRIPTOR.message_types_by_name["DeleteOperationMetadata"] = _DELETEOPERATIONMETADATA
DESCRIPTOR.message_types_by_name[
    "DeployModelOperationMetadata"
] = _DEPLOYMODELOPERATIONMETADATA
DESCRIPTOR.message_types_by_name[
    "UndeployModelOperationMetadata"
] = _UNDEPLOYMODELOPERATIONMETADATA
DESCRIPTOR.message_types_by_name[
    "CreateDatasetOperationMetadata"
] = _CREATEDATASETOPERATIONMETADATA
DESCRIPTOR.message_types_by_name[
    "CreateModelOperationMetadata"
] = _CREATEMODELOPERATIONMETADATA
DESCRIPTOR.message_types_by_name[
    "ImportDataOperationMetadata"
] = _IMPORTDATAOPERATIONMETADATA
DESCRIPTOR.message_types_by_name[
    "ExportDataOperationMetadata"
] = _EXPORTDATAOPERATIONMETADATA
DESCRIPTOR.message_types_by_name[
    "BatchPredictOperationMetadata"
] = _BATCHPREDICTOPERATIONMETADATA
DESCRIPTOR.message_types_by_name[
    "ExportModelOperationMetadata"
] = _EXPORTMODELOPERATIONMETADATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OperationMetadata = _reflection.GeneratedProtocolMessageType(
    "OperationMetadata",
    (_message.Message,),
    {
        "DESCRIPTOR": _OPERATIONMETADATA,
        "__module__": "google.cloud.automl_v1.proto.operations_pb2",
        "__doc__": """Metadata used across all long running operations returned
  by AutoML API.
  
  
  Attributes:
      details:
          Ouptut only. Details of specific operation. Even if this field
          is empty, the presence allows to distinguish different types
          of operations.
      delete_details:
          Details of a Delete operation.
      deploy_model_details:
          Details of a DeployModel operation.
      undeploy_model_details:
          Details of an UndeployModel operation.
      create_model_details:
          Details of CreateModel operation.
      create_dataset_details:
          Details of CreateDataset operation.
      import_data_details:
          Details of ImportData operation.
      batch_predict_details:
          Details of BatchPredict operation.
      export_data_details:
          Details of ExportData operation.
      export_model_details:
          Details of ExportModel operation.
      progress_percent:
          Output only. Progress of operation. Range: [0, 100]. Not used
          currently.
      partial_failures:
          Output only. Partial failures encountered. E.g. single files
          that couldn’t be read. This field should never exceed 20
          entries. Status details field will contain standard GCP error
          details.
      create_time:
          Output only. Time when the operation was created.
      update_time:
          Output only. Time when the operation was updated for the last
          time.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.OperationMetadata)
    },
)
_sym_db.RegisterMessage(OperationMetadata)

DeleteOperationMetadata = _reflection.GeneratedProtocolMessageType(
    "DeleteOperationMetadata",
    (_message.Message,),
    {
        "DESCRIPTOR": _DELETEOPERATIONMETADATA,
        "__module__": "google.cloud.automl_v1.proto.operations_pb2",
        "__doc__": """Details of operations that perform deletes of any
  entities.
  
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.DeleteOperationMetadata)
    },
)
_sym_db.RegisterMessage(DeleteOperationMetadata)

DeployModelOperationMetadata = _reflection.GeneratedProtocolMessageType(
    "DeployModelOperationMetadata",
    (_message.Message,),
    {
        "DESCRIPTOR": _DEPLOYMODELOPERATIONMETADATA,
        "__module__": "google.cloud.automl_v1.proto.operations_pb2",
        "__doc__": """Details of DeployModel operation.
  
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.DeployModelOperationMetadata)
    },
)
_sym_db.RegisterMessage(DeployModelOperationMetadata)

UndeployModelOperationMetadata = _reflection.GeneratedProtocolMessageType(
    "UndeployModelOperationMetadata",
    (_message.Message,),
    {
        "DESCRIPTOR": _UNDEPLOYMODELOPERATIONMETADATA,
        "__module__": "google.cloud.automl_v1.proto.operations_pb2",
        "__doc__": """Details of UndeployModel operation.
  
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.UndeployModelOperationMetadata)
    },
)
_sym_db.RegisterMessage(UndeployModelOperationMetadata)

CreateDatasetOperationMetadata = _reflection.GeneratedProtocolMessageType(
    "CreateDatasetOperationMetadata",
    (_message.Message,),
    {
        "DESCRIPTOR": _CREATEDATASETOPERATIONMETADATA,
        "__module__": "google.cloud.automl_v1.proto.operations_pb2",
        "__doc__": """Details of CreateDataset operation.
  
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.CreateDatasetOperationMetadata)
    },
)
_sym_db.RegisterMessage(CreateDatasetOperationMetadata)

CreateModelOperationMetadata = _reflection.GeneratedProtocolMessageType(
    "CreateModelOperationMetadata",
    (_message.Message,),
    {
        "DESCRIPTOR": _CREATEMODELOPERATIONMETADATA,
        "__module__": "google.cloud.automl_v1.proto.operations_pb2",
        "__doc__": """Details of CreateModel operation.
  
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.CreateModelOperationMetadata)
    },
)
_sym_db.RegisterMessage(CreateModelOperationMetadata)

ImportDataOperationMetadata = _reflection.GeneratedProtocolMessageType(
    "ImportDataOperationMetadata",
    (_message.Message,),
    {
        "DESCRIPTOR": _IMPORTDATAOPERATIONMETADATA,
        "__module__": "google.cloud.automl_v1.proto.operations_pb2",
        "__doc__": """Details of ImportData operation.
  
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.ImportDataOperationMetadata)
    },
)
_sym_db.RegisterMessage(ImportDataOperationMetadata)

ExportDataOperationMetadata = _reflection.GeneratedProtocolMessageType(
    "ExportDataOperationMetadata",
    (_message.Message,),
    {
        "ExportDataOutputInfo": _reflection.GeneratedProtocolMessageType(
            "ExportDataOutputInfo",
            (_message.Message,),
            {
                "DESCRIPTOR": _EXPORTDATAOPERATIONMETADATA_EXPORTDATAOUTPUTINFO,
                "__module__": "google.cloud.automl_v1.proto.operations_pb2",
                "__doc__": """Further describes this export data’s output. Supplements
    [OutputConfig][google.cloud.automl.v1.OutputConfig].
    
    
    Attributes:
        output_location:
            The output location to which the exported data is written.
        gcs_output_directory:
            The full path of the Google Cloud Storage directory created,
            into which the exported data is written.
    """,
                # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.ExportDataOperationMetadata.ExportDataOutputInfo)
            },
        ),
        "DESCRIPTOR": _EXPORTDATAOPERATIONMETADATA,
        "__module__": "google.cloud.automl_v1.proto.operations_pb2",
        "__doc__": """Details of ExportData operation.
  
  
  Attributes:
      output_info:
          Output only. Information further describing this export data’s
          output.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.ExportDataOperationMetadata)
    },
)
_sym_db.RegisterMessage(ExportDataOperationMetadata)
_sym_db.RegisterMessage(ExportDataOperationMetadata.ExportDataOutputInfo)

BatchPredictOperationMetadata = _reflection.GeneratedProtocolMessageType(
    "BatchPredictOperationMetadata",
    (_message.Message,),
    {
        "BatchPredictOutputInfo": _reflection.GeneratedProtocolMessageType(
            "BatchPredictOutputInfo",
            (_message.Message,),
            {
                "DESCRIPTOR": _BATCHPREDICTOPERATIONMETADATA_BATCHPREDICTOUTPUTINFO,
                "__module__": "google.cloud.automl_v1.proto.operations_pb2",
                "__doc__": """Further describes this batch predict’s output. Supplements
    
    [BatchPredictOutputConfig][google.cloud.automl.v1.BatchPredictOutputConfig].
    
    
    Attributes:
        output_location:
            The output location into which prediction output is written.
        gcs_output_directory:
            The full path of the Google Cloud Storage directory created,
            into which the prediction output is written.
    """,
                # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.BatchPredictOperationMetadata.BatchPredictOutputInfo)
            },
        ),
        "DESCRIPTOR": _BATCHPREDICTOPERATIONMETADATA,
        "__module__": "google.cloud.automl_v1.proto.operations_pb2",
        "__doc__": """Details of BatchPredict operation.
  
  
  Attributes:
      input_config:
          Output only. The input config that was given upon starting
          this batch predict operation.
      output_info:
          Output only. Information further describing this batch
          predict’s output.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.BatchPredictOperationMetadata)
    },
)
_sym_db.RegisterMessage(BatchPredictOperationMetadata)
_sym_db.RegisterMessage(BatchPredictOperationMetadata.BatchPredictOutputInfo)

ExportModelOperationMetadata = _reflection.GeneratedProtocolMessageType(
    "ExportModelOperationMetadata",
    (_message.Message,),
    {
        "ExportModelOutputInfo": _reflection.GeneratedProtocolMessageType(
            "ExportModelOutputInfo",
            (_message.Message,),
            {
                "DESCRIPTOR": _EXPORTMODELOPERATIONMETADATA_EXPORTMODELOUTPUTINFO,
                "__module__": "google.cloud.automl_v1.proto.operations_pb2",
                "__doc__": """Further describes the output of model export. Supplements
    [ModelExportOutputConfig][google.cloud.automl.v1.ModelExportOutputConfig].
    
    
    Attributes:
        gcs_output_directory:
            The full path of the Google Cloud Storage directory created,
            into which the model will be exported.
    """,
                # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.ExportModelOperationMetadata.ExportModelOutputInfo)
            },
        ),
        "DESCRIPTOR": _EXPORTMODELOPERATIONMETADATA,
        "__module__": "google.cloud.automl_v1.proto.operations_pb2",
        "__doc__": """Details of ExportModel operation.
  
  
  Attributes:
      output_info:
          Output only. Information further describing the output of this
          model export.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.ExportModelOperationMetadata)
    },
)
_sym_db.RegisterMessage(ExportModelOperationMetadata)
_sym_db.RegisterMessage(ExportModelOperationMetadata.ExportModelOutputInfo)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
