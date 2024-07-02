# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.browse_images_button = QtWidgets.QPushButton(self.centralwidget)
        self.browse_images_button.setObjectName("browse_images_button")
        self.verticalLayout.addWidget(self.browse_images_button)
        self.image_folder_input = QtWidgets.QLineEdit(self.centralwidget)
        self.image_folder_input.setObjectName("image_folder_input")
        self.verticalLayout.addWidget(self.image_folder_input)
        self.output_video_button = QtWidgets.QPushButton(self.centralwidget)
        self.output_video_button.setObjectName("output_video_button")
        self.verticalLayout.addWidget(self.output_video_button)
        self.output_video_input = QtWidgets.QLineEdit(self.centralwidget)
        self.output_video_input.setObjectName("output_video_input")
        self.verticalLayout.addWidget(self.output_video_input)
        self.frame_rate_input = QtWidgets.QSpinBox(self.centralwidget)
        self.frame_rate_input.setMinimum(1)
        self.frame_rate_input.setMaximum(60)
        self.frame_rate_input.setProperty("value", 30)
        self.frame_rate_input.setObjectName("frame_rate_input")
        self.verticalLayout.addWidget(self.frame_rate_input)
        self.text_input = QtWidgets.QLineEdit(self.centralwidget)
        self.text_input.setObjectName("text_input")
        self.verticalLayout.addWidget(self.text_input)
        self.text_font_input = QtWidgets.QLineEdit(self.centralwidget)
        self.text_font_input.setObjectName("text_font_input")
        self.verticalLayout.addWidget(self.text_font_input)
        self.text_size_input = QtWidgets.QSpinBox(self.centralwidget)
        self.text_size_input.setMinimum(1)
        self.text_size_input.setMaximum(100)
        self.text_size_input.setProperty("value", 24)
        self.text_size_input.setObjectName("text_size_input")
        self.verticalLayout.addWidget(self.text_size_input)
        self.text_color_input = QtWidgets.QLineEdit(self.centralwidget)
        self.text_color_input.setObjectName("text_color_input")
        self.verticalLayout.addWidget(self.text_color_input)
        self.generate_video_button = QtWidgets.QPushButton(self.centralwidget)
        self.generate_video_button.setObjectName("generate_video_button")
        self.verticalLayout.addWidget(self.generate_video_button)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.browse_images_button.setText(_translate("MainWindow", "Browse Images"))
        self.output_video_button.setText(_translate("MainWindow", "Select Output Video"))
        self.generate_video_button.setText(_translate("MainWindow", "Generate Video"))
