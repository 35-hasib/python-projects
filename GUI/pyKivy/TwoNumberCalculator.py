import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

class testApp(Widget):
    def __init__(self, **kwargs):
        super(testApp,self).__init__(**kwargs)
        
        
        self.l1 = Label(text="Number 1",pos=(0,520),size=(100,50))
        self.add_widget(self.l1)
        self.l2 = Label(text="Number 2",pos=(0,470),size=(100,50))
        self.add_widget(self.l2)
        self.l3 = Label(text="Result ",pos=(0,420),size=(100,50))
        self.add_widget(self.l3)
        
        self.t1 = TextInput(pos=(100,520),size=(200,50),font_size=30)
        self.add_widget(self.t1)
        self.t2 = TextInput(pos=(100,470),size=(200,50),font_size=30)
        self.add_widget(self.t2)
        self.t3 = TextInput(pos=(100,420),size=(200,50),font_size=30)
        self.add_widget(self.t3)
        
        b1 = Button(text="+",pos=(300,520),size=(50,50))
        b1.bind(on_press=self.button_pressed)
        self.add_widget(b1)
        b2 = Button(text="-",pos=(350,520),size=(50,50))
        b2.bind(on_press=self.button_pressed)
        self.add_widget(b2)
        b3 = Button(text="*",pos=(300,470),size=(50,50))
        b3.bind(on_press=self.button_pressed)
        self.add_widget(b3)
        b4 = Button(text="/",pos=(350,470),size=(50,50))
        b4.bind(on_press=self.button_pressed)
        self.add_widget(b4)
        
    def button_pressed(self, instance):
        a = int(self.t1.text)
        b = int(self.t2.text)
        if instance.text == "+":
            self.t3.text = str(a+b)
        if instance.text == "-":
            self.t3.text = str(a-b)
        if instance.text == "*":
            self.t3.text = str(a*b)
        if instance.text == "/":
            try:
                self.t3.text = str(a/b)
            except:
                self.t3.text = "Error"
        
        


class maintestApp(App):
    def build(self):                        #IMP
        return testApp()

if __name__ == "__main__":
    maintestApp().run()
