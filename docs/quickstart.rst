Quickstart
==========

.. contents::
   :local:
   :depth: 1

Clone & Reopen
--------------

.. code-block:: bash

   git clone https://github.com/michdo/python-starter-template.git
   cd python-starter-template

.. note::

   You can also use this repo as a GitHub Template: click **Use this template**.

Open in VSCode
--------------

1. Install Docker & VSCode Dev Containers extension.
2. Menu → **Dev Containers: Reopen in Container**.
3. Wait for container build to finish.

First Run
---------

.. code-block:: bash

   uv pip install --group dev
   pytest
   sphinx-build -b html docs/ public/
