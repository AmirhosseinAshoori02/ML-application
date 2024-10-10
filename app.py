import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QMessageBox, QLabel, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import pandas as pd
import numpy as np
from model_load import loadmodel

class SecondaryWindow(QWidget):
    def __init__(self,title,width,height,message=None,image_path1=None,image_path2=None):
        super().__init__()
        self.title = title
        self.width = width
        self.height = height
        self.message = message
        self.image_path1 = image_path1
        self.image_path2 = image_path2
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(100,100,self.width,self.height)
        layout = QVBoxLayout()
        
        if self.message:
            label = QLabel(self.message,self)
            label.setStyleSheet("font-family: Times New Roman; font-size: 16pt;")
            layout.addWidget(label)
        
        if self.image_path1 or self.image_path2:
            image_layout = QHBoxLayout()
            if self.image_path1:
                label1 = QLabel(self)
                pixmap1 = QPixmap(self.image_path1)
                label1.setPixmap(pixmap1)
                label1.setScaledContents(True)
                label1.setFixedSize(750,650)  # Set fixed size for the image
                image_layout.addWidget(label1)
            if self.image_path2:
                label2 = QLabel(self)
                pixmap2 = QPixmap(self.image_path2)
                label2.setPixmap(pixmap2)
                label2.setScaledContents(True)
                label2.setFixedSize(750,650)  # Set fixed size for the image
                image_layout.addWidget(label2)
            layout.addLayout(image_layout)
        
        self.setLayout(layout)
        self.show()


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'IBM company'
        self.left = 100
        self.top = 100
        self.width = 800
        self.height = 600
        self.initUI()
        self.data_loaded = False
        self.data = None
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setFixedSize(self.width, self.height)
        self.setGeometry(self.left,self.top,self.width,self.height)
        # Create a QLabel to set the background image
        self.background_label = QLabel(self)
        self.background_label.setGeometry(0,0,self.width,self.height)
        pixmap = QPixmap('CustomerRetention.jpg')
        self.background_label.setPixmap(pixmap)
        self.background_label.setScaledContents(True)


        # Create a vertical layout
        layout = QVBoxLayout()

        # Create a button with a background image
        self.start = QPushButton('Click for more information',self)
        self.start.clicked.connect(self.show_explanation)
        self.start.setToolTip('Click to see more information')
        self.start.setFixedSize(160,75)
        layout.addWidget(self.start)

        # Add upload button
        self.upload_button = QPushButton('Upload CSV',self)
        self.upload_button.clicked.connect(self.upload_csv)
        self.upload_button.setFixedSize(140,60)
        self.upload_button.move(200,-50)
        layout.addWidget(self.upload_button)

        # Define the buttons
        self.button_svm = QPushButton('SVM method',self)
        self.button_decisiontree = QPushButton('Decision tree method',self)
        self.button_neuralnetwork = QPushButton('Nueral network method',self)
        self.button_knn = QPushButton('KNN method',self)
        self.button_randomforest = QPushButton('Random forest method',self)
        self.button_predict = QPushButton("Predict data",self)

        # Set the size of the buttons
        self.button_svm.setFixedSize(140,60)
        self.button_decisiontree.setFixedSize(140,60)
        self.button_neuralnetwork.setFixedSize(140,60)
        self.button_knn.setFixedSize(140,60)
        self.button_randomforest.setFixedSize(140,60)
        self.button_predict.setFixedSize(140,60)

        # Change button colors
        self.start.setStyleSheet("background-color: cyan; color: black;")
        self.upload_button.setStyleSheet("background-color: gold; color: black;")
        self.button_svm.setStyleSheet("background-color: lightyellow; color: black;")
        self.button_decisiontree.setStyleSheet("background-color: lightyellow; color: black;")
        self.button_neuralnetwork.setStyleSheet("background-color: lightyellow; color: black;")
        self.button_knn.setStyleSheet("background-color: lightyellow; color: black;")
        self.button_randomforest.setStyleSheet("background-color: lightyellow; color: black;")
        self.button_predict.setStyleSheet("background-color: gold; color: black;")

        # Add buttons to the layout
        layout.addWidget(self.button_svm)
        layout.addWidget(self.button_decisiontree)
        layout.addWidget(self.button_neuralnetwork)
        layout.addWidget(self.button_knn)
        layout.addWidget(self.button_randomforest)
        layout.addWidget(self.button_predict)

        # Connect buttons to their corresponding methods
        self.button_svm.clicked.connect(self.show_result1)
        self.button_decisiontree.clicked.connect(self.show_result2)
        self.button_neuralnetwork.clicked.connect(self.show_result3)
        self.button_knn.clicked.connect(self.show_result4)
        self.button_randomforest.clicked.connect(self.show_result5)
        self.button_predict.clicked.connect(self.predict)

        # Set the layout for the window
        self.setLayout(layout)

        self.show()
    
    def show_explanation(self):
        QMessageBox.information(self,'Instruction','Welcome to IBM application. You can see the accuracy of each method by using the buttons and see the required plots for your Data frame. You can predict your data using Upload button and see the predicted result as CSV file by Predict button.') 

    def show_result1(self):
        if self.data_loaded:
            self.open_secondary_window('SVM Result',300,300,'Accuracy in SVM method is equal to 0.7')
        else:
            QMessageBox.warning(self,'Warning','Please upload a CSV file first.')

    def show_result2(self):
        if self.data_loaded:
            self.open_secondary_window_with_images('Decision Tree Result',1000,850,"Accuracy in decision tree with Adaboost method is equal to 0.75", 'Decision_tree.png', 'feature_importance_decision_tree.png')        
        else:
            QMessageBox.warning(self,'Warning','Please upload a CSV file first.')

    def show_result3(self):
        if self.data_loaded:
            self.open_secondary_window_with_text_and_image('Neural Network Result',800,750,"Accuracy in neural network method is equal to: 0.74",'neural_network_structure.png')
        else:
            QMessageBox.warning(self,'Warning','Please upload a CSV file first.')

    def show_result4(self):
        if self.data_loaded:
            self.open_secondary_window('KNN Result',300,300,'Accuracy in KNN method is equal to 0.72')
        else:
            QMessageBox.warning(self,'Warning','Please upload a CSV file first.')

    def show_result5(self):
        if self.data_loaded:
            self.open_secondary_window_with_images('Random Forest Result',1000,700,"Accuracy in random forest method is equal to: 0.76",'random_forest.png','feature_importance_random_forest.png')        
        else:
            QMessageBox.warning(self,'Warning','Please upload a CSV file first.')
            
    def open_secondary_window(self,title,width,height,message):
        self.secondary_window = SecondaryWindow(title,width,height,message)
    
    def open_secondary_window_with_text_and_image(self,title,width,height,message,image_path):
        self.secondary_window = SecondaryWindow(title,width,height,message=message,image_path1=image_path)

    def open_secondary_window_with_images(self,title,width,height,message,image_path1,image_path2):
        self.secondary_window = SecondaryWindow(title,width,height,message=message,image_path1=image_path1,image_path2=image_path2)

    def upload_csv(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "Open CSV File", "", "CSV Files (*.csv);;All Files (*)", options=options)
        if file_name:
            self.load_data(file_name)
    
    def load_data(self, file_name):
        try:
            data = pd.read_csv(file_name)
            self.data_loaded = True
            self.data = data  # Store the loaded data in a class attribute
            QMessageBox.information(self, 'Success', 'Data loaded successfully.')
        except Exception as e:
            QMessageBox.warning(self, 'Error', f'Failed to load data: {e}')
            self.data_loaded = False

    def predict(self):
        if self.data_loaded:
            load = loadmodel(self.data)  # Use the stored data
            result = load.predict_data()
            if isinstance(result, pd.DataFrame):  # Ensure result is a DataFrame
                result.to_csv("result.csv", index=False)
                QMessageBox.information(self, 'Success', 'Data saved in the given path')
            else:
                QMessageBox.warning(self, 'Error', 'Prediction result is not in the correct format.')
        else:
            QMessageBox.warning(self, 'Warning', 'Please upload a CSV file first.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
