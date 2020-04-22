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

"""Accesses the google.cloud.automl.v1beta1 AutoMl API."""

import functools
import pkg_resources
import warnings

from google.oauth2 import service_account
import google.api_core.client_options
import google.api_core.gapic_v1.client_info
import google.api_core.gapic_v1.config
import google.api_core.gapic_v1.method
import google.api_core.gapic_v1.routing_header
import google.api_core.grpc_helpers
import google.api_core.operation
import google.api_core.operations_v1
import google.api_core.page_iterator
import google.api_core.path_template
import google.api_core.protobuf_helpers
import grpc

from google.cloud.automl_v1beta1.gapic import auto_ml_client_config
from google.cloud.automl_v1beta1.gapic import enums
from google.cloud.automl_v1beta1.gapic.transports import auto_ml_grpc_transport
from google.cloud.automl_v1beta1.proto import annotation_spec_pb2
from google.cloud.automl_v1beta1.proto import column_spec_pb2
from google.cloud.automl_v1beta1.proto import data_items_pb2
from google.cloud.automl_v1beta1.proto import dataset_pb2
from google.cloud.automl_v1beta1.proto import image_pb2
from google.cloud.automl_v1beta1.proto import io_pb2
from google.cloud.automl_v1beta1.proto import model_evaluation_pb2
from google.cloud.automl_v1beta1.proto import model_pb2
from google.cloud.automl_v1beta1.proto import operations_pb2 as proto_operations_pb2
from google.cloud.automl_v1beta1.proto import prediction_service_pb2
from google.cloud.automl_v1beta1.proto import prediction_service_pb2_grpc
from google.cloud.automl_v1beta1.proto import service_pb2
from google.cloud.automl_v1beta1.proto import service_pb2_grpc
from google.cloud.automl_v1beta1.proto import table_spec_pb2
from google.longrunning import operations_pb2 as longrunning_operations_pb2
from google.protobuf import empty_pb2
from google.protobuf import field_mask_pb2


_GAPIC_LIBRARY_VERSION = pkg_resources.get_distribution("google-cloud-automl").version


class AutoMlClient(object):
    """
    If this SourceCodeInfo represents a complete declaration, these are
    any comments appearing before and after the declaration which appear to
    be attached to the declaration.

    A series of line comments appearing on consecutive lines, with no other
    tokens appearing on those lines, will be treated as a single comment.

    leading_detached_comments will keep paragraphs of comments that appear
    before (but not connected to) the current element. Each paragraph,
    separated by empty lines, will be one comment element in the repeated
    field.

    Only the comment content is provided; comment markers (e.g. //) are
    stripped out. For block comments, leading whitespace and an asterisk
    will be stripped from the beginning of each line other than the first.
    Newlines are included in the output.

    Examples:

    optional int32 foo = 1; // Comment attached to foo. // Comment attached
    to bar. optional int32 bar = 2;

    optional string baz = 3; // Comment attached to baz. // Another line
    attached to baz.

    // Comment attached to qux. // // Another line attached to qux. optional
    double qux = 4;

    // Detached comment for corge. This is not leading or trailing comments
    // to qux or corge because there are blank lines separating it from //
    both.

    // Detached comment for corge paragraph 2.

    optional string corge = 5; /\* Block comment attached \* to corge.
    Leading asterisks \* will be removed. */ /* Block comment attached to \*
    grault. \*/ optional int32 grault = 6;

    // ignored detached comments.
    """

    SERVICE_ADDRESS = "automl.googleapis.com:443"
    """The default address of the service."""

    # The name of the interface for this client. This is the key used to
    # find the method configuration in the client_config dictionary.
    _INTERFACE_NAME = "google.cloud.automl.v1beta1.AutoMl"

    @classmethod
    def from_service_account_file(cls, filename, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
        file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            AutoMlClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @classmethod
    def annotation_spec_path(cls, project, location, dataset, annotation_spec):
        """Return a fully-qualified annotation_spec string."""
        return google.api_core.path_template.expand(
            "projects/{project}/locations/{location}/datasets/{dataset}/annotationSpecs/{annotation_spec}",
            project=project,
            location=location,
            dataset=dataset,
            annotation_spec=annotation_spec,
        )

    @classmethod
    def column_spec_path(cls, project, location, dataset, table_spec, column_spec):
        """Return a fully-qualified column_spec string."""
        return google.api_core.path_template.expand(
            "projects/{project}/locations/{location}/datasets/{dataset}/tableSpecs/{table_spec}/columnSpecs/{column_spec}",
            project=project,
            location=location,
            dataset=dataset,
            table_spec=table_spec,
            column_spec=column_spec,
        )

    @classmethod
    def dataset_path(cls, project, location, dataset):
        """Return a fully-qualified dataset string."""
        return google.api_core.path_template.expand(
            "projects/{project}/locations/{location}/datasets/{dataset}",
            project=project,
            location=location,
            dataset=dataset,
        )

    @classmethod
    def location_path(cls, project, location):
        """Return a fully-qualified location string."""
        return google.api_core.path_template.expand(
            "projects/{project}/locations/{location}",
            project=project,
            location=location,
        )

    @classmethod
    def model_path(cls, project, location, model):
        """Return a fully-qualified model string."""
        return google.api_core.path_template.expand(
            "projects/{project}/locations/{location}/models/{model}",
            project=project,
            location=location,
            model=model,
        )

    @classmethod
    def model_evaluation_path(cls, project, location, model, model_evaluation):
        """Return a fully-qualified model_evaluation string."""
        return google.api_core.path_template.expand(
            "projects/{project}/locations/{location}/models/{model}/modelEvaluations/{model_evaluation}",
            project=project,
            location=location,
            model=model,
            model_evaluation=model_evaluation,
        )

    @classmethod
    def table_spec_path(cls, project, location, dataset, table_spec):
        """Return a fully-qualified table_spec string."""
        return google.api_core.path_template.expand(
            "projects/{project}/locations/{location}/datasets/{dataset}/tableSpecs/{table_spec}",
            project=project,
            location=location,
            dataset=dataset,
            table_spec=table_spec,
        )

    def __init__(
        self,
        transport=None,
        channel=None,
        credentials=None,
        client_config=None,
        client_info=None,
        client_options=None,
    ):
        """Constructor.

        Args:
            transport (Union[~.AutoMlGrpcTransport,
                    Callable[[~.Credentials, type], ~.AutoMlGrpcTransport]): A transport
                instance, responsible for actually making the API calls.
                The default transport uses the gRPC protocol.
                This argument may also be a callable which returns a
                transport instance. Callables will be sent the credentials
                as the first argument and the default transport class as
                the second argument.
            channel (grpc.Channel): DEPRECATED. A ``Channel`` instance
                through which to make calls. This argument is mutually exclusive
                with ``credentials``; providing both will raise an exception.
            credentials (google.auth.credentials.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is mutually exclusive with providing a
                transport instance to ``transport``; doing so will raise
                an exception.
            client_config (dict): DEPRECATED. A dictionary of call options for
                each method. If not specified, the default configuration is used.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            client_options (Union[dict, google.api_core.client_options.ClientOptions]):
                Client options used to set user options on the client. API Endpoint
                should be set through client_options.
        """
        # Raise deprecation warnings for things we want to go away.
        if client_config is not None:
            warnings.warn(
                "The `client_config` argument is deprecated.",
                PendingDeprecationWarning,
                stacklevel=2,
            )
        else:
            client_config = auto_ml_client_config.config

        if channel:
            warnings.warn(
                "The `channel` argument is deprecated; use " "`transport` instead.",
                PendingDeprecationWarning,
                stacklevel=2,
            )

        api_endpoint = self.SERVICE_ADDRESS
        if client_options:
            if type(client_options) == dict:
                client_options = google.api_core.client_options.from_dict(
                    client_options
                )
            if client_options.api_endpoint:
                api_endpoint = client_options.api_endpoint

        # Instantiate the transport.
        # The transport is responsible for handling serialization and
        # deserialization and actually sending data to the service.
        if transport:
            if callable(transport):
                self.transport = transport(
                    credentials=credentials,
                    default_class=auto_ml_grpc_transport.AutoMlGrpcTransport,
                    address=api_endpoint,
                )
            else:
                if credentials:
                    raise ValueError(
                        "Received both a transport instance and "
                        "credentials; these are mutually exclusive."
                    )
                self.transport = transport
        else:
            self.transport = auto_ml_grpc_transport.AutoMlGrpcTransport(
                address=api_endpoint, channel=channel, credentials=credentials
            )

        if client_info is None:
            client_info = google.api_core.gapic_v1.client_info.ClientInfo(
                gapic_version=_GAPIC_LIBRARY_VERSION
            )
        else:
            client_info.gapic_version = _GAPIC_LIBRARY_VERSION
        self._client_info = client_info

        # Parse out the default settings for retry and timeout for each RPC
        # from the client configuration.
        # (Ordinarily, these are the defaults specified in the `*_config.py`
        # file next to this one.)
        self._method_configs = google.api_core.gapic_v1.config.parse_method_configs(
            client_config["interfaces"][self._INTERFACE_NAME]
        )

        # Save a dictionary of cached API call functions.
        # These are the actual callables which invoke the proper
        # transport methods, wrapped with `wrap_method` to add retry,
        # timeout, and the like.
        self._inner_api_calls = {}

    # Service calls
    def delete_dataset(
        self,
        name,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Output only. Auxiliary information for each of the
        input_feature_column_specs with respect to this particular model.

        Example:
            >>> from google.cloud import automl_v1beta1
            >>>
            >>> client = automl_v1beta1.AutoMlClient()
            >>>
            >>> name = client.dataset_path('[PROJECT]', '[LOCATION]', '[DATASET]')
            >>>
            >>> response = client.delete_dataset(name)
            >>>
            >>> def callback(operation_future):
            ...     # Handle result.
            ...     result = operation_future.result()
            >>>
            >>> response.add_done_callback(callback)
            >>>
            >>> # Handle metadata.
            >>> metadata = response.metadata()

        Args:
            name (str): Required. The resource name of the dataset to delete.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.automl_v1beta1.types._OperationFuture` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "delete_dataset" not in self._inner_api_calls:
            self._inner_api_calls[
                "delete_dataset"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.delete_dataset,
                default_retry=self._method_configs["DeleteDataset"].retry,
                default_timeout=self._method_configs["DeleteDataset"].timeout,
                client_info=self._client_info,
            )

        request = service_pb2.DeleteDatasetRequest(name=name)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        operation = self._inner_api_calls["delete_dataset"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )
        return google.api_core.operation.from_gapic(
            operation,
            self.transport._operations_client,
            empty_pb2.Empty,
            metadata_type=proto_operations_pb2.OperationMetadata,
        )

    def import_data(
        self,
        name,
        input_config,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
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

        Example:
            >>> from google.cloud import automl_v1beta1
            >>>
            >>> client = automl_v1beta1.AutoMlClient()
            >>>
            >>> name = client.dataset_path('[PROJECT]', '[LOCATION]', '[DATASET]')
            >>>
            >>> # TODO: Initialize `input_config`:
            >>> input_config = {}
            >>>
            >>> response = client.import_data(name, input_config)
            >>>
            >>> def callback(operation_future):
            ...     # Handle result.
            ...     result = operation_future.result()
            >>>
            >>> response.add_done_callback(callback)
            >>>
            >>> # Handle metadata.
            >>> metadata = response.metadata()

        Args:
            name (str): Required. Dataset name. Dataset must already exist. All imported
                annotations and examples will be added.
            input_config (Union[dict, ~google.cloud.automl_v1beta1.types.InputConfig]): Required. The desired input location and its domain specific semantics,
                if any.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.automl_v1beta1.types.InputConfig`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.automl_v1beta1.types._OperationFuture` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "import_data" not in self._inner_api_calls:
            self._inner_api_calls[
                "import_data"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.import_data,
                default_retry=self._method_configs["ImportData"].retry,
                default_timeout=self._method_configs["ImportData"].timeout,
                client_info=self._client_info,
            )

        request = service_pb2.ImportDataRequest(name=name, input_config=input_config)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        operation = self._inner_api_calls["import_data"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )
        return google.api_core.operation.from_gapic(
            operation,
            self.transport._operations_client,
            empty_pb2.Empty,
            metadata_type=proto_operations_pb2.OperationMetadata,
        )

    def export_data(
        self,
        name,
        output_config,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
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

        Example:
            >>> from google.cloud import automl_v1beta1
            >>>
            >>> client = automl_v1beta1.AutoMlClient()
            >>>
            >>> name = client.dataset_path('[PROJECT]', '[LOCATION]', '[DATASET]')
            >>>
            >>> # TODO: Initialize `output_config`:
            >>> output_config = {}
            >>>
            >>> response = client.export_data(name, output_config)
            >>>
            >>> def callback(operation_future):
            ...     # Handle result.
            ...     result = operation_future.result()
            >>>
            >>> response.add_done_callback(callback)
            >>>
            >>> # Handle metadata.
            >>> metadata = response.metadata()

        Args:
            name (str): Required. The resource name of the dataset.
            output_config (Union[dict, ~google.cloud.automl_v1beta1.types.OutputConfig]): Required. The desired output location.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.automl_v1beta1.types.OutputConfig`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.automl_v1beta1.types._OperationFuture` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "export_data" not in self._inner_api_calls:
            self._inner_api_calls[
                "export_data"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.export_data,
                default_retry=self._method_configs["ExportData"].retry,
                default_timeout=self._method_configs["ExportData"].timeout,
                client_info=self._client_info,
            )

        request = service_pb2.ExportDataRequest(name=name, output_config=output_config)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        operation = self._inner_api_calls["export_data"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )
        return google.api_core.operation.from_gapic(
            operation,
            self.transport._operations_client,
            empty_pb2.Empty,
            metadata_type=proto_operations_pb2.OperationMetadata,
        )

    def delete_model(
        self,
        name,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Output only. The number of nodes this model is deployed on. A node
        is an abstraction of a machine resource, which can handle online
        prediction QPS as given in the qps_per_node field.

        Example:
            >>> from google.cloud import automl_v1beta1
            >>>
            >>> client = automl_v1beta1.AutoMlClient()
            >>>
            >>> name = client.model_path('[PROJECT]', '[LOCATION]', '[MODEL]')
            >>>
            >>> response = client.delete_model(name)
            >>>
            >>> def callback(operation_future):
            ...     # Handle result.
            ...     result = operation_future.result()
            >>>
            >>> response.add_done_callback(callback)
            >>>
            >>> # Handle metadata.
            >>> metadata = response.metadata()

        Args:
            name (str): Required. Resource name of the model being deleted.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.automl_v1beta1.types._OperationFuture` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "delete_model" not in self._inner_api_calls:
            self._inner_api_calls[
                "delete_model"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.delete_model,
                default_retry=self._method_configs["DeleteModel"].retry,
                default_timeout=self._method_configs["DeleteModel"].timeout,
                client_info=self._client_info,
            )

        request = service_pb2.DeleteModelRequest(name=name)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        operation = self._inner_api_calls["delete_model"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )
        return google.api_core.operation.from_gapic(
            operation,
            self.transport._operations_client,
            empty_pb2.Empty,
            metadata_type=proto_operations_pb2.OperationMetadata,
        )

    def export_model(
        self,
        name,
        output_config,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
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

        Example:
            >>> from google.cloud import automl_v1beta1
            >>>
            >>> client = automl_v1beta1.AutoMlClient()
            >>>
            >>> name = client.model_path('[PROJECT]', '[LOCATION]', '[MODEL]')
            >>>
            >>> # TODO: Initialize `output_config`:
            >>> output_config = {}
            >>>
            >>> response = client.export_model(name, output_config)
            >>>
            >>> def callback(operation_future):
            ...     # Handle result.
            ...     result = operation_future.result()
            >>>
            >>> response.add_done_callback(callback)
            >>>
            >>> # Handle metadata.
            >>> metadata = response.metadata()

        Args:
            name (str): Required. The resource name of the model to export.
            output_config (Union[dict, ~google.cloud.automl_v1beta1.types.ModelExportOutputConfig]): Required. The desired output location and configuration.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.automl_v1beta1.types.ModelExportOutputConfig`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.automl_v1beta1.types._OperationFuture` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "export_model" not in self._inner_api_calls:
            self._inner_api_calls[
                "export_model"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.export_model,
                default_retry=self._method_configs["ExportModel"].retry,
                default_timeout=self._method_configs["ExportModel"].timeout,
                client_info=self._client_info,
            )

        request = service_pb2.ExportModelRequest(name=name, output_config=output_config)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        operation = self._inner_api_calls["export_model"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )
        return google.api_core.operation.from_gapic(
            operation,
            self.transport._operations_client,
            empty_pb2.Empty,
            metadata_type=proto_operations_pb2.OperationMetadata,
        )

    def export_evaluated_examples(
        self,
        name,
        output_config,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Output only. Resource name of the model. Format:
        ``projects/{project_id}/locations/{location_id}/models/{model_id}``

        Example:
            >>> from google.cloud import automl_v1beta1
            >>>
            >>> client = automl_v1beta1.AutoMlClient()
            >>>
            >>> name = client.model_path('[PROJECT]', '[LOCATION]', '[MODEL]')
            >>>
            >>> # TODO: Initialize `output_config`:
            >>> output_config = {}
            >>>
            >>> response = client.export_evaluated_examples(name, output_config)
            >>>
            >>> def callback(operation_future):
            ...     # Handle result.
            ...     result = operation_future.result()
            >>>
            >>> response.add_done_callback(callback)
            >>>
            >>> # Handle metadata.
            >>> metadata = response.metadata()

        Args:
            name (str): Required. The resource name of the model whose evaluated examples are to
                be exported.
            output_config (Union[dict, ~google.cloud.automl_v1beta1.types.ExportEvaluatedExamplesOutputConfig]): Required. The desired output location and configuration.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.automl_v1beta1.types.ExportEvaluatedExamplesOutputConfig`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.automl_v1beta1.types._OperationFuture` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "export_evaluated_examples" not in self._inner_api_calls:
            self._inner_api_calls[
                "export_evaluated_examples"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.export_evaluated_examples,
                default_retry=self._method_configs["ExportEvaluatedExamples"].retry,
                default_timeout=self._method_configs["ExportEvaluatedExamples"].timeout,
                client_info=self._client_info,
            )

        request = service_pb2.ExportEvaluatedExamplesRequest(
            name=name, output_config=output_config
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        operation = self._inner_api_calls["export_evaluated_examples"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )
        return google.api_core.operation.from_gapic(
            operation,
            self.transport._operations_client,
            empty_pb2.Empty,
            metadata_type=proto_operations_pb2.OperationMetadata,
        )

    def list_model_evaluations(
        self,
        parent,
        filter_=None,
        page_size=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Lists model evaluations.

        Example:
            >>> from google.cloud import automl_v1beta1
            >>>
            >>> client = automl_v1beta1.AutoMlClient()
            >>>
            >>> parent = client.model_path('[PROJECT]', '[LOCATION]', '[MODEL]')
            >>>
            >>> # Iterate over all results
            >>> for element in client.list_model_evaluations(parent):
            ...     # process element
            ...     pass
            >>>
            >>>
            >>> # Alternatively:
            >>>
            >>> # Iterate over results one page at a time
            >>> for page in client.list_model_evaluations(parent).pages:
            ...     for element in page:
            ...         # process element
            ...         pass

        Args:
            parent (str): Required. Resource name of the model to list the model evaluations for.
                If modelId is set as "-", this will list model evaluations from across all
                models of the parent location.
            filter_ (str): An expression for filtering the results of the request.

                -  ``model_metadata`` - for existence of the case (e.g.
                   video_classification_model_metadata:*).

                -  ``dataset_id`` - for = or !=. Some examples of using the filter are:

                -  ``image_classification_model_metadata:*`` --> The model has
                   image_classification_model_metadata.

                -  ``dataset_id=5`` --> The model was created from a dataset with ID 5.
            page_size (int): The maximum number of resources contained in the
                underlying API response. If page streaming is performed per-
                resource, this parameter does not affect the return value. If page
                streaming is performed per-page, this determines the maximum number
                of resources in a page.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.api_core.page_iterator.PageIterator` instance.
            An iterable of :class:`~google.cloud.automl_v1beta1.types.ModelEvaluation` instances.
            You can also iterate over the pages of the response
            using its `pages` property.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "list_model_evaluations" not in self._inner_api_calls:
            self._inner_api_calls[
                "list_model_evaluations"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.list_model_evaluations,
                default_retry=self._method_configs["ListModelEvaluations"].retry,
                default_timeout=self._method_configs["ListModelEvaluations"].timeout,
                client_info=self._client_info,
            )

        request = service_pb2.ListModelEvaluationsRequest(
            parent=parent, filter=filter_, page_size=page_size
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        iterator = google.api_core.page_iterator.GRPCIterator(
            client=None,
            method=functools.partial(
                self._inner_api_calls["list_model_evaluations"],
                retry=retry,
                timeout=timeout,
                metadata=metadata,
            ),
            request=request,
            items_field="model_evaluation",
            request_token_field="page_token",
            response_token_field="next_page_token",
        )
        return iterator

    def create_dataset(
        self,
        parent,
        dataset,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Creates a dataset.

        Example:
            >>> from google.cloud import automl_v1beta1
            >>>
            >>> client = automl_v1beta1.AutoMlClient()
            >>>
            >>> parent = client.location_path('[PROJECT]', '[LOCATION]')
            >>>
            >>> # TODO: Initialize `dataset`:
            >>> dataset = {}
            >>>
            >>> response = client.create_dataset(parent, dataset)

        Args:
            parent (str): Required. The resource name of the project to create the dataset for.
            dataset (Union[dict, ~google.cloud.automl_v1beta1.types.Dataset]): Required. The dataset to create.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.automl_v1beta1.types.Dataset`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.automl_v1beta1.types.Dataset` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "create_dataset" not in self._inner_api_calls:
            self._inner_api_calls[
                "create_dataset"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.create_dataset,
                default_retry=self._method_configs["CreateDataset"].retry,
                default_timeout=self._method_configs["CreateDataset"].timeout,
                client_info=self._client_info,
            )

        request = service_pb2.CreateDatasetRequest(parent=parent, dataset=dataset)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["create_dataset"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def get_dataset(
        self,
        name,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Gets a dataset.

        Example:
            >>> from google.cloud import automl_v1beta1
            >>>
            >>> client = automl_v1beta1.AutoMlClient()
            >>>
            >>> name = client.dataset_path('[PROJECT]', '[LOCATION]', '[DATASET]')
            >>>
            >>> response = client.get_dataset(name)

        Args:
            name (str): Required. The resource name of the dataset to retrieve.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.automl_v1beta1.types.Dataset` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "get_dataset" not in self._inner_api_calls:
            self._inner_api_calls[
                "get_dataset"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_dataset,
                default_retry=self._method_configs["GetDataset"].retry,
                default_timeout=self._method_configs["GetDataset"].timeout,
                client_info=self._client_info,
            )

        request = service_pb2.GetDatasetRequest(name=name)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["get_dataset"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def list_datasets(
        self,
        parent,
        filter_=None,
        page_size=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Lists datasets in a project.

        Example:
            >>> from google.cloud import automl_v1beta1
            >>>
            >>> client = automl_v1beta1.AutoMlClient()
            >>>
            >>> parent = client.location_path('[PROJECT]', '[LOCATION]')
            >>>
            >>> # Iterate over all results
            >>> for element in client.list_datasets(parent):
            ...     # process element
            ...     pass
            >>>
            >>>
            >>> # Alternatively:
            >>>
            >>> # Iterate over results one page at a time
            >>> for page in client.list_datasets(parent).pages:
            ...     for element in page:
            ...         # process element
            ...         pass

        Args:
            parent (str): Required. The resource name of the project from which to list datasets.
            filter_ (str): Required. The name of the model to show in the interface. The name
                can be up to 32 characters long and can consist only of ASCII Latin
                letters A-Z and a-z, underscores (_), and ASCII digits 0-9. It must
                start with a letter.
            page_size (int): The maximum number of resources contained in the
                underlying API response. If page streaming is performed per-
                resource, this parameter does not affect the return value. If page
                streaming is performed per-page, this determines the maximum number
                of resources in a page.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.api_core.page_iterator.PageIterator` instance.
            An iterable of :class:`~google.cloud.automl_v1beta1.types.Dataset` instances.
            You can also iterate over the pages of the response
            using its `pages` property.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "list_datasets" not in self._inner_api_calls:
            self._inner_api_calls[
                "list_datasets"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.list_datasets,
                default_retry=self._method_configs["ListDatasets"].retry,
                default_timeout=self._method_configs["ListDatasets"].timeout,
                client_info=self._client_info,
            )

        request = service_pb2.ListDatasetsRequest(
            parent=parent, filter=filter_, page_size=page_size
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        iterator = google.api_core.page_iterator.GRPCIterator(
            client=None,
            method=functools.partial(
                self._inner_api_calls["list_datasets"],
                retry=retry,
                timeout=timeout,
                metadata=metadata,
            ),
            request=request,
            items_field="datasets",
            request_token_field="page_token",
            response_token_field="next_page_token",
        )
        return iterator

    def update_dataset(
        self,
        dataset,
        update_mask=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Updates a dataset.

        Example:
            >>> from google.cloud import automl_v1beta1
            >>>
            >>> client = automl_v1beta1.AutoMlClient()
            >>>
            >>> # TODO: Initialize `dataset`:
            >>> dataset = {}
            >>>
            >>> response = client.update_dataset(dataset)

        Args:
            dataset (Union[dict, ~google.cloud.automl_v1beta1.types.Dataset]): Required. The dataset which replaces the resource on the server.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.automl_v1beta1.types.Dataset`
            update_mask (Union[dict, ~google.cloud.automl_v1beta1.types.FieldMask]): The update mask applies to the resource.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.automl_v1beta1.types.FieldMask`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.automl_v1beta1.types.Dataset` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "update_dataset" not in self._inner_api_calls:
            self._inner_api_calls[
                "update_dataset"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.update_dataset,
                default_retry=self._method_configs["UpdateDataset"].retry,
                default_timeout=self._method_configs["UpdateDataset"].timeout,
                client_info=self._client_info,
            )

        request = service_pb2.UpdateDatasetRequest(
            dataset=dataset, update_mask=update_mask
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("dataset.name", dataset.name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["update_dataset"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def get_annotation_spec(
        self,
        name,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Gets an annotation spec.

        Example:
            >>> from google.cloud import automl_v1beta1
            >>>
            >>> client = automl_v1beta1.AutoMlClient()
            >>>
            >>> name = client.annotation_spec_path('[PROJECT]', '[LOCATION]', '[DATASET]', '[ANNOTATION_SPEC]')
            >>>
            >>> response = client.get_annotation_spec(name)

        Args:
            name (str): Required. The resource name of the annotation spec to retrieve.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.automl_v1beta1.types.AnnotationSpec` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "get_annotation_spec" not in self._inner_api_calls:
            self._inner_api_calls[
                "get_annotation_spec"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_annotation_spec,
                default_retry=self._method_configs["GetAnnotationSpec"].retry,
                default_timeout=self._method_configs["GetAnnotationSpec"].timeout,
                client_info=self._client_info,
            )

        request = service_pb2.GetAnnotationSpecRequest(name=name)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["get_annotation_spec"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def get_table_spec(
        self,
        name,
        field_mask=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Gets a table spec.

        Example:
            >>> from google.cloud import automl_v1beta1
            >>>
            >>> client = automl_v1beta1.AutoMlClient()
            >>>
            >>> name = client.table_spec_path('[PROJECT]', '[LOCATION]', '[DATASET]', '[TABLE_SPEC]')
            >>>
            >>> response = client.get_table_spec(name)

        Args:
            name (str): Required. The resource name of the table spec to retrieve.
            field_mask (Union[dict, ~google.cloud.automl_v1beta1.types.FieldMask]): Mask specifying which fields to read.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.automl_v1beta1.types.FieldMask`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.automl_v1beta1.types.TableSpec` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "get_table_spec" not in self._inner_api_calls:
            self._inner_api_calls[
                "get_table_spec"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_table_spec,
                default_retry=self._method_configs["GetTableSpec"].retry,
                default_timeout=self._method_configs["GetTableSpec"].timeout,
                client_info=self._client_info,
            )

        request = service_pb2.GetTableSpecRequest(name=name, field_mask=field_mask)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["get_table_spec"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def list_table_specs(
        self,
        parent,
        field_mask=None,
        filter_=None,
        page_size=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Lists table specs in a dataset.

        Example:
            >>> from google.cloud import automl_v1beta1
            >>>
            >>> client = automl_v1beta1.AutoMlClient()
            >>>
            >>> parent = client.dataset_path('[PROJECT]', '[LOCATION]', '[DATASET]')
            >>>
            >>> # Iterate over all results
            >>> for element in client.list_table_specs(parent):
            ...     # process element
            ...     pass
            >>>
            >>>
            >>> # Alternatively:
            >>>
            >>> # Iterate over results one page at a time
            >>> for page in client.list_table_specs(parent).pages:
            ...     for element in page:
            ...         # process element
            ...         pass

        Args:
            parent (str): Required. The resource name of the dataset to list table specs from.
            field_mask (Union[dict, ~google.cloud.automl_v1beta1.types.FieldMask]): Mask specifying which fields to read.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.automl_v1beta1.types.FieldMask`
            filter_ (str): Filter expression, see go/filtering.
            page_size (int): The maximum number of resources contained in the
                underlying API response. If page streaming is performed per-
                resource, this parameter does not affect the return value. If page
                streaming is performed per-page, this determines the maximum number
                of resources in a page.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.api_core.page_iterator.PageIterator` instance.
            An iterable of :class:`~google.cloud.automl_v1beta1.types.TableSpec` instances.
            You can also iterate over the pages of the response
            using its `pages` property.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "list_table_specs" not in self._inner_api_calls:
            self._inner_api_calls[
                "list_table_specs"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.list_table_specs,
                default_retry=self._method_configs["ListTableSpecs"].retry,
                default_timeout=self._method_configs["ListTableSpecs"].timeout,
                client_info=self._client_info,
            )

        request = service_pb2.ListTableSpecsRequest(
            parent=parent, field_mask=field_mask, filter=filter_, page_size=page_size
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        iterator = google.api_core.page_iterator.GRPCIterator(
            client=None,
            method=functools.partial(
                self._inner_api_calls["list_table_specs"],
                retry=retry,
                timeout=timeout,
                metadata=metadata,
            ),
            request=request,
            items_field="table_specs",
            request_token_field="page_token",
            response_token_field="next_page_token",
        )
        return iterator

    def update_table_spec(
        self,
        table_spec,
        update_mask=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Updates a table spec.

        Example:
            >>> from google.cloud import automl_v1beta1
            >>>
            >>> client = automl_v1beta1.AutoMlClient()
            >>>
            >>> # TODO: Initialize `table_spec`:
            >>> table_spec = {}
            >>>
            >>> response = client.update_table_spec(table_spec)

        Args:
            table_spec (Union[dict, ~google.cloud.automl_v1beta1.types.TableSpec]): Required. The table spec which replaces the resource on the server.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.automl_v1beta1.types.TableSpec`
            update_mask (Union[dict, ~google.cloud.automl_v1beta1.types.FieldMask]): The update mask applies to the resource.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.automl_v1beta1.types.FieldMask`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.automl_v1beta1.types.TableSpec` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "update_table_spec" not in self._inner_api_calls:
            self._inner_api_calls[
                "update_table_spec"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.update_table_spec,
                default_retry=self._method_configs["UpdateTableSpec"].retry,
                default_timeout=self._method_configs["UpdateTableSpec"].timeout,
                client_info=self._client_info,
            )

        request = service_pb2.UpdateTableSpecRequest(
            table_spec=table_spec, update_mask=update_mask
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("table_spec.name", table_spec.name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["update_table_spec"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def get_column_spec(
        self,
        name,
        field_mask=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Gets a column spec.

        Example:
            >>> from google.cloud import automl_v1beta1
            >>>
            >>> client = automl_v1beta1.AutoMlClient()
            >>>
            >>> name = client.column_spec_path('[PROJECT]', '[LOCATION]', '[DATASET]', '[TABLE_SPEC]', '[COLUMN_SPEC]')
            >>>
            >>> response = client.get_column_spec(name)

        Args:
            name (str): Required. The resource name of the column spec to retrieve.
            field_mask (Union[dict, ~google.cloud.automl_v1beta1.types.FieldMask]): Mask specifying which fields to read.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.automl_v1beta1.types.FieldMask`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.automl_v1beta1.types.ColumnSpec` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "get_column_spec" not in self._inner_api_calls:
            self._inner_api_calls[
                "get_column_spec"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_column_spec,
                default_retry=self._method_configs["GetColumnSpec"].retry,
                default_timeout=self._method_configs["GetColumnSpec"].timeout,
                client_info=self._client_info,
            )

        request = service_pb2.GetColumnSpecRequest(name=name, field_mask=field_mask)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["get_column_spec"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def list_column_specs(
        self,
        parent,
        field_mask=None,
        filter_=None,
        page_size=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Lists column specs in a table spec.

        Example:
            >>> from google.cloud import automl_v1beta1
            >>>
            >>> client = automl_v1beta1.AutoMlClient()
            >>>
            >>> parent = client.table_spec_path('[PROJECT]', '[LOCATION]', '[DATASET]', '[TABLE_SPEC]')
            >>>
            >>> # Iterate over all results
            >>> for element in client.list_column_specs(parent):
            ...     # process element
            ...     pass
            >>>
            >>>
            >>> # Alternatively:
            >>>
            >>> # Iterate over results one page at a time
            >>> for page in client.list_column_specs(parent).pages:
            ...     for element in page:
            ...         # process element
            ...         pass

        Args:
            parent (str): Required. The resource name of the table spec to list column specs from.
            field_mask (Union[dict, ~google.cloud.automl_v1beta1.types.FieldMask]): Mask specifying which fields to read.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.automl_v1beta1.types.FieldMask`
            filter_ (str): Filter expression, see go/filtering.
            page_size (int): The maximum number of resources contained in the
                underlying API response. If page streaming is performed per-
                resource, this parameter does not affect the return value. If page
                streaming is performed per-page, this determines the maximum number
                of resources in a page.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.api_core.page_iterator.PageIterator` instance.
            An iterable of :class:`~google.cloud.automl_v1beta1.types.ColumnSpec` instances.
            You can also iterate over the pages of the response
            using its `pages` property.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "list_column_specs" not in self._inner_api_calls:
            self._inner_api_calls[
                "list_column_specs"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.list_column_specs,
                default_retry=self._method_configs["ListColumnSpecs"].retry,
                default_timeout=self._method_configs["ListColumnSpecs"].timeout,
                client_info=self._client_info,
            )

        request = service_pb2.ListColumnSpecsRequest(
            parent=parent, field_mask=field_mask, filter=filter_, page_size=page_size
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        iterator = google.api_core.page_iterator.GRPCIterator(
            client=None,
            method=functools.partial(
                self._inner_api_calls["list_column_specs"],
                retry=retry,
                timeout=timeout,
                metadata=metadata,
            ),
            request=request,
            items_field="column_specs",
            request_token_field="page_token",
            response_token_field="next_page_token",
        )
        return iterator

    def update_column_spec(
        self,
        column_spec,
        update_mask=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Updates a column spec.

        Example:
            >>> from google.cloud import automl_v1beta1
            >>>
            >>> client = automl_v1beta1.AutoMlClient()
            >>>
            >>> # TODO: Initialize `column_spec`:
            >>> column_spec = {}
            >>>
            >>> response = client.update_column_spec(column_spec)

        Args:
            column_spec (Union[dict, ~google.cloud.automl_v1beta1.types.ColumnSpec]): Required. The column spec which replaces the resource on the server.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.automl_v1beta1.types.ColumnSpec`
            update_mask (Union[dict, ~google.cloud.automl_v1beta1.types.FieldMask]): The update mask applies to the resource.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.automl_v1beta1.types.FieldMask`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.automl_v1beta1.types.ColumnSpec` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "update_column_spec" not in self._inner_api_calls:
            self._inner_api_calls[
                "update_column_spec"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.update_column_spec,
                default_retry=self._method_configs["UpdateColumnSpec"].retry,
                default_timeout=self._method_configs["UpdateColumnSpec"].timeout,
                client_info=self._client_info,
            )

        request = service_pb2.UpdateColumnSpecRequest(
            column_spec=column_spec, update_mask=update_mask
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("column_spec.name", column_spec.name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["update_column_spec"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def create_model(
        self,
        parent,
        model,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
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

        Example:
            >>> from google.cloud import automl_v1beta1
            >>>
            >>> client = automl_v1beta1.AutoMlClient()
            >>>
            >>> parent = client.location_path('[PROJECT]', '[LOCATION]')
            >>>
            >>> # TODO: Initialize `model`:
            >>> model = {}
            >>>
            >>> response = client.create_model(parent, model)
            >>>
            >>> def callback(operation_future):
            ...     # Handle result.
            ...     result = operation_future.result()
            >>>
            >>> response.add_done_callback(callback)
            >>>
            >>> # Handle metadata.
            >>> metadata = response.metadata()

        Args:
            parent (str): Required. Resource name of the parent project where the model is being created.
            model (Union[dict, ~google.cloud.automl_v1beta1.types.Model]): Required. The model to create.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.automl_v1beta1.types.Model`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.automl_v1beta1.types._OperationFuture` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "create_model" not in self._inner_api_calls:
            self._inner_api_calls[
                "create_model"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.create_model,
                default_retry=self._method_configs["CreateModel"].retry,
                default_timeout=self._method_configs["CreateModel"].timeout,
                client_info=self._client_info,
            )

        request = service_pb2.CreateModelRequest(parent=parent, model=model)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        operation = self._inner_api_calls["create_model"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )
        return google.api_core.operation.from_gapic(
            operation,
            self.transport._operations_client,
            model_pb2.Model,
            metadata_type=proto_operations_pb2.OperationMetadata,
        )

    def get_model(
        self,
        name,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Gets a model.

        Example:
            >>> from google.cloud import automl_v1beta1
            >>>
            >>> client = automl_v1beta1.AutoMlClient()
            >>>
            >>> name = client.model_path('[PROJECT]', '[LOCATION]', '[MODEL]')
            >>>
            >>> response = client.get_model(name)

        Args:
            name (str): Required. Resource name of the model.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.automl_v1beta1.types.Model` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "get_model" not in self._inner_api_calls:
            self._inner_api_calls[
                "get_model"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_model,
                default_retry=self._method_configs["GetModel"].retry,
                default_timeout=self._method_configs["GetModel"].timeout,
                client_info=self._client_info,
            )

        request = service_pb2.GetModelRequest(name=name)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["get_model"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def list_models(
        self,
        parent,
        filter_=None,
        page_size=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Lists models.

        Example:
            >>> from google.cloud import automl_v1beta1
            >>>
            >>> client = automl_v1beta1.AutoMlClient()
            >>>
            >>> parent = client.location_path('[PROJECT]', '[LOCATION]')
            >>>
            >>> # Iterate over all results
            >>> for element in client.list_models(parent):
            ...     # process element
            ...     pass
            >>>
            >>>
            >>> # Alternatively:
            >>>
            >>> # Iterate over results one page at a time
            >>> for page in client.list_models(parent).pages:
            ...     for element in page:
            ...         # process element
            ...         pass

        Args:
            parent (str): Required. Resource name of the project, from which to list the models.
            filter_ (str): Input only. The number of nodes to deploy the model on. A node is an
                abstraction of a machine resource, which can handle online prediction
                QPS as given in the model's

                ``qps_per_node``. Must be between 1 and 100, inclusive on both ends.
            page_size (int): The maximum number of resources contained in the
                underlying API response. If page streaming is performed per-
                resource, this parameter does not affect the return value. If page
                streaming is performed per-page, this determines the maximum number
                of resources in a page.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.api_core.page_iterator.PageIterator` instance.
            An iterable of :class:`~google.cloud.automl_v1beta1.types.Model` instances.
            You can also iterate over the pages of the response
            using its `pages` property.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "list_models" not in self._inner_api_calls:
            self._inner_api_calls[
                "list_models"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.list_models,
                default_retry=self._method_configs["ListModels"].retry,
                default_timeout=self._method_configs["ListModels"].timeout,
                client_info=self._client_info,
            )

        request = service_pb2.ListModelsRequest(
            parent=parent, filter=filter_, page_size=page_size
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        iterator = google.api_core.page_iterator.GRPCIterator(
            client=None,
            method=functools.partial(
                self._inner_api_calls["list_models"],
                retry=retry,
                timeout=timeout,
                metadata=metadata,
            ),
            request=request,
            items_field="model",
            request_token_field="page_token",
            response_token_field="next_page_token",
        )
        return iterator

    def deploy_model(
        self,
        name,
        image_object_detection_model_deployment_metadata=None,
        image_classification_model_deployment_metadata=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Input only. The data representing the image. For Predict calls
        ``image_bytes`` must be set, as other options are not currently
        supported by prediction API. You can read the contents of an uploaded
        image by using the ``content_uri`` field.

        Example:
            >>> from google.cloud import automl_v1beta1
            >>>
            >>> client = automl_v1beta1.AutoMlClient()
            >>>
            >>> name = client.model_path('[PROJECT]', '[LOCATION]', '[MODEL]')
            >>>
            >>> response = client.deploy_model(name)
            >>>
            >>> def callback(operation_future):
            ...     # Handle result.
            ...     result = operation_future.result()
            >>>
            >>> response.add_done_callback(callback)
            >>>
            >>> # Handle metadata.
            >>> metadata = response.metadata()

        Args:
            name (str): Required. Resource name of the model to deploy.
            image_object_detection_model_deployment_metadata (Union[dict, ~google.cloud.automl_v1beta1.types.ImageObjectDetectionModelDeploymentMetadata]): Model deployment metadata specific to Image Object Detection.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.automl_v1beta1.types.ImageObjectDetectionModelDeploymentMetadata`
            image_classification_model_deployment_metadata (Union[dict, ~google.cloud.automl_v1beta1.types.ImageClassificationModelDeploymentMetadata]): Model deployment metadata specific to Image Classification.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.automl_v1beta1.types.ImageClassificationModelDeploymentMetadata`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.automl_v1beta1.types._OperationFuture` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "deploy_model" not in self._inner_api_calls:
            self._inner_api_calls[
                "deploy_model"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.deploy_model,
                default_retry=self._method_configs["DeployModel"].retry,
                default_timeout=self._method_configs["DeployModel"].timeout,
                client_info=self._client_info,
            )

        # Sanity check: We have some fields which are mutually exclusive;
        # raise ValueError if more than one is sent.
        google.api_core.protobuf_helpers.check_oneof(
            image_object_detection_model_deployment_metadata=image_object_detection_model_deployment_metadata,
            image_classification_model_deployment_metadata=image_classification_model_deployment_metadata,
        )

        request = service_pb2.DeployModelRequest(
            name=name,
            image_object_detection_model_deployment_metadata=image_object_detection_model_deployment_metadata,
            image_classification_model_deployment_metadata=image_classification_model_deployment_metadata,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        operation = self._inner_api_calls["deploy_model"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )
        return google.api_core.operation.from_gapic(
            operation,
            self.transport._operations_client,
            empty_pb2.Empty,
            metadata_type=proto_operations_pb2.OperationMetadata,
        )

    def undeploy_model(
        self,
        name,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Imports data into a dataset. For Tables this method can only be
        called on an empty Dataset.

        For Tables:

        -  A ``schema_inference_version`` parameter must be explicitly set.
           Returns an empty response in the ``response`` field when it
           completes.

        Example:
            >>> from google.cloud import automl_v1beta1
            >>>
            >>> client = automl_v1beta1.AutoMlClient()
            >>>
            >>> name = client.model_path('[PROJECT]', '[LOCATION]', '[MODEL]')
            >>>
            >>> response = client.undeploy_model(name)
            >>>
            >>> def callback(operation_future):
            ...     # Handle result.
            ...     result = operation_future.result()
            >>>
            >>> response.add_done_callback(callback)
            >>>
            >>> # Handle metadata.
            >>> metadata = response.metadata()

        Args:
            name (str): Required. Resource name of the model to undeploy.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.automl_v1beta1.types._OperationFuture` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "undeploy_model" not in self._inner_api_calls:
            self._inner_api_calls[
                "undeploy_model"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.undeploy_model,
                default_retry=self._method_configs["UndeployModel"].retry,
                default_timeout=self._method_configs["UndeployModel"].timeout,
                client_info=self._client_info,
            )

        request = service_pb2.UndeployModelRequest(name=name)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        operation = self._inner_api_calls["undeploy_model"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )
        return google.api_core.operation.from_gapic(
            operation,
            self.transport._operations_client,
            empty_pb2.Empty,
            metadata_type=proto_operations_pb2.OperationMetadata,
        )

    def get_model_evaluation(
        self,
        name,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Gets a model evaluation.

        Example:
            >>> from google.cloud import automl_v1beta1
            >>>
            >>> client = automl_v1beta1.AutoMlClient()
            >>>
            >>> name = client.model_evaluation_path('[PROJECT]', '[LOCATION]', '[MODEL]', '[MODEL_EVALUATION]')
            >>>
            >>> response = client.get_model_evaluation(name)

        Args:
            name (str): Required. Resource name for the model evaluation.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.automl_v1beta1.types.ModelEvaluation` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "get_model_evaluation" not in self._inner_api_calls:
            self._inner_api_calls[
                "get_model_evaluation"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_model_evaluation,
                default_retry=self._method_configs["GetModelEvaluation"].retry,
                default_timeout=self._method_configs["GetModelEvaluation"].timeout,
                client_info=self._client_info,
            )

        request = service_pb2.GetModelEvaluationRequest(name=name)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["get_model_evaluation"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )
