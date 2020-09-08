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

from google.cloud.automl_v1.proto import prediction_service_pb2_grpc


class PredictionServiceGrpcTransport(object):
    """gRPC transport class providing stubs for
    google.cloud.automl.v1 PredictionService API.

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
                "The `channel` and `credentials` arguments are mutually " "exclusive.",
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
        self._stubs = {
            "prediction_service_stub": prediction_service_pb2_grpc.PredictionServiceStub(
                channel
            ),
        }

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
    def predict(self):
        """Return the gRPC stub for :meth:`PredictionServiceClient.predict`.

        Perform an online prediction. The prediction result is directly
        returned in the response. Available for following ML scenarios, and
        their expected request payloads:

        AutoML Vision Classification

        -  An image in .JPEG, .GIF or .PNG format, image_bytes up to 30MB.

        AutoML Vision Object Detection

        -  An image in .JPEG, .GIF or .PNG format, image_bytes up to 30MB.

        AutoML Natural Language Classification

        -  A TextSnippet up to 60,000 characters, UTF-8 encoded or a document in
           .PDF, .TIF or .TIFF format with size upto 2MB.

        AutoML Natural Language Entity Extraction

        -  A TextSnippet up to 10,000 characters, UTF-8 NFC encoded or a
           document in .PDF, .TIF or .TIFF format with size upto 20MB.

        AutoML Natural Language Sentiment Analysis

        -  A TextSnippet up to 60,000 characters, UTF-8 encoded or a document in
           .PDF, .TIF or .TIFF format with size upto 2MB.

        AutoML Translation

        -  A TextSnippet up to 25,000 characters, UTF-8 encoded.

        AutoML Tables

        -  A row with column values matching the columns of the model, up to
           5MB. Not available for FORECASTING ``prediction_type``.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["prediction_service_stub"].Predict

    @property
    def batch_predict(self):
        """Return the gRPC stub for :meth:`PredictionServiceClient.batch_predict`.

        Perform a batch prediction. Unlike the online ``Predict``, batch
        prediction result won't be immediately available in the response.
        Instead, a long running operation object is returned. User can poll the
        operation result via ``GetOperation`` method. Once the operation is
        done, ``BatchPredictResult`` is returned in the ``response`` field.
        Available for following ML scenarios:

        -  AutoML Vision Classification
        -  AutoML Vision Object Detection
        -  AutoML Video Intelligence Classification
        -  AutoML Video Intelligence Object Tracking \* AutoML Natural Language
           Classification
        -  AutoML Natural Language Entity Extraction
        -  AutoML Natural Language Sentiment Analysis
        -  AutoML Tables

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["prediction_service_stub"].BatchPredict
