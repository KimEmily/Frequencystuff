'''
Created on 07.08.2018

@author: kimemily
'''
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(507, 800)
        Widget.setMinimumSize(QtCore.QSize(400, 800))
        Widget.setMaximumSize(QtCore.QSize(800, 1000))
        Widget.setToolTip("")
        Widget.setToolTipDuration(2)
        Widget.setStyleSheet("")
        
        self.Freq = QtWidgets.QLineEdit(Widget)
        self.Freq.setGeometry(QtCore.QRect(40, 70, 121, 21))
        self.Freq.setText("")
        self.Freq.setObjectName("Freq")
        
        self.lineEdit = QtWidgets.QLineEdit(Widget)
        self.lineEdit.setGeometry(QtCore.QRect(40, 130, 121, 21))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        
        self.Frequenztabelle = QtWidgets.QListView(Widget)
        self.Frequenztabelle.setGeometry(QtCore.QRect(20, 480, 401, 251))
        self.Frequenztabelle.setStyleSheet("")
        self.Frequenztabelle.setObjectName("Frequenztabelle")
        
        self.label = QtWidgets.QLabel(Widget)
        self.label.setGeometry(QtCore.QRect(20, 450, 241, 21))
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(Widget)
        self.label_2.setGeometry(QtCore.QRect(40, 50, 171, 16))
        self.label_2.setObjectName("label_2")
        
        self.label_3 = QtWidgets.QLabel(Widget)
        self.label_3.setGeometry(QtCore.QRect(40, 110, 231, 16))
        self.label_3.setObjectName("label_3")
        
        self.lineEdit_2 = QtWidgets.QLineEdit(Widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 190, 121, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        
        self.label_4 = QtWidgets.QLabel(Widget)
        self.label_4.setGeometry(QtCore.QRect(40, 170, 181, 16))
        self.label_4.setObjectName("label_4")
        
        self.pushButton_2 = QtWidgets.QPushButton(Widget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 750, 114, 32))
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.label_5 = QtWidgets.QLabel(Widget)
        self.label_5.setGeometry(QtCore.QRect(220, 100, 59, 16))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        
        self.lineEdit_3 = QtWidgets.QLineEdit(Widget)
        self.lineEdit_3.setGeometry(QtCore.QRect(40, 250, 121, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        
        self.label_6 = QtWidgets.QLabel(Widget)
        self.label_6.setGeometry(QtCore.QRect(40, 230, 141, 16))
        self.label_6.setObjectName("label_6")
        
        self.lineEdit_4 = QtWidgets.QLineEdit(Widget)
        self.lineEdit_4.setGeometry(QtCore.QRect(40, 310, 113, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        
        self.label_7 = QtWidgets.QLabel(Widget)
        self.label_7.setGeometry(QtCore.QRect(40, 290, 111, 20))
        self.label_7.setObjectName("label_7")
        
        self.pushButton = QtWidgets.QPushButton(Widget)
        self.pushButton.setGeometry(QtCore.QRect(40, 370, 114, 32))
        self.pushButton.setObjectName("pushButton")
        
        self.label_2.setBuddy(self.Freq)
        self.label_3.setBuddy(self.lineEdit)
        self.label_4.setBuddy(self.lineEdit_2)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Frequenzverhältnix"))
        self.Freq.setToolTip(_translate("Widget", "<html><head/><body><p>Eingabe von Referenzfrequenz <span style=\" font-weight:600;\">F1</span> (Default: 440)</p></body></html>"))
        self.Freq.setWhatsThis(_translate("Widget", "<html><head/><body><p>Freq</p></body></html>"))
        self.lineEdit.setToolTip(_translate("Widget", "<html><head/><body><p>Eingabe von Frequenzverhältnis <span style=\" font-weight:600;\">N </span>(Default: 2)</p></body></html>"))
        self.Frequenztabelle.setToolTip(_translate("Widget", "<html><head/><body><p>Hier wird Ihnen ihr Equal Step Tuning ausgegeben (<span style=\" font-weight:600;\">EDn = Equal Divisions per N</span>)</p></body></html>"))
        self.label.setToolTip(_translate("Widget", "<html><head/><body><p>Hier wird Ihnen ihr Equal Step Tuning ausgegeben (<span style=\" font-weight:600;\">EDn = Equal Divisions per N</span>)</p></body></html>"))
        self.label.setText(_translate("Widget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">Frequenzverhältnixtabelle</span></p></body></html>"))
        self.label_2.setToolTip(_translate("Widget", "<html><head/><body><p>Eingabe von Referenzfrequenz <span style=\" font-weight:600;\">F1</span> (Default: 440)</p></body></html>"))
        self.label_2.setText(_translate("Widget", "<html><head/><body><p>Frequenz </p></body></html>"))
        self.label_3.setToolTip(_translate("Widget", "<html><head/><body><p>Eingabe von Frequenzverhältnis <span style=\" font-weight:600;\">N </span>(Default: 2)</p></body></html>"))
        self.label_3.setText(_translate("Widget", "Frequenzverhältnis"))
        self.lineEdit_2.setToolTip(_translate("Widget", "<html><head/><body><p>Anzahl der Devisions im Frequenzverhältnis <span style=\" font-weight:600;\">D </span>(Default:12)</p></body></html>"))
        self.label_4.setToolTip(_translate("Widget", "<html><head/><body><p>Anzahl der Devisions im Frequenzverhältnis <span style=\" font-weight:600;\">D </span>(Default:12)</p></body></html>"))
        self.label_4.setText(_translate("Widget", "Divisions"))
        self.pushButton_2.setToolTip(_translate("Widget", "<html><head/><body><p>Open as Txt-Data</p></body></html>"))
        self.pushButton_2.setText(_translate("Widget", "open Text"))
        self.lineEdit_3.setToolTip(_translate("Widget", "<html><head/><body><p>ANzahl der Wiederholungen bei Output <span style=\" font-weight:600;\">W</span> (Default: 1)</p></body></html>"))
        self.label_6.setToolTip(_translate("Widget", "<html><head/><body><p>ANzahl der Wiederholungen bei Output <span style=\" font-weight:600;\">W</span> (Default: 1)</p></body></html>"))
        self.label_6.setText(_translate("Widget", "Wiederholungen"))
        self.lineEdit_4.setToolTip(_translate("Widget", "<html><head/><body><p>Kammerton für a\' für Entsprechungen in unserm 12-Ton-System bestimmen (Default: <span style=\" font-weight:600;\">12EDO</span>=440Hertz)</p></body></html>"))
        self.label_7.setToolTip(_translate("Widget", "<html><head/><body><p>Kammerton für a\' für Entsprechungen in unserm 12-Ton-System bestimmen (Default: <span style=\" font-weight:600;\">12EDO</span>=440Hertz)</p></body></html>"))
        self.label_7.setText(_translate("Widget", "Kammerton"))
        self.pushButton.setToolTip(_translate("Widget", "<html><head/><body><p>Hier Drücken für die Ausgabe</p></body></html>"))
        self.pushButton.setText(_translate("Widget", "Berechne"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())

