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
# Generated code. DO NOT EDIT!
#
# Snippet for BatchPredict
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-automl


# [START automl_generated_automl_v1_PredictionService_BatchPredict_async]
from google.cloud import automl_v1


async def sample_batch_predict():
    # Create a client
    client = automl_v1.PredictionServiceAsyncClient()

    # Initialize request argument(s)
    input_config = automl_v1.BatchPredictInputConfig()
    input_config.gcs_source.input_uris = ['input_uris_value_1', 'input_uris_value_2']

    output_config = automl_v1.BatchPredictOutputConfig()
    output_config.gcs_destination.output_uri_prefix = "output_uri_prefix_value"

    request = automl_v1.BatchPredictRequest(
        name="name_value",
        input_config=input_config,
        output_config=output_config,
    )

    # Make the request
    operation = client.batch_predict(request=request)

    print("Waiting for operation to complete...")

    response = await operation.result()
    print(response)

# [END automl_generated_automl_v1_PredictionService_BatchPredict_async]
