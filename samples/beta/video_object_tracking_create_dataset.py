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

# [START automl_video_object_tracking_create_dataset_beta]
from google.cloud import automl_v1beta1 as automl


def create_dataset(
    project_id="YOUR_PROJECT_ID", display_name="your_datasets_display_name"
):
    """Create a automl video object tracking dataset."""
    client = automl.AutoMlClient()

    # A resource that represents Google Cloud Platform location.
    project_location = client.location_path(project_id, "us-central1")
    metadata = automl.types.VideoObjectTrackingDatasetMetadata()
    dataset = automl.types.Dataset(
        display_name=display_name,
        video_object_tracking_dataset_metadata=metadata,
    )

    # Create a dataset with the dataset metadata in the region.
    created_dataset = client.create_dataset(project_location, dataset)
    # Display the dataset information
    print("Dataset name: {}".format(created_dataset.name))
    print("Dataset id: {}".format(created_dataset.name.split("/")[-1]))
# [END automl_video_object_tracking_create_dataset_beta]
