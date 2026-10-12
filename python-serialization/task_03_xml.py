#!/usr/bin/env python3
"""Module: Serialization."""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    elem = ET.Element("data")
    for key, val in dictionary.items():
        child = ET.Element(key)
        child.text = str(val)
        elem.append(child)

    xml = ET.ElementTree(elem)
    xml.write(filename)


def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    dict = {}

    for child in root:
        dict[child.tag] = child.text

    return dict
