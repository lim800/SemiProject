#!/usr/bin/env python
# coding: utf-8

# In[1]:

import sys
import os

PATH = os.path.dirname(os.path.abspath("C:\\Users\\pmcsp\\eclipse-workspace\\Final"))
sys.path.insert(0, PATH)



from PIL import Image
from PIL.ExifTags import TAGS
from PIL.ExifTags import GPSTAGS
from geopy.geocoders import Nominatim

# import image function
def get_exif(filename):
    image = Image.open(filename)
    image.verify()
    return image.getexif()

# get metadata function
def get_metadata(exif):
    if not exif:
        raise ValueError("No EXIF metadata found")
    metadata = {}
    
    # info for AM or PM
    for tag_id in exif:
        tag = TAGS.get(tag_id, tag_id)
        data = exif.get(tag_id)

        if tag == "DateTimeOriginal" :
            time_str = data.split(' ')[1]
            if int(time_str[0:2]) >=12:
                metadata["Time"] = 'PM'
            else:
                metadata["Time"] = 'AM'
                
    # info for GPS
    dms = {}
    geo = {}
    for (idx, tag) in TAGS.items():
        if tag == 'GPSInfo':
            if idx not in exif:
                raise ValueError("No EXIF GeoInfo found")
            
            for (key, val) in GPSTAGS.items():
                if key in exif[idx]:
                    dms[val] = exif[idx][key]
    
    for (key, val) in {'GPSLatitude':'GPSLatitudeRef','GPSLongitude':'GPSLongitudeRef'}.items():
        degrees = dms[key][0][0] / dms[key][0][1]
        minutes = dms[key][1][0] / dms[key][1][1] / 60.0
        seconds = dms[key][2][0] / dms[key][2][1] / 3600.0
        if dms[val] in ['S', 'W']:
            degrees = -degrees
            minutes = -minutes
            seconds = -seconds
        geo[key] = round(degrees + minutes + seconds, 5)

    coords = (geo['GPSLatitude'], geo['GPSLongitude'])
    geocoder = Nominatim(user_agent="aaa")
    location = geocoder.reverse(coords)
    metadata['Location'] = location.address.split(', ')[-3]
    
    return metadata

exif = get_exif('C:\\Users\\pmcsp\\eclipse-workspace\\Final\\IMG_9574.jpg') # location of picture file to be loaded
meta_list = get_metadata(exif)

# export as text file
text_file = open("C:\\Users\\pmcsp\\eclipse-workspace\\FinalOutput.txt", "w") # location for saving a text file
text_file.write("{}_{}".format(meta_list['Location'], meta_list['Time']))
text_file.close()


# In[5]:





# In[ ]:




