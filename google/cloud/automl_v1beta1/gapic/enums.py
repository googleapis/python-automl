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


class NullValue(enum.IntEnum):
    """
    Output only. Metrics are computed with an assumption that the model
    always returns at most this many predictions (ordered by their score,
    descendingly), but they all still need to meet the confidence_threshold.

    Attributes:
      NULL_VALUE (int): Null value.
    """

    NULL_VALUE = 0


class TypeCode(enum.IntEnum):
    """
    Output only. The number of examples used for model evaluation, i.e.
    for which ground truth from time of model creation is compared against
    the predicted annotations created by the model. For overall
    ModelEvaluation (i.e. with annotation_spec_id not set) this is the total
    number of all examples used for evaluation. Otherwise, this is the count
    of examples that according to the ground truth were annotated by the

    ``annotation_spec_id``.

    Attributes:
      TYPE_CODE_UNSPECIFIED (int): Not specified. Should not be used.
      FLOAT64 (int): The position of the ``text_segment`` in the page. Contains exactly 4

      ``normalized_vertices`` and they are connected by edges in the order
      provided, which will represent a rectangle parallel to the frame. The
      ``NormalizedVertex-s`` are relative to the page. Coordinates are based
      on top-left as point (0,0).
      TIMESTAMP (int): Output only. Auxiliary information for each of the model's

      ``input_feature_column_specs`` with respect to this particular
      prediction. If no other fields than

      ``column_spec_name`` and

      ``column_display_name`` would be populated, then this whole field is
      not.
      STRING (int): The statistics of the top 20 CATEGORY values, ordered by

      ``count``.
      ARRAY (int): Required. BigQuery URI to a project, up to 2000 characters long.
      Accepted forms:

      -  BigQuery path e.g. bq://projectId
      STRUCT (int): The type of the ``text_segment`` in document.
      CATEGORY (int): Protocol Buffers - Google's data interchange format Copyright 2008
      Google Inc. All rights reserved.
      https://developers.google.com/protocol-buffers/

      Redistribution and use in source and binary forms, with or without
      modification, are permitted provided that the following conditions are
      met:

      ::

          * Redistributions of source code must retain the above copyright

      notice, this list of conditions and the following disclaimer. \*
      Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution. \*
      Neither the name of Google Inc. nor the names of its contributors may be
      used to endorse or promote products derived from this software without
      specific prior written permission.

      THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
      IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
      TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
      PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER
      OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
      EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
      PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
      PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
      LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
      NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
      SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
    """

    TYPE_CODE_UNSPECIFIED = 0
    FLOAT64 = 3
    TIMESTAMP = 4
    STRING = 6
    ARRAY = 8
    STRUCT = 9
    CATEGORY = 10


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
              FORM_FIELD_NAME (int): Exports examples on which the model was evaluated (i.e. which were
              in the TEST set of the dataset the model was created from), together
              with their ground truth annotations and the annotations created
              (predicted) by the model. The examples, ground truth and predictions are
              exported in the state they were at the moment the model was evaluated.

              This export is available only for 30 days since the model evaluation is
              created.

              Currently only available for Tables.

              Returns an empty response in the ``response`` field when it completes.
              FORM_FIELD_CONTENTS (int): AutoML Prediction API.

              On any input that is documented to expect a string parameter in
              snake_case or kebab-case, either of those cases is accepted.
              TABLE (int): The text segment is a whole table, including headers, and all rows.
              TABLE_HEADER (int): The text segment is a table's headers. It will be treated as child of
              another TABLE TextSegment if its span is subspan of another TextSegment
              with type TABLE.
              TABLE_ROW (int): The text segment is a row in table. It will be treated as child of
              another TABLE TextSegment if its span is subspan of another TextSegment
              with type TABLE.
              TABLE_CELL (int): Encoded as ``struct``, where field values are represented according
              to ``struct_type``.
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
