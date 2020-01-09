# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


def import_dataset(project_id, dataset_id, path):
    """Import a dataset."""
    # [START automl_import_data]
    from google.cloud import automl

    # TODO(developer): Uncomment and set the following variables
    # project_id = "YOUR_PROJECT_ID"
    # dataset_id = "YOUR_DATASET_ID"
    # path = "gs://YOUR_BUCKET_ID/path/to/data.csv"

    client = automl.AutoMlClient()
    # Get the full path of the dataset.
    dataset_full_id = client.dataset_path(
        project_id, "us-central1", dataset_id
    )
    # Get the multiple Google Cloud Storage URIs
    input_uris = path.split(",")
    gcs_source = automl.types.GcsSource(input_uris=input_uris)
    input_config = automl.types.InputConfig(gcs_source=gcs_source)
    # Import data from the input URI
    response = client.import_data(dataset_full_id, input_config)

    print("Processing import...")
    print("Data imported. {}".format(response.result()))
    # [END automl_import_data]
