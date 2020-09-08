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


# [START automl_video_classification_list_datasets_beta]
# [START automl_video_object_tracking_list_datasets_beta]
from google.cloud import automl_v1beta1 as automl


def list_datasets(project_id="YOUR_PROJECT_ID"):
    """List datasets."""
    client = automl.AutoMlClient()
    # A resource that represents Google Cloud Platform location.
    project_location = client.location_path(project_id, "us-central1")

    # List all the datasets available in the region.
    response = client.list_datasets(project_location, "")

    print("List of datasets:")
    for dataset in response:
        print("Dataset name: {}".format(dataset.name))
        print("Dataset id: {}".format(dataset.name.split("/")[-1]))
        print("Dataset display name: {}".format(dataset.display_name))
        print("Dataset create time:")
        print("\tseconds: {}".format(dataset.create_time.seconds))
        print("\tnanos: {}".format(dataset.create_time.nanos))
        # [END automl_video_object_tracking_list_datasets_beta]

        print(
            "Video classification dataset metadata: {}".format(
                dataset.video_classification_dataset_metadata
            )
        )
        # [END automl_video_classification_list_datasets_beta]

        # [START automl_video_object_tracking_list_datasets_beta]
        print(
            "Video object tracking dataset metadata: {}".format(
                dataset.video_object_tracking_dataset_metadata
            )
        )
        # [END automl_video_object_tracking_list_datasets_beta]
