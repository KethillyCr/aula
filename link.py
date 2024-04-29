from kivy.app import App
from kivy.uix.image import Image,AsyncImage

class MyApp(App):
    def build(self):

        return AsyncImage(source='https://oimparcial.com.br/app/uploads/2019/10/mini-porco.jpg')
    
if __name__ == "__main__":
    MyApp().run()