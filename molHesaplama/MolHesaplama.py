import sys
from PyQt5 import QtWidgets,QtGui



app=QtWidgets.QApplication(sys.argv)
win=QtWidgets.QWidget()
win.setWindowTitle("Mol Hesaplama")
win.setWindowIcon(QtGui.QIcon("icon.ico"))
win.setGeometry(600,200,512,512)
win.setMaximumSize(512,512)
win.setMinimumSize(512,512)

wallpaper=QtWidgets.QLabel(win)
wallpaper.setPixmap(QtGui.QPixmap("wallpaper.jpg"))

lbl_gram=QtWidgets.QLabel(win)
lbl_gram.setText('<font color="green" size="5">Kütlesi(g): </font>')
lbl_gram.move(20,50)

input_gram=QtWidgets.QLineEdit(win)
input_gram.move(120,50)

lbl_element=QtWidgets.QLabel(win)
lbl_element.setText('<font color="green" size="5">Element sembolü: </font>')
lbl_element.move(20,150)

input_element=QtWidgets.QLineEdit(win)
input_element.move(185,150)

buton=QtWidgets.QPushButton(win)
buton.setText("Hesapla")
buton.move(180,220)

result=QtWidgets.QLabel(win)
result.setText('<font color="red" size="5">Sonuç: </font>')
result.move(20,315)
result.resize(500,32)

name=QtWidgets.QLabel(win)
name.setText('<font color="brown" size="4">Made by Mete Başoluk </font>')
name.move(10,480)


def hesaplama():
    with open("mass.csv","r") as file:
        elementler=[]
        for i in file:
            i=i.split(",")
            elementler.append(i[0].upper())
        file.seek(0)
        for i in file:
            i=i.split(",")

            if i[0].upper()==str(input_element.text()).upper():
                try:
                    a = i[1].rstrip("\n")
                    b=str(float(input_gram.text())/float(a)).split(".")
                    result.setText(f'<font color="red" size="5">Sonuç: {b[0]+","+b[1]} mol</font>')
                except:
                    result.setText(f'<font color="red" size="5">Kütleyi düzgün gir.</font>')

            elif not str(input_element.text()).upper() in elementler:
                result.setText(f'<font color="red" size="5">Element sembolünü düzgün gir.</font>')



buton.clicked.connect(hesaplama)

win.show()
sys.exit(app.exec_())



