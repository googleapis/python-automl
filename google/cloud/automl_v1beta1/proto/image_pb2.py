# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/automl_v1beta1/proto/image.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.cloud.automl_v1beta1.proto import (
    annotation_spec_pb2 as google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_annotation__spec__pb2,
)
from google.cloud.automl_v1beta1.proto import (
    classification_pb2 as google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_classification__pb2,
)
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/automl_v1beta1/proto/image.proto",
    package="google.cloud.automl.v1beta1",
    syntax="proto3",
    serialized_options=b"\n\037com.google.cloud.automl.v1beta1B\nImageProtoP\001ZAgoogle.golang.org/genproto/googleapis/cloud/automl/v1beta1;automl\312\002\033Google\\Cloud\\AutoMl\\V1beta1\352\002\036Google::Cloud::AutoML::V1beta1",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n-google/cloud/automl_v1beta1/proto/image.proto\x12\x1bgoogle.cloud.automl.v1beta1\x1a\x19google/api/resource.proto\x1a\x37google/cloud/automl_v1beta1/proto/annotation_spec.proto\x1a\x36google/cloud/automl_v1beta1/proto/classification.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/api/annotations.proto"r\n"ImageClassificationDatasetMetadata\x12L\n\x13\x63lassification_type\x18\x01 \x01(\x0e\x32/.google.cloud.automl.v1beta1.ClassificationType"%\n#ImageObjectDetectionDatasetMetadata"\xb2\x01\n ImageClassificationModelMetadata\x12\x15\n\rbase_model_id\x18\x01 \x01(\t\x12\x14\n\x0ctrain_budget\x18\x02 \x01(\x03\x12\x12\n\ntrain_cost\x18\x03 \x01(\x03\x12\x13\n\x0bstop_reason\x18\x05 \x01(\t\x12\x12\n\nmodel_type\x18\x07 \x01(\t\x12\x10\n\x08node_qps\x18\r \x01(\x01\x12\x12\n\nnode_count\x18\x0e \x01(\x03"\xbe\x01\n!ImageObjectDetectionModelMetadata\x12\x12\n\nmodel_type\x18\x01 \x01(\t\x12\x12\n\nnode_count\x18\x03 \x01(\x03\x12\x10\n\x08node_qps\x18\x04 \x01(\x01\x12\x13\n\x0bstop_reason\x18\x05 \x01(\t\x12%\n\x1dtrain_budget_milli_node_hours\x18\x06 \x01(\x03\x12#\n\x1btrain_cost_milli_node_hours\x18\x07 \x01(\x03"@\n*ImageClassificationModelDeploymentMetadata\x12\x12\n\nnode_count\x18\x01 \x01(\x03"A\n+ImageObjectDetectionModelDeploymentMetadata\x12\x12\n\nnode_count\x18\x01 \x01(\x03\x42\xb1\x01\n\x1f\x63om.google.cloud.automl.v1beta1B\nImageProtoP\x01ZAgoogle.golang.org/genproto/googleapis/cloud/automl/v1beta1;automl\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1\xea\x02\x1eGoogle::Cloud::AutoML::V1beta1b\x06proto3',
    dependencies=[
        google_dot_api_dot_resource__pb2.DESCRIPTOR,
        google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_annotation__spec__pb2.DESCRIPTOR,
        google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_classification__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
    ],
)


_IMAGECLASSIFICATIONDATASETMETADATA = _descriptor.Descriptor(
    name="ImageClassificationDatasetMetadata",
    full_name="google.cloud.automl.v1beta1.ImageClassificationDatasetMetadata",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="classification_type",
            full_name="google.cloud.automl.v1beta1.ImageClassificationDatasetMetadata.classification_type",
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
            create_key=_descriptor._internal_create_key,
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
    serialized_start=281,
    serialized_end=395,
)


_IMAGEOBJECTDETECTIONDATASETMETADATA = _descriptor.Descriptor(
    name="ImageObjectDetectionDatasetMetadata",
    full_name="google.cloud.automl.v1beta1.ImageObjectDetectionDatasetMetadata",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=397,
    serialized_end=434,
)


_IMAGECLASSIFICATIONMODELMETADATA = _descriptor.Descriptor(
    name="ImageClassificationModelMetadata",
    full_name="google.cloud.automl.v1beta1.ImageClassificationModelMetadata",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="base_model_id",
            full_name="google.cloud.automl.v1beta1.ImageClassificationModelMetadata.base_model_id",
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
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="train_budget",
            full_name="google.cloud.automl.v1beta1.ImageClassificationModelMetadata.train_budget",
            index=1,
            number=2,
            type=3,
            cpp_type=2,
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
            name="train_cost",
            full_name="google.cloud.automl.v1beta1.ImageClassificationModelMetadata.train_cost",
            index=2,
            number=3,
            type=3,
            cpp_type=2,
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
            name="stop_reason",
            full_name="google.cloud.automl.v1beta1.ImageClassificationModelMetadata.stop_reason",
            index=3,
            number=5,
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
            name="model_type",
            full_name="google.cloud.automl.v1beta1.ImageClassificationModelMetadata.model_type",
            index=4,
            number=7,
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
            name="node_qps",
            full_name="google.cloud.automl.v1beta1.ImageClassificationModelMetadata.node_qps",
            index=5,
            number=13,
            type=1,
            cpp_type=5,
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
            name="node_count",
            full_name="google.cloud.automl.v1beta1.ImageClassificationModelMetadata.node_count",
            index=6,
            number=14,
            type=3,
            cpp_type=2,
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=437,
    serialized_end=615,
)


_IMAGEOBJECTDETECTIONMODELMETADATA = _descriptor.Descriptor(
    name="ImageObjectDetectionModelMetadata",
    full_name="google.cloud.automl.v1beta1.ImageObjectDetectionModelMetadata",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="model_type",
            full_name="google.cloud.automl.v1beta1.ImageObjectDetectionModelMetadata.model_type",
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
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="node_count",
            full_name="google.cloud.automl.v1beta1.ImageObjectDetectionModelMetadata.node_count",
            index=1,
            number=3,
            type=3,
            cpp_type=2,
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
            name="node_qps",
            full_name="google.cloud.automl.v1beta1.ImageObjectDetectionModelMetadata.node_qps",
            index=2,
            number=4,
            type=1,
            cpp_type=5,
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
            name="stop_reason",
            full_name="google.cloud.automl.v1beta1.ImageObjectDetectionModelMetadata.stop_reason",
            index=3,
            number=5,
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
            name="train_budget_milli_node_hours",
            full_name="google.cloud.automl.v1beta1.ImageObjectDetectionModelMetadata.train_budget_milli_node_hours",
            index=4,
            number=6,
            type=3,
            cpp_type=2,
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
            name="train_cost_milli_node_hours",
            full_name="google.cloud.automl.v1beta1.ImageObjectDetectionModelMetadata.train_cost_milli_node_hours",
            index=5,
            number=7,
            type=3,
            cpp_type=2,
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=618,
    serialized_end=808,
)


_IMAGECLASSIFICATIONMODELDEPLOYMENTMETADATA = _descriptor.Descriptor(
    name="ImageClassificationModelDeploymentMetadata",
    full_name="google.cloud.automl.v1beta1.ImageClassificationModelDeploymentMetadata",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="node_count",
            full_name="google.cloud.automl.v1beta1.ImageClassificationModelDeploymentMetadata.node_count",
            index=0,
            number=1,
            type=3,
            cpp_type=2,
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
    serialized_start=810,
    serialized_end=874,
)


_IMAGEOBJECTDETECTIONMODELDEPLOYMENTMETADATA = _descriptor.Descriptor(
    name="ImageObjectDetectionModelDeploymentMetadata",
    full_name="google.cloud.automl.v1beta1.ImageObjectDetectionModelDeploymentMetadata",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="node_count",
            full_name="google.cloud.automl.v1beta1.ImageObjectDetectionModelDeploymentMetadata.node_count",
            index=0,
            number=1,
            type=3,
            cpp_type=2,
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
    serialized_start=876,
    serialized_end=941,
)

_IMAGECLASSIFICATIONDATASETMETADATA.fields_by_name[
    "classification_type"
].enum_type = (
    google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_classification__pb2._CLASSIFICATIONTYPE
)
DESCRIPTOR.message_types_by_name[
    "ImageClassificationDatasetMetadata"
] = _IMAGECLASSIFICATIONDATASETMETADATA
DESCRIPTOR.message_types_by_name[
    "ImageObjectDetectionDatasetMetadata"
] = _IMAGEOBJECTDETECTIONDATASETMETADATA
DESCRIPTOR.message_types_by_name[
    "ImageClassificationModelMetadata"
] = _IMAGECLASSIFICATIONMODELMETADATA
DESCRIPTOR.message_types_by_name[
    "ImageObjectDetectionModelMetadata"
] = _IMAGEOBJECTDETECTIONMODELMETADATA
DESCRIPTOR.message_types_by_name[
    "ImageClassificationModelDeploymentMetadata"
] = _IMAGECLASSIFICATIONMODELDEPLOYMENTMETADATA
DESCRIPTOR.message_types_by_name[
    "ImageObjectDetectionModelDeploymentMetadata"
] = _IMAGEOBJECTDETECTIONMODELDEPLOYMENTMETADATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ImageClassificationDatasetMetadata = _reflection.GeneratedProtocolMessageType(
    "ImageClassificationDatasetMetadata",
    (_message.Message,),
    {
        "DESCRIPTOR": _IMAGECLASSIFICATIONDATASETMETADATA,
        "__module__": "google.cloud.automl_v1beta1.proto.image_pb2",
        "__doc__": """Dataset metadata that is specific to image classification.
  Attributes:
      classification_type:
          Required. Type of the classification problem.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.ImageClassificationDatasetMetadata)
    },
)
_sym_db.RegisterMessage(ImageClassificationDatasetMetadata)

ImageObjectDetectionDatasetMetadata = _reflection.GeneratedProtocolMessageType(
    "ImageObjectDetectionDatasetMetadata",
    (_message.Message,),
    {
        "DESCRIPTOR": _IMAGEOBJECTDETECTIONDATASETMETADATA,
        "__module__": "google.cloud.automl_v1beta1.proto.image_pb2",
        "__doc__": """Dataset metadata specific to image object detection.""",
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.ImageObjectDetectionDatasetMetadata)
    },
)
_sym_db.RegisterMessage(ImageObjectDetectionDatasetMetadata)

ImageClassificationModelMetadata = _reflection.GeneratedProtocolMessageType(
    "ImageClassificationModelMetadata",
    (_message.Message,),
    {
        "DESCRIPTOR": _IMAGECLASSIFICATIONMODELMETADATA,
        "__module__": "google.cloud.automl_v1beta1.proto.image_pb2",
        "__doc__": """Model metadata for image classification.
  Attributes:
      base_model_id:
          Optional. The ID of the ``base`` model. If it is specified,
          the new model will be created based on the ``base`` model.
          Otherwise, the new model will be created from scratch. The
          ``base`` model must be in the same ``project`` and
          ``location`` as the new model to create, and have the same
          ``model_type``.
      train_budget:
          Required. The train budget of creating this model, expressed
          in hours. The actual ``train_cost`` will be equal or less than
          this value.
      train_cost:
          Output only. The actual train cost of creating this model,
          expressed in hours. If this model is created from a ``base``
          model, the train cost used to create the ``base`` model are
          not included.
      stop_reason:
          Output only. The reason that this create model operation
          stopped, e.g. ``BUDGET_REACHED``, ``MODEL_CONVERGED``.
      model_type:
          Optional. Type of the model. The available values are: \*
          ``cloud`` - Model to be used via prediction calls to AutoML
          API. This is the default value. \* ``mobile-low-latency-1`` -
          A model that, in addition to providing prediction via AutoML
          API, can also be exported (see [AutoMl.ExportModel][google.clo
          ud.automl.v1beta1.AutoMl.ExportModel]) and used on a mobile or
          edge device with TensorFlow afterwards. Expected to have low
          latency, but may have lower prediction quality than other
          models. \* ``mobile-versatile-1`` - A model that, in addition
          to providing prediction via AutoML API, can also be exported
          (see [AutoMl.ExportModel][google.cloud.automl.v1beta1.AutoMl.E
          xportModel]) and used on a mobile or edge device with
          TensorFlow afterwards. \* ``mobile-high-accuracy-1`` - A model
          that, in addition to providing prediction via AutoML API, can
          also be exported (see [AutoMl.ExportModel][google.cloud.automl
          .v1beta1.AutoMl.ExportModel]) and used on a mobile or edge
          device with TensorFlow afterwards. Expected to have a higher
          latency, but should also have a higher prediction quality than
          other models. \* ``mobile-core-ml-low-latency-1`` - A model
          that, in addition to providing prediction via AutoML API, can
          also be exported (see [AutoMl.ExportModel][google.cloud.automl
          .v1beta1.AutoMl.ExportModel]) and used on a mobile device with
          Core ML afterwards. Expected to have low latency, but may have
          lower prediction quality than other models. \* ``mobile-core-
          ml-versatile-1`` - A model that, in addition to providing
          prediction via AutoML API, can also be exported (see [AutoMl.E
          xportModel][google.cloud.automl.v1beta1.AutoMl.ExportModel])
          and used on a mobile device with Core ML afterwards. \*
          ``mobile-core-ml-high-accuracy-1`` - A model that, in addition
          to providing prediction via AutoML API, can also be exported
          (see [AutoMl.ExportModel][google.cloud.automl.v1beta1.AutoMl.E
          xportModel]) and used on a mobile device with Core ML
          afterwards. Expected to have a higher latency, but should also
          have a higher prediction quality than other models.
      node_qps:
          Output only. An approximate number of online prediction QPS
          that can be supported by this model per each node on which it
          is deployed.
      node_count:
          Output only. The number of nodes this model is deployed on. A
          node is an abstraction of a machine resource, which can handle
          online prediction QPS as given in the node_qps field.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.ImageClassificationModelMetadata)
    },
)
_sym_db.RegisterMessage(ImageClassificationModelMetadata)

ImageObjectDetectionModelMetadata = _reflection.GeneratedProtocolMessageType(
    "ImageObjectDetectionModelMetadata",
    (_message.Message,),
    {
        "DESCRIPTOR": _IMAGEOBJECTDETECTIONMODELMETADATA,
        "__module__": "google.cloud.automl_v1beta1.proto.image_pb2",
        "__doc__": """Model metadata specific to image object detection.
  Attributes:
      model_type:
          Optional. Type of the model. The available values are: \*
          ``cloud-high-accuracy-1`` - (default) A model to be used via
          prediction calls to AutoML API. Expected to have a higher
          latency, but should also have a higher prediction quality than
          other models. \* ``cloud-low-latency-1`` - A model to be used
          via prediction calls to AutoML API. Expected to have low
          latency, but may have lower prediction quality than other
          models. \* ``mobile-low-latency-1`` - A model that, in
          addition to providing prediction via AutoML API, can also be
          exported (see [AutoMl.ExportModel][google.cloud.automl.v1beta1
          .AutoMl.ExportModel]) and used on a mobile or edge device with
          TensorFlow afterwards. Expected to have low latency, but may
          have lower prediction quality than other models. \* ``mobile-
          versatile-1`` - A model that, in addition to providing
          prediction via AutoML API, can also be exported (see [AutoMl.E
          xportModel][google.cloud.automl.v1beta1.AutoMl.ExportModel])
          and used on a mobile or edge device with TensorFlow
          afterwards. \* ``mobile-high-accuracy-1`` - A model that, in
          addition to providing prediction via AutoML API, can also be
          exported (see [AutoMl.ExportModel][google.cloud.automl.v1beta1
          .AutoMl.ExportModel]) and used on a mobile or edge device with
          TensorFlow afterwards. Expected to have a higher latency, but
          should also have a higher prediction quality than other
          models.
      node_count:
          Output only. The number of nodes this model is deployed on. A
          node is an abstraction of a machine resource, which can handle
          online prediction QPS as given in the qps_per_node field.
      node_qps:
          Output only. An approximate number of online prediction QPS
          that can be supported by this model per each node on which it
          is deployed.
      stop_reason:
          Output only. The reason that this create model operation
          stopped, e.g. ``BUDGET_REACHED``, ``MODEL_CONVERGED``.
      train_budget_milli_node_hours:
          The train budget of creating this model, expressed in milli
          node hours i.e. 1,000 value in this field means 1 node hour.
          The actual ``train_cost`` will be equal or less than this
          value. If further model training ceases to provide any
          improvements, it will stop without using full budget and the
          stop_reason will be ``MODEL_CONVERGED``. Note, node_hour =
          actual_hour \* number_of_nodes_invovled. For model type
          ``cloud-high-accuracy-1``\ (default) and ``cloud-low-
          latency-1``, the train budget must be between 20,000 and
          900,000 milli node hours, inclusive. The default value is 216,
          000 which represents one day in wall time. For model type
          ``mobile-low-latency-1``, ``mobile-versatile-1``, ``mobile-
          high-accuracy-1``, ``mobile-core-ml-low-latency-1``, ``mobile-
          core-ml-versatile-1``, ``mobile-core-ml-high-accuracy-1``, the
          train budget must be between 1,000 and 100,000 milli node
          hours, inclusive. The default value is 24, 000 which
          represents one day in wall time.
      train_cost_milli_node_hours:
          Output only. The actual train cost of creating this model,
          expressed in milli node hours, i.e. 1,000 value in this field
          means 1 node hour. Guaranteed to not exceed the train budget.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.ImageObjectDetectionModelMetadata)
    },
)
_sym_db.RegisterMessage(ImageObjectDetectionModelMetadata)

ImageClassificationModelDeploymentMetadata = _reflection.GeneratedProtocolMessageType(
    "ImageClassificationModelDeploymentMetadata",
    (_message.Message,),
    {
        "DESCRIPTOR": _IMAGECLASSIFICATIONMODELDEPLOYMENTMETADATA,
        "__module__": "google.cloud.automl_v1beta1.proto.image_pb2",
        "__doc__": """Model deployment metadata specific to Image Classification.
  Attributes:
      node_count:
          Input only. The number of nodes to deploy the model on. A node
          is an abstraction of a machine resource, which can handle
          online prediction QPS as given in the model’s  [node_qps][goog
          le.cloud.automl.v1beta1.ImageClassificationModelMetadata.node_
          qps]. Must be between 1 and 100, inclusive on both ends.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.ImageClassificationModelDeploymentMetadata)
    },
)
_sym_db.RegisterMessage(ImageClassificationModelDeploymentMetadata)

ImageObjectDetectionModelDeploymentMetadata = _reflection.GeneratedProtocolMessageType(
    "ImageObjectDetectionModelDeploymentMetadata",
    (_message.Message,),
    {
        "DESCRIPTOR": _IMAGEOBJECTDETECTIONMODELDEPLOYMENTMETADATA,
        "__module__": "google.cloud.automl_v1beta1.proto.image_pb2",
        "__doc__": """Model deployment metadata specific to Image Object Detection.
  Attributes:
      node_count:
          Input only. The number of nodes to deploy the model on. A node
          is an abstraction of a machine resource, which can handle
          online prediction QPS as given in the model’s  [qps_per_node][
          google.cloud.automl.v1beta1.ImageObjectDetectionModelMetadata.
          qps_per_node]. Must be between 1 and 100, inclusive on both
          ends.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.ImageObjectDetectionModelDeploymentMetadata)
    },
)
_sym_db.RegisterMessage(ImageObjectDetectionModelDeploymentMetadata)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
