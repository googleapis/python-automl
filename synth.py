# Copyright 2018 Google LLC
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

"""This script is used to synthesize generated parts of this library."""

import re

import synthtool as s
from synthtool import gcp
from synthtool.languages import python

gapic = gcp.GAPICBazel()
common = gcp.CommonTemplates()
versions = ["v1beta1", "v1"]


# ----------------------------------------------------------------------------
# Generate automl GAPIC layer
# ----------------------------------------------------------------------------
for version in versions:
    library = gapic.py_library(
        service="automl",
        version=version,
        bazel_target=f"//google/cloud/automl/{version}:automl-{version}-py",
        include_protos=True
    )


    s.move(library, excludes=["README.rst", "docs/index.rst", "setup.py"])

# Add TablesClient and GcsClient to v1beta1
s.replace(
f"google/cloud/automl_v1beta1/__init__.py",
"""from \.services\.auto_ml import AutoMlClient
from \.services\.prediction_service import PredictionServiceClient""",
"""from .services.auto_ml import AutoMlClient
from .services.prediction_service import PredictionServiceClient
from .services.tables.gcs_client import GcsClient
from .services.tables.tables_client import TablesClient"""
)

s.replace(
    f"google/cloud/automl_v1beta1/__init__.py",
    f"""__all__ = \(""",
    """__all__ = ("GcsClient", "TablesClient","""
)

s.replace(
    "docs/automl_v1beta1/services.rst",
    """(google\.cloud\.automl_v1beta1\.services\.prediction_service
    :members:
    :inherited-members:)""",
    """\g<1>\n.. automodule:: google.cloud.automl_v1beta1.services.tables	
    :members:	
    :inherited-members:"""
)

# ----------------------------------------------------------------------------
# Add templated files
# ----------------------------------------------------------------------------
templated_files = common.py_library(
    unit_cov_level=82, cov_level=83, samples=True, microgenerator=True
)

python.py_samples(skip_readmes=True)

s.move(templated_files)

# TODO(busunkim): Use latest sphinx after microgenerator transition
s.replace("noxfile.py", """['"]sphinx['"]""", '"sphinx<3.0.0"')
# TODO(busunkim): Remove after microgenerator transition.
# This is being added to AutoML because the proto comments are long and
# regex replaces are a brittle temporary solution. 
s.replace(
"noxfile.py", 
"""'-W',  # warnings as errors
\s+'-T',  \# show full traceback on exception""",
""""-T",  # show full traceback on exception""")


# install with extras (pandas, storage)
s.replace(
    "noxfile.py",
    """session\.install\(['"]-e['"], ['"]\.['"]\)""",
    """session.install("-e", ".[pandas,storage]")""",
)

s.shell.run(["nox", "-s", "blacken"], hide_output=False)
