# Based on the beautiful tutorial by John from Codemy.com (https://www.youtube.com/c/Codemycom)
# freeCodeCamp.org (2019) Tkinter Course - Create Graphic User Interfaces in Python Tutorial https://www.youtube.com/watch?v=YXPyB4XeYLA

# Connect to a third-party API
# https://docs.airnowapi.org/CurrentObservationsByZip/query

import os
import re
import time
import requests

from tkinter import *
from tkinter import messagebox

from PIL import ImageTk, Image
# decode from json into python
import json

os.chdir(".\\images\\")

root = Tk()
root.geometry("550x250")
root.title("Weather App")

sun = ".\\sun.png"
logo = PhotoImage(file=sun)
root.iconphoto(False, logo)

level1 = ".\\level1.png"
level2 = ".\\level2.png"
level3 = ".\\level3.png"
level4 = ".\\level4.png"
level5 = ".\\level5.png"
level6 = ".\\level6.png"
fail = ".\\fail.png"

img1 = Image.open(level1)
img1 = img1.resize((120, 120))
img1 = ImageTk.PhotoImage(img1)
img2 = Image.open(level2)
img2 = img2.resize((120, 120))
img2 = ImageTk.PhotoImage(img2)
img3 = Image.open(level3)
img3 = img3.resize((120, 120))
img3 = ImageTk.PhotoImage(img3)
img4 = Image.open(level4)
img4 = img4.resize((120, 120))
img4 = ImageTk.PhotoImage(img4)
img5 = Image.open(level5)
img5 = img5.resize((120, 120))
img5 = ImageTk.PhotoImage(img5)
img6 = Image.open(level6)
img6 = img6.resize((120, 120))
img6 = ImageTk.PhotoImage(img6)

img_fail = Image.open(fail)
img_fail = img_fail.resize((120, 120))
img_fail = ImageTk.PhotoImage(img_fail)

zipcode_label = Label(root, text="Zipcode: ")
zipcode_entry = Entry(root, width=30, borderwidth=1)

zipcode_label.grid(row=0, column=0, padx=20)
zipcode_entry.grid(row=0, column=1)

distance_label = Label(root, text="Distance: ")
distance_entry = Entry(root, width=30, borderwidth=1)

distance_label.grid(row=1, column=0, padx=20)
distance_entry.grid(row=1, column=1)

def get_air_quality():
    zipcode = zipcode_entry.get().strip()
    distance = distance_entry.get().strip()

    zipcode_pattern = "^[0-9]{5}$"

    # Input data integrity check
    if re.search(zipcode_pattern, zipcode) == None:
        warning_popup = messagebox.showerror("Zipcode error", "Please enter a correct zipcode.")
        return

    if distance == "":
        distance = 15

    print(zipcode, distance)

    url = f"https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={zipcode}&distance={distance}&API_KEY=152A7C68-0122-4920-9EB7-D7E8F2128AC7"
    print(url)

    try:
        start = time.perf_counter()

        api_request = requests.get(url)
        api = json.loads(api_request.content)  # parse json into pythonic
        print(api_request)

        date = api[0]['DateObserved']
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']
        latitude = api[0]['Latitude']
        longitude = api[0]['Longitude']
        print(date, city, quality, category, latitude, longitude, sep="\n")

        end = time.perf_counter() - start
        print('perf time: ', end)

        fontsize = 12
        padding = 43
        if category.lower() == "good":
            color_code = "green"
            status_image = img1
        elif category.lower() == "moderate":
            color_code = "#FFFF00"
            status_image = img2
        elif "sensitive" in category.lower():
            padding = 1
            color_code = "#FF7E00"
            status_image = img3
        elif category.lower() == "unhealthy":
            color_code = "#FF0000"
            status_image = img4
        elif category.lower() == "very unhealthy":
            color_code = "#8F3F97"
            status_image = img5
        elif category.lower() == "hazardous":
            fontsize = 15
            color_code = "#7E0023"
            status_image = img6
            category = "RUN for your life!"

        label1 = Label(root, text=f'Date: {date}', font=("Helvetica", 10))
        label2 = Label(root, text=f'City: {city}\nQuality: {quality}\nCategory: {category}',
                       font=("Helvetica", fontsize), background=color_code)
        label3 = Label(root, text=f'Lat/long: {latitude}, {longitude}', font=("Helvetica", 10))
        label_image = Label(root, image=status_image)

        label1.grid(row=3, column=0, columnspan=2)
        label2.grid(row=4, column=0, columnspan=2, ipadx=padding)
        label3.grid(row=5, column=0, columnspan=2, ipadx=15)
        label_image.grid(row=3, rowspan=3, column=2)

    except Exception as e:
        api = "Error occurred :("


button_check = Button(root, text="Check air quality", command=get_air_quality)
button_check.grid(row=2, column=1)

root.mainloop()
