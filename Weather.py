# Weather App - By Faizanscommunit
# Language = Python
# License = MIT
# Requires = YOUR-API-KEY

# Imports
from tkinter import *
from tkinter import font
import requests

# Setting up Tkinter Window
window = Tk()
window.title('Weather App | By Faizanscommunit')
window.iconbitmap("icon.ico")

# Variables
HEIGHT = 500
WIDTH = 600

# Components
canvas = Canvas(window, height=HEIGHT, width=WIDTH)
canvas.pack()
background_image = PhotoImage(file='landscape.png')
background_label = Label(window, image=background_image)
background_label.place(relwidth=1, relheight=1)
frame = Frame(window, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')
entry = Entry(frame, font=('Courier', 18))
entry.place(relheight=1, relwidth=0.65)
entry.focus()

# Functions


def format_response(weather):
    try:
        name = (weather['name'])
        description = (weather['weather'][0]['description'])
        temperature = (weather['main']['temp'])
        centigrade = ((temperature-32)*5/9)
        humidity = (weather['main']['humidity'])
        country = (weather['sys']['country'])
        label['text'] = 'City : '+str(name) + '\nConditions : '+str(description) + '\nFarenheit : ' + str(
            temperature)+'(°F)\nCentigrade : '+str(centigrade)+'(°C)\nCountry : '+str(country)+'\nHumidity : '+str(humidity)
    except:
        error = 'There was a problem retrieving\n that information '
        label['text'] = error


def get_weather(city):
    weather_key = 'YOUR-API-KEY'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params=params)
    weather = response.json()
    label['text'] = format_response(weather)


button = Button(frame, text='Get Weather', bg='grey',
                command=lambda: get_weather(entry.get()), fg='white', font=40)
button.place(relx=0.7, relheight=1, relwidth=0.3)
lower_frame = Frame(window, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75,
                  relheight=0.6, anchor='n')
label = Label(lower_frame, font=('Courier', 18),
              anchor='nw', bd=4,  justify='left')
label.place(relwidth=1, relheight=1)

window.mainloop()
