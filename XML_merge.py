# -*- coding: utf-8 -*-
"""
Created on Fri Aug  8 17:28:37 2025

@author: suksi
"""

import xml.etree.ElementTree as ET

def merge_xml_files(file1, file2, output_file):
    # Parse both XML files
    tree1 = ET.parse(file1)
    root1 = tree1.getroot()

    tree2 = ET.parse(file2)
    root2 = tree2.getroot()

    # Create a new root element for the merged file
    merged_root = ET.Element('MergedRoot')

    # Append children of first root
    for child in root1:
        merged_root.append(child)

    # Append children of second root
    for child in root2:
        merged_root.append(child)

    # Create a new tree with merged root and write to output file
    merged_tree = ET.ElementTree(merged_root)
    merged_tree.write(output_file, encoding='utf-8', xml_declaration=True)

if __name__ == "__main__":
    merge_xml_files('input1.xml', 'input2.xml', 'merged_output.xml')
