import tkinter as tk
from tkinter import font
import requests
from PIL import Image, ImageTk

def format_response(weather):
    try:
        name = weather['name']
        country = weather['sys']['country']
        description = weather['weather'][0]['description']
        temp = weather['main']['temp']
        humidity = weather['main']['humidity']
        mintemp = weather['main']['temp_min']
        maxtemp = weather['main']['temp_max']
        final_str = 'City: %s \nCountry: %s \nConditions: %s \nTemperature (°C): %s °C\nMinimum Temperature (°C): %s °C\nMax Temperature (°C): %s °C' %(name, country, description, temp, mintemp, maxtemp)
    except:
        final_str = 'There was some problem in retrieving the information'
    return final_str


def func(city):
    weather_key= '21cae77cd17a81570ed11723077c4954'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPId':weather_key, 'q':city, 'units':'Metric'}
    response = requests.get(url, params=params)
    weather = response.json()
    label['text']= format_response(weather)
    icon_name = weather['weather'][0]['icon']
    open_image(icon_name)

def open_image(icon):
    size = int(lframe.winfo_height()*0.35)
    img = ImageTk.PhotoImage(Image.open('./img/'+icon+'.png').resize((size, size)))
    weather_icon.delete("all")
    weather_icon.create_image(0,0, anchor='nw', image=img)
    weather_icon.image = img


 

root = tk.Tk()
canvas=tk.Canvas(root, height=500, width=800, bg='white')
canvas.pack()
backimg=tk.PhotoImage(file='nature.png')
backlabel=tk.Label(root, image=backimg)
backlabel.place(relwidth=1, relheight=1)

#21cae77cd17a81570ed11723077c4954
# api.openweathermap.org/data/2.5/weather?q={city name}


frame=tk.Frame(root, bg='blue', bd=4)
frame.place(relheight=0.1, relwidth=0.75, relx=0.5,rely=0.1,anchor='n')
entry = tk.Entry(frame, font=40,bg='white',fg='black')
entry.place(relwidth=0.65, relheight=1)

button=tk.Button(frame, text="Get Weather", font=40,bg='white',fg='black',command=lambda: func(entry.get()))
button.place(relx=0.7,relwidth=0.3, relheight=1)

lframe=tk.Frame(root, bg='purple', bd=10)
lframe.place(anchor='n', relx=0.5, rely=0.25, relheight=0.6, relwidth=0.75)


label=tk.Label(lframe, bg="white",font=('Noto Sans Canadian Aboriginal', 15), fg='black', anchor='nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)

weather_icon = tk.Canvas(label, bg='white', bd=0, highlightthickness=0)
weather_icon.place(relx=.75, rely=0, relwidth=1, relheight=0.5)
root.mainloop()
