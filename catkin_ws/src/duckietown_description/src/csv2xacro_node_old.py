#!/usr/bin/env python
import rospy
import csv
from duckietown_description import Csv2Xacro
from xml.dom.minidom import Document

myobject = Csv2Xacro()

# Read csv file
csvfile = open('/home/amado/Downloads/duckietown_tiles_226.csv', 'rb')
map_csv = csv.reader(csvfile, delimiter=',')

# Open file to write on
map_xml = open("parsed_test_map.urdf.xacro", 'w')

# Create document
doc = Document()

# Create comment
comment = doc.createComment('WARNING: This file was auto-generated by csv2xacro_node.py. It should not be edited by hand.')
doc.appendChild(comment)

# Create root label
root = doc.createElement('robot')
root.setAttribute( 'name', 'duckietown' )
root.setAttribute('xmlns:xacro', 'http://www.ros.org/wiki/xacro')
doc.appendChild(root)

comment = doc.createComment('Parameters')
root.appendChild(comment)

# Create child
tempChild = doc.createElement('xacro:property')
tempChild.setAttribute('name','tile_width')
tempChild.setAttribute('value','0.595')
root.appendChild(tempChild)

tempChild = doc.createElement('xacro:property')
tempChild.setAttribute('name','pos_0')
tempChild.setAttribute('value','0.04 0')
root.appendChild(tempChild)

tempChild = doc.createElement('xacro:property')
tempChild.setAttribute('name','pos_1')
tempChild.setAttribute('value','0 0.04')
root.appendChild(tempChild)

tempChild = doc.createElement('xacro:property')
tempChild.setAttribute('name','pos_2')
tempChild.setAttribute('value','-0.04 0')
root.appendChild(tempChild)

tempChild = doc.createElement('xacro:property')
tempChild.setAttribute('name','pos_3')
tempChild.setAttribute('value','0 -0.04')
root.appendChild(tempChild)

comment = doc.createComment('Include the tile and tag macros')
root.appendChild(comment)

tempChild = doc.createElement('xacro:include')
tempChild.setAttribute('filename','$(find duckietown_description)/urdf/macros.urdf.xacro')
root.appendChild(tempChild)

comment = doc.createComment('The world frame is at the lower left corner of duckietown')
root.appendChild(comment)

tempChild = doc.createElement('link')
tempChild.setAttribute('name','world')
root.appendChild(tempChild)

comment = doc.createComment('Describe the tiles')
root.appendChild(comment)

for row in map_csv:
    tempChild = doc.createElement('xacro:tile')
    tempChild.setAttribute('x',row[0].strip('" '))
    tempChild.setAttribute('y',row[1].strip('" '))
    tempChild.setAttribute('type',row[2].strip('" '))
    tempChild.setAttribute('rotation',row[3].strip('" '))
    root.appendChild(tempChild)

# Write to file
doc.writexml(map_xml,indent='    ',addindent='    ',newl='\n')
csvfile.close()
