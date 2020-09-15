# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
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

import os
import mock

import grpc
from grpc.experimental import aio
import math
import pytest
from proto.marshal.rules.dates import DurationRule, TimestampRule

from google import auth
from google.api_core import client_options
from google.api_core import exceptions
from google.api_core import future
from google.api_core import gapic_v1
from google.api_core import grpc_helpers
from google.api_core import grpc_helpers_async
from google.api_core import operation_async
from google.api_core import operations_v1
from google.auth import credentials
from google.auth.exceptions import MutualTLSChannelError
from google.cloud.automl_v1.services.auto_ml import AutoMlAsyncClient
from google.cloud.automl_v1.services.auto_ml import AutoMlClient
from google.cloud.automl_v1.services.auto_ml import pagers
from google.cloud.automl_v1.services.auto_ml import transports
from google.cloud.automl_v1.types import annotation_spec
from google.cloud.automl_v1.types import classification
from google.cloud.automl_v1.types import dataset
from google.cloud.automl_v1.types import dataset as gca_dataset
from google.cloud.automl_v1.types import detection
from google.cloud.automl_v1.types import image
from google.cloud.automl_v1.types import io
from google.cloud.automl_v1.types import model
from google.cloud.automl_v1.types import model as gca_model
from google.cloud.automl_v1.types import model_evaluation
from google.cloud.automl_v1.types import operations
from google.cloud.automl_v1.types import service
from google.cloud.automl_v1.types import text
from google.cloud.automl_v1.types import text_extraction
from google.cloud.automl_v1.types import text_sentiment
from google.cloud.automl_v1.types import translation
from google.longrunning import operations_pb2
from google.oauth2 import service_account
from google.protobuf import field_mask_pb2 as field_mask  # type: ignore
from google.protobuf import timestamp_pb2 as timestamp  # type: ignore


def client_cert_source_callback():
    return b"cert bytes", b"key bytes"


# If default endpoint is localhost, then default mtls endpoint will be the same.
# This method modifies the default endpoint so the client can produce a different
# mtls endpoint for endpoint testing purposes.
def modify_default_endpoint(client):
    return (
        "foo.googleapis.com"
        if ("localhost" in client.DEFAULT_ENDPOINT)
        else client.DEFAULT_ENDPOINT
    )


def test__get_default_mtls_endpoint():
    api_endpoint = "example.googleapis.com"
    api_mtls_endpoint = "example.mtls.googleapis.com"
    sandbox_endpoint = "example.sandbox.googleapis.com"
    sandbox_mtls_endpoint = "example.mtls.sandbox.googleapis.com"
    non_googleapi = "api.example.com"

    assert AutoMlClient._get_default_mtls_endpoint(None) is None
    assert AutoMlClient._get_default_mtls_endpoint(api_endpoint) == api_mtls_endpoint
    assert (
        AutoMlClient._get_default_mtls_endpoint(api_mtls_endpoint) == api_mtls_endpoint
    )
    assert (
        AutoMlClient._get_default_mtls_endpoint(sandbox_endpoint)
        == sandbox_mtls_endpoint
    )
    assert (
        AutoMlClient._get_default_mtls_endpoint(sandbox_mtls_endpoint)
        == sandbox_mtls_endpoint
    )
    assert AutoMlClient._get_default_mtls_endpoint(non_googleapi) == non_googleapi


@pytest.mark.parametrize("client_class", [AutoMlClient, AutoMlAsyncClient])
def test_auto_ml_client_from_service_account_file(client_class):
    creds = credentials.AnonymousCredentials()
    with mock.patch.object(
        service_account.Credentials, "from_service_account_file"
    ) as factory:
        factory.return_value = creds
        client = client_class.from_service_account_file("dummy/file/path.json")
        assert client._transport._credentials == creds

        client = client_class.from_service_account_json("dummy/file/path.json")
        assert client._transport._credentials == creds

        assert client._transport._host == "automl.googleapis.com:443"


def test_auto_ml_client_get_transport_class():
    transport = AutoMlClient.get_transport_class()
    assert transport == transports.AutoMlGrpcTransport

    transport = AutoMlClient.get_transport_class("grpc")
    assert transport == transports.AutoMlGrpcTransport


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name",
    [
        (AutoMlClient, transports.AutoMlGrpcTransport, "grpc"),
        (AutoMlAsyncClient, transports.AutoMlGrpcAsyncIOTransport, "grpc_asyncio"),
    ],
)
@mock.patch.object(
    AutoMlClient, "DEFAULT_ENDPOINT", modify_default_endpoint(AutoMlClient)
)
@mock.patch.object(
    AutoMlAsyncClient, "DEFAULT_ENDPOINT", modify_default_endpoint(AutoMlAsyncClient)
)
def test_auto_ml_client_client_options(client_class, transport_class, transport_name):
    # Check that if channel is provided we won't create a new one.
    with mock.patch.object(AutoMlClient, "get_transport_class") as gtc:
        transport = transport_class(credentials=credentials.AnonymousCredentials())
        client = client_class(transport=transport)
        gtc.assert_not_called()

    # Check that if channel is provided via str we will create a new one.
    with mock.patch.object(AutoMlClient, "get_transport_class") as gtc:
        client = client_class(transport=transport_name)
        gtc.assert_called()

    # Check the case api_endpoint is provided.
    options = client_options.ClientOptions(api_endpoint="squid.clam.whelk")
    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class(client_options=options)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host="squid.clam.whelk",
            scopes=None,
            api_mtls_endpoint="squid.clam.whelk",
            client_cert_source=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
        )

    # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS is
    # "never".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS": "never"}):
        with mock.patch.object(transport_class, "__init__") as patched:
            patched.return_value = None
            client = client_class()
            patched.assert_called_once_with(
                credentials=None,
                credentials_file=None,
                host=client.DEFAULT_ENDPOINT,
                scopes=None,
                api_mtls_endpoint=client.DEFAULT_ENDPOINT,
                client_cert_source=None,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
            )

    # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS is
    # "always".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS": "always"}):
        with mock.patch.object(transport_class, "__init__") as patched:
            patched.return_value = None
            client = client_class()
            patched.assert_called_once_with(
                credentials=None,
                credentials_file=None,
                host=client.DEFAULT_MTLS_ENDPOINT,
                scopes=None,
                api_mtls_endpoint=client.DEFAULT_MTLS_ENDPOINT,
                client_cert_source=None,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
            )

    # Check the case api_endpoint is not provided, GOOGLE_API_USE_MTLS is
    # "auto", and client_cert_source is provided.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS": "auto"}):
        options = client_options.ClientOptions(
            client_cert_source=client_cert_source_callback
        )
        with mock.patch.object(transport_class, "__init__") as patched:
            patched.return_value = None
            client = client_class(client_options=options)
            patched.assert_called_once_with(
                credentials=None,
                credentials_file=None,
                host=client.DEFAULT_MTLS_ENDPOINT,
                scopes=None,
                api_mtls_endpoint=client.DEFAULT_MTLS_ENDPOINT,
                client_cert_source=client_cert_source_callback,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
            )

    # Check the case api_endpoint is not provided, GOOGLE_API_USE_MTLS is
    # "auto", and default_client_cert_source is provided.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS": "auto"}):
        with mock.patch.object(transport_class, "__init__") as patched:
            with mock.patch(
                "google.auth.transport.mtls.has_default_client_cert_source",
                return_value=True,
            ):
                patched.return_value = None
                client = client_class()
                patched.assert_called_once_with(
                    credentials=None,
                    credentials_file=None,
                    host=client.DEFAULT_MTLS_ENDPOINT,
                    scopes=None,
                    api_mtls_endpoint=client.DEFAULT_MTLS_ENDPOINT,
                    client_cert_source=None,
                    quota_project_id=None,
                    client_info=transports.base.DEFAULT_CLIENT_INFO,
                )

    # Check the case api_endpoint is not provided, GOOGLE_API_USE_MTLS is
    # "auto", but client_cert_source and default_client_cert_source are None.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS": "auto"}):
        with mock.patch.object(transport_class, "__init__") as patched:
            with mock.patch(
                "google.auth.transport.mtls.has_default_client_cert_source",
                return_value=False,
            ):
                patched.return_value = None
                client = client_class()
                patched.assert_called_once_with(
                    credentials=None,
                    credentials_file=None,
                    host=client.DEFAULT_ENDPOINT,
                    scopes=None,
                    api_mtls_endpoint=client.DEFAULT_ENDPOINT,
                    client_cert_source=None,
                    quota_project_id=None,
                    client_info=transports.base.DEFAULT_CLIENT_INFO,
                )

    # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS has
    # unsupported value.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS": "Unsupported"}):
        with pytest.raises(MutualTLSChannelError):
            client = client_class()

    # Check the case quota_project_id is provided
    options = client_options.ClientOptions(quota_project_id="octopus")
    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class(client_options=options)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host=client.DEFAULT_ENDPOINT,
            scopes=None,
            api_mtls_endpoint=client.DEFAULT_ENDPOINT,
            client_cert_source=None,
            quota_project_id="octopus",
            client_info=transports.base.DEFAULT_CLIENT_INFO,
        )


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name",
    [
        (AutoMlClient, transports.AutoMlGrpcTransport, "grpc"),
        (AutoMlAsyncClient, transports.AutoMlGrpcAsyncIOTransport, "grpc_asyncio"),
    ],
)
def test_auto_ml_client_client_options_scopes(
    client_class, transport_class, transport_name
):
    # Check the case scopes are provided.
    options = client_options.ClientOptions(scopes=["1", "2"],)
    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class(client_options=options)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host=client.DEFAULT_ENDPOINT,
            scopes=["1", "2"],
            api_mtls_endpoint=client.DEFAULT_ENDPOINT,
            client_cert_source=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
        )


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name",
    [
        (AutoMlClient, transports.AutoMlGrpcTransport, "grpc"),
        (AutoMlAsyncClient, transports.AutoMlGrpcAsyncIOTransport, "grpc_asyncio"),
    ],
)
def test_auto_ml_client_client_options_credentials_file(
    client_class, transport_class, transport_name
):
    # Check the case credentials file is provided.
    options = client_options.ClientOptions(credentials_file="credentials.json")
    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class(client_options=options)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file="credentials.json",
            host=client.DEFAULT_ENDPOINT,
            scopes=None,
            api_mtls_endpoint=client.DEFAULT_ENDPOINT,
            client_cert_source=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
        )


def test_auto_ml_client_client_options_from_dict():
    with mock.patch(
        "google.cloud.automl_v1.services.auto_ml.transports.AutoMlGrpcTransport.__init__"
    ) as grpc_transport:
        grpc_transport.return_value = None
        client = AutoMlClient(client_options={"api_endpoint": "squid.clam.whelk"})
        grpc_transport.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host="squid.clam.whelk",
            scopes=None,
            api_mtls_endpoint="squid.clam.whelk",
            client_cert_source=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
        )


def test_create_dataset(
    transport: str = "grpc", request_type=service.CreateDatasetRequest
):
    client = AutoMlClient(
        credentials=credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.create_dataset), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/spam")

        response = client.create_dataset(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.CreateDatasetRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_create_dataset_from_dict():
    test_create_dataset(request_type=dict)


@pytest.mark.asyncio
async def test_create_dataset_async(transport: str = "grpc_asyncio"):
    client = AutoMlAsyncClient(
        credentials=credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = service.CreateDatasetRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.create_dataset), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )

        response = await client.create_dataset(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_create_dataset_field_headers():
    client = AutoMlClient(credentials=credentials.AnonymousCredentials(),)

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.CreateDatasetRequest()
    request.parent = "parent/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.create_dataset), "__call__") as call:
        call.return_value = operations_pb2.Operation(name="operations/op")

        client.create_dataset(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "parent=parent/value",) in kw["metadata"]


@pytest.mark.asyncio
async def test_create_dataset_field_headers_async():
    client = AutoMlAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.CreateDatasetRequest()
    request.parent = "parent/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.create_dataset), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/op")
        )

        await client.create_dataset(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "parent=parent/value",) in kw["metadata"]


def test_create_dataset_flattened():
    client = AutoMlClient(credentials=credentials.AnonymousCredentials(),)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.create_dataset), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.create_dataset(
            parent="parent_value",
            dataset=gca_dataset.Dataset(
                translation_dataset_metadata=translation.TranslationDatasetMetadata(
                    source_language_code="source_language_code_value"
                )
            ),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0].parent == "parent_value"

        assert args[0].dataset == gca_dataset.Dataset(
            translation_dataset_metadata=translation.TranslationDatasetMetadata(
                source_language_code="source_language_code_value"
            )
        )


def test_create_dataset_flattened_error():
    client = AutoMlClient(credentials=credentials.AnonymousCredentials(),)

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.create_dataset(
            service.CreateDatasetRequest(),
            parent="parent_value",
            dataset=gca_dataset.Dataset(
                translation_dataset_metadata=translation.TranslationDatasetMetadata(
                    source_language_code="source_language_code_value"
                )
            ),
        )


@pytest.mark.asyncio
async def test_create_dataset_flattened_async():
    client = AutoMlAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.create_dataset), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.create_dataset(
            parent="parent_value",
            dataset=gca_dataset.Dataset(
                translation_dataset_metadata=translation.TranslationDatasetMetadata(
                    source_language_code="source_language_code_value"
                )
            ),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0].parent == "parent_value"

        assert args[0].dataset == gca_dataset.Dataset(
            translation_dataset_metadata=translation.TranslationDatasetMetadata(
                source_language_code="source_language_code_value"
            )
        )


@pytest.mark.asyncio
async def test_create_dataset_flattened_error_async():
    client = AutoMlAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.create_dataset(
            service.CreateDatasetRequest(),
            parent="parent_value",
            dataset=gca_dataset.Dataset(
                translation_dataset_metadata=translation.TranslationDatasetMetadata(
                    source_language_code="source_language_code_value"
                )
            ),
        )


def test_get_dataset(transport: str = "grpc", request_type=service.GetDatasetRequest):
    client = AutoMlClient(
        credentials=credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.get_dataset), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = dataset.Dataset(
            name="name_value",
            display_name="display_name_value",
            description="description_value",
            example_count=1396,
            etag="etag_value",
            translation_dataset_metadata=translation.TranslationDatasetMetadata(
                source_language_code="source_language_code_value"
            ),
        )

        response = client.get_dataset(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.GetDatasetRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, dataset.Dataset)

    assert response.name == "name_value"

    assert response.display_name == "display_name_value"

    assert response.description == "description_value"

    assert response.example_count == 1396

    assert response.etag == "etag_value"


def test_get_dataset_from_dict():
    test_get_dataset(request_type=dict)


@pytest.mark.asyncio
async def test_get_dataset_async(transport: str = "grpc_asyncio"):
    client = AutoMlAsyncClient(
        credentials=credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = service.GetDatasetRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.get_dataset), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            dataset.Dataset(
                name="name_value",
                display_name="display_name_value",
                description="description_value",
                example_count=1396,
                etag="etag_value",
            )
        )

        response = await client.get_dataset(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, dataset.Dataset)

    assert response.name == "name_value"

    assert response.display_name == "display_name_value"

    assert response.description == "description_value"

    assert response.example_count == 1396

    assert response.etag == "etag_value"


def test_get_dataset_field_headers():
    client = AutoMlClient(credentials=credentials.AnonymousCredentials(),)

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.GetDatasetRequest()
    request.name = "name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.get_dataset), "__call__") as call:
        call.return_value = dataset.Dataset()

        client.get_dataset(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=name/value",) in kw["metadata"]


@pytest.mark.asyncio
async def test_get_dataset_field_headers_async():
    client = AutoMlAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.GetDatasetRequest()
    request.name = "name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.get_dataset), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(dataset.Dataset())

        await client.get_dataset(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=name/value",) in kw["metadata"]


def test_get_dataset_flattened():
    client = AutoMlClient(credentials=credentials.AnonymousCredentials(),)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.get_dataset), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = dataset.Dataset()

        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.get_dataset(name="name_value",)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0].name == "name_value"


def test_get_dataset_flattened_error():
    client = AutoMlClient(credentials=credentials.AnonymousCredentials(),)

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_dataset(
            service.GetDatasetRequest(), name="name_value",
        )


@pytest.mark.asyncio
async def test_get_dataset_flattened_async():
    client = AutoMlAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.get_dataset), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = dataset.Dataset()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(dataset.Dataset())
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.get_dataset(name="name_value",)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0].name == "name_value"


@pytest.mark.asyncio
async def test_get_dataset_flattened_error_async():
    client = AutoMlAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.get_dataset(
            service.GetDatasetRequest(), name="name_value",
        )


def test_list_datasets(
    transport: str = "grpc", request_type=service.ListDatasetsRequest
):
    client = AutoMlClient(
        credentials=credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.list_datasets), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.ListDatasetsResponse(
            next_page_token="next_page_token_value",
        )

        response = client.list_datasets(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.ListDatasetsRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListDatasetsPager)

    assert response.next_page_token == "next_page_token_value"


def test_list_datasets_from_dict():
    test_list_datasets(request_type=dict)


@pytest.mark.asyncio
async def test_list_datasets_async(transport: str = "grpc_asyncio"):
    client = AutoMlAsyncClient(
        credentials=credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = service.ListDatasetsRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.list_datasets), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            service.ListDatasetsResponse(next_page_token="next_page_token_value",)
        )

        response = await client.list_datasets(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListDatasetsAsyncPager)

    assert response.next_page_token == "next_page_token_value"


def test_list_datasets_field_headers():
    client = AutoMlClient(credentials=credentials.AnonymousCredentials(),)

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.ListDatasetsRequest()
    request.parent = "parent/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.list_datasets), "__call__") as call:
        call.return_value = service.ListDatasetsResponse()

        client.list_datasets(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "parent=parent/value",) in kw["metadata"]


@pytest.mark.asyncio
async def test_list_datasets_field_headers_async():
    client = AutoMlAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.ListDatasetsRequest()
    request.parent = "parent/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.list_datasets), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            service.ListDatasetsResponse()
        )

        await client.list_datasets(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "parent=parent/value",) in kw["metadata"]


def test_list_datasets_flattened():
    client = AutoMlClient(credentials=credentials.AnonymousCredentials(),)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.list_datasets), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.ListDatasetsResponse()

        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.list_datasets(parent="parent_value",)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0].parent == "parent_value"


def test_list_datasets_flattened_error():
    client = AutoMlClient(credentials=credentials.AnonymousCredentials(),)

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_datasets(
            service.ListDatasetsRequest(), parent="parent_value",
        )


@pytest.mark.asyncio
async def test_list_datasets_flattened_async():
    client = AutoMlAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.list_datasets), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.ListDatasetsResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            service.ListDatasetsResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.list_datasets(parent="parent_value",)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0].parent == "parent_value"


@pytest.mark.asyncio
async def test_list_datasets_flattened_error_async():
    client = AutoMlAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.list_datasets(
            service.ListDatasetsRequest(), parent="parent_value",
        )


def test_list_datasets_pager():
    client = AutoMlClient(credentials=credentials.AnonymousCredentials,)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.list_datasets), "__call__") as call:
        # Set the response to a series of pages.
        call.side_effect = (
            service.ListDatasetsResponse(
                datasets=[dataset.Dataset(), dataset.Dataset(), dataset.Dataset(),],
                next_page_token="abc",
            ),
            service.ListDatasetsResponse(datasets=[], next_page_token="def",),
            service.ListDatasetsResponse(
                datasets=[dataset.Dataset(),], next_page_token="ghi",
            ),
            service.ListDatasetsResponse(
                datasets=[dataset.Dataset(), dataset.Dataset(),],
            ),
            RuntimeError,
        )

        metadata = ()
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", ""),)),
        )
        pager = client.list_datasets(request={})

        assert pager._metadata == metadata

        results = [i for i in pager]
        assert len(results) == 6
        assert all(isinstance(i, dataset.Dataset) for i in results)


def test_list_datasets_pages():
    client = AutoMlClient(credentials=credentials.AnonymousCredentials,)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.list_datasets), "__call__") as call:
        # Set the response to a series of pages.
        call.side_effect = (
            service.ListDatasetsResponse(
                datasets=[dataset.Dataset(), dataset.Dataset(), dataset.Dataset(),],
                next_page_token="abc",
            ),
            service.ListDatasetsResponse(datasets=[], next_page_token="def",),
            service.ListDatasetsResponse(
                datasets=[dataset.Dataset(),], next_page_token="ghi",
            ),
            service.ListDatasetsResponse(
                datasets=[dataset.Dataset(), dataset.Dataset(),],
            ),
            RuntimeError,
        )
        pages = list(client.list_datasets(request={}).pages)
        for page, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page.raw_page.next_page_token == token


@pytest.mark.asyncio
async def test_list_datasets_async_pager():
    client = AutoMlAsyncClient(credentials=credentials.AnonymousCredentials,)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.list_datasets),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            service.ListDatasetsResponse(
                datasets=[dataset.Dataset(), dataset.Dataset(), dataset.Dataset(),],
                next_page_token="abc",
            ),
            service.ListDatasetsResponse(datasets=[], next_page_token="def",),
            service.ListDatasetsResponse(
                datasets=[dataset.Dataset(),], next_page_token="ghi",
            ),
            service.ListDatasetsResponse(
                datasets=[dataset.Dataset(), dataset.Dataset(),],
            ),
            RuntimeError,
        )
        async_pager = await client.list_datasets(request={},)
        assert async_pager.next_page_token == "abc"
        responses = []
        async for response in async_pager:
            responses.append(response)

        assert len(responses) == 6
        assert all(isinstance(i, dataset.Dataset) for i in responses)


@pytest.mark.asyncio
async def test_list_datasets_async_pages():
    client = AutoMlAsyncClient(credentials=credentials.AnonymousCredentials,)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.list_datasets),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            service.ListDatasetsResponse(
                datasets=[dataset.Dataset(), dataset.Dataset(), dataset.Dataset(),],
                next_page_token="abc",
            ),
            service.ListDatasetsResponse(datasets=[], next_page_token="def",),
            service.ListDatasetsResponse(
                datasets=[dataset.Dataset(),], next_page_token="ghi",
            ),
            service.ListDatasetsResponse(
                datasets=[dataset.Dataset(), dataset.Dataset(),],
            ),
            RuntimeError,
        )
        pages = []
        async for page in (await client.list_datasets(request={})).pages:
            pages.append(page)
        for page, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page.raw_page.next_page_token == token


def test_update_dataset(
    transport: str = "grpc", request_type=service.UpdateDatasetRequest
):
    client = AutoMlClient(
        credentials=credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.update_dataset), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = gca_dataset.Dataset(
            name="name_value",
            display_name="display_name_value",
            description="description_value",
            example_count=1396,
            etag="etag_value",
            translation_dataset_metadata=translation.TranslationDatasetMetadata(
                source_language_code="source_language_code_value"
            ),
        )

        response = client.update_dataset(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.UpdateDatasetRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, gca_dataset.Dataset)

    assert response.name == "name_value"

    assert response.display_name == "display_name_value"

    assert response.description == "description_value"

    assert response.example_count == 1396

    assert response.etag == "etag_value"


def test_update_dataset_from_dict():
    test_update_dataset(request_type=dict)


@pytest.mark.asyncio
async def test_update_dataset_async(transport: str = "grpc_asyncio"):
    client = AutoMlAsyncClient(
        credentials=credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = service.UpdateDatasetRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.update_dataset), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            gca_dataset.Dataset(
                name="name_value",
                display_name="display_name_value",
                description="description_value",
                example_count=1396,
                etag="etag_value",
            )
        )

        response = await client.update_dataset(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, gca_dataset.Dataset)

    assert response.name == "name_value"

    assert response.display_name == "display_name_value"

    assert response.description == "description_value"

    assert response.example_count == 1396

    assert response.etag == "etag_value"


def test_update_dataset_field_headers():
    client = AutoMlClient(credentials=credentials.AnonymousCredentials(),)

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.UpdateDatasetRequest()
    request.dataset.name = "dataset.name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.update_dataset), "__call__") as call:
        call.return_value = gca_dataset.Dataset()

        client.update_dataset(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "dataset.name=dataset.name/value",) in kw[
        "metadata"
    ]


@pytest.mark.asyncio
async def test_update_dataset_field_headers_async():
    client = AutoMlAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.UpdateDatasetRequest()
    request.dataset.name = "dataset.name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.update_dataset), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(gca_dataset.Dataset())

        await client.update_dataset(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "dataset.name=dataset.name/value",) in kw[
        "metadata"
    ]


def test_update_dataset_flattened():
    client = AutoMlClient(credentials=credentials.AnonymousCredentials(),)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.update_dataset), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = gca_dataset.Dataset()

        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.update_dataset(
            dataset=gca_dataset.Dataset(
                translation_dataset_metadata=translation.TranslationDatasetMetadata(
                    source_language_code="source_language_code_value"
                )
            ),
            update_mask=field_mask.FieldMask(paths=["paths_value"]),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0].dataset == gca_dataset.Dataset(
            translation_dataset_metadata=translation.TranslationDatasetMetadata(
                source_language_code="source_language_code_value"
            )
        )

        assert args[0].update_mask == field_mask.FieldMask(paths=["paths_value"])


def test_update_dataset_flattened_error():
    client = AutoMlClient(credentials=credentials.AnonymousCredentials(),)

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_dataset(
            service.UpdateDatasetRequest(),
            dataset=gca_dataset.Dataset(
                translation_dataset_metadata=translation.TranslationDatasetMetadata(
                    source_language_code="source_language_code_value"
                )
            ),
            update_mask=field_mask.FieldMask(paths=["paths_value"]),
        )


@pytest.mark.asyncio
async def test_update_dataset_flattened_async():
    client = AutoMlAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.update_dataset), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = gca_dataset.Dataset()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(gca_dataset.Dataset())
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.update_dataset(
            dataset=gca_dataset.Dataset(
                translation_dataset_metadata=translation.TranslationDatasetMetadata(
                    source_language_code="source_language_code_value"
                )
            ),
            update_mask=field_mask.FieldMask(paths=["paths_value"]),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0].dataset == gca_dataset.Dataset(
            translation_dataset_metadata=translation.TranslationDatasetMetadata(
                source_language_code="source_language_code_value"
            )
        )

        assert args[0].update_mask == field_mask.FieldMask(paths=["paths_value"])


@pytest.mark.asyncio
async def test_update_dataset_flattened_error_async():
    client = AutoMlAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.update_dataset(
            service.UpdateDatasetRequest(),
            dataset=gca_dataset.Dataset(
                translation_dataset_metadata=translation.TranslationDatasetMetadata(
                    source_language_code="source_language_code_value"
                )
            ),
            update_mask=field_mask.FieldMask(paths=["paths_value"]),
        )


def test_delete_dataset(
    transport: str = "grpc", request_type=service.DeleteDatasetRequest
):
    client = AutoMlClient(
        credentials=credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.delete_dataset), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/spam")

        response = client.delete_dataset(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.DeleteDatasetRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_delete_dataset_from_dict():
    test_delete_dataset(request_type=dict)


@pytest.mark.asyncio
async def test_delete_dataset_async(transport: str = "grpc_asyncio"):
    client = AutoMlAsyncClient(
        credentials=credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = service.DeleteDatasetRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.delete_dataset), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )

        response = await client.delete_dataset(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_delete_dataset_field_headers():
    client = AutoMlClient(credentials=credentials.AnonymousCredentials(),)

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.DeleteDatasetRequest()
    request.name = "name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.delete_dataset), "__call__") as call:
        call.return_value = operations_pb2.Operation(name="operations/op")

        client.delete_dataset(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=name/value",) in kw["metadata"]


@pytest.mark.asyncio
async def test_delete_dataset_field_headers_async():
    client = AutoMlAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.DeleteDatasetRequest()
    request.name = "name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.delete_dataset), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/op")
        )

        await client.delete_dataset(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=name/value",) in kw["metadata"]


def test_delete_dataset_flattened():
    client = AutoMlClient(credentials=credentials.AnonymousCredentials(),)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.delete_dataset), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.delete_dataset(name="name_value",)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0].name == "name_value"


def test_delete_dataset_flattened_error():
    client = AutoMlClient(credentials=credentials.AnonymousCredentials(),)

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.delete_dataset(
            service.DeleteDatasetRequest(), name="name_value",
        )


@pytest.mark.asyncio
async def test_delete_dataset_flattened_async():
    client = AutoMlAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.delete_dataset), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.delete_dataset(name="name_value",)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0].name == "name_value"


@pytest.mark.asyncio
async def test_delete_dataset_flattened_error_async():
    client = AutoMlAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.delete_dataset(
            service.DeleteDatasetRequest(), name="name_value",
        )


def test_import_data(transport: str = "grpc", request_type=service.ImportDataRequest):
    client = AutoMlClient(
        credentials=credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.import_data), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/spam")

        response = client.import_data(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.ImportDataRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_import_data_from_dict():
    test_import_data(request_type=dict)


@pytest.mark.asyncio
async def test_import_data_async(transport: str = "grpc_asyncio"):
    client = AutoMlAsyncClient(
        credentials=credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = service.ImportDataRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.import_data), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )

        response = await client.import_data(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_import_data_field_headers():
    client = AutoMlClient(credentials=credentials.AnonymousCredentials(),)

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.ImportDataRequest()
    request.name = "name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.import_data), "__call__") as call:
        call.return_value = operations_pb2.Operation(name="operations/op")

        client.import_data(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=name/value",) in kw["metadata"]


@pytest.mark.asyncio
async def test_import_data_field_headers_async():
    client = AutoMlAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.ImportDataRequest()
    request.name = "name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.import_data), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/op")
        )

        await client.import_data(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=name/value",) in kw["metadata"]


def test_import_data_flattened():
    client = AutoMlClient(credentials=credentials.AnonymousCredentials(),)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.import_data), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.import_data(
            name="name_value",
            input_config=io.InputConfig(
                gcs_source=io.GcsSource(input_uris=["input_uris_value"])
            ),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0].name == "name_value"

        assert args[0].input_config == io.InputConfig(
            gcs_source=io.GcsSource(input_uris=["input_uris_value"])
        )


def test_import_data_flattened_error():
    client = AutoMlClient(credentials=credentials.AnonymousCredentials(),)

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.import_data(
            service.ImportDataRequest(),
            name="name_value",
            input_config=io.InputConfig(
                gcs_source=io.GcsSource(input_uris=["input_uris_value"])
            ),
        )


@pytest.mark.asyncio
async def test_import_data_flattened_async():
    client = AutoMlAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.import_data), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.import_data(
            name="name_value",
            input_config=io.InputConfig(
                gcs_source=io.GcsSource(input_uris=["input_uris_value"])
            ),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0].name == "name_value"

        assert args[0].input_config == io.InputConfig(
            gcs_source=io.GcsSource(input_uris=["input_uris_value"])
        )


@pytest.mark.asyncio
async def test_import_data_flattened_error_async():
    client = AutoMlAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.import_data(
            service.ImportDataRequest(),
            name="name_value",
            input_config=io.InputConfig(
                gcs_source=io.GcsSource(input_uris=["input_uris_value"])
            ),
        )


def test_export_data(transport: str = "grpc", request_type=service.ExportDataRequest):
    client = AutoMlClient(
        credentials=credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.export_data), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/spam")

        response = client.export_data(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.ExportDataRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_export_data_from_dict():
    test_export_data(request_type=dict)


@pytest.mark.asyncio
async def test_export_data_async(transport: str = "grpc_asyncio"):
    client = AutoMlAsyncClient(
        credentials=credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = service.ExportDataRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.export_data), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )

        response = await client.export_data(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_export_data_field_headers():
    client = AutoMlClient(credentials=credentials.AnonymousCredentials(),)

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.ExportDataRequest()
    request.name = "name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.export_data), "__call__") as call:
        call.return_value = operations_pb2.Operation(name="operations/op")

        client.export_data(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=name/value",) in kw["metadata"]


@pytest.mark.asyncio
async def test_export_data_field_headers_async():
    client = AutoMlAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.ExportDataRequest()
    request.name = "name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.export_data), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/op")
        )

        await client.export_data(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=name/value",) in kw["metadata"]


def test_export_data_flattened():
    client = AutoMlClient(credentials=credentials.AnonymousCredentials(),)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.export_data), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.export_data(
            name="name_value",
            output_config=io.OutputConfig(
                gcs_destination=io.GcsDestination(
                    output_uri_prefix="output_uri_prefix_value"
                )
            ),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0].name == "name_value"

        assert args[0].output_config == io.OutputConfig(
            gcs_destination=io.GcsDestination(
                output_uri_prefix="output_uri_prefix_value"
            )
        )


def test_export_data_flattened_error():
    client = AutoMlClient(credentials=credentials.AnonymousCredentials(),)

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.export_data(
            service.ExportDataRequest(),
            name="name_value",
            output_config=io.OutputConfig(
                gcs_destination=io.GcsDestination(
                    output_uri_prefix="output_uri_prefix_value"
                )
            ),
        )


@pytest.mark.asyncio
async def test_export_data_flattened_async():
    client = AutoMlAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.export_data), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.export_data(
            name="name_value",
            output_config=io.OutputConfig(
                gcs_destination=io.GcsDestination(
                    output_uri_prefix="output_uri_prefix_value"
                )
            ),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0].name == "name_value"

        assert args[0].output_config == io.OutputConfig(
            gcs_destination=io.GcsDestination(
                output_uri_prefix="output_uri_prefix_value"
            )
        )


@pytest.mark.asyncio
async def test_export_data_flattened_error_async():
    client = AutoMlAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.export_data(
            service.ExportDataRequest(),
            name="name_value",
            output_config=io.OutputConfig(
                gcs_destination=io.GcsDestination(
                    output_uri_prefix="output_uri_prefix_value"
                )
            ),
        )


def test_get_annotation_spec(
    transport: str = "grpc", request_type=service.GetAnnotationSpecRequest
):
    client = AutoMlClient(
        credentials=credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._transport.get_annotation_spec), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = annotation_spec.AnnotationSpec(
            name="name_value", display_name="display_name_value", example_count=1396,
        )

        response = client.get_annotation_spec(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.GetAnnotationSpecRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, annotation_spec.AnnotationSpec)

    assert response.name == "name_value"

    assert response.display_name == "display_name_value"

    assert response.example_count == 1396


def test_get_annotation_spec_from_dict():
    test_get_annotation_spec(request_type=dict)


@pytest.mark.asyncio
async def test_get_annotation_spec_async(transport: str = "grpc_asyncio"):
    client = AutoMlAsyncClient(
        credentials=credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = service.GetAnnotationSpecRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.get_annotation_spec), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            annotation_spec.AnnotationSpec(
                name="name_value",
                display_name="display_name_value",
                example_count=1396,
            )
        )

        response = await client.get_annotation_spec(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, annotation_spec.AnnotationSpec)

    assert response.name == "name_value"

    assert response.display_name == "display_name_value"

    assert response.example_count == 1396


def test_get_annotation_spec_field_headers():
    client = AutoMlClient(credentials=credentials.AnonymousCredentials(),)

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.GetAnnotationSpecRequest()
    request.name = "name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._transport.get_annotation_spec), "__call__"
    ) as call:
        call.return_value = annotation_spec.AnnotationSpec()

        client.get_annotation_spec(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=name/value",) in kw["metadata"]


@pytest.mark.asyncio
async def test_get_annotation_spec_field_headers_async():
    client = AutoMlAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.GetAnnotationSpecRequest()
    request.name = "name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.get_annotation_spec), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            annotation_spec.AnnotationSpec()
        )

        await client.get_annotation_spec(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=name/value",) in kw["metadata"]


def test_get_annotation_spec_flattened():
    client = AutoMlClient(credentials=credentials.AnonymousCredentials(),)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._transport.get_annotation_spec), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = annotation_spec.AnnotationSpec()

        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.get_annotation_spec(name="name_value",)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0].name == "name_value"


def test_get_annotation_spec_flattened_error():
    client = AutoMlClient(credentials=credentials.AnonymousCredentials(),)

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_annotation_spec(
            service.GetAnnotationSpecRequest(), name="name_value",
        )


@pytest.mark.asyncio
async def test_get_annotation_spec_flattened_async():
    client = AutoMlAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.get_annotation_spec), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = annotation_spec.AnnotationSpec()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            annotation_spec.AnnotationSpec()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.get_annotation_spec(name="name_value",)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0].name == "name_value"


@pytest.mark.asyncio
async def test_get_annotation_spec_flattened_error_async():
    client = AutoMlAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.get_annotation_spec(
            service.GetAnnotationSpecRequest(), name="name_value",
        )


def test_create_model(transport: str = "grpc", request_type=service.CreateModelRequest):
    client = AutoMlClient(
        credentials=credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.create_model), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/spam")

        response = client.create_model(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.CreateModelRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_create_model_from_dict():
    test_create_model(request_type=dict)


@pytest.mark.asyncio
async def test_create_model_async(transport: str = "grpc_asyncio"):
    client = AutoMlAsyncClient(
        credentials=credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = service.CreateModelRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.create_model), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )

        response = await client.create_model(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_create_model_field_headers():
    client = AutoMlClient(credentials=credentials.AnonymousCredentials(),)

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.CreateModelRequest()
    request.parent = "parent/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.create_model), "__call__") as call:
        call.return_value = operations_pb2.Operation(name="operations/op")

        client.create_model(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "parent=parent/value",) in kw["metadata"]


@pytest.mark.asyncio
async def test_create_model_field_headers_async():
    client = AutoMlAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.CreateModelRequest()
    request.parent = "parent/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.create_model), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/op")
        )

        await client.create_model(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "parent=parent/value",) in kw["metadata"]


def test_create_model_flattened():
    client = AutoMlClient(credentials=credentials.AnonymousCredentials(),)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.create_model), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.create_model(
            parent="parent_value",
            model=gca_model.Model(
                translation_model_metadata=translation.TranslationModelMetadata(
                    base_model="base_model_value"
                )
            ),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0].parent == "parent_value"

        assert args[0].model == gca_model.Model(
            translation_model_metadata=translation.TranslationModelMetadata(
                base_model="base_model_value"
            )
        )


def test_create_model_flattened_error():
    client = AutoMlClient(credentials=credentials.AnonymousCredentials(),)

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.create_model(
            service.CreateModelRequest(),
            parent="parent_value",
            model=gca_model.Model(
                translation_model_metadata=translation.TranslationModelMetadata(
                    base_model="base_model_value"
                )
            ),
        )


@pytest.mark.asyncio
async def test_create_model_flattened_async():
    client = AutoMlAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.create_model), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.create_model(
            parent="parent_value",
            model=gca_model.Model(
                translation_model_metadata=translation.TranslationModelMetadata(
                    base_model="base_model_value"
                )
            ),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0].parent == "parent_value"

        assert args[0].model == gca_model.Model(
            translation_model_metadata=translation.TranslationModelMetadata(
                base_model="base_model_value"
            )
        )


@pytest.mark.asyncio
async def test_create_model_flattened_error_async():
    client = AutoMlAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.create_model(
            service.CreateModelRequest(),
            parent="parent_value",
            model=gca_model.Model(
                translation_model_metadata=translation.TranslationModelMetadata(
                    base_model="base_model_value"
                )
            ),
        )


def test_get_model(transport: str = "grpc", request_type=service.GetModelRequest):
    client = AutoMlClient(
        credentials=credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.get_model), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = model.Model(
            name="name_value",
            display_name="display_name_value",
            dataset_id="dataset_id_value",
            deployment_state=model.Model.DeploymentState.DEPLOYED,
            etag="etag_value",
            translation_model_metadata=translation.TranslationModelMetadata(
                base_model="base_model_value"
            ),
        )

        response = client.get_model(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.GetModelRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, model.Model)

    assert response.name == "name_value"

    assert response.display_name == "display_name_value"

    assert response.dataset_id == "dataset_id_value"

    assert response.deployment_state == model.Model.DeploymentState.DEPLOYED

    assert response.etag == "etag_value"


def test_get_model_from_dict():
    test_get_model(request_type=dict)


@pytest.mark.asyncio
async def test_get_model_async(transport: str = "grpc_asyncio"):
    client = AutoMlAsyncClient(
        credentials=credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = service.GetModelRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.get_model), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            model.Model(
                name="name_value",
                display_name="display_name_value",
                dataset_id="dataset_id_value",
                deployment_state=model.Model.DeploymentState.DEPLOYED,
                etag="etag_value",
            )
        )

        response = await client.get_model(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, model.Model)

    assert response.name == "name_value"

    assert response.display_name == "display_name_value"

    assert response.dataset_id == "dataset_id_value"

    assert response.deployment_state == model.Model.DeploymentState.DEPLOYED

    assert response.etag == "etag_value"


def test_get_model_field_headers():
    client = AutoMlClient(credentials=credentials.AnonymousCredentials(),)

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.GetModelRequest()
    request.name = "name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.get_model), "__call__") as call:
        call.return_value = model.Model()

        client.get_model(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=name/value",) in kw["metadata"]


@pytest.mark.asyncio
async def test_get_model_field_headers_async():
    client = AutoMlAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.GetModelRequest()
    request.name = "name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.get_model), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(model.Model())

        await client.get_model(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=name/value",) in kw["metadata"]


def test_get_model_flattened():
    client = AutoMlClient(credentials=credentials.AnonymousCredentials(),)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.get_model), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = model.Model()

        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.get_model(name="name_value",)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0].name == "name_value"


def test_get_model_flattened_error():
    client = AutoMlClient(credentials=credentials.AnonymousCredentials(),)

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_model(
            service.GetModelRequest(), name="name_value",
        )


@pytest.mark.asyncio
async def test_get_model_flattened_async():
    client = AutoMlAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.get_model), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = model.Model()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(model.Model())
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.get_model(name="name_value",)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0].name == "name_value"


@pytest.mark.asyncio
async def test_get_model_flattened_error_async():
    client = AutoMlAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.get_model(
            service.GetModelRequest(), name="name_value",
        )


def test_list_models(transport: str = "grpc", request_type=service.ListModelsRequest):
    client = AutoMlClient(
        credentials=credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.list_models), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.ListModelsResponse(
            next_page_token="next_page_token_value",
        )

        response = client.list_models(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.ListModelsRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListModelsPager)

    assert response.next_page_token == "next_page_token_value"


def test_list_models_from_dict():
    test_list_models(request_type=dict)


@pytest.mark.asyncio
async def test_list_models_async(transport: str = "grpc_asyncio"):
    client = AutoMlAsyncClient(
        credentials=credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = service.ListModelsRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.list_models), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            service.ListModelsResponse(next_page_token="next_page_token_value",)
        )

        response = await client.list_models(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListModelsAsyncPager)

    assert response.next_page_token == "next_page_token_value"


def test_list_models_field_headers():
    client = AutoMlClient(credentials=credentials.AnonymousCredentials(),)

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.ListModelsRequest()
    request.parent = "parent/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.list_models), "__call__") as call:
        call.return_value = service.ListModelsResponse()

        client.list_models(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "parent=parent/value",) in kw["metadata"]


@pytest.mark.asyncio
async def test_list_models_field_headers_async():
    client = AutoMlAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.ListModelsRequest()
    request.parent = "parent/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.list_models), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            service.ListModelsResponse()
        )

        await client.list_models(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "parent=parent/value",) in kw["metadata"]


def test_list_models_flattened():
    client = AutoMlClient(credentials=credentials.AnonymousCredentials(),)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.list_models), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.ListModelsResponse()

        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.list_models(parent="parent_value",)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0].parent == "parent_value"


def test_list_models_flattened_error():
    client = AutoMlClient(credentials=credentials.AnonymousCredentials(),)

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_models(
            service.ListModelsRequest(), parent="parent_value",
        )


@pytest.mark.asyncio
async def test_list_models_flattened_async():
    client = AutoMlAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.list_models), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.ListModelsResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            service.ListModelsResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.list_models(parent="parent_value",)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0].parent == "parent_value"


@pytest.mark.asyncio
async def test_list_models_flattened_error_async():
    client = AutoMlAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.list_models(
            service.ListModelsRequest(), parent="parent_value",
        )


def test_list_models_pager():
    client = AutoMlClient(credentials=credentials.AnonymousCredentials,)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.list_models), "__call__") as call:
        # Set the response to a series of pages.
        call.side_effect = (
            service.ListModelsResponse(
                model=[model.Model(), model.Model(), model.Model(),],
                next_page_token="abc",
            ),
            service.ListModelsResponse(model=[], next_page_token="def",),
            service.ListModelsResponse(model=[model.Model(),], next_page_token="ghi",),
            service.ListModelsResponse(model=[model.Model(), model.Model(),],),
            RuntimeError,
        )

        metadata = ()
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", ""),)),
        )
        pager = client.list_models(request={})

        assert pager._metadata == metadata

        results = [i for i in pager]
        assert len(results) == 6
        assert all(isinstance(i, model.Model) for i in results)


def test_list_models_pages():
    client = AutoMlClient(credentials=credentials.AnonymousCredentials,)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.list_models), "__call__") as call:
        # Set the response to a series of pages.
        call.side_effect = (
            service.ListModelsResponse(
                model=[model.Model(), model.Model(), model.Model(),],
                next_page_token="abc",
            ),
            service.ListModelsResponse(model=[], next_page_token="def",),
            service.ListModelsResponse(model=[model.Model(),], next_page_token="ghi",),
            service.ListModelsResponse(model=[model.Model(), model.Model(),],),
            RuntimeError,
        )
        pages = list(client.list_models(request={}).pages)
        for page, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page.raw_page.next_page_token == token


@pytest.mark.asyncio
async def test_list_models_async_pager():
    client = AutoMlAsyncClient(credentials=credentials.AnonymousCredentials,)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.list_models),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            service.ListModelsResponse(
                model=[model.Model(), model.Model(), model.Model(),],
                next_page_token="abc",
            ),
            service.ListModelsResponse(model=[], next_page_token="def",),
            service.ListModelsResponse(model=[model.Model(),], next_page_token="ghi",),
            service.ListModelsResponse(model=[model.Model(), model.Model(),],),
            RuntimeError,
        )
        async_pager = await client.list_models(request={},)
        assert async_pager.next_page_token == "abc"
        responses = []
        async for response in async_pager:
            responses.append(response)

        assert len(responses) == 6
        assert all(isinstance(i, model.Model) for i in responses)


@pytest.mark.asyncio
async def test_list_models_async_pages():
    client = AutoMlAsyncClient(credentials=credentials.AnonymousCredentials,)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.list_models),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            service.ListModelsResponse(
                model=[model.Model(), model.Model(), model.Model(),],
                next_page_token="abc",
            ),
            service.ListModelsResponse(model=[], next_page_token="def",),
            service.ListModelsResponse(model=[model.Model(),], next_page_token="ghi",),
            service.ListModelsResponse(model=[model.Model(), model.Model(),],),
            RuntimeError,
        )
        pages = []
        async for page in (await client.list_models(request={})).pages:
            pages.append(page)
        for page, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page.raw_page.next_page_token == token


def test_delete_model(transport: str = "grpc", request_type=service.DeleteModelRequest):
    client = AutoMlClient(
        credentials=credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.delete_model), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/spam")

        response = client.delete_model(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.DeleteModelRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_delete_model_from_dict():
    test_delete_model(request_type=dict)


@pytest.mark.asyncio
async def test_delete_model_async(transport: str = "grpc_asyncio"):
    client = AutoMlAsyncClient(
        credentials=credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = service.DeleteModelRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.delete_model), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )

        response = await client.delete_model(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_delete_model_field_headers():
    client = AutoMlClient(credentials=credentials.AnonymousCredentials(),)

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.DeleteModelRequest()
    request.name = "name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.delete_model), "__call__") as call:
        call.return_value = operations_pb2.Operation(name="operations/op")

        client.delete_model(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=name/value",) in kw["metadata"]


@pytest.mark.asyncio
async def test_delete_model_field_headers_async():
    client = AutoMlAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.DeleteModelRequest()
    request.name = "name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.delete_model), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/op")
        )

        await client.delete_model(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=name/value",) in kw["metadata"]


def test_delete_model_flattened():
    client = AutoMlClient(credentials=credentials.AnonymousCredentials(),)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.delete_model), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.delete_model(name="name_value",)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0].name == "name_value"


def test_delete_model_flattened_error():
    client = AutoMlClient(credentials=credentials.AnonymousCredentials(),)

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.delete_model(
            service.DeleteModelRequest(), name="name_value",
        )


@pytest.mark.asyncio
async def test_delete_model_flattened_async():
    client = AutoMlAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.delete_model), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.delete_model(name="name_value",)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0].name == "name_value"


@pytest.mark.asyncio
async def test_delete_model_flattened_error_async():
    client = AutoMlAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.delete_model(
            service.DeleteModelRequest(), name="name_value",
        )


def test_update_model(transport: str = "grpc", request_type=service.UpdateModelRequest):
    client = AutoMlClient(
        credentials=credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.update_model), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = gca_model.Model(
            name="name_value",
            display_name="display_name_value",
            dataset_id="dataset_id_value",
            deployment_state=gca_model.Model.DeploymentState.DEPLOYED,
            etag="etag_value",
            translation_model_metadata=translation.TranslationModelMetadata(
                base_model="base_model_value"
            ),
        )

        response = client.update_model(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.UpdateModelRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, gca_model.Model)

    assert response.name == "name_value"

    assert response.display_name == "display_name_value"

    assert response.dataset_id == "dataset_id_value"

    assert response.deployment_state == gca_model.Model.DeploymentState.DEPLOYED

    assert response.etag == "etag_value"


def test_update_model_from_dict():
    test_update_model(request_type=dict)


@pytest.mark.asyncio
async def test_update_model_async(transport: str = "grpc_asyncio"):
    client = AutoMlAsyncClient(
        credentials=credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = service.UpdateModelRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.update_model), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            gca_model.Model(
                name="name_value",
                display_name="display_name_value",
                dataset_id="dataset_id_value",
                deployment_state=gca_model.Model.DeploymentState.DEPLOYED,
                etag="etag_value",
            )
        )

        response = await client.update_model(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, gca_model.Model)

    assert response.name == "name_value"

    assert response.display_name == "display_name_value"

    assert response.dataset_id == "dataset_id_value"

    assert response.deployment_state == gca_model.Model.DeploymentState.DEPLOYED

    assert response.etag == "etag_value"


def test_update_model_field_headers():
    client = AutoMlClient(credentials=credentials.AnonymousCredentials(),)

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.UpdateModelRequest()
    request.model.name = "model.name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.update_model), "__call__") as call:
        call.return_value = gca_model.Model()

        client.update_model(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "model.name=model.name/value",) in kw["metadata"]


@pytest.mark.asyncio
async def test_update_model_field_headers_async():
    client = AutoMlAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.UpdateModelRequest()
    request.model.name = "model.name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.update_model), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(gca_model.Model())

        await client.update_model(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "model.name=model.name/value",) in kw["metadata"]


def test_update_model_flattened():
    client = AutoMlClient(credentials=credentials.AnonymousCredentials(),)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.update_model), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = gca_model.Model()

        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.update_model(
            model=gca_model.Model(
                translation_model_metadata=translation.TranslationModelMetadata(
                    base_model="base_model_value"
                )
            ),
            update_mask=field_mask.FieldMask(paths=["paths_value"]),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0].model == gca_model.Model(
            translation_model_metadata=translation.TranslationModelMetadata(
                base_model="base_model_value"
            )
        )

        assert args[0].update_mask == field_mask.FieldMask(paths=["paths_value"])


def test_update_model_flattened_error():
    client = AutoMlClient(credentials=credentials.AnonymousCredentials(),)

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_model(
            service.UpdateModelRequest(),
            model=gca_model.Model(
                translation_model_metadata=translation.TranslationModelMetadata(
                    base_model="base_model_value"
                )
            ),
            update_mask=field_mask.FieldMask(paths=["paths_value"]),
        )


@pytest.mark.asyncio
async def test_update_model_flattened_async():
    client = AutoMlAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.update_model), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = gca_model.Model()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(gca_model.Model())
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.update_model(
            model=gca_model.Model(
                translation_model_metadata=translation.TranslationModelMetadata(
                    base_model="base_model_value"
                )
            ),
            update_mask=field_mask.FieldMask(paths=["paths_value"]),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0].model == gca_model.Model(
            translation_model_metadata=translation.TranslationModelMetadata(
                base_model="base_model_value"
            )
        )

        assert args[0].update_mask == field_mask.FieldMask(paths=["paths_value"])


@pytest.mark.asyncio
async def test_update_model_flattened_error_async():
    client = AutoMlAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.update_model(
            service.UpdateModelRequest(),
            model=gca_model.Model(
                translation_model_metadata=translation.TranslationModelMetadata(
                    base_model="base_model_value"
                )
            ),
            update_mask=field_mask.FieldMask(paths=["paths_value"]),
        )


def test_deploy_model(transport: str = "grpc", request_type=service.DeployModelRequest):
    client = AutoMlClient(
        credentials=credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.deploy_model), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/spam")

        response = client.deploy_model(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.DeployModelRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_deploy_model_from_dict():
    test_deploy_model(request_type=dict)


@pytest.mark.asyncio
async def test_deploy_model_async(transport: str = "grpc_asyncio"):
    client = AutoMlAsyncClient(
        credentials=credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = service.DeployModelRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.deploy_model), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )

        response = await client.deploy_model(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_deploy_model_field_headers():
    client = AutoMlClient(credentials=credentials.AnonymousCredentials(),)

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.DeployModelRequest()
    request.name = "name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.deploy_model), "__call__") as call:
        call.return_value = operations_pb2.Operation(name="operations/op")

        client.deploy_model(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=name/value",) in kw["metadata"]


@pytest.mark.asyncio
async def test_deploy_model_field_headers_async():
    client = AutoMlAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.DeployModelRequest()
    request.name = "name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.deploy_model), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/op")
        )

        await client.deploy_model(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=name/value",) in kw["metadata"]


def test_deploy_model_flattened():
    client = AutoMlClient(credentials=credentials.AnonymousCredentials(),)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.deploy_model), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.deploy_model(name="name_value",)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0].name == "name_value"


def test_deploy_model_flattened_error():
    client = AutoMlClient(credentials=credentials.AnonymousCredentials(),)

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.deploy_model(
            service.DeployModelRequest(), name="name_value",
        )


@pytest.mark.asyncio
async def test_deploy_model_flattened_async():
    client = AutoMlAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.deploy_model), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.deploy_model(name="name_value",)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0].name == "name_value"


@pytest.mark.asyncio
async def test_deploy_model_flattened_error_async():
    client = AutoMlAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.deploy_model(
            service.DeployModelRequest(), name="name_value",
        )


def test_undeploy_model(
    transport: str = "grpc", request_type=service.UndeployModelRequest
):
    client = AutoMlClient(
        credentials=credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.undeploy_model), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/spam")

        response = client.undeploy_model(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.UndeployModelRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_undeploy_model_from_dict():
    test_undeploy_model(request_type=dict)


@pytest.mark.asyncio
async def test_undeploy_model_async(transport: str = "grpc_asyncio"):
    client = AutoMlAsyncClient(
        credentials=credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = service.UndeployModelRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.undeploy_model), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )

        response = await client.undeploy_model(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_undeploy_model_field_headers():
    client = AutoMlClient(credentials=credentials.AnonymousCredentials(),)

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.UndeployModelRequest()
    request.name = "name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.undeploy_model), "__call__") as call:
        call.return_value = operations_pb2.Operation(name="operations/op")

        client.undeploy_model(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=name/value",) in kw["metadata"]


@pytest.mark.asyncio
async def test_undeploy_model_field_headers_async():
    client = AutoMlAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.UndeployModelRequest()
    request.name = "name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.undeploy_model), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/op")
        )

        await client.undeploy_model(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=name/value",) in kw["metadata"]


def test_undeploy_model_flattened():
    client = AutoMlClient(credentials=credentials.AnonymousCredentials(),)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.undeploy_model), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.undeploy_model(name="name_value",)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0].name == "name_value"


def test_undeploy_model_flattened_error():
    client = AutoMlClient(credentials=credentials.AnonymousCredentials(),)

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.undeploy_model(
            service.UndeployModelRequest(), name="name_value",
        )


@pytest.mark.asyncio
async def test_undeploy_model_flattened_async():
    client = AutoMlAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.undeploy_model), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.undeploy_model(name="name_value",)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0].name == "name_value"


@pytest.mark.asyncio
async def test_undeploy_model_flattened_error_async():
    client = AutoMlAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.undeploy_model(
            service.UndeployModelRequest(), name="name_value",
        )


def test_export_model(transport: str = "grpc", request_type=service.ExportModelRequest):
    client = AutoMlClient(
        credentials=credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.export_model), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/spam")

        response = client.export_model(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.ExportModelRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_export_model_from_dict():
    test_export_model(request_type=dict)


@pytest.mark.asyncio
async def test_export_model_async(transport: str = "grpc_asyncio"):
    client = AutoMlAsyncClient(
        credentials=credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = service.ExportModelRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.export_model), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )

        response = await client.export_model(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_export_model_field_headers():
    client = AutoMlClient(credentials=credentials.AnonymousCredentials(),)

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.ExportModelRequest()
    request.name = "name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.export_model), "__call__") as call:
        call.return_value = operations_pb2.Operation(name="operations/op")

        client.export_model(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=name/value",) in kw["metadata"]


@pytest.mark.asyncio
async def test_export_model_field_headers_async():
    client = AutoMlAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.ExportModelRequest()
    request.name = "name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.export_model), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/op")
        )

        await client.export_model(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=name/value",) in kw["metadata"]


def test_export_model_flattened():
    client = AutoMlClient(credentials=credentials.AnonymousCredentials(),)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.export_model), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.export_model(
            name="name_value",
            output_config=io.ModelExportOutputConfig(
                gcs_destination=io.GcsDestination(
                    output_uri_prefix="output_uri_prefix_value"
                )
            ),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0].name == "name_value"

        assert args[0].output_config == io.ModelExportOutputConfig(
            gcs_destination=io.GcsDestination(
                output_uri_prefix="output_uri_prefix_value"
            )
        )


def test_export_model_flattened_error():
    client = AutoMlClient(credentials=credentials.AnonymousCredentials(),)

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.export_model(
            service.ExportModelRequest(),
            name="name_value",
            output_config=io.ModelExportOutputConfig(
                gcs_destination=io.GcsDestination(
                    output_uri_prefix="output_uri_prefix_value"
                )
            ),
        )


@pytest.mark.asyncio
async def test_export_model_flattened_async():
    client = AutoMlAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.export_model), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.export_model(
            name="name_value",
            output_config=io.ModelExportOutputConfig(
                gcs_destination=io.GcsDestination(
                    output_uri_prefix="output_uri_prefix_value"
                )
            ),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0].name == "name_value"

        assert args[0].output_config == io.ModelExportOutputConfig(
            gcs_destination=io.GcsDestination(
                output_uri_prefix="output_uri_prefix_value"
            )
        )


@pytest.mark.asyncio
async def test_export_model_flattened_error_async():
    client = AutoMlAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.export_model(
            service.ExportModelRequest(),
            name="name_value",
            output_config=io.ModelExportOutputConfig(
                gcs_destination=io.GcsDestination(
                    output_uri_prefix="output_uri_prefix_value"
                )
            ),
        )


def test_get_model_evaluation(
    transport: str = "grpc", request_type=service.GetModelEvaluationRequest
):
    client = AutoMlClient(
        credentials=credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._transport.get_model_evaluation), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = model_evaluation.ModelEvaluation(
            name="name_value",
            annotation_spec_id="annotation_spec_id_value",
            display_name="display_name_value",
            evaluated_example_count=2446,
            classification_evaluation_metrics=classification.ClassificationEvaluationMetrics(
                au_prc=0.634
            ),
        )

        response = client.get_model_evaluation(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.GetModelEvaluationRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, model_evaluation.ModelEvaluation)

    assert response.name == "name_value"

    assert response.annotation_spec_id == "annotation_spec_id_value"

    assert response.display_name == "display_name_value"

    assert response.evaluated_example_count == 2446


def test_get_model_evaluation_from_dict():
    test_get_model_evaluation(request_type=dict)


@pytest.mark.asyncio
async def test_get_model_evaluation_async(transport: str = "grpc_asyncio"):
    client = AutoMlAsyncClient(
        credentials=credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = service.GetModelEvaluationRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.get_model_evaluation), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            model_evaluation.ModelEvaluation(
                name="name_value",
                annotation_spec_id="annotation_spec_id_value",
                display_name="display_name_value",
                evaluated_example_count=2446,
            )
        )

        response = await client.get_model_evaluation(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, model_evaluation.ModelEvaluation)

    assert response.name == "name_value"

    assert response.annotation_spec_id == "annotation_spec_id_value"

    assert response.display_name == "display_name_value"

    assert response.evaluated_example_count == 2446


def test_get_model_evaluation_field_headers():
    client = AutoMlClient(credentials=credentials.AnonymousCredentials(),)

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.GetModelEvaluationRequest()
    request.name = "name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._transport.get_model_evaluation), "__call__"
    ) as call:
        call.return_value = model_evaluation.ModelEvaluation()

        client.get_model_evaluation(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=name/value",) in kw["metadata"]


@pytest.mark.asyncio
async def test_get_model_evaluation_field_headers_async():
    client = AutoMlAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.GetModelEvaluationRequest()
    request.name = "name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.get_model_evaluation), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            model_evaluation.ModelEvaluation()
        )

        await client.get_model_evaluation(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=name/value",) in kw["metadata"]


def test_get_model_evaluation_flattened():
    client = AutoMlClient(credentials=credentials.AnonymousCredentials(),)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._transport.get_model_evaluation), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = model_evaluation.ModelEvaluation()

        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.get_model_evaluation(name="name_value",)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0].name == "name_value"


def test_get_model_evaluation_flattened_error():
    client = AutoMlClient(credentials=credentials.AnonymousCredentials(),)

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_model_evaluation(
            service.GetModelEvaluationRequest(), name="name_value",
        )


@pytest.mark.asyncio
async def test_get_model_evaluation_flattened_async():
    client = AutoMlAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.get_model_evaluation), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = model_evaluation.ModelEvaluation()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            model_evaluation.ModelEvaluation()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.get_model_evaluation(name="name_value",)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0].name == "name_value"


@pytest.mark.asyncio
async def test_get_model_evaluation_flattened_error_async():
    client = AutoMlAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.get_model_evaluation(
            service.GetModelEvaluationRequest(), name="name_value",
        )


def test_list_model_evaluations(
    transport: str = "grpc", request_type=service.ListModelEvaluationsRequest
):
    client = AutoMlClient(
        credentials=credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._transport.list_model_evaluations), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.ListModelEvaluationsResponse(
            next_page_token="next_page_token_value",
        )

        response = client.list_model_evaluations(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == service.ListModelEvaluationsRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListModelEvaluationsPager)

    assert response.next_page_token == "next_page_token_value"


def test_list_model_evaluations_from_dict():
    test_list_model_evaluations(request_type=dict)


@pytest.mark.asyncio
async def test_list_model_evaluations_async(transport: str = "grpc_asyncio"):
    client = AutoMlAsyncClient(
        credentials=credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = service.ListModelEvaluationsRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.list_model_evaluations), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            service.ListModelEvaluationsResponse(
                next_page_token="next_page_token_value",
            )
        )

        response = await client.list_model_evaluations(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListModelEvaluationsAsyncPager)

    assert response.next_page_token == "next_page_token_value"


def test_list_model_evaluations_field_headers():
    client = AutoMlClient(credentials=credentials.AnonymousCredentials(),)

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.ListModelEvaluationsRequest()
    request.parent = "parent/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._transport.list_model_evaluations), "__call__"
    ) as call:
        call.return_value = service.ListModelEvaluationsResponse()

        client.list_model_evaluations(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "parent=parent/value",) in kw["metadata"]


@pytest.mark.asyncio
async def test_list_model_evaluations_field_headers_async():
    client = AutoMlAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service.ListModelEvaluationsRequest()
    request.parent = "parent/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.list_model_evaluations), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            service.ListModelEvaluationsResponse()
        )

        await client.list_model_evaluations(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "parent=parent/value",) in kw["metadata"]


def test_list_model_evaluations_flattened():
    client = AutoMlClient(credentials=credentials.AnonymousCredentials(),)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._transport.list_model_evaluations), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.ListModelEvaluationsResponse()

        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.list_model_evaluations(
            parent="parent_value", filter="filter_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0].parent == "parent_value"

        assert args[0].filter == "filter_value"


def test_list_model_evaluations_flattened_error():
    client = AutoMlClient(credentials=credentials.AnonymousCredentials(),)

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_model_evaluations(
            service.ListModelEvaluationsRequest(),
            parent="parent_value",
            filter="filter_value",
        )


@pytest.mark.asyncio
async def test_list_model_evaluations_flattened_async():
    client = AutoMlAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.list_model_evaluations), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.ListModelEvaluationsResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            service.ListModelEvaluationsResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.list_model_evaluations(
            parent="parent_value", filter="filter_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0].parent == "parent_value"

        assert args[0].filter == "filter_value"


@pytest.mark.asyncio
async def test_list_model_evaluations_flattened_error_async():
    client = AutoMlAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.list_model_evaluations(
            service.ListModelEvaluationsRequest(),
            parent="parent_value",
            filter="filter_value",
        )


def test_list_model_evaluations_pager():
    client = AutoMlClient(credentials=credentials.AnonymousCredentials,)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._transport.list_model_evaluations), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            service.ListModelEvaluationsResponse(
                model_evaluation=[
                    model_evaluation.ModelEvaluation(),
                    model_evaluation.ModelEvaluation(),
                    model_evaluation.ModelEvaluation(),
                ],
                next_page_token="abc",
            ),
            service.ListModelEvaluationsResponse(
                model_evaluation=[], next_page_token="def",
            ),
            service.ListModelEvaluationsResponse(
                model_evaluation=[model_evaluation.ModelEvaluation(),],
                next_page_token="ghi",
            ),
            service.ListModelEvaluationsResponse(
                model_evaluation=[
                    model_evaluation.ModelEvaluation(),
                    model_evaluation.ModelEvaluation(),
                ],
            ),
            RuntimeError,
        )

        metadata = ()
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", ""),)),
        )
        pager = client.list_model_evaluations(request={})

        assert pager._metadata == metadata

        results = [i for i in pager]
        assert len(results) == 6
        assert all(isinstance(i, model_evaluation.ModelEvaluation) for i in results)


def test_list_model_evaluations_pages():
    client = AutoMlClient(credentials=credentials.AnonymousCredentials,)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._transport.list_model_evaluations), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            service.ListModelEvaluationsResponse(
                model_evaluation=[
                    model_evaluation.ModelEvaluation(),
                    model_evaluation.ModelEvaluation(),
                    model_evaluation.ModelEvaluation(),
                ],
                next_page_token="abc",
            ),
            service.ListModelEvaluationsResponse(
                model_evaluation=[], next_page_token="def",
            ),
            service.ListModelEvaluationsResponse(
                model_evaluation=[model_evaluation.ModelEvaluation(),],
                next_page_token="ghi",
            ),
            service.ListModelEvaluationsResponse(
                model_evaluation=[
                    model_evaluation.ModelEvaluation(),
                    model_evaluation.ModelEvaluation(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.list_model_evaluations(request={}).pages)
        for page, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page.raw_page.next_page_token == token


@pytest.mark.asyncio
async def test_list_model_evaluations_async_pager():
    client = AutoMlAsyncClient(credentials=credentials.AnonymousCredentials,)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.list_model_evaluations),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            service.ListModelEvaluationsResponse(
                model_evaluation=[
                    model_evaluation.ModelEvaluation(),
                    model_evaluation.ModelEvaluation(),
                    model_evaluation.ModelEvaluation(),
                ],
                next_page_token="abc",
            ),
            service.ListModelEvaluationsResponse(
                model_evaluation=[], next_page_token="def",
            ),
            service.ListModelEvaluationsResponse(
                model_evaluation=[model_evaluation.ModelEvaluation(),],
                next_page_token="ghi",
            ),
            service.ListModelEvaluationsResponse(
                model_evaluation=[
                    model_evaluation.ModelEvaluation(),
                    model_evaluation.ModelEvaluation(),
                ],
            ),
            RuntimeError,
        )
        async_pager = await client.list_model_evaluations(request={},)
        assert async_pager.next_page_token == "abc"
        responses = []
        async for response in async_pager:
            responses.append(response)

        assert len(responses) == 6
        assert all(isinstance(i, model_evaluation.ModelEvaluation) for i in responses)


@pytest.mark.asyncio
async def test_list_model_evaluations_async_pages():
    client = AutoMlAsyncClient(credentials=credentials.AnonymousCredentials,)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.list_model_evaluations),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            service.ListModelEvaluationsResponse(
                model_evaluation=[
                    model_evaluation.ModelEvaluation(),
                    model_evaluation.ModelEvaluation(),
                    model_evaluation.ModelEvaluation(),
                ],
                next_page_token="abc",
            ),
            service.ListModelEvaluationsResponse(
                model_evaluation=[], next_page_token="def",
            ),
            service.ListModelEvaluationsResponse(
                model_evaluation=[model_evaluation.ModelEvaluation(),],
                next_page_token="ghi",
            ),
            service.ListModelEvaluationsResponse(
                model_evaluation=[
                    model_evaluation.ModelEvaluation(),
                    model_evaluation.ModelEvaluation(),
                ],
            ),
            RuntimeError,
        )
        pages = []
        async for page in (await client.list_model_evaluations(request={})).pages:
            pages.append(page)
        for page, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page.raw_page.next_page_token == token


def test_credentials_transport_error():
    # It is an error to provide credentials and a transport instance.
    transport = transports.AutoMlGrpcTransport(
        credentials=credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = AutoMlClient(
            credentials=credentials.AnonymousCredentials(), transport=transport,
        )

    # It is an error to provide a credentials file and a transport instance.
    transport = transports.AutoMlGrpcTransport(
        credentials=credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = AutoMlClient(
            client_options={"credentials_file": "credentials.json"},
            transport=transport,
        )

    # It is an error to provide scopes and a transport instance.
    transport = transports.AutoMlGrpcTransport(
        credentials=credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = AutoMlClient(
            client_options={"scopes": ["1", "2"]}, transport=transport,
        )


def test_transport_instance():
    # A client may be instantiated with a custom transport instance.
    transport = transports.AutoMlGrpcTransport(
        credentials=credentials.AnonymousCredentials(),
    )
    client = AutoMlClient(transport=transport)
    assert client._transport is transport


def test_transport_get_channel():
    # A client may be instantiated with a custom transport instance.
    transport = transports.AutoMlGrpcTransport(
        credentials=credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel

    transport = transports.AutoMlGrpcAsyncIOTransport(
        credentials=credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel


def test_transport_grpc_default():
    # A client should use the gRPC transport by default.
    client = AutoMlClient(credentials=credentials.AnonymousCredentials(),)
    assert isinstance(client._transport, transports.AutoMlGrpcTransport,)


def test_auto_ml_base_transport_error():
    # Passing both a credentials object and credentials_file should raise an error
    with pytest.raises(exceptions.DuplicateCredentialArgs):
        transport = transports.AutoMlTransport(
            credentials=credentials.AnonymousCredentials(),
            credentials_file="credentials.json",
        )


def test_auto_ml_base_transport():
    # Instantiate the base transport.
    with mock.patch(
        "google.cloud.automl_v1.services.auto_ml.transports.AutoMlTransport.__init__"
    ) as Transport:
        Transport.return_value = None
        transport = transports.AutoMlTransport(
            credentials=credentials.AnonymousCredentials(),
        )

    # Every method on the transport should just blindly
    # raise NotImplementedError.
    methods = (
        "create_dataset",
        "get_dataset",
        "list_datasets",
        "update_dataset",
        "delete_dataset",
        "import_data",
        "export_data",
        "get_annotation_spec",
        "create_model",
        "get_model",
        "list_models",
        "delete_model",
        "update_model",
        "deploy_model",
        "undeploy_model",
        "export_model",
        "get_model_evaluation",
        "list_model_evaluations",
    )
    for method in methods:
        with pytest.raises(NotImplementedError):
            getattr(transport, method)(request=object())

    # Additionally, the LRO client (a property) should
    # also raise NotImplementedError
    with pytest.raises(NotImplementedError):
        transport.operations_client


def test_auto_ml_base_transport_with_credentials_file():
    # Instantiate the base transport with a credentials file
    with mock.patch.object(
        auth, "load_credentials_from_file"
    ) as load_creds, mock.patch(
        "google.cloud.automl_v1.services.auto_ml.transports.AutoMlTransport._prep_wrapped_messages"
    ) as Transport:
        Transport.return_value = None
        load_creds.return_value = (credentials.AnonymousCredentials(), None)
        transport = transports.AutoMlTransport(
            credentials_file="credentials.json", quota_project_id="octopus",
        )
        load_creds.assert_called_once_with(
            "credentials.json",
            scopes=("https://www.googleapis.com/auth/cloud-platform",),
            quota_project_id="octopus",
        )


def test_auto_ml_auth_adc():
    # If no credentials are provided, we should use ADC credentials.
    with mock.patch.object(auth, "default") as adc:
        adc.return_value = (credentials.AnonymousCredentials(), None)
        AutoMlClient()
        adc.assert_called_once_with(
            scopes=("https://www.googleapis.com/auth/cloud-platform",),
            quota_project_id=None,
        )


def test_auto_ml_transport_auth_adc():
    # If credentials and host are not provided, the transport class should use
    # ADC credentials.
    with mock.patch.object(auth, "default") as adc:
        adc.return_value = (credentials.AnonymousCredentials(), None)
        transports.AutoMlGrpcTransport(
            host="squid.clam.whelk", quota_project_id="octopus"
        )
        adc.assert_called_once_with(
            scopes=("https://www.googleapis.com/auth/cloud-platform",),
            quota_project_id="octopus",
        )


def test_auto_ml_host_no_port():
    client = AutoMlClient(
        credentials=credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(
            api_endpoint="automl.googleapis.com"
        ),
    )
    assert client._transport._host == "automl.googleapis.com:443"


def test_auto_ml_host_with_port():
    client = AutoMlClient(
        credentials=credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(
            api_endpoint="automl.googleapis.com:8000"
        ),
    )
    assert client._transport._host == "automl.googleapis.com:8000"


def test_auto_ml_grpc_transport_channel():
    channel = grpc.insecure_channel("http://localhost/")

    # Check that if channel is provided, mtls endpoint and client_cert_source
    # won't be used.
    callback = mock.MagicMock()
    transport = transports.AutoMlGrpcTransport(
        host="squid.clam.whelk",
        channel=channel,
        api_mtls_endpoint="mtls.squid.clam.whelk",
        client_cert_source=callback,
    )
    assert transport.grpc_channel == channel
    assert transport._host == "squid.clam.whelk:443"
    assert not callback.called


def test_auto_ml_grpc_asyncio_transport_channel():
    channel = aio.insecure_channel("http://localhost/")

    # Check that if channel is provided, mtls endpoint and client_cert_source
    # won't be used.
    callback = mock.MagicMock()
    transport = transports.AutoMlGrpcAsyncIOTransport(
        host="squid.clam.whelk",
        channel=channel,
        api_mtls_endpoint="mtls.squid.clam.whelk",
        client_cert_source=callback,
    )
    assert transport.grpc_channel == channel
    assert transport._host == "squid.clam.whelk:443"
    assert not callback.called


@mock.patch("grpc.ssl_channel_credentials", autospec=True)
@mock.patch("google.api_core.grpc_helpers.create_channel", autospec=True)
def test_auto_ml_grpc_transport_channel_mtls_with_client_cert_source(
    grpc_create_channel, grpc_ssl_channel_cred
):
    # Check that if channel is None, but api_mtls_endpoint and client_cert_source
    # are provided, then a mTLS channel will be created.
    mock_cred = mock.Mock()

    mock_ssl_cred = mock.Mock()
    grpc_ssl_channel_cred.return_value = mock_ssl_cred

    mock_grpc_channel = mock.Mock()
    grpc_create_channel.return_value = mock_grpc_channel

    transport = transports.AutoMlGrpcTransport(
        host="squid.clam.whelk",
        credentials=mock_cred,
        api_mtls_endpoint="mtls.squid.clam.whelk",
        client_cert_source=client_cert_source_callback,
    )
    grpc_ssl_channel_cred.assert_called_once_with(
        certificate_chain=b"cert bytes", private_key=b"key bytes"
    )
    grpc_create_channel.assert_called_once_with(
        "mtls.squid.clam.whelk:443",
        credentials=mock_cred,
        credentials_file=None,
        scopes=("https://www.googleapis.com/auth/cloud-platform",),
        ssl_credentials=mock_ssl_cred,
        quota_project_id=None,
    )
    assert transport.grpc_channel == mock_grpc_channel


@mock.patch("grpc.ssl_channel_credentials", autospec=True)
@mock.patch("google.api_core.grpc_helpers_async.create_channel", autospec=True)
def test_auto_ml_grpc_asyncio_transport_channel_mtls_with_client_cert_source(
    grpc_create_channel, grpc_ssl_channel_cred
):
    # Check that if channel is None, but api_mtls_endpoint and client_cert_source
    # are provided, then a mTLS channel will be created.
    mock_cred = mock.Mock()

    mock_ssl_cred = mock.Mock()
    grpc_ssl_channel_cred.return_value = mock_ssl_cred

    mock_grpc_channel = mock.Mock()
    grpc_create_channel.return_value = mock_grpc_channel

    transport = transports.AutoMlGrpcAsyncIOTransport(
        host="squid.clam.whelk",
        credentials=mock_cred,
        api_mtls_endpoint="mtls.squid.clam.whelk",
        client_cert_source=client_cert_source_callback,
    )
    grpc_ssl_channel_cred.assert_called_once_with(
        certificate_chain=b"cert bytes", private_key=b"key bytes"
    )
    grpc_create_channel.assert_called_once_with(
        "mtls.squid.clam.whelk:443",
        credentials=mock_cred,
        credentials_file=None,
        scopes=("https://www.googleapis.com/auth/cloud-platform",),
        ssl_credentials=mock_ssl_cred,
        quota_project_id=None,
    )
    assert transport.grpc_channel == mock_grpc_channel


@pytest.mark.parametrize(
    "api_mtls_endpoint", ["mtls.squid.clam.whelk", "mtls.squid.clam.whelk:443"]
)
@mock.patch("google.api_core.grpc_helpers.create_channel", autospec=True)
def test_auto_ml_grpc_transport_channel_mtls_with_adc(
    grpc_create_channel, api_mtls_endpoint
):
    # Check that if channel and client_cert_source are None, but api_mtls_endpoint
    # is provided, then a mTLS channel will be created with SSL ADC.
    mock_grpc_channel = mock.Mock()
    grpc_create_channel.return_value = mock_grpc_channel

    # Mock google.auth.transport.grpc.SslCredentials class.
    mock_ssl_cred = mock.Mock()
    with mock.patch.multiple(
        "google.auth.transport.grpc.SslCredentials",
        __init__=mock.Mock(return_value=None),
        ssl_credentials=mock.PropertyMock(return_value=mock_ssl_cred),
    ):
        mock_cred = mock.Mock()
        transport = transports.AutoMlGrpcTransport(
            host="squid.clam.whelk",
            credentials=mock_cred,
            api_mtls_endpoint=api_mtls_endpoint,
            client_cert_source=None,
        )
        grpc_create_channel.assert_called_once_with(
            "mtls.squid.clam.whelk:443",
            credentials=mock_cred,
            credentials_file=None,
            scopes=("https://www.googleapis.com/auth/cloud-platform",),
            ssl_credentials=mock_ssl_cred,
            quota_project_id=None,
        )
        assert transport.grpc_channel == mock_grpc_channel


@pytest.mark.parametrize(
    "api_mtls_endpoint", ["mtls.squid.clam.whelk", "mtls.squid.clam.whelk:443"]
)
@mock.patch("google.api_core.grpc_helpers_async.create_channel", autospec=True)
def test_auto_ml_grpc_asyncio_transport_channel_mtls_with_adc(
    grpc_create_channel, api_mtls_endpoint
):
    # Check that if channel and client_cert_source are None, but api_mtls_endpoint
    # is provided, then a mTLS channel will be created with SSL ADC.
    mock_grpc_channel = mock.Mock()
    grpc_create_channel.return_value = mock_grpc_channel

    # Mock google.auth.transport.grpc.SslCredentials class.
    mock_ssl_cred = mock.Mock()
    with mock.patch.multiple(
        "google.auth.transport.grpc.SslCredentials",
        __init__=mock.Mock(return_value=None),
        ssl_credentials=mock.PropertyMock(return_value=mock_ssl_cred),
    ):
        mock_cred = mock.Mock()
        transport = transports.AutoMlGrpcAsyncIOTransport(
            host="squid.clam.whelk",
            credentials=mock_cred,
            api_mtls_endpoint=api_mtls_endpoint,
            client_cert_source=None,
        )
        grpc_create_channel.assert_called_once_with(
            "mtls.squid.clam.whelk:443",
            credentials=mock_cred,
            credentials_file=None,
            scopes=("https://www.googleapis.com/auth/cloud-platform",),
            ssl_credentials=mock_ssl_cred,
            quota_project_id=None,
        )
        assert transport.grpc_channel == mock_grpc_channel


def test_auto_ml_grpc_lro_client():
    client = AutoMlClient(
        credentials=credentials.AnonymousCredentials(), transport="grpc",
    )
    transport = client._transport

    # Ensure that we have a api-core operations client.
    assert isinstance(transport.operations_client, operations_v1.OperationsClient,)

    # Ensure that subsequent calls to the property send the exact same object.
    assert transport.operations_client is transport.operations_client


def test_auto_ml_grpc_lro_async_client():
    client = AutoMlAsyncClient(
        credentials=credentials.AnonymousCredentials(), transport="grpc_asyncio",
    )
    transport = client._client._transport

    # Ensure that we have a api-core operations client.
    assert isinstance(transport.operations_client, operations_v1.OperationsAsyncClient,)

    # Ensure that subsequent calls to the property send the exact same object.
    assert transport.operations_client is transport.operations_client


def test_model_path():
    project = "squid"
    location = "clam"
    model = "whelk"

    expected = "projects/{project}/locations/{location}/models/{model}".format(
        project=project, location=location, model=model,
    )
    actual = AutoMlClient.model_path(project, location, model)
    assert expected == actual


def test_parse_model_path():
    expected = {
        "project": "octopus",
        "location": "oyster",
        "model": "nudibranch",
    }
    path = AutoMlClient.model_path(**expected)

    # Check that the path construction is reversible.
    actual = AutoMlClient.parse_model_path(path)
    assert expected == actual


def test_dataset_path():
    project = "squid"
    location = "clam"
    dataset = "whelk"

    expected = "projects/{project}/locations/{location}/datasets/{dataset}".format(
        project=project, location=location, dataset=dataset,
    )
    actual = AutoMlClient.dataset_path(project, location, dataset)
    assert expected == actual


def test_parse_dataset_path():
    expected = {
        "project": "octopus",
        "location": "oyster",
        "dataset": "nudibranch",
    }
    path = AutoMlClient.dataset_path(**expected)

    # Check that the path construction is reversible.
    actual = AutoMlClient.parse_dataset_path(path)
    assert expected == actual


def test_client_withDEFAULT_CLIENT_INFO():
    client_info = gapic_v1.client_info.ClientInfo()

    with mock.patch.object(
        transports.AutoMlTransport, "_prep_wrapped_messages"
    ) as prep:
        client = AutoMlClient(
            credentials=credentials.AnonymousCredentials(), client_info=client_info,
        )
        prep.assert_called_once_with(client_info)

    with mock.patch.object(
        transports.AutoMlTransport, "_prep_wrapped_messages"
    ) as prep:
        transport_class = AutoMlClient.get_transport_class()
        transport = transport_class(
            credentials=credentials.AnonymousCredentials(), client_info=client_info,
        )
        prep.assert_called_once_with(client_info)
