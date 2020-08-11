# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/automl_v1beta1/proto/text_extraction.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.cloud.automl_v1beta1.proto import (
    text_segment_pb2 as google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_text__segment__pb2,
)
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/automl_v1beta1/proto/text_extraction.proto",
    package="google.cloud.automl.v1beta1",
    syntax="proto3",
    serialized_options=b"\n\037com.google.cloud.automl.v1beta1P\001ZAgoogle.golang.org/genproto/googleapis/cloud/automl/v1beta1;automl\312\002\033Google\\Cloud\\AutoMl\\V1beta1\352\002\036Google::Cloud::AutoML::V1beta1",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n7google/cloud/automl_v1beta1/proto/text_extraction.proto\x12\x1bgoogle.cloud.automl.v1beta1\x1a\x34google/cloud/automl_v1beta1/proto/text_segment.proto\x1a\x1cgoogle/api/annotations.proto"y\n\x18TextExtractionAnnotation\x12@\n\x0ctext_segment\x18\x03 \x01(\x0b\x32(.google.cloud.automl.v1beta1.TextSegmentH\x00\x12\r\n\x05score\x18\x01 \x01(\x02\x42\x0c\n\nannotation"\x97\x02\n\x1fTextExtractionEvaluationMetrics\x12\x0e\n\x06\x61u_prc\x18\x01 \x01(\x02\x12w\n\x1a\x63onfidence_metrics_entries\x18\x02 \x03(\x0b\x32S.google.cloud.automl.v1beta1.TextExtractionEvaluationMetrics.ConfidenceMetricsEntry\x1ak\n\x16\x43onfidenceMetricsEntry\x12\x1c\n\x14\x63onfidence_threshold\x18\x01 \x01(\x02\x12\x0e\n\x06recall\x18\x03 \x01(\x02\x12\x11\n\tprecision\x18\x04 \x01(\x02\x12\x10\n\x08\x66\x31_score\x18\x05 \x01(\x02\x42\xa5\x01\n\x1f\x63om.google.cloud.automl.v1beta1P\x01ZAgoogle.golang.org/genproto/googleapis/cloud/automl/v1beta1;automl\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1\xea\x02\x1eGoogle::Cloud::AutoML::V1beta1b\x06proto3',
    dependencies=[
        google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_text__segment__pb2.DESCRIPTOR,
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
    ],
)


_TEXTEXTRACTIONANNOTATION = _descriptor.Descriptor(
    name="TextExtractionAnnotation",
    full_name="google.cloud.automl.v1beta1.TextExtractionAnnotation",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="text_segment",
            full_name="google.cloud.automl.v1beta1.TextExtractionAnnotation.text_segment",
            index=0,
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
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="score",
            full_name="google.cloud.automl.v1beta1.TextExtractionAnnotation.score",
            index=1,
            number=1,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
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
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="annotation",
            full_name="google.cloud.automl.v1beta1.TextExtractionAnnotation.annotation",
            index=0,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        ),
    ],
    serialized_start=172,
    serialized_end=293,
)


_TEXTEXTRACTIONEVALUATIONMETRICS_CONFIDENCEMETRICSENTRY = _descriptor.Descriptor(
    name="ConfidenceMetricsEntry",
    full_name="google.cloud.automl.v1beta1.TextExtractionEvaluationMetrics.ConfidenceMetricsEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="confidence_threshold",
            full_name="google.cloud.automl.v1beta1.TextExtractionEvaluationMetrics.ConfidenceMetricsEntry.confidence_threshold",
            index=0,
            number=1,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
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
            name="recall",
            full_name="google.cloud.automl.v1beta1.TextExtractionEvaluationMetrics.ConfidenceMetricsEntry.recall",
            index=1,
            number=3,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
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
            name="precision",
            full_name="google.cloud.automl.v1beta1.TextExtractionEvaluationMetrics.ConfidenceMetricsEntry.precision",
            index=2,
            number=4,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
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
            name="f1_score",
            full_name="google.cloud.automl.v1beta1.TextExtractionEvaluationMetrics.ConfidenceMetricsEntry.f1_score",
            index=3,
            number=5,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
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
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=468,
    serialized_end=575,
)

_TEXTEXTRACTIONEVALUATIONMETRICS = _descriptor.Descriptor(
    name="TextExtractionEvaluationMetrics",
    full_name="google.cloud.automl.v1beta1.TextExtractionEvaluationMetrics",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="au_prc",
            full_name="google.cloud.automl.v1beta1.TextExtractionEvaluationMetrics.au_prc",
            index=0,
            number=1,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
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
            name="confidence_metrics_entries",
            full_name="google.cloud.automl.v1beta1.TextExtractionEvaluationMetrics.confidence_metrics_entries",
            index=1,
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
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[_TEXTEXTRACTIONEVALUATIONMETRICS_CONFIDENCEMETRICSENTRY,],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=296,
    serialized_end=575,
)

_TEXTEXTRACTIONANNOTATION.fields_by_name[
    "text_segment"
].message_type = (
    google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_text__segment__pb2._TEXTSEGMENT
)
_TEXTEXTRACTIONANNOTATION.oneofs_by_name["annotation"].fields.append(
    _TEXTEXTRACTIONANNOTATION.fields_by_name["text_segment"]
)
_TEXTEXTRACTIONANNOTATION.fields_by_name[
    "text_segment"
].containing_oneof = _TEXTEXTRACTIONANNOTATION.oneofs_by_name["annotation"]
_TEXTEXTRACTIONEVALUATIONMETRICS_CONFIDENCEMETRICSENTRY.containing_type = (
    _TEXTEXTRACTIONEVALUATIONMETRICS
)
_TEXTEXTRACTIONEVALUATIONMETRICS.fields_by_name[
    "confidence_metrics_entries"
].message_type = _TEXTEXTRACTIONEVALUATIONMETRICS_CONFIDENCEMETRICSENTRY
DESCRIPTOR.message_types_by_name["TextExtractionAnnotation"] = _TEXTEXTRACTIONANNOTATION
DESCRIPTOR.message_types_by_name[
    "TextExtractionEvaluationMetrics"
] = _TEXTEXTRACTIONEVALUATIONMETRICS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TextExtractionAnnotation = _reflection.GeneratedProtocolMessageType(
    "TextExtractionAnnotation",
    (_message.Message,),
    {
        "DESCRIPTOR": _TEXTEXTRACTIONANNOTATION,
        "__module__": "google.cloud.automl_v1beta1.proto.text_extraction_pb2",
        "__doc__": """Annotation for identifying spans of text.
  
  Attributes:
      annotation:
          Required. Text extraction annotations can either be a text
          segment or a text relation.
      text_segment:
          An entity annotation will set this, which is the part of the
          original text to which the annotation pertains.
      score:
          Output only. A confidence estimate between 0.0 and 1.0. A
          higher value means greater confidence in correctness of the
          annotation.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.TextExtractionAnnotation)
    },
)
_sym_db.RegisterMessage(TextExtractionAnnotation)

TextExtractionEvaluationMetrics = _reflection.GeneratedProtocolMessageType(
    "TextExtractionEvaluationMetrics",
    (_message.Message,),
    {
        "ConfidenceMetricsEntry": _reflection.GeneratedProtocolMessageType(
            "ConfidenceMetricsEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _TEXTEXTRACTIONEVALUATIONMETRICS_CONFIDENCEMETRICSENTRY,
                "__module__": "google.cloud.automl_v1beta1.proto.text_extraction_pb2",
                "__doc__": """Metrics for a single confidence threshold.
    
    Attributes:
        confidence_threshold:
            Output only. The confidence threshold value used to compute
            the metrics. Only annotations with score of at least this
            threshold are considered to be ones the model would return.
        recall:
            Output only. Recall under the given confidence threshold.
        precision:
            Output only. Precision under the given confidence threshold.
        f1_score:
            Output only. The harmonic mean of recall and precision.
    """,
                # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.TextExtractionEvaluationMetrics.ConfidenceMetricsEntry)
            },
        ),
        "DESCRIPTOR": _TEXTEXTRACTIONEVALUATIONMETRICS,
        "__module__": "google.cloud.automl_v1beta1.proto.text_extraction_pb2",
        "__doc__": """Model evaluation metrics for text extraction problems.
  
  Attributes:
      au_prc:
          Output only. The Area under precision recall curve metric.
      confidence_metrics_entries:
          Output only. Metrics that have confidence thresholds.
          Precision-recall curve can be derived from it.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.TextExtractionEvaluationMetrics)
    },
)
_sym_db.RegisterMessage(TextExtractionEvaluationMetrics)
_sym_db.RegisterMessage(TextExtractionEvaluationMetrics.ConfidenceMetricsEntry)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
