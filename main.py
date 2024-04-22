from tkinter import *
from PIL import ImageTk,Image
import requests
import json

root = Tk()
root.title("Weather")
root.iconbitmap('C:/Users/DELL/Downloads/mfclogo.ico')
root.geometry("930x400")

forecast = Label(root,text ="    Forecast",font ="calibri 15 bold",bg = "black",fg ="White",width =95,anchor=W)
forecast.grid(row = 0,column=0,columnspan=8,padx=0,pady=0,ipady=10)


#TO GET USER LOCATION
ip_address = requests.get("https://api.ipify.org").text
response = requests.get(f'http://ip-api.com/json/{ip_address}').json()
location =response['city']

#GETTING WEATHER DATA
api_request = requests.get("http://api.weatherapi.com/v1/current.json?key=963cdaf630cd4f4b82e164304242104&q=vellore&aqi=yes")
api = json.loads(api_request.content)
address =api["location"]["name"] +", "+api["location"]["region"]+", "+api["location"]["country"]
time_date= api["location"]["localtime"]
time = time_date[-5:]
date=time_date[8:10]+"-"+time_date[5:7]+"-"+time_date[:4]
temp = api["current"]["temp_c"]
cond= api["current"]["condition"]["text"]
wind= api["current"]["wind_kph"]
wind_direc =api["current"]["wind_dir"]
pressure =api["current"]["pressure_mb"]
humid =api["current"]["humidity"]
feelslike =api["current"]["feelslike_c"]
vis = api["current"]["vis_km"]

#HOME TAB designs
home = Label(root,text = address, font = "calibiri 14",bg ="#104E8B",fg="white",width =80,anchor =W)
home.grid(row=1,column=1,columnspan=15,padx=0,pady=0,ipady=13)
homeimg =ImageTk.PhotoImage(Image.open("C:/Users/DELL/Downloads/homelogo.png"))
homeicon = Label(root,image = homeimg,bg ="#104E8B")
homeicon.grid(row=1,column = 0,padx= 0,pady =0, ipadx =23,ipady=12)

#BODY DESIGN
current_weather =Label(root,text = "Current weather",font ="calibiri 12 bold",bg ="#3A5FCD",fg ="white",width =95,anchor=NW)
current_weather.grid(row=2,column=0,columnspan=10,rowspan=20,ipady=128)
if (int(time[:2])>12):
    time_ampm = str(int(time[:2])-12)+":"+time[3:]+" PM"
else:
    time_ampm =time+" AM"

time_label =Label(root,text =time_ampm, font ="calibiri 10",bg ="#3A5FCD",fg ="white",anchor=W)
time_label.grid(row =2,column =1)


#Getting the images

sunny = ImageTk.PhotoImage(Image.open('Sunny-.jpeg'))
partlycloudy =ImageTk.PhotoImage(Image.open("partlysunny.jpeg"))
night= ImageTk.PhotoImage(Image.open("night.jpeg"))
nightcloudy =ImageTk.PhotoImage(Image.open("nightpartlycloudy.jpeg"))
cloudy =ImageTk.PhotoImage(Image.open("cloudy.jpeg"))
raining =ImageTk.PhotoImage(Image.open("raining.jpeg"))
thunder =ImageTk.PhotoImage(Image.open("thunder.jpeg"))
snowing =ImageTk.PhotoImage(Image.open("snowing.jpeg"))
thunderstorm =ImageTk.PhotoImage(Image.open("thunderstorm.jpeg"))
windy =ImageTk.PhotoImage(Image.open("windy.jpeg"))

#putting these images
sunny_label =Label(root, image =sunny)
partlycloudy_label =Label(root,image = partlycloudy)
night_label =Label(root, image =night)
nightcloudy_label =Label(root, image =nightcloudy)
cloudy_label =Label(root, image =cloudy)
raining_label =Label(root, image =raining)
thunder_label =Label(root, image =thunder)
snowing_label =Label(root, image =snowing)
thunderstorm_label =Label(root, image =thunderstorm)
windy_label =Label(root, image =windy)

#putting the pic
if cond=='Clear':
    if int(time[:2])>6 and int(time[:2])<20:
        sunny_label.grid(row=4,column=1,rowspan=5)
    else:
        night_label.grid(row=4,column=1,rowspan=20)
elif cond == 'Rain':
    raining_label.grid(row=4,column=1,rowspan=5)
elif cond =='Partly cloudy':
        if int(time[:2])>6 and int(time[:2])<20:
            partlycloudy_label.grid(row=4,column=1,rowspan=5)
        else:
            nightcloudy_label.grid(row=4,column=1,rowspan=20)


temp_label =Label(root,text =str(int(temp))+"°C", font = "calibiri 50 bold",bg="#3A5FCD",fg ="white",anchor=W)
temp_label.grid(row = 4,column=2,ipadx=0,ipady=0,padx=0,pady=0)
cond_label = Label(root,text =cond,font = "calibiri 12 bold",bg="#3A5FCD",fg ="white",anchor=NW)
cond_label.grid(row= 5,column =2)
feelslike_label=Label(root,text="Feels Like "+str(feelslike)+"°C",font ="calibiri 12 bold",bg="#3A5FCD",fg ="white",anchor=E)
feelslike_label.grid(row= 6,column =2)

wind_label=Label(root,text ="  Wind\n  "+str(wind)+"km/h "+str(wind_direc),font ="calibri 13 italic",bg="#3A5FCD",fg ="white",anchor=W)
wind_label.grid(row=7,column=2,padx=0,pady=0,ipady=0)

humidity_label=Label(root,text ="  Humidity\n  "+str(humid)+"%",font ="calibri 13 italic",bg="#3A5FCD",fg ="white",anchor=W)
humidity_label.grid(row=7,column=3,padx=0,pady=0,ipady=0)

visibility_label=Label(root,text ="    Visibility\n    "+str(vis)+"Km",font ="calibri 13 italic",bg="#3A5FCD",fg ="white",anchor=W)
visibility_label.grid(row=7,column=4,padx=0,pady=0,ipady=0)

pressure_label=Label(root,text ="    Pressure\n    "+str(pressure)+"mb",font ="calibri 13 italic",bg="#3A5FCD",fg ="white",anchor=W)
pressure_label.grid(row=7,column=5,padx=0,pady=0,ipady=0)

root.mainloop()

