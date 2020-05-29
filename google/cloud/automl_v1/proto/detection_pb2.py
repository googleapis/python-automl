# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/automl_v1/proto/detection.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.cloud.automl_v1.proto import (
    geometry_pb2 as google_dot_cloud_dot_automl__v1_dot_proto_dot_geometry__pb2,
)
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/automl_v1/proto/detection.proto",
    package="google.cloud.automl.v1",
    syntax="proto3",
    serialized_options=b"\n\032com.google.cloud.automl.v1P\001Z<google.golang.org/genproto/googleapis/cloud/automl/v1;automl\252\002\026Google.Cloud.AutoML.V1\312\002\026Google\\Cloud\\AutoMl\\V1\352\002\031Google::Cloud::AutoML::V1",
    serialized_pb=b'\n,google/cloud/automl_v1/proto/detection.proto\x12\x16google.cloud.automl.v1\x1a+google/cloud/automl_v1/proto/geometry.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1cgoogle/api/annotations.proto"k\n\x1eImageObjectDetectionAnnotation\x12:\n\x0c\x62ounding_box\x18\x01 \x01(\x0b\x32$.google.cloud.automl.v1.BoundingPoly\x12\r\n\x05score\x18\x02 \x01(\x02"\xa9\x02\n\x17\x42oundingBoxMetricsEntry\x12\x15\n\riou_threshold\x18\x01 \x01(\x02\x12\x1e\n\x16mean_average_precision\x18\x02 \x01(\x02\x12j\n\x1a\x63onfidence_metrics_entries\x18\x03 \x03(\x0b\x32\x46.google.cloud.automl.v1.BoundingBoxMetricsEntry.ConfidenceMetricsEntry\x1ak\n\x16\x43onfidenceMetricsEntry\x12\x1c\n\x14\x63onfidence_threshold\x18\x01 \x01(\x02\x12\x0e\n\x06recall\x18\x02 \x01(\x02\x12\x11\n\tprecision\x18\x03 \x01(\x02\x12\x10\n\x08\x66\x31_score\x18\x04 \x01(\x02"\xd1\x01\n%ImageObjectDetectionEvaluationMetrics\x12$\n\x1c\x65valuated_bounding_box_count\x18\x01 \x01(\x05\x12U\n\x1c\x62ounding_box_metrics_entries\x18\x02 \x03(\x0b\x32/.google.cloud.automl.v1.BoundingBoxMetricsEntry\x12+\n#bounding_box_mean_average_precision\x18\x03 \x01(\x02\x42\xaa\x01\n\x1a\x63om.google.cloud.automl.v1P\x01Z<google.golang.org/genproto/googleapis/cloud/automl/v1;automl\xaa\x02\x16Google.Cloud.AutoML.V1\xca\x02\x16Google\\Cloud\\AutoMl\\V1\xea\x02\x19Google::Cloud::AutoML::V1b\x06proto3',
    dependencies=[
        google_dot_cloud_dot_automl__v1_dot_proto_dot_geometry__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
    ],
)


_IMAGEOBJECTDETECTIONANNOTATION = _descriptor.Descriptor(
    name="ImageObjectDetectionAnnotation",
    full_name="google.cloud.automl.v1.ImageObjectDetectionAnnotation",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="bounding_box",
            full_name="google.cloud.automl.v1.ImageObjectDetectionAnnotation.bounding_box",
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
            name="score",
            full_name="google.cloud.automl.v1.ImageObjectDetectionAnnotation.score",
            index=1,
            number=2,
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
    serialized_start=179,
    serialized_end=286,
)


_BOUNDINGBOXMETRICSENTRY_CONFIDENCEMETRICSENTRY = _descriptor.Descriptor(
    name="ConfidenceMetricsEntry",
    full_name="google.cloud.automl.v1.BoundingBoxMetricsEntry.ConfidenceMetricsEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="confidence_threshold",
            full_name="google.cloud.automl.v1.BoundingBoxMetricsEntry.ConfidenceMetricsEntry.confidence_threshold",
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
        ),
        _descriptor.FieldDescriptor(
            name="recall",
            full_name="google.cloud.automl.v1.BoundingBoxMetricsEntry.ConfidenceMetricsEntry.recall",
            index=1,
            number=2,
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
        ),
        _descriptor.FieldDescriptor(
            name="precision",
            full_name="google.cloud.automl.v1.BoundingBoxMetricsEntry.ConfidenceMetricsEntry.precision",
            index=2,
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
        ),
        _descriptor.FieldDescriptor(
            name="f1_score",
            full_name="google.cloud.automl.v1.BoundingBoxMetricsEntry.ConfidenceMetricsEntry.f1_score",
            index=3,
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
    serialized_start=479,
    serialized_end=586,
)

_BOUNDINGBOXMETRICSENTRY = _descriptor.Descriptor(
    name="BoundingBoxMetricsEntry",
    full_name="google.cloud.automl.v1.BoundingBoxMetricsEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="iou_threshold",
            full_name="google.cloud.automl.v1.BoundingBoxMetricsEntry.iou_threshold",
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
        ),
        _descriptor.FieldDescriptor(
            name="mean_average_precision",
            full_name="google.cloud.automl.v1.BoundingBoxMetricsEntry.mean_average_precision",
            index=1,
            number=2,
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
        ),
        _descriptor.FieldDescriptor(
            name="confidence_metrics_entries",
            full_name="google.cloud.automl.v1.BoundingBoxMetricsEntry.confidence_metrics_entries",
            index=2,
            number=3,
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
    ],
    extensions=[],
    nested_types=[_BOUNDINGBOXMETRICSENTRY_CONFIDENCEMETRICSENTRY],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=289,
    serialized_end=586,
)


_IMAGEOBJECTDETECTIONEVALUATIONMETRICS = _descriptor.Descriptor(
    name="ImageObjectDetectionEvaluationMetrics",
    full_name="google.cloud.automl.v1.ImageObjectDetectionEvaluationMetrics",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="evaluated_bounding_box_count",
            full_name="google.cloud.automl.v1.ImageObjectDetectionEvaluationMetrics.evaluated_bounding_box_count",
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
        ),
        _descriptor.FieldDescriptor(
            name="bounding_box_metrics_entries",
            full_name="google.cloud.automl.v1.ImageObjectDetectionEvaluationMetrics.bounding_box_metrics_entries",
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
        ),
        _descriptor.FieldDescriptor(
            name="bounding_box_mean_average_precision",
            full_name="google.cloud.automl.v1.ImageObjectDetectionEvaluationMetrics.bounding_box_mean_average_precision",
            index=2,
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
    serialized_start=589,
    serialized_end=798,
)

_IMAGEOBJECTDETECTIONANNOTATION.fields_by_name[
    "bounding_box"
].message_type = (
    google_dot_cloud_dot_automl__v1_dot_proto_dot_geometry__pb2._BOUNDINGPOLY
)
_BOUNDINGBOXMETRICSENTRY_CONFIDENCEMETRICSENTRY.containing_type = (
    _BOUNDINGBOXMETRICSENTRY
)
_BOUNDINGBOXMETRICSENTRY.fields_by_name[
    "confidence_metrics_entries"
].message_type = _BOUNDINGBOXMETRICSENTRY_CONFIDENCEMETRICSENTRY
_IMAGEOBJECTDETECTIONEVALUATIONMETRICS.fields_by_name[
    "bounding_box_metrics_entries"
].message_type = _BOUNDINGBOXMETRICSENTRY
DESCRIPTOR.message_types_by_name[
    "ImageObjectDetectionAnnotation"
] = _IMAGEOBJECTDETECTIONANNOTATION
DESCRIPTOR.message_types_by_name["BoundingBoxMetricsEntry"] = _BOUNDINGBOXMETRICSENTRY
DESCRIPTOR.message_types_by_name[
    "ImageObjectDetectionEvaluationMetrics"
] = _IMAGEOBJECTDETECTIONEVALUATIONMETRICS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ImageObjectDetectionAnnotation = _reflection.GeneratedProtocolMessageType(
    "ImageObjectDetectionAnnotation",
    (_message.Message,),
    {
        "DESCRIPTOR": _IMAGEOBJECTDETECTIONANNOTATION,
        "__module__": "google.cloud.automl_v1.proto.detection_pb2",
        "__doc__": """Annotation details for image object detection.
  Attributes:
      bounding_box:
          Output only. The rectangle representing the object location.
      score:
          Output only. The confidence that this annotation is positive
          for the parent example, value in [0, 1], higher means higher
          positivity confidence.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.ImageObjectDetectionAnnotation)
    },
)
_sym_db.RegisterMessage(ImageObjectDetectionAnnotation)

BoundingBoxMetricsEntry = _reflection.GeneratedProtocolMessageType(
    "BoundingBoxMetricsEntry",
    (_message.Message,),
    {
        "ConfidenceMetricsEntry": _reflection.GeneratedProtocolMessageType(
            "ConfidenceMetricsEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _BOUNDINGBOXMETRICSENTRY_CONFIDENCEMETRICSENTRY,
                "__module__": "google.cloud.automl_v1.proto.detection_pb2",
                "__doc__": """Metrics for a single confidence threshold.
    Attributes:
        confidence_threshold:
            Output only. The confidence threshold value used to compute
            the metrics.
        recall:
            Output only. Recall under the given confidence threshold.
        precision:
            Output only. Precision under the given confidence threshold.
        f1_score:
            Output only. The harmonic mean of recall and precision.
    """,
                # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.BoundingBoxMetricsEntry.ConfidenceMetricsEntry)
            },
        ),
        "DESCRIPTOR": _BOUNDINGBOXMETRICSENTRY,
        "__module__": "google.cloud.automl_v1.proto.detection_pb2",
        "__doc__": """Bounding box matching model metrics for a single intersection-over-
  union threshold and multiple label match confidence thresholds.
  Attributes:
      iou_threshold:
          Output only. The intersection-over-union threshold value used
          to compute this metrics entry.
      mean_average_precision:
          Output only. The mean average precision, most often close to
          au_prc.
      confidence_metrics_entries:
          Output only. Metrics for each label-match confidence_threshold
          from 0.05,0.10,…,0.95,0.96,0.97,0.98,0.99. Precision-recall
          curve is derived from them.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.BoundingBoxMetricsEntry)
    },
)
_sym_db.RegisterMessage(BoundingBoxMetricsEntry)
_sym_db.RegisterMessage(BoundingBoxMetricsEntry.ConfidenceMetricsEntry)

ImageObjectDetectionEvaluationMetrics = _reflection.GeneratedProtocolMessageType(
    "ImageObjectDetectionEvaluationMetrics",
    (_message.Message,),
    {
        "DESCRIPTOR": _IMAGEOBJECTDETECTIONEVALUATIONMETRICS,
        "__module__": "google.cloud.automl_v1.proto.detection_pb2",
        "__doc__": """Model evaluation metrics for image object detection problems.
  Evaluates prediction quality of labeled bounding boxes.
  Attributes:
      evaluated_bounding_box_count:
          Output only. The total number of bounding boxes (i.e. summed
          over all images) the ground truth used to create this
          evaluation had.
      bounding_box_metrics_entries:
          Output only. The bounding boxes match metrics for each
          Intersection-over-union threshold
          0.05,0.10,…,0.95,0.96,0.97,0.98,0.99 and each label confidence
          threshold 0.05,0.10,…,0.95,0.96,0.97,0.98,0.99 pair.
      bounding_box_mean_average_precision:
          Output only. The single metric for bounding boxes evaluation:
          the mean_average_precision averaged over all
          bounding_box_metrics_entries.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.ImageObjectDetectionEvaluationMetrics)
    },
)
_sym_db.RegisterMessage(ImageObjectDetectionEvaluationMetrics)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
