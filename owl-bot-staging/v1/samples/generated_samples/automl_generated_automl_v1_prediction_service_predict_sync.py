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
# Snippet for Predict
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-automl


# [START automl_generated_automl_v1_PredictionService_Predict_sync]
from google.cloud import automl_v1


def sample_predict():
    # Create a client
    client = automl_v1.PredictionServiceClient()

    # Initialize request argument(s)
    payload = automl_v1.ExamplePayload()
    payload.image.image_bytes = b'image_bytes_blob'

    request = automl_v1.PredictRequest(
        name="name_value",
        payload=payload,
    )

    # Make the request
    response = client.predict(request=request)

    # Handle response
    print(response)

# [END automl_generated_automl_v1_PredictionService_Predict_sync]
