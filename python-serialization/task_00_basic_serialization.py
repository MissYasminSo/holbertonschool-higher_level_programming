#!/usr/bin/env python3
"""Module: Serialization."""

import json


def serialize_and_save_to_file(data, filename):
    """Serialize file"""

    with open(filename, "w") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Deserialize file"""

    with open(filename,) as f:
        return json.load(f)
