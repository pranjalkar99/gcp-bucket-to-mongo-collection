# gcp-bucket-to-mongo-collection

[![Build Status](https://travis-ci.com/yourusername/your_project.svg?branch=main)](https://travis-ci.com/yourusername/your_project)
[![Documentation Status](https://readthedocs.org/projects/your_project/badge/?version=latest)](https://your_project.readthedocs.io/en/latest/?badge=latest)
[![codecov](https://codecov.io/gh/yourusername/your_project/branch/main/graph/badge.svg)](https://codecov.io/gh/yourusername/your_project)
[![Maintainability](https://api.codeclimate.com/v1/badges/your_project_id/maintainability)](https://codeclimate.com/github/yourusername/your_project/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/your_project_id/test_coverage)](https://codeclimate.com/github/yourusername/your_project/test_coverage)

**Description:** Briefly describe what your project does and its main features.

[![PyPI Version](https://img.shields.io/pypi/v/your_project_name)](https://pypi.org/project/your_project_name/)
[![Python Version](https://img.shields.io/pypi/pyversions/your_project_name)](https://pypi.org/project/your_project_name/)
[![License](https://img.shields.io/pypi/l/your_project_name)](https://github.com/yourusername/your_project/blob/main/LICENSE)

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

You can install this package using pip:

```shell
pip install gcp-bucket-to-mongo-collection
```

## Usage

Don't forget to download your credentials.json for authorising your service account into the gcp bucket.

You can use it like this:

```python
from gcp-bucket-to-mongo-collection import transfer_json_to_mongodb

# Usage example:
transfer_json_to_mongodb(bucket_name, gcs_credentials_path, mongo_uri, mongo_db_name, mongo_collection_name)
```

## License
I made this for my private project. It may or may not be useful.
