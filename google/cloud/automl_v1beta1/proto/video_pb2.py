# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/automl_v1beta1/proto/video.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.cloud.automl_v1beta1.proto import (
    classification_pb2 as google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_classification__pb2,
)
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/automl_v1beta1/proto/video.proto",
    package="google.cloud.automl.v1beta1",
    syntax="proto3",
    serialized_options=b"\n\037com.google.cloud.automl.v1beta1B\nVideoProtoP\001ZAgoogle.golang.org/genproto/googleapis/cloud/automl/v1beta1;automl\312\002\033Google\\Cloud\\AutoMl\\V1beta1\352\002\036Google::Cloud::AutoML::V1beta1",
    serialized_pb=b'\n-google/cloud/automl_v1beta1/proto/video.proto\x12\x1bgoogle.cloud.automl.v1beta1\x1a\x36google/cloud/automl_v1beta1/proto/classification.proto\x1a\x1cgoogle/api/annotations.proto"$\n"VideoClassificationDatasetMetadata"$\n"VideoObjectTrackingDatasetMetadata""\n VideoClassificationModelMetadata""\n VideoObjectTrackingModelMetadataB\xb1\x01\n\x1f\x63om.google.cloud.automl.v1beta1B\nVideoProtoP\x01ZAgoogle.golang.org/genproto/googleapis/cloud/automl/v1beta1;automl\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1\xea\x02\x1eGoogle::Cloud::AutoML::V1beta1b\x06proto3',
    dependencies=[
        google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_classification__pb2.DESCRIPTOR,
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
    ],
)


_VIDEOCLASSIFICATIONDATASETMETADATA = _descriptor.Descriptor(
    name="VideoClassificationDatasetMetadata",
    full_name="google.cloud.automl.v1beta1.VideoClassificationDatasetMetadata",
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
    serialized_start=164,
    serialized_end=200,
)


_VIDEOOBJECTTRACKINGDATASETMETADATA = _descriptor.Descriptor(
    name="VideoObjectTrackingDatasetMetadata",
    full_name="google.cloud.automl.v1beta1.VideoObjectTrackingDatasetMetadata",
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
    serialized_start=202,
    serialized_end=238,
)


_VIDEOCLASSIFICATIONMODELMETADATA = _descriptor.Descriptor(
    name="VideoClassificationModelMetadata",
    full_name="google.cloud.automl.v1beta1.VideoClassificationModelMetadata",
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
    serialized_start=240,
    serialized_end=274,
)


_VIDEOOBJECTTRACKINGMODELMETADATA = _descriptor.Descriptor(
    name="VideoObjectTrackingModelMetadata",
    full_name="google.cloud.automl.v1beta1.VideoObjectTrackingModelMetadata",
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
    serialized_start=276,
    serialized_end=310,
)

DESCRIPTOR.message_types_by_name[
    "VideoClassificationDatasetMetadata"
] = _VIDEOCLASSIFICATIONDATASETMETADATA
DESCRIPTOR.message_types_by_name[
    "VideoObjectTrackingDatasetMetadata"
] = _VIDEOOBJECTTRACKINGDATASETMETADATA
DESCRIPTOR.message_types_by_name[
    "VideoClassificationModelMetadata"
] = _VIDEOCLASSIFICATIONMODELMETADATA
DESCRIPTOR.message_types_by_name[
    "VideoObjectTrackingModelMetadata"
] = _VIDEOOBJECTTRACKINGMODELMETADATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VideoClassificationDatasetMetadata = _reflection.GeneratedProtocolMessageType(
    "VideoClassificationDatasetMetadata",
    (_message.Message,),
    {
        "DESCRIPTOR": _VIDEOCLASSIFICATIONDATASETMETADATA,
        "__module__": "google.cloud.automl_v1beta1.proto.video_pb2",
        "__doc__": """Dataset metadata specific to video classification. All Video
  Classification datasets are treated as multi label.""",
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.VideoClassificationDatasetMetadata)
    },
)
_sym_db.RegisterMessage(VideoClassificationDatasetMetadata)

VideoObjectTrackingDatasetMetadata = _reflection.GeneratedProtocolMessageType(
    "VideoObjectTrackingDatasetMetadata",
    (_message.Message,),
    {
        "DESCRIPTOR": _VIDEOOBJECTTRACKINGDATASETMETADATA,
        "__module__": "google.cloud.automl_v1beta1.proto.video_pb2",
        "__doc__": """Dataset metadata specific to video object tracking.""",
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.VideoObjectTrackingDatasetMetadata)
    },
)
_sym_db.RegisterMessage(VideoObjectTrackingDatasetMetadata)

VideoClassificationModelMetadata = _reflection.GeneratedProtocolMessageType(
    "VideoClassificationModelMetadata",
    (_message.Message,),
    {
        "DESCRIPTOR": _VIDEOCLASSIFICATIONMODELMETADATA,
        "__module__": "google.cloud.automl_v1beta1.proto.video_pb2",
        "__doc__": """Model metadata specific to video classification.""",
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.VideoClassificationModelMetadata)
    },
)
_sym_db.RegisterMessage(VideoClassificationModelMetadata)

VideoObjectTrackingModelMetadata = _reflection.GeneratedProtocolMessageType(
    "VideoObjectTrackingModelMetadata",
    (_message.Message,),
    {
        "DESCRIPTOR": _VIDEOOBJECTTRACKINGMODELMETADATA,
        "__module__": "google.cloud.automl_v1beta1.proto.video_pb2",
        "__doc__": """Model metadata specific to video object tracking.""",
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.VideoObjectTrackingModelMetadata)
    },
)
_sym_db.RegisterMessage(VideoObjectTrackingModelMetadata)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
