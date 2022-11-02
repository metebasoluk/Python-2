import sys
from PyQt5 import QtWidgets,QtGui
import requests
import bs4



class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.resize(550, 550)
        self.setWindowTitle("Haber Bildirim Uygulaması")
        self.setWindowIcon(QtGui.QIcon("sabah.ico"))
        self.appName=QtWidgets.QLabel('<font color="brown" size="4">Haber Uygulaması</font>')
        hbox1 = QtWidgets.QHBoxLayout()
        hbox1.addStretch()
        hbox1.addWidget(self.appName)
        hbox1.addStretch()
        self.gundem=QtWidgets.QRadioButton("Gündem")
        self.yaşam=QtWidgets.QRadioButton("Yaşam")
        self.ekonomi=QtWidgets.QRadioButton("Ekonomi")
        self.dünya=QtWidgets.QRadioButton("Dünya")
        self.ara=QtWidgets.QPushButton("Ara")
        hbox2=QtWidgets.QHBoxLayout()
        hbox2.addStretch()
        hbox2.addWidget(self.ara)
        hbox2.addStretch()
        self.textedit=QtWidgets.QTextEdit()
        self.textedit.setReadOnly(True)
        # self.textedit.setDisabled(True)
        self.habericerigi=QtWidgets.QLabel('<font color="brown" size="4">Görüntülenmesini İstediğiniz Haber Kategorisini İşaretleyin</font>')
        v_box=QtWidgets.QVBoxLayout()
        v_box.addLayout(hbox1)
        v_box.addWidget(self.textedit)
        v_box.addWidget(self.habericerigi)
        v_box.addWidget(self.ekonomi)
        v_box.addWidget(self.gundem)
        v_box.addWidget(self.yaşam)
        v_box.addWidget(self.dünya)
        v_box.addLayout(hbox2)
        self.setLayout(v_box)
        self.ara.clicked.connect(self.funch)
        self.show()
    def işlemler(self,parametre):
        x = 1
        url = f"https://www.sabah.com.tr/son-dakika-haberleri/{parametre}/{x}"
        içerik = requests.get(url).content
        bs = bs4.BeautifulSoup(içerik,"html.parser")
        all_news = bs.find_all("div", {"class": "galleryItem"})
        liste = []
        date = all_news[0].find("span", {"class": "date"}).text
        news = all_news[0].find("span", {"class": "heading"}).text
        time = all_news[0].find("span", {"class": "time"}).text
        liste.append(([time, date, news]))
        for i in all_news:
            date = i.find("span", {"class": "date"}).text
            news = i.find("span", {"class": "heading"}).text
            time = i.find("span", {"class": "time"}).text
            if date == liste[0][1]:
                liste.append(([time, date, news]))
        liste.pop(0)
        while True:
            try:
                x += 1
                url = f"https://www.sabah.com.tr/son-dakika-haberleri/{parametre}/{x}"
                içerik = requests.get(url).content
                bs = bs4.BeautifulSoup(içerik, "html.parser")
                all_news = bs.find_all("div", {"class": "galleryItem"})
                for i in all_news:
                    date = i.find("span", {"class": "date"}).text
                    news = i.find("span", {"class": "heading"}).text
                    time = i.find("span", {"class": "time"}).text
                    if date == liste[0][1]:
                        liste.append(([time, date,news]))
                    else:
                        break
                if date != liste[0][1]:
                    break
            except:
                break
        string = ""
        for time, date, news in liste:
            string = string + (f"{time} {date} {news}\n\n")
        self.textedit.setText(f"BUGÜNÜN SAATLERE GÖRE GÜNCEL {parametre.upper()} HABERLERİ\n\n{string}")
    def funch(self):
        if self.gundem.isChecked()==True:
            self.işlemler("gundem")
        elif self.dünya.isChecked()==True:
            self.işlemler("dunya")
        elif self.yaşam.isChecked()==True:
            self.işlemler("yasam")
        elif self.ekonomi.isChecked()==True:
            self.işlemler("ekonomi")





app = QtWidgets.QApplication(sys.argv)
menu = App()
sys.exit(app.exec_())


