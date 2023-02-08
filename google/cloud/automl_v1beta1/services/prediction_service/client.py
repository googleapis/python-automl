# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from collections import OrderedDict
import os
import re
from typing import (
    Dict,
    Mapping,
    MutableMapping,
    MutableSequence,
    Optional,
    Sequence,
    Tuple,
    Type,
    Union,
    cast,
)

from google.cloud.automl_v1beta1 import gapic_version as package_version

from google.api_core import client_options as client_options_lib
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport import mtls  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.auth.exceptions import MutualTLSChannelError  # type: ignore
from google.oauth2 import service_account  # type: ignore

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore

from google.api_core import operation  # type: ignore
from google.api_core import operation_async  # type: ignore
from google.cloud.automl_v1beta1.types import annotation_payload
from google.cloud.automl_v1beta1.types import data_items
from google.cloud.automl_v1beta1.types import io
from google.cloud.automl_v1beta1.types import operations
from google.cloud.automl_v1beta1.types import prediction_service
from .transports.base import PredictionServiceTransport, DEFAULT_CLIENT_INFO
from .transports.grpc import PredictionServiceGrpcTransport
from .transports.grpc_asyncio import PredictionServiceGrpcAsyncIOTransport
from .transports.rest import PredictionServiceRestTransport


class PredictionServiceClientMeta(type):
    """Metaclass for the PredictionService client.

    This provides class-level methods for building and retrieving
    support objects (e.g. transport) without polluting the client instance
    objects.
    """

    _transport_registry = (
        OrderedDict()
    )  # type: Dict[str, Type[PredictionServiceTransport]]
    _transport_registry["grpc"] = PredictionServiceGrpcTransport
    _transport_registry["grpc_asyncio"] = PredictionServiceGrpcAsyncIOTransport
    _transport_registry["rest"] = PredictionServiceRestTransport

    def get_transport_class(
        cls,
        label: Optional[str] = None,
    ) -> Type[PredictionServiceTransport]:
        """Returns an appropriate transport class.

        Args:
            label: The name of the desired transport. If none is
                provided, then the first transport in the registry is used.

        Returns:
            The transport class to use.
        """
        # If a specific transport is requested, return that one.
        if label:
            return cls._transport_registry[label]

        # No transport is requested; return the default (that is, the first one
        # in the dictionary).
        return next(iter(cls._transport_registry.values()))


class PredictionServiceClient(metaclass=PredictionServiceClientMeta):
    """AutoML Prediction API.

    On any input that is documented to expect a string parameter in
    snake_case or kebab-case, either of those cases is accepted.
    """

    @staticmethod
    def _get_default_mtls_endpoint(api_endpoint):
        """Converts api endpoint to mTLS endpoint.

        Convert "*.sandbox.googleapis.com" and "*.googleapis.com" to
        "*.mtls.sandbox.googleapis.com" and "*.mtls.googleapis.com" respectively.
        Args:
            api_endpoint (Optional[str]): the api endpoint to convert.
        Returns:
            str: converted mTLS api endpoint.
        """
        if not api_endpoint:
            return api_endpoint

        mtls_endpoint_re = re.compile(
            r"(?P<name>[^.]+)(?P<mtls>\.mtls)?(?P<sandbox>\.sandbox)?(?P<googledomain>\.googleapis\.com)?"
        )

        m = mtls_endpoint_re.match(api_endpoint)
        name, mtls, sandbox, googledomain = m.groups()
        if mtls or not googledomain:
            return api_endpoint

        if sandbox:
            return api_endpoint.replace(
                "sandbox.googleapis.com", "mtls.sandbox.googleapis.com"
            )

        return api_endpoint.replace(".googleapis.com", ".mtls.googleapis.com")

    DEFAULT_ENDPOINT = "automl.googleapis.com"
    DEFAULT_MTLS_ENDPOINT = _get_default_mtls_endpoint.__func__(  # type: ignore
        DEFAULT_ENDPOINT
    )

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            PredictionServiceClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_info(info)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            PredictionServiceClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @property
    def transport(self) -> PredictionServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            PredictionServiceTransport: The transport used by the client
                instance.
        """
        return self._transport

    @staticmethod
    def model_path(
        project: str,
        location: str,
        model: str,
    ) -> str:
        """Returns a fully-qualified model string."""
        return "projects/{project}/locations/{location}/models/{model}".format(
            project=project,
            location=location,
            model=model,
        )

    @staticmethod
    def parse_model_path(path: str) -> Dict[str, str]:
        """Parses a model path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/models/(?P<model>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def common_billing_account_path(
        billing_account: str,
    ) -> str:
        """Returns a fully-qualified billing_account string."""
        return "billingAccounts/{billing_account}".format(
            billing_account=billing_account,
        )

    @staticmethod
    def parse_common_billing_account_path(path: str) -> Dict[str, str]:
        """Parse a billing_account path into its component segments."""
        m = re.match(r"^billingAccounts/(?P<billing_account>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_folder_path(
        folder: str,
    ) -> str:
        """Returns a fully-qualified folder string."""
        return "folders/{folder}".format(
            folder=folder,
        )

    @staticmethod
    def parse_common_folder_path(path: str) -> Dict[str, str]:
        """Parse a folder path into its component segments."""
        m = re.match(r"^folders/(?P<folder>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_organization_path(
        organization: str,
    ) -> str:
        """Returns a fully-qualified organization string."""
        return "organizations/{organization}".format(
            organization=organization,
        )

    @staticmethod
    def parse_common_organization_path(path: str) -> Dict[str, str]:
        """Parse a organization path into its component segments."""
        m = re.match(r"^organizations/(?P<organization>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_project_path(
        project: str,
    ) -> str:
        """Returns a fully-qualified project string."""
        return "projects/{project}".format(
            project=project,
        )

    @staticmethod
    def parse_common_project_path(path: str) -> Dict[str, str]:
        """Parse a project path into its component segments."""
        m = re.match(r"^projects/(?P<project>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_location_path(
        project: str,
        location: str,
    ) -> str:
        """Returns a fully-qualified location string."""
        return "projects/{project}/locations/{location}".format(
            project=project,
            location=location,
        )

    @staticmethod
    def parse_common_location_path(path: str) -> Dict[str, str]:
        """Parse a location path into its component segments."""
        m = re.match(r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)$", path)
        return m.groupdict() if m else {}

    @classmethod
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: Optional[client_options_lib.ClientOptions] = None
    ):
        """Return the API endpoint and client cert source for mutual TLS.

        The client cert source is determined in the following order:
        (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the
        client cert source is None.
        (2) if `client_options.client_cert_source` is provided, use the provided one; if the
        default client cert source exists, use the default one; otherwise the client cert
        source is None.

        The API endpoint is determined in the following order:
        (1) if `client_options.api_endpoint` if provided, use the provided one.
        (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the
        default mTLS endpoint; if the environment variable is "never", use the default API
        endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise
        use the default API endpoint.

        More details can be found at https://google.aip.dev/auth/4114.

        Args:
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. Only the `api_endpoint` and `client_cert_source` properties may be used
                in this method.

        Returns:
            Tuple[str, Callable[[], Tuple[bytes, bytes]]]: returns the API endpoint and the
                client cert source to use.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If any errors happen.
        """
        if client_options is None:
            client_options = client_options_lib.ClientOptions()
        use_client_cert = os.getenv("GOOGLE_API_USE_CLIENT_CERTIFICATE", "false")
        use_mtls_endpoint = os.getenv("GOOGLE_API_USE_MTLS_ENDPOINT", "auto")
        if use_client_cert not in ("true", "false"):
            raise ValueError(
                "Environment variable `GOOGLE_API_USE_CLIENT_CERTIFICATE` must be either `true` or `false`"
            )
        if use_mtls_endpoint not in ("auto", "never", "always"):
            raise MutualTLSChannelError(
                "Environment variable `GOOGLE_API_USE_MTLS_ENDPOINT` must be `never`, `auto` or `always`"
            )

        # Figure out the client cert source to use.
        client_cert_source = None
        if use_client_cert == "true":
            if client_options.client_cert_source:
                client_cert_source = client_options.client_cert_source
            elif mtls.has_default_client_cert_source():
                client_cert_source = mtls.default_client_cert_source()

        # Figure out which api endpoint to use.
        if client_options.api_endpoint is not None:
            api_endpoint = client_options.api_endpoint
        elif use_mtls_endpoint == "always" or (
            use_mtls_endpoint == "auto" and client_cert_source
        ):
            api_endpoint = cls.DEFAULT_MTLS_ENDPOINT
        else:
            api_endpoint = cls.DEFAULT_ENDPOINT

        return api_endpoint, client_cert_source

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[Union[str, PredictionServiceTransport]] = None,
        client_options: Optional[Union[client_options_lib.ClientOptions, dict]] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the prediction service client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, PredictionServiceTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (Optional[Union[google.api_core.client_options.ClientOptions, dict]]): Custom options for the
                client. It won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        if isinstance(client_options, dict):
            client_options = client_options_lib.from_dict(client_options)
        if client_options is None:
            client_options = client_options_lib.ClientOptions()
        client_options = cast(client_options_lib.ClientOptions, client_options)

        api_endpoint, client_cert_source_func = self.get_mtls_endpoint_and_cert_source(
            client_options
        )

        api_key_value = getattr(client_options, "api_key", None)
        if api_key_value and credentials:
            raise ValueError(
                "client_options.api_key and credentials are mutually exclusive"
            )

        # Save or instantiate the transport.
        # Ordinarily, we provide the transport, but allowing a custom transport
        # instance provides an extensibility point for unusual situations.
        if isinstance(transport, PredictionServiceTransport):
            # transport is a PredictionServiceTransport instance.
            if credentials or client_options.credentials_file or api_key_value:
                raise ValueError(
                    "When providing a transport instance, "
                    "provide its credentials directly."
                )
            if client_options.scopes:
                raise ValueError(
                    "When providing a transport instance, provide its scopes "
                    "directly."
                )
            self._transport = transport
        else:
            import google.auth._default  # type: ignore

            if api_key_value and hasattr(
                google.auth._default, "get_api_key_credentials"
            ):
                credentials = google.auth._default.get_api_key_credentials(
                    api_key_value
                )

            Transport = type(self).get_transport_class(transport)
            self._transport = Transport(
                credentials=credentials,
                credentials_file=client_options.credentials_file,
                host=api_endpoint,
                scopes=client_options.scopes,
                client_cert_source_for_mtls=client_cert_source_func,
                quota_project_id=client_options.quota_project_id,
                client_info=client_info,
                always_use_jwt_access=True,
                api_audience=client_options.api_audience,
            )

    def predict(
        self,
        request: Optional[Union[prediction_service.PredictRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        payload: Optional[data_items.ExamplePayload] = None,
        params: Optional[MutableMapping[str, str]] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> prediction_service.PredictResponse:
        r"""Perform an online prediction. The prediction result will be
        directly returned in the response. Available for following ML
        problems, and their expected request payloads:

        -  Image Classification - Image in .JPEG, .GIF or .PNG format,
           image_bytes up to 30MB.
        -  Image Object Detection - Image in .JPEG, .GIF or .PNG format,
           image_bytes up to 30MB.
        -  Text Classification - TextSnippet, content up to 60,000
           characters, UTF-8 encoded.
        -  Text Extraction - TextSnippet, content up to 30,000
           characters, UTF-8 NFC encoded.
        -  Translation - TextSnippet, content up to 25,000 characters,
           UTF-8 encoded.
        -  Tables - Row, with column values matching the columns of the
           model, up to 5MB. Not available for FORECASTING

        [prediction_type][google.cloud.automl.v1beta1.TablesModelMetadata.prediction_type].

        -  Text Sentiment - TextSnippet, content up 500 characters,
           UTF-8 encoded.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import automl_v1beta1

            def sample_predict():
                # Create a client
                client = automl_v1beta1.PredictionServiceClient()

                # Initialize request argument(s)
                payload = automl_v1beta1.ExamplePayload()
                payload.image.image_bytes = b'image_bytes_blob'

                request = automl_v1beta1.PredictRequest(
                    name="name_value",
                    payload=payload,
                )

                # Make the request
                response = client.predict(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.automl_v1beta1.types.PredictRequest, dict]):
                The request object. Request message for
                [PredictionService.Predict][google.cloud.automl.v1beta1.PredictionService.Predict].
            name (str):
                Required. Name of the model requested
                to serve the prediction.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            payload (google.cloud.automl_v1beta1.types.ExamplePayload):
                Required. Payload to perform a
                prediction on. The payload must match
                the problem type that the model was
                trained to solve.

                This corresponds to the ``payload`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            params (MutableMapping[str, str]):
                Additional domain-specific parameters, any string must
                be up to 25000 characters long.

                -  For Image Classification:

                   ``score_threshold`` - (float) A value from 0.0 to
                   1.0. When the model makes predictions for an image,
                   it will only produce results that have at least this
                   confidence score. The default is 0.5.

                -  For Image Object Detection: ``score_threshold`` -
                   (float) When Model detects objects on the image, it
                   will only produce bounding boxes which have at least
                   this confidence score. Value in 0 to 1 range, default
                   is 0.5. ``max_bounding_box_count`` - (int64) No more
                   than this number of bounding boxes will be returned
                   in the response. Default is 100, the requested value
                   may be limited by server.

                -  For Tables: feature_importance - (boolean) Whether
                   feature importance should be populated in the
                   returned TablesAnnotation. The default is false.

                This corresponds to the ``params`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.automl_v1beta1.types.PredictResponse:
                Response message for
                [PredictionService.Predict][google.cloud.automl.v1beta1.PredictionService.Predict].

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name, payload, params])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a prediction_service.PredictRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, prediction_service.PredictRequest):
            request = prediction_service.PredictRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name
            if payload is not None:
                request.payload = payload
            if params is not None:
                request.params = params

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.predict]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def batch_predict(
        self,
        request: Optional[Union[prediction_service.BatchPredictRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        input_config: Optional[io.BatchPredictInputConfig] = None,
        output_config: Optional[io.BatchPredictOutputConfig] = None,
        params: Optional[MutableMapping[str, str]] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation.Operation:
        r"""Perform a batch prediction. Unlike the online
        [Predict][google.cloud.automl.v1beta1.PredictionService.Predict],
        batch prediction result won't be immediately available in the
        response. Instead, a long running operation object is returned.
        User can poll the operation result via
        [GetOperation][google.longrunning.Operations.GetOperation]
        method. Once the operation is done,
        [BatchPredictResult][google.cloud.automl.v1beta1.BatchPredictResult]
        is returned in the
        [response][google.longrunning.Operation.response] field.
        Available for following ML problems:

        -  Image Classification
        -  Image Object Detection
        -  Video Classification
        -  Video Object Tracking \* Text Extraction
        -  Tables

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import automl_v1beta1

            def sample_batch_predict():
                # Create a client
                client = automl_v1beta1.PredictionServiceClient()

                # Initialize request argument(s)
                request = automl_v1beta1.BatchPredictRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.batch_predict(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.automl_v1beta1.types.BatchPredictRequest, dict]):
                The request object. Request message for
                [PredictionService.BatchPredict][google.cloud.automl.v1beta1.PredictionService.BatchPredict].
            name (str):
                Required. Name of the model requested
                to serve the batch prediction.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            input_config (google.cloud.automl_v1beta1.types.BatchPredictInputConfig):
                Required. The input configuration for
                batch prediction.

                This corresponds to the ``input_config`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            output_config (google.cloud.automl_v1beta1.types.BatchPredictOutputConfig):
                Required. The Configuration
                specifying where output predictions
                should be written.

                This corresponds to the ``output_config`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            params (MutableMapping[str, str]):
                Required. Additional domain-specific parameters for the
                predictions, any string must be up to 25000 characters
                long.

                -  For Text Classification:

                   ``score_threshold`` - (float) A value from 0.0 to
                   1.0. When the model makes predictions for a text
                   snippet, it will only produce results that have at
                   least this confidence score. The default is 0.5.

                -  For Image Classification:

                   ``score_threshold`` - (float) A value from 0.0 to
                   1.0. When the model makes predictions for an image,
                   it will only produce results that have at least this
                   confidence score. The default is 0.5.

                -  For Image Object Detection:

                   ``score_threshold`` - (float) When Model detects
                   objects on the image, it will only produce bounding
                   boxes which have at least this confidence score.
                   Value in 0 to 1 range, default is 0.5.
                   ``max_bounding_box_count`` - (int64) No more than
                   this number of bounding boxes will be produced per
                   image. Default is 100, the requested value may be
                   limited by server.

                -  For Video Classification :

                   ``score_threshold`` - (float) A value from 0.0 to
                   1.0. When the model makes predictions for a video, it
                   will only produce results that have at least this
                   confidence score. The default is 0.5.
                   ``segment_classification`` - (boolean) Set to true to
                   request segment-level classification. AutoML Video
                   Intelligence returns labels and their confidence
                   scores for the entire segment of the video that user
                   specified in the request configuration. The default
                   is "true". ``shot_classification`` - (boolean) Set to
                   true to request shot-level classification. AutoML
                   Video Intelligence determines the boundaries for each
                   camera shot in the entire segment of the video that
                   user specified in the request configuration. AutoML
                   Video Intelligence then returns labels and their
                   confidence scores for each detected shot, along with
                   the start and end time of the shot. WARNING: Model
                   evaluation is not done for this classification type,
                   the quality of it depends on training data, but there
                   are no metrics provided to describe that quality. The
                   default is "false". ``1s_interval_classification`` -
                   (boolean) Set to true to request classification for a
                   video at one-second intervals. AutoML Video
                   Intelligence returns labels and their confidence
                   scores for each second of the entire segment of the
                   video that user specified in the request
                   configuration. WARNING: Model evaluation is not done
                   for this classification type, the quality of it
                   depends on training data, but there are no metrics
                   provided to describe that quality. The default is
                   "false".

                -  For Tables:

                   feature_importance - (boolean) Whether feature
                   importance should be populated in the returned
                   TablesAnnotations. The default is false.

                -  For Video Object Tracking:

                   ``score_threshold`` - (float) When Model detects
                   objects on video frames, it will only produce
                   bounding boxes which have at least this confidence
                   score. Value in 0 to 1 range, default is 0.5.
                   ``max_bounding_box_count`` - (int64) No more than
                   this number of bounding boxes will be returned per
                   frame. Default is 100, the requested value may be
                   limited by server. ``min_bounding_box_size`` -
                   (float) Only bounding boxes with shortest edge at
                   least that long as a relative value of video frame
                   size will be returned. Value in 0 to 1 range. Default
                   is 0.

                This corresponds to the ``params`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.automl_v1beta1.types.BatchPredictResult` Result of the Batch Predict. This message is returned in
                   [response][google.longrunning.Operation.response] of
                   the operation returned by the
                   [PredictionService.BatchPredict][google.cloud.automl.v1beta1.PredictionService.BatchPredict].

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name, input_config, output_config, params])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a prediction_service.BatchPredictRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, prediction_service.BatchPredictRequest):
            request = prediction_service.BatchPredictRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name
            if input_config is not None:
                request.input_config = input_config
            if output_config is not None:
                request.output_config = output_config
            if params is not None:
                request.params = params

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.batch_predict]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            prediction_service.BatchPredictResult,
            metadata_type=operations.OperationMetadata,
        )

        # Done; return the response.
        return response

    def __enter__(self) -> "PredictionServiceClient":
        return self

    def __exit__(self, type, value, traceback):
        """Releases underlying transport's resources.

        .. warning::
            ONLY use as a context manager if the transport is NOT shared
            with other clients! Exiting the with block will CLOSE the transport
            and may cause errors in other clients!
        """
        self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)


__all__ = ("PredictionServiceClient",)
