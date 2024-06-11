import kivy
from kivymd.app import MDApp
from kivy.uix.label import Label as L
from kivy.uix.button import Button as B
from kivy.uix.checkbox import CheckBox as C
from kivy.uix.image import Image as I
from kivy.uix.scatter import Scatter
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
#from html  import html
import mysql.connector
import sqlite3
from kivy.clock import Clock
from kivy.properties import StringProperty, NumericProperty
from kivy.animation import Animation
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import cv2
from cvzone.ClassificationModule import Classifier
from tkinter import filedialog
from tkinter import Tk
import os

class Manager(ScreenManager):
    Builder.load_string("""
<Manager>:
    Screen:
        name:'logo'
        canvas:
            Rectangle:
                pos: self.pos
                size: self.size
                source:'i/1 (1).jpg'
        Label:
            text:"Covid-19 Detection From Lungs X-rays "
            color: 0,1,0,1
            font_style:"italic"
            font_size: 50
            pos_hint:{"center_x":0.5,"center_y":0.83}
        Label:
            text:"LOGIN"
            color: 0,1,0,1
            font_style:"italic"
            font_size: 30
            pos_hint:{"center_x":0.51,"center_y":0.65}
        MDTextField:
            id:username
            mode: "rectangle"
            hint_text: "Username"
            multiline:False
            color_mode: 'custom'
            line_color_focus: 0, 1, 0, 1
            size_hint:.15,.08
            pos_hint:{"center_x":0.51,"center_y":0.55}

        MDTextField:
            id:password
            mode: "rectangle"
            hint_text: "Password"
            multiline:False
            color_mode: 'custom'
            line_color_focus: 0, 1, 0, 1
            pos_hint:{"center_x":0.51,"center_y":0.45}
            size_hint:.15,.08
        MDRectangleFlatButton:
            text: "login"
            pos_hint:{"center_x":0.51,"center_y":0.35}
            theme_text_color: "Custom"
            text_color: "white"
            line_color: "green"
            on_press:
                app.load()
        Label:
            id:label
            text:""
            color: 1,0,0,1
            font_style:"italic"
            font_size: 20
            pos_hint:{"center_x":0.51,"center_y":0.25}
    Screen:
        name:'user'
        canvas:
            Rectangle:
                pos: self.pos
                size: self.size
                source:'i/user.png'
        Label:
            text:"Patient Details : "
            color: 1,1,0,1
            font_style:"italic"
            font_size: 40
            pos_hint:{"center_x":0.2,"center_y":0.8}
        Label:
            text:"Name : "
            color: 1,1,1,1
            font_style:"italic"
            font_size: 30
            pos_hint:{"center_x":0.25,"center_y":0.7}
        MDTextField:
            id:name
            mode: "rectangle"
            hint_text: "Name"
            multiline:False
            color_mode: 'custom'
            line_color_focus: 1, 1, 1, 1
            size_hint:.15,.08
            pos_hint:{"center_x":0.45,"center_y":0.7}
        Label:
            text:"Mobile.No : "
            color: 1,1,1,1
            font_style:"italic"
            font_size: 30
            pos_hint:{"center_x":0.25,"center_y":0.6}
        MDTextField:
            id:mobile
            mode: "rectangle"
            hint_text: "Mobile.No"
            multiline:False
            color_mode: 'custom'
            line_color_focus: 1, 1, 1, 1
            pos_hint:{"center_x":0.45,"center_y":0.6}
            size_hint:.15,.08
        Label:
            text:"Gender : "
            color: 1,1,1,1
            font_style:"italic"
            font_size: 30
            pos_hint:{"center_x":0.25,"center_y":0.5}
        MDTextField:
            id:gender
            mode: "rectangle"
            hint_text: "Gender"
            multiline:False
            color_mode: 'custom'
            line_color_focus: 1, 1, 1, 1
            pos_hint:{"center_x":0.45,"center_y":0.5}
            size_hint:.15,.08
        Label:
            text:"Blood Group : "
            color: 1,1,1,1
            font_style:"italic"
            font_size: 30
            pos_hint:{"center_x":0.25,"center_y":0.4}
        MDTextField:
            id:blood
            mode: "rectangle"
            hint_text: "Blood Group"
            multiline:False
            color_mode: 'custom'
            line_color_focus: 1, 1, 1, 1
            pos_hint:{"center_x":0.45,"center_y":0.4}
            size_hint:.15,.08
        Label:
            text:"Address : "
            color: 1,1,1,1
            font_style:"italic"
            font_size: 30
            pos_hint:{"center_x":0.25,"center_y":0.3}
        MDTextField:
            id:address
            mode: "rectangle"
            hint_text: "Address"
            multiline:False
            color_mode: 'custom'
            line_color_focus: 1, 1, 1, 1
            pos_hint:{"center_x":0.45,"center_y":0.3}
            size_hint:.15,.08
        MDRectangleFlatButton:
            text: "Check..>"
            pos_hint:{"center_x":0.8,"center_y":0.15}
            theme_text_color: "Custom"
            text_color: "white"
            line_color: "green"
            on_press:
                root.current='detect'  
                app.main() 
                app.new()                     
        Image:
            id:image
            size_hint:(.25,.25)
            pos_hint:{"center_x":0.75,"center_y":0.6}
        MDRectangleFlatButton:
            text: "Choose file"
            pos_hint:{"center_x":0.75,"center_y":0.4}
            theme_text_color: "Custom"
            text_color: "white"
            line_color: "blue"
            on_press:
                app.main1()
                
    Screen:
        name:'detect'
        canvas:
            Rectangle:
                pos: self.pos
                size: self.size
                source:'i/user.png'
        Label:
            text:"Detect Covid-19 from X-ray : "
            color: 0,1,1,1
            font_style:"italic"
            font_size: 40
            pos_hint:{"center_x":0.2,"center_y":0.8}
        Image:
            id:image1
            size_hint:(.4,.4)
            pos_hint:{"center_x":0.35,"center_y":0.5}
        Label:
            id:l1
            text:""
            color: 0,1,1,1
            font_style:"italic"
            font_size: 20
            pos_hint:{"center_x":0.6,"center_y":0.7}
        Label:
            id:l2
            text:""
            color: 1,0,0,1
            font_style:"italic"
            font_size: 30
            pos_hint:{"center_x":0.6,"center_y":0.6}
        Label:
            id:l3
            text:""
            color: 0,1,1,1
            font_style:"italic"
            font_size: 30
            pos_hint:{"center_x":0.6,"center_y":0.5}
        Label:
            id:l4
            text:""
            color: 0,1,0,1
            font_style:"italic"
            font_size: 30
            pos_hint:{"center_x":0.6,"center_y":0.4}
        MDRectangleFlatButton:
            text: "Menu"
            pos_hint:{"center_x":0.8,"center_y":0.15}
            theme_text_color: "Custom"
            text_color: "white"
            line_color: "green"
            on_press:
                root.current='logo'   
    """)
    pass
class covid(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        mydb = mysql.connector.connect(

			host = "localhost", 
			user = "root",
			passwd = "",
			database = "second1_db"
			)
        c = mydb.cursor()
        c.execute("CREATE DATABASE IF NOT EXISTS second1_db")
        c.execute("""CREATE TABLE if not exists patient (name  VARCHAR(15),mobile_NO VARCHAR(20),Gender VARCHAR(5),Blood_group VARCHAR(10),result VARCHAR(20),Address VARCHAR(100))""")
        mydb.commit()
        mydb.close()
        return Manager()
    #image_source = StringProperty()
    def new(self):
        self.root.ids.name.text = ''
        self.root.ids.mobile.text = ''
        self.root.ids.gender.text = ''
        self.root.ids.blood.text = ''
        self.root.ids.address.text = ''
    def selected(self,filename):
        try:    
            self.image_source = filename[0]
        except:
            pass
    def load(self):
        if self.root.ids.password.text=="123":
            self.root.current='user'
        else:
            self.root.ids.label.text="wrong password"
    def main1(self):
            filename = filedialog.askopenfilename()
            self.root.ids.image.source =filename

    def main(self):
            if True:

                    mc=Classifier('model/keras_model.h5','model/labels.txt')
                    #filename = filedialog.askopenfilename()
                    img=cv2.imread(str(self.root.ids.image.source))
                    p=mc.getPrediction(img)
                    self.root.ids.image1.source=self.root.ids.image.source
                    mydb = mysql.connector.connect(
                        host = "localhost", 
                        user = "root",
                        passwd = "",
                        database = "second1_db"
                        )
                    c = mydb.cursor()
    
                    if p[1]==0:
                        self.root.ids.l1.text=("Detection : "+str(p))
                        self.root.ids.l2.text=('Warning : positive result')
                        self.root.ids.l3.text=('COVID-19 indentified')
                        sq=("INSERT INTO patient (name,mobile_No,Gender,Blood_group,result,Address) VALUES (%s,%s,%s,%s,%s,%s)")
                        r=[(self.root.ids.name.text,self.root.ids.mobile.text,self.root.ids.gender.text,self.root.ids.blood.text,'Positive',
                        self.root.ids.address.text,
                        )]
                        c.executemany(sq,r)	
                        mydb.commit()
                        mydb.close()
                    elif p[1]==1:
                        self.root.ids.l1.text=("Detection : "+str(p))
                        self.root.ids.l2.text=('Safe : Negative result')
                        self.root.ids.l3.text=('COVID-19 is not detected')
                        self.root.ids.l4.text=("your in safe")
                        sq=("INSERT INTO patient (name,mobile_No,Gender,Blood_group,result,Address) VALUES (%s,%s,%s,%s,%s,%s)")
                        r=[(self.root.ids.name.text,self.root.ids.mobile.text,self.root.ids.gender.text,self.root.ids.blood.text,'Negative',
                        self.root.ids.address.text,
                        )]
                        c.executemany(sq,r)	
                        mydb.commit()
                        mydb.close()
                    #cv2.imshow("out",img)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
                    self.root.ids.image.source='i/user1.png'


if __name__ == '__main__':
    covid().run()