#підкл. модулі
import requests
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from  PyQt5.QtGui import QPixmap


app = QApplication([])
win_card = QWidget()
win_card.setWindowTitle('Weather forecast') 
win_card.resize(700, 700)

app.setStyleSheet("""
        QWidget {
            background: #fcfc8b;
            border-radius: 11px;    

        }
        
        QPushButton{
            background: #03dbfc;
            color: #ffffff;
            border-radius: 11px;
            min-width: 6em;    
            min-height: 2em;
            font-family: Arial;
            font: bold 18px;      
        }
        
        QLineEdit{
            background-color: ;
            max-width: 20em;
            max-height: 7em;
            font-family: Arial;
            font: bold 18px;
            border-color: beige;
            color:#ff0505;
            
        }

"""
)


oneEdit = QLineEdit()
oneEdit.setPlaceholderText("Input your city or  town")

twoEdit = QLineEdit()
twoEdit.setReadOnly(True) 

threeEdit = QLineEdit()
threeEdit.setReadOnly(True) 

fourEdit = QLineEdit()
fourEdit.setReadOnly(True) 

fiveEdit = QLineEdit()
fiveEdit.setReadOnly(True) 

sixEdit = QLineEdit()
sixEdit.setReadOnly(True) 

sevenEdit = QLineEdit()
sevenEdit.setReadOnly(True) 

eightEdit = QLineEdit()
eightEdit.setReadOnly(True) 

nineEdit = QLineEdit()
nineEdit.setReadOnly(True) 

tenEdit = QLineEdit()
tenEdit.setReadOnly(True) 

weatherButton = QPushButton("Find out weather")

oneV = QVBoxLayout()

im = QPixmap("D:\\Projects\\maze\\2275.png")
label = QLabel()
label.setPixmap(im)
oneV.addWidget(label)
oneV.addWidget(oneEdit)
oneV.addWidget(twoEdit)
oneV.addWidget(threeEdit)
oneV.addWidget(fourEdit)
oneV.addWidget(fiveEdit)
oneV.addWidget(sixEdit)
oneV.addWidget(sevenEdit)
oneV.addWidget(eightEdit)
oneV.addWidget(nineEdit)
oneV.addWidget(tenEdit)
oneV.addWidget(weatherButton)
API = 'f81703c1f3b81ad93e6644153c4a426e'
#url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API}'
def weather():
    city = oneEdit.text()
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        likefeel = data["main"]["feels_like"]
        pressure = data["main"]["pressure"]
        humidity = data["main"]["humidity"]
        temp_min = data["main"]["temp_min"]
        sealevel = data["main"]["sea_level"]
        temp_max = data["main"]["temp_max"]
        windspeed = data["wind"]["speed"]
        clouds = data["clouds"]["all"]

        pon1 = "Temperature:"+" "+ str(temp)+" "+"К"
        pon2 = "Like feel temperature:"+" "+ str(likefeel)+" "+"К"
        pon3 = "Pressure:"+" "+ str(pressure)+" "+"millimeters of mercury"
        pon4 = "Humidity:"+" "+ str(humidity)+" "+"%"
        pon5 = "Min. temperature:"+" "+ str(temp_min)+" "+"К"
        pon6 = "Max. temperature:"+" "+ str(temp_max)+" "+"К"
        pon7 = "Sea level:"+" "+ str(sealevel)+" "+"m"
        pon8 = "Wind speed:"+" "+ str(windspeed)+" "+"m/s"
        pon9 = "Clouds:"+" "+ str(clouds)+" "+"%"

        twoEdit.setText(str(pon1))
        threeEdit.setText(str(pon2))
        fourEdit.setText(str(pon3))
        fiveEdit.setText(str(pon4))
        sixEdit.setText(str(pon5))
        sevenEdit.setText(str(pon6))
        eightEdit.setText(str(pon7))
        nineEdit.setText(str(pon8))
        tenEdit.setText(str(pon9))        
    else:
        print('помилка')


weatherButton.clicked.connect(weather)
win_card.setLayout(oneV)
win_card.show()
app.exec_()
