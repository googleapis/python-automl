# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/automl_v1beta1/proto/dataset.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.cloud.automl_v1beta1.proto import (
    image_pb2 as google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_image__pb2,
)
from google.cloud.automl_v1beta1.proto import (
    tables_pb2 as google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_tables__pb2,
)
from google.cloud.automl_v1beta1.proto import (
    text_pb2 as google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_text__pb2,
)
from google.cloud.automl_v1beta1.proto import (
    translation_pb2 as google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_translation__pb2,
)
from google.cloud.automl_v1beta1.proto import (
    video_pb2 as google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_video__pb2,
)
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/automl_v1beta1/proto/dataset.proto",
    package="google.cloud.automl.v1beta1",
    syntax="proto3",
    serialized_options=b"\n\037com.google.cloud.automl.v1beta1P\001ZAgoogle.golang.org/genproto/googleapis/cloud/automl/v1beta1;automl\312\002\033Google\\Cloud\\AutoMl\\V1beta1\352\002\036Google::Cloud::AutoML::V1beta1",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b"\n/google/cloud/automl_v1beta1/proto/dataset.proto\x12\x1bgoogle.cloud.automl.v1beta1\x1a\x19google/api/resource.proto\x1a-google/cloud/automl_v1beta1/proto/image.proto\x1a.google/cloud/automl_v1beta1/proto/tables.proto\x1a,google/cloud/automl_v1beta1/proto/text.proto\x1a\x33google/cloud/automl_v1beta1/proto/translation.proto\x1a-google/cloud/automl_v1beta1/proto/video.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/api/annotations.proto\"\xce\t\n\x07\x44\x61taset\x12_\n\x1ctranslation_dataset_metadata\x18\x17 \x01(\x0b\x32\x37.google.cloud.automl.v1beta1.TranslationDatasetMetadataH\x00\x12p\n%image_classification_dataset_metadata\x18\x18 \x01(\x0b\x32?.google.cloud.automl.v1beta1.ImageClassificationDatasetMetadataH\x00\x12n\n$text_classification_dataset_metadata\x18\x19 \x01(\x0b\x32>.google.cloud.automl.v1beta1.TextClassificationDatasetMetadataH\x00\x12s\n'image_object_detection_dataset_metadata\x18\x1a \x01(\x0b\x32@.google.cloud.automl.v1beta1.ImageObjectDetectionDatasetMetadataH\x00\x12p\n%video_classification_dataset_metadata\x18\x1f \x01(\x0b\x32?.google.cloud.automl.v1beta1.VideoClassificationDatasetMetadataH\x00\x12q\n&video_object_tracking_dataset_metadata\x18\x1d \x01(\x0b\x32?.google.cloud.automl.v1beta1.VideoObjectTrackingDatasetMetadataH\x00\x12\x66\n text_extraction_dataset_metadata\x18\x1c \x01(\x0b\x32:.google.cloud.automl.v1beta1.TextExtractionDatasetMetadataH\x00\x12\x64\n\x1ftext_sentiment_dataset_metadata\x18\x1e \x01(\x0b\x32\x39.google.cloud.automl.v1beta1.TextSentimentDatasetMetadataH\x00\x12U\n\x17tables_dataset_metadata\x18! \x01(\x0b\x32\x32.google.cloud.automl.v1beta1.TablesDatasetMetadataH\x00\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x15\n\rexample_count\x18\x15 \x01(\x05\x12/\n\x0b\x63reate_time\x18\x0e \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04\x65tag\x18\x11 \x01(\t:^\xea\x41[\n\x1d\x61utoml.googleapis.com/Dataset\x12:projects/{project}/locations/{location}/datasets/{dataset}B\x12\n\x10\x64\x61taset_metadataB\xa5\x01\n\x1f\x63om.google.cloud.automl.v1beta1P\x01ZAgoogle.golang.org/genproto/googleapis/cloud/automl/v1beta1;automl\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1\xea\x02\x1eGoogle::Cloud::AutoML::V1beta1b\x06proto3",
    dependencies=[
        google_dot_api_dot_resource__pb2.DESCRIPTOR,
        google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_image__pb2.DESCRIPTOR,
        google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_tables__pb2.DESCRIPTOR,
        google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_text__pb2.DESCRIPTOR,
        google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_translation__pb2.DESCRIPTOR,
        google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_video__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
    ],
)


_DATASET = _descriptor.Descriptor(
    name="Dataset",
    full_name="google.cloud.automl.v1beta1.Dataset",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="translation_dataset_metadata",
            full_name="google.cloud.automl.v1beta1.Dataset.translation_dataset_metadata",
            index=0,
            number=23,
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
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="image_classification_dataset_metadata",
            full_name="google.cloud.automl.v1beta1.Dataset.image_classification_dataset_metadata",
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
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="text_classification_dataset_metadata",
            full_name="google.cloud.automl.v1beta1.Dataset.text_classification_dataset_metadata",
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
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="image_object_detection_dataset_metadata",
            full_name="google.cloud.automl.v1beta1.Dataset.image_object_detection_dataset_metadata",
            index=3,
            number=26,
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
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="video_classification_dataset_metadata",
            full_name="google.cloud.automl.v1beta1.Dataset.video_classification_dataset_metadata",
            index=4,
            number=31,
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
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="video_object_tracking_dataset_metadata",
            full_name="google.cloud.automl.v1beta1.Dataset.video_object_tracking_dataset_metadata",
            index=5,
            number=29,
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
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="text_extraction_dataset_metadata",
            full_name="google.cloud.automl.v1beta1.Dataset.text_extraction_dataset_metadata",
            index=6,
            number=28,
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
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="text_sentiment_dataset_metadata",
            full_name="google.cloud.automl.v1beta1.Dataset.text_sentiment_dataset_metadata",
            index=7,
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
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="tables_dataset_metadata",
            full_name="google.cloud.automl.v1beta1.Dataset.tables_dataset_metadata",
            index=8,
            number=33,
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
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.cloud.automl.v1beta1.Dataset.name",
            index=9,
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
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="display_name",
            full_name="google.cloud.automl.v1beta1.Dataset.display_name",
            index=10,
            number=2,
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
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="description",
            full_name="google.cloud.automl.v1beta1.Dataset.description",
            index=11,
            number=3,
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
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="example_count",
            full_name="google.cloud.automl.v1beta1.Dataset.example_count",
            index=12,
            number=21,
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
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="create_time",
            full_name="google.cloud.automl.v1beta1.Dataset.create_time",
            index=13,
            number=14,
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
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="etag",
            full_name="google.cloud.automl.v1beta1.Dataset.etag",
            index=14,
            number=17,
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
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b"\352A[\n\035automl.googleapis.com/Dataset\022:projects/{project}/locations/{location}/datasets/{dataset}",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="dataset_metadata",
            full_name="google.cloud.automl.v1beta1.Dataset.dataset_metadata",
            index=0,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        )
    ],
    serialized_start=412,
    serialized_end=1642,
)

_DATASET.fields_by_name[
    "translation_dataset_metadata"
].message_type = (
    google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_translation__pb2._TRANSLATIONDATASETMETADATA
)
_DATASET.fields_by_name[
    "image_classification_dataset_metadata"
].message_type = (
    google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_image__pb2._IMAGECLASSIFICATIONDATASETMETADATA
)
_DATASET.fields_by_name[
    "text_classification_dataset_metadata"
].message_type = (
    google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_text__pb2._TEXTCLASSIFICATIONDATASETMETADATA
)
_DATASET.fields_by_name[
    "image_object_detection_dataset_metadata"
].message_type = (
    google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_image__pb2._IMAGEOBJECTDETECTIONDATASETMETADATA
)
_DATASET.fields_by_name[
    "video_classification_dataset_metadata"
].message_type = (
    google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_video__pb2._VIDEOCLASSIFICATIONDATASETMETADATA
)
_DATASET.fields_by_name[
    "video_object_tracking_dataset_metadata"
].message_type = (
    google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_video__pb2._VIDEOOBJECTTRACKINGDATASETMETADATA
)
_DATASET.fields_by_name[
    "text_extraction_dataset_metadata"
].message_type = (
    google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_text__pb2._TEXTEXTRACTIONDATASETMETADATA
)
_DATASET.fields_by_name[
    "text_sentiment_dataset_metadata"
].message_type = (
    google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_text__pb2._TEXTSENTIMENTDATASETMETADATA
)
_DATASET.fields_by_name[
    "tables_dataset_metadata"
].message_type = (
    google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_tables__pb2._TABLESDATASETMETADATA
)
_DATASET.fields_by_name[
    "create_time"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_DATASET.oneofs_by_name["dataset_metadata"].fields.append(
    _DATASET.fields_by_name["translation_dataset_metadata"]
)
_DATASET.fields_by_name[
    "translation_dataset_metadata"
].containing_oneof = _DATASET.oneofs_by_name["dataset_metadata"]
_DATASET.oneofs_by_name["dataset_metadata"].fields.append(
    _DATASET.fields_by_name["image_classification_dataset_metadata"]
)
_DATASET.fields_by_name[
    "image_classification_dataset_metadata"
].containing_oneof = _DATASET.oneofs_by_name["dataset_metadata"]
_DATASET.oneofs_by_name["dataset_metadata"].fields.append(
    _DATASET.fields_by_name["text_classification_dataset_metadata"]
)
_DATASET.fields_by_name[
    "text_classification_dataset_metadata"
].containing_oneof = _DATASET.oneofs_by_name["dataset_metadata"]
_DATASET.oneofs_by_name["dataset_metadata"].fields.append(
    _DATASET.fields_by_name["image_object_detection_dataset_metadata"]
)
_DATASET.fields_by_name[
    "image_object_detection_dataset_metadata"
].containing_oneof = _DATASET.oneofs_by_name["dataset_metadata"]
_DATASET.oneofs_by_name["dataset_metadata"].fields.append(
    _DATASET.fields_by_name["video_classification_dataset_metadata"]
)
_DATASET.fields_by_name[
    "video_classification_dataset_metadata"
].containing_oneof = _DATASET.oneofs_by_name["dataset_metadata"]
_DATASET.oneofs_by_name["dataset_metadata"].fields.append(
    _DATASET.fields_by_name["video_object_tracking_dataset_metadata"]
)
_DATASET.fields_by_name[
    "video_object_tracking_dataset_metadata"
].containing_oneof = _DATASET.oneofs_by_name["dataset_metadata"]
_DATASET.oneofs_by_name["dataset_metadata"].fields.append(
    _DATASET.fields_by_name["text_extraction_dataset_metadata"]
)
_DATASET.fields_by_name[
    "text_extraction_dataset_metadata"
].containing_oneof = _DATASET.oneofs_by_name["dataset_metadata"]
_DATASET.oneofs_by_name["dataset_metadata"].fields.append(
    _DATASET.fields_by_name["text_sentiment_dataset_metadata"]
)
_DATASET.fields_by_name[
    "text_sentiment_dataset_metadata"
].containing_oneof = _DATASET.oneofs_by_name["dataset_metadata"]
_DATASET.oneofs_by_name["dataset_metadata"].fields.append(
    _DATASET.fields_by_name["tables_dataset_metadata"]
)
_DATASET.fields_by_name[
    "tables_dataset_metadata"
].containing_oneof = _DATASET.oneofs_by_name["dataset_metadata"]
DESCRIPTOR.message_types_by_name["Dataset"] = _DATASET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Dataset = _reflection.GeneratedProtocolMessageType(
    "Dataset",
    (_message.Message,),
    {
        "DESCRIPTOR": _DATASET,
        "__module__": "google.cloud.automl_v1beta1.proto.dataset_pb2",
        "__doc__": """A workspace for solving a single, particular machine learning (ML)
  problem. A workspace contains examples that may be annotated.
  Attributes:
      dataset_metadata:
          Required. The dataset metadata that is specific to the problem
          type.
      translation_dataset_metadata:
          Metadata for a dataset used for translation.
      image_classification_dataset_metadata:
          Metadata for a dataset used for image classification.
      text_classification_dataset_metadata:
          Metadata for a dataset used for text classification.
      image_object_detection_dataset_metadata:
          Metadata for a dataset used for image object detection.
      video_classification_dataset_metadata:
          Metadata for a dataset used for video classification.
      video_object_tracking_dataset_metadata:
          Metadata for a dataset used for video object tracking.
      text_extraction_dataset_metadata:
          Metadata for a dataset used for text extraction.
      text_sentiment_dataset_metadata:
          Metadata for a dataset used for text sentiment.
      tables_dataset_metadata:
          Metadata for a dataset used for Tables.
      name:
          Output only. The resource name of the dataset. Form: ``project
          s/{project_id}/locations/{location_id}/datasets/{dataset_id}``
      display_name:
          Required. The name of the dataset to show in the interface.
          The name can be up to 32 characters long and can consist only
          of ASCII Latin letters A-Z and a-z, underscores (_), and ASCII
          digits 0-9.
      description:
          User-provided description of the dataset. The description can
          be up to 25000 characters long.
      example_count:
          Output only. The number of examples in the dataset.
      create_time:
          Output only. Timestamp when this dataset was created.
      etag:
          Used to perform consistent read-modify-write updates. If not
          set, a blind “overwrite” update happens.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.Dataset)
    },
)
_sym_db.RegisterMessage(Dataset)


DESCRIPTOR._options = None
_DATASET._options = None
# @@protoc_insertion_point(module_scope)
