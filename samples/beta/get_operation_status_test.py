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

import os

from google.cloud import automl_v1beta1 as automl
import pytest

import get_operation_status

PROJECT_ID = os.environ["AUTOML_PROJECT_ID"]


@pytest.fixture(scope="function")
def operation_id():
    client = automl.AutoMlClient()
    project_location = client.location_path(PROJECT_ID, "us-central1")
    generator = client.transport._operations_client.list_operations(
        project_location, filter_=""
    ).pages
    page = next(generator)
    operation = page.next()
    yield operation.name


def test_get_operation_status(capsys, operation_id):
    get_operation_status.get_operation_status(operation_id)
    out, _ = capsys.readouterr()
    assert "Operation details" in out
