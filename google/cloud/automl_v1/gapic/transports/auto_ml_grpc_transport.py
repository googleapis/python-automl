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

from google.cloud.automl_v1.proto import service_pb2_grpc


class AutoMlGrpcTransport(object):
    """gRPC transport class providing stubs for
    google.cloud.automl.v1 AutoMl API.

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

        An annotation that describes a resource definition, see
        ``ResourceDescriptor``.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["auto_ml_stub"].DeleteDataset

    @property
    def delete_model(self):
        """Return the gRPC stub for :meth:`AutoMlClient.delete_model`.

        Starts asynchronous cancellation on a long-running operation. The
        server makes a best effort to cancel the operation, but success is not
        guaranteed. If the server doesn't support this method, it returns
        ``google.rpc.Code.UNIMPLEMENTED``. Clients can use
        ``Operations.GetOperation`` or other methods to check whether the
        cancellation succeeded or whether the operation completed despite
        cancellation. On successful cancellation, the operation is not deleted;
        instead, it becomes an operation with an ``Operation.error`` value with
        a ``google.rpc.Status.code`` of 1, corresponding to ``Code.CANCELLED``.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["auto_ml_stub"].DeleteModel

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
    def import_data(self):
        """Return the gRPC stub for :meth:`AutoMlClient.import_data`.

        The ``Status`` type defines a logical error model that is suitable
        for different programming environments, including REST APIs and RPC
        APIs. It is used by `gRPC <https://github.com/grpc>`__. Each ``Status``
        message contains three pieces of data: error code, error message, and
        error details.

        You can find out more about this error model and how to work with it in
        the `API Design Guide <https://cloud.google.com/apis/design/errors>`__.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["auto_ml_stub"].ImportData

    @property
    def export_data(self):
        """Return the gRPC stub for :meth:`AutoMlClient.export_data`.

        A simple descriptor of a resource type.

        ResourceDescriptor annotates a resource message (either by means of a
        protobuf annotation or use in the service config), and associates the
        resource's schema, the resource type, and the pattern of the resource
        name.

        Example:

        ::

            message Topic {
              // Indicates this message defines a resource schema.
              // Declares the resource type in the format of {service}/{kind}.
              // For Kubernetes resources, the format is {api group}/{kind}.
              option (google.api.resource) = {
                type: "pubsub.googleapis.com/Topic"
                name_descriptor: {
                  pattern: "projects/{project}/topics/{topic}"
                  parent_type: "cloudresourcemanager.googleapis.com/Project"
                  parent_name_extractor: "projects/{project}"
                }
              };
            }

        The ResourceDescriptor Yaml config will look like:

        ::

            resources:
            - type: "pubsub.googleapis.com/Topic"
              name_descriptor:
                - pattern: "projects/{project}/topics/{topic}"
                  parent_type: "cloudresourcemanager.googleapis.com/Project"
                  parent_name_extractor: "projects/{project}"

        Sometimes, resources have multiple patterns, typically because they can
        live under multiple parents.

        Example:

        ::

            message LogEntry {
              option (google.api.resource) = {
                type: "logging.googleapis.com/LogEntry"
                name_descriptor: {
                  pattern: "projects/{project}/logs/{log}"
                  parent_type: "cloudresourcemanager.googleapis.com/Project"
                  parent_name_extractor: "projects/{project}"
                }
                name_descriptor: {
                  pattern: "folders/{folder}/logs/{log}"
                  parent_type: "cloudresourcemanager.googleapis.com/Folder"
                  parent_name_extractor: "folders/{folder}"
                }
                name_descriptor: {
                  pattern: "organizations/{organization}/logs/{log}"
                  parent_type: "cloudresourcemanager.googleapis.com/Organization"
                  parent_name_extractor: "organizations/{organization}"
                }
                name_descriptor: {
                  pattern: "billingAccounts/{billing_account}/logs/{log}"
                  parent_type: "billing.googleapis.com/BillingAccount"
                  parent_name_extractor: "billingAccounts/{billing_account}"
                }
              };
            }

        The ResourceDescriptor Yaml config will look like:

        ::

            resources:
            - type: 'logging.googleapis.com/LogEntry'
              name_descriptor:
                - pattern: "projects/{project}/logs/{log}"
                  parent_type: "cloudresourcemanager.googleapis.com/Project"
                  parent_name_extractor: "projects/{project}"
                - pattern: "folders/{folder}/logs/{log}"
                  parent_type: "cloudresourcemanager.googleapis.com/Folder"
                  parent_name_extractor: "folders/{folder}"
                - pattern: "organizations/{organization}/logs/{log}"
                  parent_type: "cloudresourcemanager.googleapis.com/Organization"
                  parent_name_extractor: "organizations/{organization}"
                - pattern: "billingAccounts/{billing_account}/logs/{log}"
                  parent_type: "billing.googleapis.com/BillingAccount"
                  parent_name_extractor: "billingAccounts/{billing_account}"

        For flexible resources, the resource name doesn't contain parent names,
        but the resource itself has parents for policy evaluation.

        Example:

        ::

            message Shelf {
              option (google.api.resource) = {
                type: "library.googleapis.com/Shelf"
                name_descriptor: {
                  pattern: "shelves/{shelf}"
                  parent_type: "cloudresourcemanager.googleapis.com/Project"
                }
                name_descriptor: {
                  pattern: "shelves/{shelf}"
                  parent_type: "cloudresourcemanager.googleapis.com/Folder"
                }
              };
            }

        The ResourceDescriptor Yaml config will look like:

        ::

            resources:
            - type: 'library.googleapis.com/Shelf'
              name_descriptor:
                - pattern: "shelves/{shelf}"
                  parent_type: "cloudresourcemanager.googleapis.com/Project"
                - pattern: "shelves/{shelf}"
                  parent_type: "cloudresourcemanager.googleapis.com/Folder"

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["auto_ml_stub"].ExportData

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
    def create_model(self):
        """Return the gRPC stub for :meth:`AutoMlClient.create_model`.

        The status code, which should be an enum value of
        ``google.rpc.Code``.

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
    def update_model(self):
        """Return the gRPC stub for :meth:`AutoMlClient.update_model`.

        Updates a model.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["auto_ml_stub"].UpdateModel

    @property
    def deploy_model(self):
        """Return the gRPC stub for :meth:`AutoMlClient.deploy_model`.

        Input and output type names. These are resolved in the same way as
        FieldDescriptorProto.type_name, but must refer to a message type.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["auto_ml_stub"].DeployModel

    @property
    def undeploy_model(self):
        """Return the gRPC stub for :meth:`AutoMlClient.undeploy_model`.

        javalite_serializable

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["auto_ml_stub"].UndeployModel

    @property
    def export_model(self):
        """Return the gRPC stub for :meth:`AutoMlClient.export_model`.

        Request message for ``AutoMl.ExportModel``. Models need to be
        enabled for exporting, otherwise an error code will be returned.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["auto_ml_stub"].ExportModel

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
