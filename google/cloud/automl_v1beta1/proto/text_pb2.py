# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/automl_v1beta1/proto/text.proto

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
    name="google/cloud/automl_v1beta1/proto/text.proto",
    package="google.cloud.automl.v1beta1",
    syntax="proto3",
    serialized_options=b"\n\037com.google.cloud.automl.v1beta1B\tTextProtoP\001ZAgoogle.golang.org/genproto/googleapis/cloud/automl/v1beta1;automl\312\002\033Google\\Cloud\\AutoMl\\V1beta1\352\002\036Google::Cloud::AutoML::V1beta1",
    serialized_pb=b'\n,google/cloud/automl_v1beta1/proto/text.proto\x12\x1bgoogle.cloud.automl.v1beta1\x1a\x36google/cloud/automl_v1beta1/proto/classification.proto\x1a\x1cgoogle/api/annotations.proto"q\n!TextClassificationDatasetMetadata\x12L\n\x13\x63lassification_type\x18\x01 \x01(\x0e\x32/.google.cloud.automl.v1beta1.ClassificationType"o\n\x1fTextClassificationModelMetadata\x12L\n\x13\x63lassification_type\x18\x03 \x01(\x0e\x32/.google.cloud.automl.v1beta1.ClassificationType"\x1f\n\x1dTextExtractionDatasetMetadata"\x1d\n\x1bTextExtractionModelMetadata"5\n\x1cTextSentimentDatasetMetadata\x12\x15\n\rsentiment_max\x18\x01 \x01(\x05"\x1c\n\x1aTextSentimentModelMetadataB\xb0\x01\n\x1f\x63om.google.cloud.automl.v1beta1B\tTextProtoP\x01ZAgoogle.golang.org/genproto/googleapis/cloud/automl/v1beta1;automl\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1\xea\x02\x1eGoogle::Cloud::AutoML::V1beta1b\x06proto3',
    dependencies=[
        google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_classification__pb2.DESCRIPTOR,
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
    ],
)


_TEXTCLASSIFICATIONDATASETMETADATA = _descriptor.Descriptor(
    name="TextClassificationDatasetMetadata",
    full_name="google.cloud.automl.v1beta1.TextClassificationDatasetMetadata",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="classification_type",
            full_name="google.cloud.automl.v1beta1.TextClassificationDatasetMetadata.classification_type",
            index=0,
            number=1,
            type=14,
            cpp_type=8,
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
    serialized_start=163,
    serialized_end=276,
)


_TEXTCLASSIFICATIONMODELMETADATA = _descriptor.Descriptor(
    name="TextClassificationModelMetadata",
    full_name="google.cloud.automl.v1beta1.TextClassificationModelMetadata",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="classification_type",
            full_name="google.cloud.automl.v1beta1.TextClassificationModelMetadata.classification_type",
            index=0,
            number=3,
            type=14,
            cpp_type=8,
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
    serialized_start=278,
    serialized_end=389,
)


_TEXTEXTRACTIONDATASETMETADATA = _descriptor.Descriptor(
    name="TextExtractionDatasetMetadata",
    full_name="google.cloud.automl.v1beta1.TextExtractionDatasetMetadata",
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
    serialized_start=391,
    serialized_end=422,
)


_TEXTEXTRACTIONMODELMETADATA = _descriptor.Descriptor(
    name="TextExtractionModelMetadata",
    full_name="google.cloud.automl.v1beta1.TextExtractionModelMetadata",
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
    serialized_start=424,
    serialized_end=453,
)


_TEXTSENTIMENTDATASETMETADATA = _descriptor.Descriptor(
    name="TextSentimentDatasetMetadata",
    full_name="google.cloud.automl.v1beta1.TextSentimentDatasetMetadata",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="sentiment_max",
            full_name="google.cloud.automl.v1beta1.TextSentimentDatasetMetadata.sentiment_max",
            index=0,
            number=1,
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
    serialized_start=455,
    serialized_end=508,
)


_TEXTSENTIMENTMODELMETADATA = _descriptor.Descriptor(
    name="TextSentimentModelMetadata",
    full_name="google.cloud.automl.v1beta1.TextSentimentModelMetadata",
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
    serialized_start=510,
    serialized_end=538,
)

_TEXTCLASSIFICATIONDATASETMETADATA.fields_by_name[
    "classification_type"
].enum_type = (
    google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_classification__pb2._CLASSIFICATIONTYPE
)
_TEXTCLASSIFICATIONMODELMETADATA.fields_by_name[
    "classification_type"
].enum_type = (
    google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_classification__pb2._CLASSIFICATIONTYPE
)
DESCRIPTOR.message_types_by_name[
    "TextClassificationDatasetMetadata"
] = _TEXTCLASSIFICATIONDATASETMETADATA
DESCRIPTOR.message_types_by_name[
    "TextClassificationModelMetadata"
] = _TEXTCLASSIFICATIONMODELMETADATA
DESCRIPTOR.message_types_by_name[
    "TextExtractionDatasetMetadata"
] = _TEXTEXTRACTIONDATASETMETADATA
DESCRIPTOR.message_types_by_name[
    "TextExtractionModelMetadata"
] = _TEXTEXTRACTIONMODELMETADATA
DESCRIPTOR.message_types_by_name[
    "TextSentimentDatasetMetadata"
] = _TEXTSENTIMENTDATASETMETADATA
DESCRIPTOR.message_types_by_name[
    "TextSentimentModelMetadata"
] = _TEXTSENTIMENTMODELMETADATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TextClassificationDatasetMetadata = _reflection.GeneratedProtocolMessageType(
    "TextClassificationDatasetMetadata",
    (_message.Message,),
    {
        "DESCRIPTOR": _TEXTCLASSIFICATIONDATASETMETADATA,
        "__module__": "google.cloud.automl_v1beta1.proto.text_pb2",
        "__doc__": """Dataset metadata for classification.
  
  
  Attributes:
      classification_type:
          Required. Type of the classification problem.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.TextClassificationDatasetMetadata)
    },
)
_sym_db.RegisterMessage(TextClassificationDatasetMetadata)

TextClassificationModelMetadata = _reflection.GeneratedProtocolMessageType(
    "TextClassificationModelMetadata",
    (_message.Message,),
    {
        "DESCRIPTOR": _TEXTCLASSIFICATIONMODELMETADATA,
        "__module__": "google.cloud.automl_v1beta1.proto.text_pb2",
        "__doc__": """Model metadata that is specific to text classification.
  
  
  Attributes:
      classification_type:
          Output only. Classification type of the dataset used to train
          this model.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.TextClassificationModelMetadata)
    },
)
_sym_db.RegisterMessage(TextClassificationModelMetadata)

TextExtractionDatasetMetadata = _reflection.GeneratedProtocolMessageType(
    "TextExtractionDatasetMetadata",
    (_message.Message,),
    {
        "DESCRIPTOR": _TEXTEXTRACTIONDATASETMETADATA,
        "__module__": "google.cloud.automl_v1beta1.proto.text_pb2",
        "__doc__": """Dataset metadata that is specific to text extraction
  
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.TextExtractionDatasetMetadata)
    },
)
_sym_db.RegisterMessage(TextExtractionDatasetMetadata)

TextExtractionModelMetadata = _reflection.GeneratedProtocolMessageType(
    "TextExtractionModelMetadata",
    (_message.Message,),
    {
        "DESCRIPTOR": _TEXTEXTRACTIONMODELMETADATA,
        "__module__": "google.cloud.automl_v1beta1.proto.text_pb2",
        "__doc__": """Model metadata that is specific to text extraction.
  
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.TextExtractionModelMetadata)
    },
)
_sym_db.RegisterMessage(TextExtractionModelMetadata)

TextSentimentDatasetMetadata = _reflection.GeneratedProtocolMessageType(
    "TextSentimentDatasetMetadata",
    (_message.Message,),
    {
        "DESCRIPTOR": _TEXTSENTIMENTDATASETMETADATA,
        "__module__": "google.cloud.automl_v1beta1.proto.text_pb2",
        "__doc__": """Dataset metadata for text sentiment.
  
  
  Attributes:
      sentiment_max:
          Required. A sentiment is expressed as an integer ordinal,
          where higher value means a more positive sentiment. The range
          of sentiments that will be used is between 0 and sentiment_max
          (inclusive on both ends), and all the values in the range must
          be represented in the dataset before a model can be created.
          sentiment_max value must be between 1 and 10 (inclusive).
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.TextSentimentDatasetMetadata)
    },
)
_sym_db.RegisterMessage(TextSentimentDatasetMetadata)

TextSentimentModelMetadata = _reflection.GeneratedProtocolMessageType(
    "TextSentimentModelMetadata",
    (_message.Message,),
    {
        "DESCRIPTOR": _TEXTSENTIMENTMODELMETADATA,
        "__module__": "google.cloud.automl_v1beta1.proto.text_pb2",
        "__doc__": """Model metadata that is specific to text sentiment.
  
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.TextSentimentModelMetadata)
    },
)
_sym_db.RegisterMessage(TextSentimentModelMetadata)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
