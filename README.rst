Python Client for Cloud AutoML API
==================================
|ga| |pypi| |versions| 

🔔 **AutoML API Python Client is now available in Vertex AI. Please visit** `Vertex SDK for Python`_ **for the new Python Vertex AI client.** Vertex AI is our next generation AI Platform, with many new features that are unavailable in the current platform. `Migrate your resources to Vertex AI`_ to get the latest machine learning features, simplify end-to-end journeys, and productionize models with MLOps.

The `Cloud AutoML API`_ is a suite of machine learning products that enables
developers with limited machine learning expertise to train high-quality models
specific to their business needs, by leveraging Google’s state-of-the-art
transfer learning, and Neural Architecture Search technology.

- `Client Library Documentation`_
- `Product Documentation`_

.. |ga| image:: https://img.shields.io/badge/support-ga-gold.svg
   :target: https://github.com/googleapis/google-cloud-python/blob/main/README.rst#ga-support
.. |pypi| image:: https://img.shields.io/pypi/v/google-cloud-automl.svg
   :target: https://pypi.org/project/google-cloud-automl/
.. |versions| image:: https://img.shields.io/pypi/pyversions/google-cloud-automl.svg
   :target: https://pypi.org/project/google-cloud-automl/
.. _Vertex SDK for Python: https://github.com/googleapis/python-aiplatform
.. _Cloud AutoML API: https://cloud.google.com/automl
.. _Client Library Documentation: https://cloud.google.com/python/docs/reference/automl/latest
.. _Product Documentation:  https://cloud.google.com/automl
.. _Migrate your resources to Vertex AI: https://cloud.google.com/vertex-ai/docs/start/migrating-to-vertex-ai

Quick Start
-----------

In order to use this library, you first need to go through the following steps:

1. `Select or create a Cloud Platform project.`_
2. `Enable billing for your project.`_
3. `Enable the Cloud AutoML API.`_
4. `Setup Authentication.`_

.. _Select or create a Cloud Platform project.: https://console.cloud.google.com/project
.. _Enable billing for your project.: https://cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_a_project
.. _Enable the Cloud AutoML API.:  https://cloud.google.com/automl
.. _Setup Authentication.: https://googleapis.dev/python/google-api-core/latest/auth.html

Installation
~~~~~~~~~~~~

Install this library in a `virtualenv`_ using pip. `virtualenv`_ is a tool to
create isolated Python environments. The basic problem it addresses is one of
dependencies and versions, and indirectly permissions.

With `virtualenv`_, it's possible to install this library without needing system
install permissions, and without clashing with the installed system
dependencies.

.. _`virtualenv`: https://virtualenv.pypa.io/en/latest/


Supported Python Versions
^^^^^^^^^^^^^^^^^^^^^^^^^
Python >= 3.7

Unsupported Python Versions
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Python <= 3.6.

The last version of this library compatible with Python 2.7 is google-cloud-automl==1.0.1.
The last version of this library compatible with Python 3.6 is google-cloud-automl==2.7.3.


Mac/Linux
^^^^^^^^^

.. code-block:: console

    pip install virtualenv
    virtualenv <your-env>
    source <your-env>/bin/activate
    <your-env>/bin/pip install google-cloud-automl


Windows
^^^^^^^

.. code-block:: console

    pip install virtualenv
    virtualenv <your-env>
    <your-env>\Scripts\activate
    <your-env>\Scripts\pip.exe install google-cloud-automl


Next Steps
~~~~~~~~~~

-  Read the `Client Library Documentation`_ for Cloud AutoML API
   API to see other available methods on the client.
-  Read the `Product documentation`_ to learn
   more about the product and see How-to Guides.
