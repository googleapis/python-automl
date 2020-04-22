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


import google.api_core.grpc_helpers
import google.api_core.operations_v1

from google.cloud.automl_v1beta1.proto import service_pb2_grpc


class AutoMlGrpcTransport(object):
    """gRPC transport class providing stubs for
    google.cloud.automl.v1beta1 AutoMl API.

    The transport provides access to the raw gRPC stubs,
    which can be used to take advantage of advanced
    features of gRPC.
    """

    # The scopes needed to make gRPC calls to all of the methods defined
    # in this service.
    _OAUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    def __init__(
        self, channel=None, credentials=None, address="automl.googleapis.com:443"
    ):
        """Instantiate the transport class.

        Args:
            channel (grpc.Channel): A ``Channel`` instance through
                which to make calls. This argument is mutually exclusive
                with ``credentials``; providing both will raise an exception.
            credentials (google.auth.credentials.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            address (str): The address where the service is hosted.
        """
        # If both `channel` and `credentials` are specified, raise an
        # exception (channels come with credentials baked in already).
        if channel is not None and credentials is not None:
            raise ValueError(
                "The `channel` and `credentials` arguments are mutually " "exclusive."
            )

        # Create the channel.
        if channel is None:
            channel = self.create_channel(
                address=address,
                credentials=credentials,
                options={
                    "grpc.max_send_message_length": -1,
                    "grpc.max_receive_message_length": -1,
                }.items(),
            )

        self._channel = channel

        # gRPC uses objects called "stubs" that are bound to the
        # channel and provide a basic method for each RPC.
        self._stubs = {"auto_ml_stub": service_pb2_grpc.AutoMlStub(channel)}

        # Because this API includes a method that returns a
        # long-running operation (proto: google.longrunning.Operation),
        # instantiate an LRO client.
        self._operations_client = google.api_core.operations_v1.OperationsClient(
            channel
        )

    @classmethod
    def create_channel(
        cls, address="automl.googleapis.com:443", credentials=None, **kwargs
    ):
        """Create and return a gRPC channel object.

        Args:
            address (str): The host for the channel to use.
            credentials (~.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            kwargs (dict): Keyword arguments, which are passed to the
                channel creation.

        Returns:
            grpc.Channel: A gRPC channel object.
        """
        return google.api_core.grpc_helpers.create_channel(
            address, credentials=credentials, scopes=cls._OAUTH_SCOPES, **kwargs
        )

    @property
    def channel(self):
        """The gRPC channel used by the transport.

        Returns:
            grpc.Channel: A gRPC channel object.
        """
        return self._channel

    @property
    def delete_dataset(self):
        """Return the gRPC stub for :meth:`AutoMlClient.delete_dataset`.

        Output only. Auxiliary information for each of the
        input_feature_column_specs with respect to this particular model.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["auto_ml_stub"].DeleteDataset

    @property
    def import_data(self):
        """Return the gRPC stub for :meth:`AutoMlClient.import_data`.

        Optional. Type of the model. The available values are:

        -  ``cloud-high-accuracy-1`` - (default) A model to be used via
           prediction calls to AutoML API. Expected to have a higher latency,
           but should also have a higher prediction quality than other models.
        -  ``cloud-low-latency-1`` - A model to be used via prediction calls to
           AutoML API. Expected to have low latency, but may have lower
           prediction quality than other models.
        -  ``mobile-low-latency-1`` - A model that, in addition to providing
           prediction via AutoML API, can also be exported (see
           ``AutoMl.ExportModel``) and used on a mobile or edge device with
           TensorFlow afterwards. Expected to have low latency, but may have
           lower prediction quality than other models.
        -  ``mobile-versatile-1`` - A model that, in addition to providing
           prediction via AutoML API, can also be exported (see
           ``AutoMl.ExportModel``) and used on a mobile or edge device with
           TensorFlow afterwards.
        -  ``mobile-high-accuracy-1`` - A model that, in addition to providing
           prediction via AutoML API, can also be exported (see
           ``AutoMl.ExportModel``) and used on a mobile or edge device with
           TensorFlow afterwards. Expected to have a higher latency, but should
           also have a higher prediction quality than other models.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["auto_ml_stub"].ImportData

    @property
    def export_data(self):
        """Return the gRPC stub for :meth:`AutoMlClient.export_data`.

        A Location identifies a piece of source code in a .proto file which
        corresponds to a particular definition. This information is intended to
        be useful to IDEs, code indexers, documentation generators, and similar
        tools.

        For example, say we have a file like: message Foo { optional string foo
        = 1; } Let's look at just the field definition: optional string foo = 1;
        ^ ^^ ^^ ^ ^^^ a bc de f ghi We have the following locations: span path
        represents [a,i) [ 4, 0, 2, 0 ] The whole field definition. [a,b) [ 4,
        0, 2, 0, 4 ] The label (optional). [c,d) [ 4, 0, 2, 0, 5 ] The type
        (string). [e,f) [ 4, 0, 2, 0, 1 ] The name (foo). [g,h) [ 4, 0, 2, 0, 3
        ] The number (1).

        Notes:

        -  A location may refer to a repeated field itself (i.e. not to any
           particular index within it). This is used whenever a set of elements
           are logically enclosed in a single code segment. For example, an
           entire extend block (possibly containing multiple extension
           definitions) will have an outer location whose path refers to the
           "extensions" repeated field without an index.
        -  Multiple locations may have the same path. This happens when a single
           logical declaration is spread out across multiple places. The most
           obvious example is the "extend" block again -- there may be multiple
           extend blocks in the same scope, each of which will have the same
           path.
        -  A location's span is not always a subset of its parent's span. For
           example, the "extendee" of an extension declaration appears at the
           beginning of the "extend" block and is shared by all extensions
           within the block.
        -  Just because a location's span is a subset of some other location's
           span does not mean that it is a descendant. For example, a "group"
           defines both a type and a field in a single declaration. Thus, the
           locations corresponding to the type and field and their components
           will overlap.
        -  Code which tries to interpret locations should probably be designed
           to ignore those that it doesn't understand, as more types of
           locations could be recorded in the future.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["auto_ml_stub"].ExportData

    @property
    def delete_model(self):
        """Return the gRPC stub for :meth:`AutoMlClient.delete_model`.

        Output only. The number of nodes this model is deployed on. A node
        is an abstraction of a machine resource, which can handle online
        prediction QPS as given in the qps_per_node field.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["auto_ml_stub"].DeleteModel

    @property
    def export_model(self):
        """Return the gRPC stub for :meth:`AutoMlClient.export_model`.

        Set true to use the old proto1 MessageSet wire format for
        extensions. This is provided for backwards-compatibility with the
        MessageSet wire format. You should not use this for any other reason:
        It's less efficient, has fewer features, and is more complicated.

        The message must be defined exactly as follows: message Foo { option
        message_set_wire_format = true; extensions 4 to max; } Note that the
        message cannot have any defined fields; MessageSets only have
        extensions.

        All extensions of your type must be singular messages; e.g. they cannot
        be int32s, enums, or repeated messages.

        Because this is an option, the above two restrictions are not enforced
        by the protocol compiler.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["auto_ml_stub"].ExportModel

    @property
    def export_evaluated_examples(self):
        """Return the gRPC stub for :meth:`AutoMlClient.export_evaluated_examples`.

        Output only. Resource name of the model. Format:
        ``projects/{project_id}/locations/{location_id}/models/{model_id}``

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["auto_ml_stub"].ExportEvaluatedExamples

    @property
    def list_model_evaluations(self):
        """Return the gRPC stub for :meth:`AutoMlClient.list_model_evaluations`.

        Lists model evaluations.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["auto_ml_stub"].ListModelEvaluations

    @property
    def create_dataset(self):
        """Return the gRPC stub for :meth:`AutoMlClient.create_dataset`.

        Creates a dataset.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["auto_ml_stub"].CreateDataset

    @property
    def get_dataset(self):
        """Return the gRPC stub for :meth:`AutoMlClient.get_dataset`.

        Gets a dataset.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["auto_ml_stub"].GetDataset

    @property
    def list_datasets(self):
        """Return the gRPC stub for :meth:`AutoMlClient.list_datasets`.

        Lists datasets in a project.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["auto_ml_stub"].ListDatasets

    @property
    def update_dataset(self):
        """Return the gRPC stub for :meth:`AutoMlClient.update_dataset`.

        Updates a dataset.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["auto_ml_stub"].UpdateDataset

    @property
    def get_annotation_spec(self):
        """Return the gRPC stub for :meth:`AutoMlClient.get_annotation_spec`.

        Gets an annotation spec.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["auto_ml_stub"].GetAnnotationSpec

    @property
    def get_table_spec(self):
        """Return the gRPC stub for :meth:`AutoMlClient.get_table_spec`.

        Gets a table spec.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["auto_ml_stub"].GetTableSpec

    @property
    def list_table_specs(self):
        """Return the gRPC stub for :meth:`AutoMlClient.list_table_specs`.

        Lists table specs in a dataset.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["auto_ml_stub"].ListTableSpecs

    @property
    def update_table_spec(self):
        """Return the gRPC stub for :meth:`AutoMlClient.update_table_spec`.

        Updates a table spec.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["auto_ml_stub"].UpdateTableSpec

    @property
    def get_column_spec(self):
        """Return the gRPC stub for :meth:`AutoMlClient.get_column_spec`.

        Gets a column spec.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["auto_ml_stub"].GetColumnSpec

    @property
    def list_column_specs(self):
        """Return the gRPC stub for :meth:`AutoMlClient.list_column_specs`.

        Lists column specs in a table spec.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["auto_ml_stub"].ListColumnSpecs

    @property
    def update_column_spec(self):
        """Return the gRPC stub for :meth:`AutoMlClient.update_column_spec`.

        Updates a column spec.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["auto_ml_stub"].UpdateColumnSpec

    @property
    def create_model(self):
        """Return the gRPC stub for :meth:`AutoMlClient.create_model`.

        Input configuration for ImportData Action.

        The format of input depends on dataset_metadata the Dataset into which
        the import is happening has. As input source the ``gcs_source`` is
        expected, unless specified otherwise. Additionally any input .CSV file
        by itself must be 100MB or smaller, unless specified otherwise. If an
        "example" file (that is, image, video etc.) with identical content (even
        if it had different GCS_FILE_PATH) is mentioned multiple times, then its
        label, bounding boxes etc. are appended. The same file should be always
        provided with the same ML_USE and GCS_FILE_PATH, if it is not, then
        these values are nondeterministically selected from the given ones.

        The formats are represented in EBNF with commas being literal and with
        non-terminal symbols defined near the end of this comment. The formats
        are:

        -  For Image Classification: CSV file(s) with each line in format:
           ML_USE,GCS_FILE_PATH,LABEL,LABEL,... GCS_FILE_PATH leads to image of
           up to 30MB in size. Supported extensions: .JPEG, .GIF, .PNG, .WEBP,
           .BMP, .TIFF, .ICO For MULTICLASS classification type, at most one
           LABEL is allowed per image. If an image has not yet been labeled,
           then it should be mentioned just once with no LABEL. Some sample
           rows: TRAIN,gs://folder/image1.jpg,daisy
           TEST,gs://folder/image2.jpg,dandelion,tulip,rose
           UNASSIGNED,gs://folder/image3.jpg,daisy
           UNASSIGNED,gs://folder/image4.jpg

        -  For Image Object Detection: CSV file(s) with each line in format:
           ML_USE,GCS_FILE_PATH,(LABEL,BOUNDING_BOX \| ,,,,,,,) GCS_FILE_PATH
           leads to image of up to 30MB in size. Supported extensions: .JPEG,
           .GIF, .PNG. Each image is assumed to be exhaustively labeled. The
           minimum allowed BOUNDING_BOX edge length is 0.01, and no more than
           500 BOUNDING_BOX-es per image are allowed (one BOUNDING_BOX is
           defined per line). If an image has not yet been labeled, then it
           should be mentioned just once with no LABEL and the ",,,,,,," in
           place of the BOUNDING_BOX. For images which are known to not contain
           any bounding boxes, they should be labelled explictly as
           "NEGATIVE_IMAGE", followed by ",,,,,,," in place of the BOUNDING_BOX.
           Sample rows: TRAIN,gs://folder/image1.png,car,0.1,0.1,,,0.3,0.3,,
           TRAIN,gs://folder/image1.png,bike,.7,.6,,,.8,.9,,
           UNASSIGNED,gs://folder/im2.png,car,0.1,0.1,0.2,0.1,0.2,0.3,0.1,0.3
           TEST,gs://folder/im3.png,,,,,,,,,
           TRAIN,gs://folder/im4.png,NEGATIVE_IMAGE,,,,,,,,,

        -  For Video Classification: CSV file(s) with each line in format:
           ML_USE,GCS_FILE_PATH where ML_USE VALIDATE value should not be used.
           The GCS_FILE_PATH should lead to another .csv file which describes
           examples that have given ML_USE, using the following row format:
           GCS_FILE_PATH,(LABEL,TIME_SEGMENT_START,TIME_SEGMENT_END \| ,,) Here
           GCS_FILE_PATH leads to a video of up to 50GB in size and up to 3h
           duration. Supported extensions: .MOV, .MPEG4, .MP4, .AVI.
           TIME_SEGMENT_START and TIME_SEGMENT_END must be within the length of
           the video, and end has to be after the start. Any segment of a video
           which has one or more labels on it, is considered a hard negative for
           all other labels. Any segment with no labels on it is considered to
           be unknown. If a whole video is unknown, then it shuold be mentioned
           just once with ",," in place of LABEL,
           TIME_SEGMENT_START,TIME_SEGMENT_END. Sample top level CSV file:
           TRAIN,gs://folder/train_videos.csv TEST,gs://folder/test_videos.csv
           UNASSIGNED,gs://folder/other_videos.csv Sample rows of a CSV file for
           a particular ML_USE: gs://folder/video1.avi,car,120,180.000021
           gs://folder/video1.avi,bike,150,180.000021
           gs://folder/vid2.avi,car,0,60.5 gs://folder/vid3.avi,,,

        -  For Video Object Tracking: CSV file(s) with each line in format:
           ML_USE,GCS_FILE_PATH where ML_USE VALIDATE value should not be used.
           The GCS_FILE_PATH should lead to another .csv file which describes
           examples that have given ML_USE, using one of the following row
           format: GCS_FILE_PATH,LABEL,[INSTANCE_ID],TIMESTAMP,BOUNDING_BOX or
           GCS_FILE_PATH,,,,,,,,,, Here GCS_FILE_PATH leads to a video of up to
           50GB in size and up to 3h duration. Supported extensions: .MOV,
           .MPEG4, .MP4, .AVI. Providing INSTANCE_IDs can help to obtain a
           better model. When a specific labeled entity leaves the video frame,
           and shows up afterwards it is not required, albeit preferable, that
           the same INSTANCE_ID is given to it. TIMESTAMP must be within the
           length of the video, the BOUNDING_BOX is assumed to be drawn on the
           closest video's frame to the TIMESTAMP. Any mentioned by the
           TIMESTAMP frame is expected to be exhaustively labeled and no more
           than 500 BOUNDING_BOX-es per frame are allowed. If a whole video is
           unknown, then it should be mentioned just once with ",,,,,,,,,," in
           place of LABEL, [INSTANCE_ID],TIMESTAMP,BOUNDING_BOX. Sample top
           level CSV file: TRAIN,gs://folder/train_videos.csv
           TEST,gs://folder/test_videos.csv
           UNASSIGNED,gs://folder/other_videos.csv Seven sample rows of a CSV
           file for a particular ML_USE:
           gs://folder/video1.avi,car,1,12.10,0.8,0.8,0.9,0.8,0.9,0.9,0.8,0.9
           gs://folder/video1.avi,car,1,12.90,0.4,0.8,0.5,0.8,0.5,0.9,0.4,0.9
           gs://folder/video1.avi,car,2,12.10,.4,.2,.5,.2,.5,.3,.4,.3
           gs://folder/video1.avi,car,2,12.90,.8,.2,,,.9,.3,,
           gs://folder/video1.avi,bike,,12.50,.45,.45,,,.55,.55,,
           gs://folder/video2.avi,car,1,0,.1,.9,,,.9,.1,,
           gs://folder/video2.avi,,,,,,,,,,,

        -  For Text Extraction: CSV file(s) with each line in format:
           ML_USE,GCS_FILE_PATH GCS_FILE_PATH leads to a .JSONL (that is, JSON
           Lines) file which either imports text in-line or as documents. Any
           given .JSONL file must be 100MB or smaller. The in-line .JSONL file
           contains, per line, a proto that wraps a TextSnippet proto (in json
           representation) followed by one or more AnnotationPayload protos
           (called annotations), which have display_name and text_extraction
           detail populated. The given text is expected to be annotated
           exhaustively, for example, if you look for animals and text contains
           "dolphin" that is not labeled, then "dolphin" is assumed to not be an
           animal. Any given text snippet content must be 10KB or smaller, and
           also be UTF-8 NFC encoded (ASCII already is). The document .JSONL
           file contains, per line, a proto that wraps a Document proto. The
           Document proto must have either document_text or input_config set. In
           document_text case, the Document proto may also contain the spatial
           information of the document, including layout, document dimension and
           page number. In input_config case, only PDF documents are supported
           now, and each document may be up to 2MB large. Currently, annotations
           on documents cannot be specified at import. Three sample CSV rows:
           TRAIN,gs://folder/file1.jsonl VALIDATE,gs://folder/file2.jsonl
           TEST,gs://folder/file3.jsonl Sample in-line JSON Lines file for
           entity extraction (presented here with artificial line breaks, but
           the only actual line break is denoted by \\n).: { "document": {
           "document_text": {"content": "dog cat"} "layout": [ { "text_segment":
           { "start_offset": 0, "end_offset": 3, }, "page_number": 1,
           "bounding_poly": { "normalized_vertices": [ {"x": 0.1, "y": 0.1},
           {"x": 0.1, "y": 0.3}, {"x": 0.3, "y": 0.3}, {"x": 0.3, "y": 0.1}, ],
           }, "text_segment_type": TOKEN, }, { "text_segment": { "start_offset":
           4, "end_offset": 7, }, "page_number": 1, "bounding_poly": {
           "normalized_vertices": [ {"x": 0.4, "y": 0.1}, {"x": 0.4, "y": 0.3},
           {"x": 0.8, "y": 0.3}, {"x": 0.8, "y": 0.1}, ], },
           "text_segment_type": TOKEN, }

           ::

                    ],
                    "document_dimensions": {
                      "width": 8.27,
                      "height": 11.69,
                      "unit": INCH,
                    }
                    "page_count": 1,
                  },
                  "annotations": [
                    {
                      "display_name": "animal",
                      "text_extraction": {"text_segment": {"start_offset": 0,
                      "end_offset": 3}}
                    },
                    {
                      "display_name": "animal",
                      "text_extraction": {"text_segment": {"start_offset": 4,
                      "end_offset": 7}}
                    }
                  ],
                }\n
                {
                   "text_snippet": {
                     "content": "This dog is good."
                   },
                   "annotations": [
                     {
                       "display_name": "animal",
                       "text_extraction": {
                         "text_segment": {"start_offset": 5, "end_offset": 8}
                       }
                     }
                   ]
                }
              Sample document JSON Lines file (presented here with artificial line
              breaks, but the only actual line break is denoted by \n).:
                {
                  "document": {
                    "input_config": {
                      "gcs_source": { "input_uris": [ "gs://folder/document1.pdf" ]
                      }
                    }
                  }
                }\n
                {
                  "document": {
                    "input_config": {
                      "gcs_source": { "input_uris": [ "gs://folder/document2.pdf" ]
                      }
                    }
                  }
                }

        -  For Text Classification: CSV file(s) with each line in format:
           ML_USE,(TEXT_SNIPPET \| GCS_FILE_PATH),LABEL,LABEL,... TEXT_SNIPPET
           and GCS_FILE_PATH are distinguished by a pattern. If the column
           content is a valid gcs file path, i.e. prefixed by "gs://", it will
           be treated as a GCS_FILE_PATH, else if the content is enclosed within
           double quotes (""), it is treated as a TEXT_SNIPPET. In the
           GCS_FILE_PATH case, the path must lead to a .txt file with UTF-8
           encoding, for example, "gs://folder/content.txt", and the content in
           it is extracted as a text snippet. In TEXT_SNIPPET case, the column
           content excluding quotes is treated as to be imported text snippet.
           In both cases, the text snippet/file size must be within 128kB.
           Maximum 100 unique labels are allowed per CSV row. Sample rows:
           TRAIN,"They have bad food and very rude",RudeService,BadFood
           TRAIN,gs://folder/content.txt,SlowService TEST,"Typically always bad
           service there.",RudeService VALIDATE,"Stomach ache to go.",BadFood

        -  For Text Sentiment: CSV file(s) with each line in format:
           ML_USE,(TEXT_SNIPPET \| GCS_FILE_PATH),SENTIMENT TEXT_SNIPPET and
           GCS_FILE_PATH are distinguished by a pattern. If the column content
           is a valid gcs file path, that is, prefixed by "gs://", it is treated
           as a GCS_FILE_PATH, otherwise it is treated as a TEXT_SNIPPET. In the
           GCS_FILE_PATH case, the path must lead to a .txt file with UTF-8
           encoding, for example, "gs://folder/content.txt", and the content in
           it is extracted as a text snippet. In TEXT_SNIPPET case, the column
           content itself is treated as to be imported text snippet. In both
           cases, the text snippet must be up to 500 characters long. Sample
           rows: TRAIN,"@freewrytin this is way too good for your product",2
           TRAIN,"I need this product so bad",3 TEST,"Thank you for this
           product.",4 VALIDATE,gs://folder/content.txt,2

        -  For Tables: Either ``gcs_source`` or

        ``bigquery_source`` can be used. All inputs is concatenated into a
        single

        ``primary_table`` For gcs_source: CSV file(s), where the first row of
        the first file is the header, containing unique column names. If the
        first row of a subsequent file is the same as the header, then it is
        also treated as a header. All other rows contain values for the
        corresponding columns. Each .CSV file by itself must be 10GB or smaller,
        and their total size must be 100GB or smaller. First three sample rows
        of a CSV file: "Id","First Name","Last Name","Dob","Addresses"

        "1","John","Doe","1968-01-22","[{"status":"current","address":"123_First_Avenue","city":"Seattle","state":"WA","zip":"11111","numberOfYears":"1"},{"status":"previous","address":"456_Main_Street","city":"Portland","state":"OR","zip":"22222","numberOfYears":"5"}]"

        "2","Jane","Doe","1980-10-16","[{"status":"current","address":"789_Any_Avenue","city":"Albany","state":"NY","zip":"33333","numberOfYears":"2"},{"status":"previous","address":"321_Main_Street","city":"Hoboken","state":"NJ","zip":"44444","numberOfYears":"3"}]}
        For bigquery_source: An URI of a BigQuery table. The user data size of
        the BigQuery table must be 100GB or smaller. An imported table must have
        between 2 and 1,000 columns, inclusive, and between 1000 and 100,000,000
        rows, inclusive. There are at most 5 import data running in parallel.
        Definitions: ML_USE = "TRAIN" \| "VALIDATE" \| "TEST" \| "UNASSIGNED"
        Describes how the given example (file) should be used for model
        training. "UNASSIGNED" can be used when user has no preference.
        GCS_FILE_PATH = A path to file on GCS, e.g. "gs://folder/image1.png".
        LABEL = A display name of an object on an image, video etc., e.g. "dog".
        Must be up to 32 characters long and can consist only of ASCII Latin
        letters A-Z and a-z, underscores(_), and ASCII digits 0-9. For each
        label an AnnotationSpec is created which display_name becomes the label;
        AnnotationSpecs are given back in predictions. INSTANCE_ID = A positive
        integer that identifies a specific instance of a labeled entity on an
        example. Used e.g. to track two cars on a video while being able to tell
        apart which one is which. BOUNDING_BOX = VERTEX,VERTEX,VERTEX,VERTEX \|
        VERTEX,,,VERTEX,, A rectangle parallel to the frame of the example
        (image, video). If 4 vertices are given they are connected by edges in
        the order provided, if 2 are given they are recognized as diagonally
        opposite vertices of the rectangle. VERTEX = COORDINATE,COORDINATE First
        coordinate is horizontal (x), the second is vertical (y). COORDINATE = A
        float in 0 to 1 range, relative to total length of image or video in
        given dimension. For fractions the leading non-decimal 0 can be omitted
        (i.e. 0.3 = .3). Point 0,0 is in top left. TIME_SEGMENT_START =
        TIME_OFFSET Expresses a beginning, inclusive, of a time segment within
        an example that has a time dimension (e.g. video). TIME_SEGMENT_END =
        TIME_OFFSET Expresses an end, exclusive, of a time segment within an
        example that has a time dimension (e.g. video). TIME_OFFSET = A number
        of seconds as measured from the start of an example (e.g. video).
        Fractions are allowed, up to a microsecond precision. "inf" is allowed,
        and it means the end of the example. TEXT_SNIPPET = A content of a text
        snippet, UTF-8 encoded, enclosed within double quotes (""). SENTIMENT =
        An integer between 0 and
        Dataset.text_sentiment_dataset_metadata.sentiment_max (inclusive).
        Describes the ordinal of the sentiment - higher value means a more
        positive sentiment. All the values are completely relative, i.e. neither
        0 needs to mean a negative or neutral sentiment nor sentiment_max needs
        to mean a positive one - it is just required that 0 is the least
        positive sentiment in the data, and sentiment_max is the most positive
        one. The SENTIMENT shouldn't be confused with "score" or "magnitude"
        from the previous Natural Language Sentiment Analysis API. All SENTIMENT
        values between 0 and sentiment_max must be represented in the imported
        data. On prediction the same 0 to sentiment_max range will be used. The
        difference between neighboring sentiment values needs not to be uniform,
        e.g. 1 and 2 may be similar whereas the difference between 2 and 3 may
        be huge.

        Errors: If any of the provided CSV files can't be parsed or if more than
        certain percent of CSV rows cannot be processed then the operation fails
        and nothing is imported. Regardless of overall success or failure the
        per-row failures, up to a certain count cap, is listed in
        Operation.metadata.partial_failures.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["auto_ml_stub"].CreateModel

    @property
    def get_model(self):
        """Return the gRPC stub for :meth:`AutoMlClient.get_model`.

        Gets a model.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["auto_ml_stub"].GetModel

    @property
    def list_models(self):
        """Return the gRPC stub for :meth:`AutoMlClient.list_models`.

        Lists models.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["auto_ml_stub"].ListModels

    @property
    def deploy_model(self):
        """Return the gRPC stub for :meth:`AutoMlClient.deploy_model`.

        Input only. The data representing the image. For Predict calls
        ``image_bytes`` must be set, as other options are not currently
        supported by prediction API. You can read the contents of an uploaded
        image by using the ``content_uri`` field.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["auto_ml_stub"].DeployModel

    @property
    def undeploy_model(self):
        """Return the gRPC stub for :meth:`AutoMlClient.undeploy_model`.

        Imports data into a dataset. For Tables this method can only be
        called on an empty Dataset.

        For Tables:

        -  A ``schema_inference_version`` parameter must be explicitly set.
           Returns an empty response in the ``response`` field when it
           completes.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["auto_ml_stub"].UndeployModel

    @property
    def get_model_evaluation(self):
        """Return the gRPC stub for :meth:`AutoMlClient.get_model_evaluation`.

        Gets a model evaluation.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["auto_ml_stub"].GetModelEvaluation
