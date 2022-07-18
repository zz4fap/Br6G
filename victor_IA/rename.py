import xml.etree.ElementTree as ET
import glob

path = 'train/*.xml'
index=1
for filename in glob.glob(path):
    tree = ET.parse(filename)
    root = tree.getroot()
    for files in tree.findall("filename"):
        files.text = f'image_{index}.jpg'
        tree.write(f'{filename}')
    index = index+1