from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
import pymysql
Window.clearcolor = (100/250.0,50/250.0,0,0)

class App1(App):
    def build(self):
        self.title = 'Employee'
        layout = GridLayout(cols=1)
        self.L1 = Label(text="Employee")
        self.imo = Image(source='emp1.jpg')
        self.L2 = Label(text="Add new employee")
        self.username = TextInput(hint_text="username")
        self.work = TextInput(hint_text="work")
        self.phone = TextInput(hint_text="phone")
        self.country = TextInput(hint_text="country")
        self.gender = TextInput(hint_text="gender")
        submit = Button(text="Add Employee", on_press=self.sub)
        layout.add_widget(self.imo)
        layout.add_widget(self.L1)
        layout.add_widget(self.L2)
        layout.add_widget(self.username)
        layout.add_widget(self.work)
        layout.add_widget(self.phone)
        layout.add_widget(self.country)
        layout.add_widget(self.gender)
        layout.add_widget(submit)
        return layout
    def sub(self, ob):
        un = self.username.text
        wo = self.work.text
        ph = self.phone.text
        co = self.country.text
        ge = self.gender.text
        con = pymysql.connect(host='localhost',user='root',password='',database='kivo')
        cur = con.cursor()
        query = 'Insert into users (username,work,phone,country,gender) values (%s,%s,%s,%s,%s)'
        val = (un, wo, ph, co, ge)
        cur.execute(query, val)
        con.commit()
        con.close()
if __name__ == '__main__':
    App1().run()