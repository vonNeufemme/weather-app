# Connect to a third-party API
# https://docs.airnowapi.org/CurrentObservationsByZip/query

import os
import re
import time
import datetime
import requests

from tkinter import *
from tkinter import messagebox

from PIL import ImageTk, Image
# decode from json into python
import json

os.chdir("IMAGE_DIR")

root = Tk()
root.geometry("550x250")
root.title("날씨 앱")

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

zipcode_label = Label(root, text="우편번호: ")
zipcode_entry = Entry(root, width=30, borderwidth=1)

zipcode_label.grid(row=0, column=0, padx=20)
zipcode_entry.grid(row=0, column=1)

distance_label = Label(root, text="반경(마일): ")
distance_entry = Entry(root, width=30, borderwidth=1)

distance_label.grid(row=1, column=0, padx=20)
distance_entry.grid(row=1, column=1)

def get_air_quality():

    date, city, quality, category, latitude, longitude, color_code, status_image = "", "", "", "", "", "", "", ""

    fontsize = 12
    font_settings = ("Helvetica", fontsize)
    font_color = 'black'
    padding = 43

    zipcode = zipcode_entry.get().strip()
    distance = distance_entry.get().strip()

    zipcode_pattern = "^[0-9]{5}$"

    if distance == "":
        distance = 15

    # Input data integrity check
    if re.search(zipcode_pattern, zipcode) == None:
        warning_popup = messagebox.showerror("우편번호 오류", "알맞은 우편번호를 입력하세요.")
        return
    elif zipcode == "00000":
        messagebox.showinfo("축하합니다", "비밀 운동코드를 깨셨군요!")

        date = datetime.datetime.now()
        city = 'Nowhere'
        quality = '999'
        category = 'BAD'
        latitude = 'Unknown'
        longitude = 'Unknown'

        font_settings = ("Helvetica", 15, 'bold')
        color_code = "#7E0023"
        font_color = 'white'
        status_image = img6
        category = "목숨이 아까우면 도망치세요!"

    else:
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

        except Exception as e:
            api = "Error occurred :("

        if category.lower() == "good":
            category = "좋음"
            color_code = "green"
            status_image = img1
        elif category.lower() == "moderate":
            category = "보통"
            color_code = "#FFFF00"
            status_image = img2
        elif "sensitive" in category.lower():
            padding = 1
            category = "민감한 사람에게 안 좋음"
            color_code = "#FF7E00"
            status_image = img3
        elif category.lower() == "unhealthy":
            category = "안 좋음"
            color_code = "#FF0000"
            status_image = img4
        elif category.lower() == "very unhealthy":
            category = "나쁨"
            color_code = "#8F3F97"
            status_image = img5
        elif category.lower() == "hazardous":
            font_settings = ("Helvetica", 15, 'bold')
            color_code = "#7E0023"
            font_color = 'white'
            status_image = img6
            category = "목숨이 아까우면 도망치세요!"

    label1 = Label(root, text=f'날짜: {date}', font=("Helvetica", 10))
    label2 = Label(root, text=f'도시: {city}\n대기질: {quality}\n분류: {category}',
                   font=font_settings, foreground=font_color, background=color_code)
    label3 = Label(root, text=f'위경도: {latitude}, {longitude}', font=("Helvetica", 10))
    label_image = Label(root, image=status_image)

    label1.grid(row=3, column=0, columnspan=2)
    label2.grid(row=4, column=0, columnspan=2, ipadx=padding)
    label3.grid(row=5, column=0, columnspan=2, ipadx=15)
    label_image.grid(row=3, rowspan=3, column=2)


button_check = Button(root, text="Check air quality", command=get_air_quality)
button_check.grid(row=2, column=1)

root.mainloop()
