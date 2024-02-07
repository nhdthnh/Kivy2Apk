from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class MyFirstApp(App):
    def build(self):
        # Tạo một root widget là BoxLayout
        root = BoxLayout(orientation='vertical')

        # Tạo một label
        label = Label(text="Xin chào từ ứng dụng của tôi!",
                      size_hint=(.5, .5),
                      pos_hint={'center_x': .5, 'center_y': .5})

        # Tạo một button
        button = Button(text="Nhấn vào đây!",
                        size_hint=(.3, .3),
                        pos_hint={'center_x': .5, 'y': .4})

        # Thiết lập sự kiện khi button được nhấn
        button.bind(on_press=self.on_button_click)

        # Thêm label và button vào root widget
        root.add_widget(label)
        root.add_widget(button)

        return root

    def on_button_click(self, instance):
        # Xử lý sự kiện khi button được nhấn
        print("Button được nhấn!")

if __name__ == "__main__":
    MyFirstApp().run()
