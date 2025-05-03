Testing
=======

We use pytest with coverage:

.. code-block:: bash

   pytest --cov=src

Cache & config directories:

- `.pytest_cache/`
- Coverage reports in `htmlcov/`

Add new tests under `tests/`, mirroring your `src/` package layout.
