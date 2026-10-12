#!/usr/bin/env python3
"""Module: Serialization."""

import csv
import json


def convert_csv_to_json(filename=''):
    try:
        with open(filename, 'r') as f:
            data = list(csv.DictReader(f))

        with open('data.json', 'w') as file:
            json.dump(data, file, indent=4)

        return True
    except Exception:
        return False
