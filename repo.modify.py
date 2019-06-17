#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
from xml.etree.ElementTree import ElementTree,Element

def if_match(node, kv_map):
    for key in kv_map:
        if node.get(key) != kv_map.get(key):
            return False
    return True

def create_node(tag, property_map, content):
    element = Element(tag, property_map)
    element.text = content
    return element

if __name__ == "__main__":
    print sys.argv[1]
    tree = ElementTree()
    tree.parse(sys.argv[1])
    projects = tree.findall('project')
    hasXiaomi = False
    for node in projects:
        if if_match(node, {'name':'TheMuppets/proprietary_vendor_xiaomi'}):
            hasXiaomi = True
            print 'hasXiaomi'
            break
    
    if not hasXiaomi:
        tree.getroot().append(create_node('project',{'name':'TheMuppets/proprietary_vendor_xiaomi','path':'vendor/xiaomi','remote':'github'}, ''))

    tree.write(sys.argv[1], encoding='utf-8', xml_declaration=True)
