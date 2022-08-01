import time
from random import random, randint, choice

import kivy
from kivy.graphics import Color, Rectangle
from kivy.core.audio import SoundLoader
from kivy.uix.label import Label
from functions import cena, moneta, rnd_krome

kivy.require('1.0.7')
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
#from kivy.config import Config

global window_width
#window_width = 1440
global window_height
#window_height = 720


#Config.set('graphics','resizeble','0')
#Config.set('graphics','width',str(window_width))
#Config.set('graphics','height',str(window_height))

from kivy.core.window import Window

global k_x


global k_y


kot = ('zastavka1.jpg',
       'emotsii12.jpg',
       'kot2.jpg',
       'magazin.png',
       '1624279607240.jpg',
       'foto-iz-kosmosa_30.jpg')
pikture_game = ('kot1.jpg',
                'kot2.jpg')
global i
i = 1

global schet
schet = 0

global tovaru
tovaru = []

class MyApp(App):

    def konec(self,j):
        sound = SoundLoader.load('Story2.wav')
        sound.play()
        self.fl.clear_widgets()
        with self.fl.canvas:
            Color(1, 1, 1)
            Rectangle(pos=self.fl.pos, size=(window_width, window_height), source=(kot[5]))

    def magazin(self,j):
        global schet



        self.fl.clear_widgets()

        print(tovaru)

        print(j.text)

        print(schet)
        print(cena(j.text))

        with self.fl.canvas:
            Color(1, 1, 1)
            Rectangle(pos=self.fl.pos, size=(window_width, window_height), source=(kot[3]))
        y = 150
        y_lbl = -110
        shrift = '25'
        txt = j.text
        print(txt)
        print(txt.find('Купить'))
        if int(cena(j.text)) <= schet:

            if (tovaru.count(j.text) == 0) and (txt.find('Купить') != -1):
                tovaru.append(j.text)
                schet = schet - cena(j.text)

            else:
                if txt.find('Купить') != -1:
                    self.fl.add_widget(Label(text='[color=ff3333]' + 'Уже куплено!', markup=True, font_size=shrift, pos=(0, 0)))
        else:
            self.fl.add_widget(
                Label(text='[color=ff3333]' + 'Недостаточно монет', markup=True, font_size=shrift, pos=(round(k_x*30), round(k_y*180))))
        if tovaru.count('Купить шляпку') == 0:
            self.fl.add_widget(Button(text='Купить шляпку', size_hint=(.3, .1), pos=(round(k_x*30), round(k_y*y)), on_press=self.magazin))
        else:
            self.fl.add_widget(Label(text='[color=4ae324]' + 'Шляпка куплена', markup=True, font_size=shrift, pos=(round(k_x*-250), round(k_y*y_lbl))))
        if tovaru.count('Купить бабочку') == 0:
            self.fl.add_widget(Button(text='Купить бабочку', size_hint=(.3, .1), pos=(round(k_x*280), round(k_y*y)), on_press=self.magazin))
        else:
            self.fl.add_widget(
                Label(text='[color=4ae324]' + 'Бабочка куплена', markup=True, font_size=shrift, pos=(0, round(k_y*y_lbl))))
        if tovaru.count('Купить шарфик') == 0:
            self.fl.add_widget(Button(text='Купить шарфик', size_hint=(.3, .1), pos=(round(k_x*530), round(k_y*y)), on_press=self.magazin))
        else:
            self.fl.add_widget(
                Label(text='[color=4ae324]' + 'Шарфик куплен', markup=True, font_size=shrift, pos=(round(k_x*250), round(k_y*y_lbl))))
        if (len(tovaru) ==3) and (schet>5):
            self.fl.add_widget(Button(text='Продолжить', size_hint=(.3, .1), pos=(round(k_x*280), round(k_y*80)), on_press=self.konec))
        else:
            self.fl.add_widget(Button(text='Продолжить', size_hint=(.3, .1), pos=(round(k_x*280), round(k_y*80)), on_press=self.menu1))
        lb_text = ' У тебя ' + str(schet) + moneta(schet)
        self.fl.add_widget(Label(text = '[color=ff3333]' + lb_text, markup=True, font_size=shrift, pos=(round(k_x*30), round(k_y*220))))

    def game(self,j):
        global schet

        self.fl.clear_widgets()
        global i
        i = abs(i-1)
        with self.fl.canvas:
            Color(1, 1, 1)
            Rectangle(pos=self.fl.pos, size=(window_width, window_height), source=(pikture_game[i]))
        self.fl.add_widget(Button(text='Жми', size_hint=(.3, .1), pos=(round(k_x*300), round(k_y*100)), on_press=self.game))

        if (len(tovaru) ==3) and (schet>5):
            self.fl.add_widget(Button(text='Хватит уже', size_hint=(.3, .1), pos=(round(k_x*300), round(k_y*20)), on_press=self.konec))
        else:
            self.fl.add_widget(Button(text='Хватит уже', size_hint=(.3, .1), pos=(round(k_x*300), round(k_y*20)), on_press=self.menu1))

        lb_text = ' У тебя ' + str(schet) + moneta(schet)
        self.fl.add_widget(Label(text='[color=ff3300]' + lb_text, markup=True, font_size='40sp', pos=(round(k_x*30), round(k_y*220))))
        schet += 1

    def pravilnyi_otvet(self,j):
        self.fl.add_widget(Label(text='[color=ff3300]' + 'Правильный ответ: ' + str(otvet), markup=True, font_size='40sp',
                                 pos=(round(k_x * 30), round(k_y * 180))))

    def slognye_primery(self,j):
        global schet
        #формируем пример
        a = randint(2, 200)
        b = randint(1, (a-1))
        c = choice(['+', '-'])
        global primer, otvet
        primer = str(a) + c + str(b)
        otvet = eval(primer)
        # primer = primer + '=' + str(eval(primer))
        nomer_pravilnoi_knopki = randint(1, 3)
        knopka = j.text
        if knopka.isdigit():
            print('Reshali primer')

        self.fl.clear_widgets()

        with self.fl.canvas:
            Color(1, 1, 1)
            Rectangle(pos=self.fl.pos, size=(window_width, window_height), source=('emotsii12.jpg'))

        if nomer_pravilnoi_knopki == 1:
            y1 = 100
            y2 = 180
            y3 = 260
        if nomer_pravilnoi_knopki == 2:
            y1 = 180
            y2 = 100
            y3 = 260
        if nomer_pravilnoi_knopki == 3:
            y1 = 260
            y2 = 180
            y3 = 100

        self.fl.add_widget(Button(text=str(otvet), size_hint=(.3, .1), pos=(round(k_x*300), round(k_y*y1)), on_press=self.slognye_primery))
        self.fl.add_widget(Button(text=rnd_krome(otvet), size_hint=(.3, .1), pos=(round(k_x * 300), round(k_y * y2)), on_press=self.pravilnyi_otvet))
        self.fl.add_widget(Button(text=rnd_krome(otvet), size_hint=(.3, .1), pos=(round(k_x * 300), round(k_y * y3)), on_press=self.pravilnyi_otvet))

        if (len(tovaru) ==3) and (schet>5):
            self.fl.add_widget(Button(text='Выход', size_hint=(.3, .1), pos=(round(k_x*300), round(k_y*20)), on_press=self.konec))
        else:
            self.fl.add_widget(Button(text='Выход', size_hint=(.3, .1), pos=(round(k_x*300), round(k_y*20)), on_press=self.menu1))
        if knopka.isdigit():
            schet += 100
        lb_text = ' У тебя ' + str(schet) + moneta(schet)
        self.fl.add_widget(Label(text='[color=6c03ff]' + primer + '=', markup=True, font_size='60sp', pos=(round(k_x*30), round(k_y*120))))
        self.fl.add_widget(Label(text='[color=ff3300]' + lb_text, markup=True, font_size='40sp', pos=(round(k_x * 30), round(k_y * 260))))



    def primery(self,j):
        global schet
        #формируем пример
        a = randint(2, 20)
        b = randint(1, (a-1))
        c = choice(['+', '-'])
        global primer, otvet
        primer = str(a) + c + str(b)
        otvet = eval(primer)
        # primer = primer + '=' + str(eval(primer))
        nomer_pravilnoi_knopki = randint(1, 3)
        knopka = j.text
        if knopka.isdigit():
            print('Reshali primer')

        self.fl.clear_widgets()

        with self.fl.canvas:
            Color(1, 1, 1)
            Rectangle(pos=self.fl.pos, size=(window_width, window_height), source=('emotsii12.jpg'))

        if nomer_pravilnoi_knopki == 1:
            y1 = 100
            y2 = 180
            y3 = 260
        if nomer_pravilnoi_knopki == 2:
            y1 = 180
            y2 = 100
            y3 = 260
        if nomer_pravilnoi_knopki == 3:
            y1 = 260
            y2 = 180
            y3 = 100

        self.fl.add_widget(Button(text=str(otvet), size_hint=(.3, .1), pos=(round(k_x*300), round(k_y*y1)), on_press=self.primery))
        self.fl.add_widget(Button(text=rnd_krome(otvet), size_hint=(.3, .1), pos=(round(k_x * 300), round(k_y * y2)), on_press=self.pravilnyi_otvet))
        self.fl.add_widget(Button(text=rnd_krome(otvet), size_hint=(.3, .1), pos=(round(k_x * 300), round(k_y * y3)), on_press=self.pravilnyi_otvet))

        if (len(tovaru) ==3) and (schet>5):
            self.fl.add_widget(Button(text='Выход', size_hint=(.3, .1), pos=(round(k_x*300), round(k_y*20)), on_press=self.konec))
        else:
            self.fl.add_widget(Button(text='Выход', size_hint=(.3, .1), pos=(round(k_x*300), round(k_y*20)), on_press=self.menu1))
        if knopka.isdigit():
            schet += 10
        lb_text = ' У тебя ' + str(schet) + moneta(schet)
        self.fl.add_widget(Label(text='[color=6c03ff]' + primer + '=', markup=True, font_size='60sp', pos=(round(k_x*30), round(k_y*120))))
        self.fl.add_widget(Label(text='[color=ff3300]' + lb_text, markup=True, font_size='40sp', pos=(round(k_x * 30), round(k_y * 260))))
        if knopka.isdigit():
            schet += 10

    def menu1(self,j):
        self.fl.clear_widgets()
        with self.fl.canvas:
            Color(1, 1, 1)
            Rectangle(pos=self.fl.pos, size=(window_width, window_height),
                      source=(kot[4]))
        self.fl.add_widget(Button(text='Магазин одежды', size_hint=(.3, .1), pos=(round(k_x*300), round(k_y*100)),
                                  on_press=self.magazin))
        self.fl.add_widget(Button(text='Заработать монетки', size_hint=(.3, .1), pos=(round(k_x*300), round(k_y*200)),
                                  on_press=self.game))
        self.fl.add_widget(
            Button(text='Решать лёгкие примеры', size_hint=(.3, .1), pos=(round(k_x * 300), round(k_y * 400)),
                   on_press=self.primery))
        self.fl.add_widget(
            Button(text='Решать сложные примеры', size_hint=(.3, .1), pos=(round(k_x * 300), round(k_y * 300)),
                   on_press=self.slognye_primery))
    def build(self):
        sound = SoundLoader.load('Story1.wav')
        sound.play()
        sound.bind(on_stop = self.menu1)
        global window_width
        window_width = Window.size[0]
        global window_height
        window_height = Window.size[1]
        print(Window.size)
        global k_x
        k_x = window_width/800

        global k_y
        k_y = window_height/600
        print(str(k_x), ' ', str(k_y))


        self.fl = FloatLayout()
        with self.fl.canvas:
            Color(1, 1, 1)
            Rectangle(pos=self.fl.pos, size=(window_width, window_height),
                      source=(kot[0]))


        #self.fl.add_widget(Label(text='[color=ff3300]' + str(window_width) + 'x' + str(window_height), markup=True, font_size='40sp', pos=(30, 220)))
        return self.fl


if __name__ == '__main__':
    MyApp().run()