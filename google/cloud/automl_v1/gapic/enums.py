# -*- coding: utf-8 -*-
#
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Wrappers for protocol buffer enum types."""

import enum


class ClassificationType(enum.IntEnum):
    """
    Type of the classification problem.

    Attributes:
      CLASSIFICATION_TYPE_UNSPECIFIED (int): An un-set value of this enum.
      MULTICLASS (int): At most one label is allowed per example.
      MULTILABEL (int): Multiple labels are allowed for one example.
    """

    CLASSIFICATION_TYPE_UNSPECIFIED = 0
    MULTICLASS = 1
    MULTILABEL = 2


class Document(object):
    class Layout(object):
        class TextSegmentType(enum.IntEnum):
            """
            The type of TextSegment in the context of the original document.

            Attributes:
              TEXT_SEGMENT_TYPE_UNSPECIFIED (int): Should not be used.
              TOKEN (int): The text segment is a token. e.g. word.
              PARAGRAPH (int): The text segment is a paragraph.
              FORM_FIELD (int): The text segment is a form field.
              FORM_FIELD_NAME (int): Deploys a model. If a model is already deployed, deploying it with
              the same parameters has no effect. Deploying with different parametrs
              (as e.g. changing

              ``node_number``) will reset the deployment state without pausing the
              model's availability.

              Only applicable for Text Classification, Image Object Detection ,
              Tables, and Image Segmentation; all other domains manage deployment
              automatically.

              Returns an empty response in the ``response`` field when it completes.
              FORM_FIELD_CONTENTS (int): Output only. IDs of the annotation specs used in the confusion
              matrix. For Tables CLASSIFICATION

              ``prediction_type`` only list of ``annotation_spec_display_name-s`` is
              populated.
              TABLE (int): The text segment is a whole table, including headers, and all rows.
              TABLE_HEADER (int): The text segment is a table's headers. It will be treated as child of
              another TABLE TextSegment if its span is subspan of another TextSegment
              with type TABLE.
              TABLE_ROW (int): The text segment is a row in table. It will be treated as child of
              another TABLE TextSegment if its span is subspan of another TextSegment
              with type TABLE.
              TABLE_CELL (int): The train budget of creating this model, expressed in milli node
              hours i.e. 1,000 value in this field means 1 node hour. The actual
              ``train_cost`` will be equal or less than this value. If further model
              training ceases to provide any improvements, it will stop without using
              full budget and the stop_reason will be ``MODEL_CONVERGED``. Note,
              node_hour = actual_hour \* number_of_nodes_invovled. For model type
              ``cloud``\ (default), the train budget must be between 8,000 and 800,000
              milli node hours, inclusive. The default value is 192, 000 which
              represents one day in wall time. For model type
              ``mobile-low-latency-1``, ``mobile-versatile-1``,
              ``mobile-high-accuracy-1``, ``mobile-core-ml-low-latency-1``,
              ``mobile-core-ml-versatile-1``, ``mobile-core-ml-high-accuracy-1``, the
              train budget must be between 1,000 and 100,000 milli node hours,
              inclusive. The default value is 24, 000 which represents one day in wall
              time.
            """

            TEXT_SEGMENT_TYPE_UNSPECIFIED = 0
            TOKEN = 1
            PARAGRAPH = 2
            FORM_FIELD = 3
            FORM_FIELD_NAME = 4
            FORM_FIELD_CONTENTS = 5
            TABLE = 6
            TABLE_HEADER = 7
            TABLE_ROW = 8
            TABLE_CELL = 9


class DocumentDimensions(object):
    class DocumentDimensionUnit(enum.IntEnum):
        """
        Unit of the document dimension.

        Attributes:
          DOCUMENT_DIMENSION_UNIT_UNSPECIFIED (int): Should not be used.
          INCH (int): Document dimension is measured in inches.
          CENTIMETER (int): Document dimension is measured in centimeters.
          POINT (int): Document dimension is measured in points. 72 points = 1 inch.
        """

        DOCUMENT_DIMENSION_UNIT_UNSPECIFIED = 0
        INCH = 1
        CENTIMETER = 2
        POINT = 3


class Model(object):
    class DeploymentState(enum.IntEnum):
        """
        Deployment state of the model.

        Attributes:
          DEPLOYMENT_STATE_UNSPECIFIED (int): Should not be used, an un-set enum has this value by default.
          DEPLOYED (int): Model is deployed.
          UNDEPLOYED (int): Model is not deployed.
        """

        DEPLOYMENT_STATE_UNSPECIFIED = 0
        DEPLOYED = 1
        UNDEPLOYED = 2
