from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from passlib.hash import pbkdf2_sha256

class RegisterScreen(Screen):
    def __init__(self, **kwargs):
        super(RegisterScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        self.username_input = TextInput(hint_text='Username')
        self.password_input = TextInput(hint_text='Password', password=True)
        self.register_button = Button(text='Register', on_press=self.register)
        layout.add_widget(Label(text='Register', font_size=30))
        layout.add_widget(self.username_input)
        layout.add_widget(self.password_input)
        layout.add_widget(self.register_button)
        self.add_widget(layout)

    def register(self, instance):
        username = self.username_input.text.strip()
        password = self.password_input.text.strip()
        if username and password:
            # В реальном приложении здесь будет код для сохранения пользовательских данных
            hashed_password = pbkdf2_sha256.hash(password)
            print(f"Registered: {username}, {hashed_password}")
            self.parent.current = 'login'

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        self.username_input = TextInput(hint_text='Username')
        self.password_input = TextInput(hint_text='Password', password=True)
        self.login_button = Button(text='Login', on_press=self.login)
        layout.add_widget(Label(text='Login', font_size=30))
        layout.add_widget(self.username_input)
        layout.add_widget(self.password_input)
        layout.add_widget(self.login_button)
        self.add_widget(layout)

    def login(self, instance):
        username = self.username_input.text.strip()
        password = self.password_input.text.strip()
        if username and password:
            # В реальном приложении здесь будет код для проверки пользовательских данных
            print(f"Logging in: {username}, {password}")

class MainApp(App):
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(RegisterScreen(name='register'))
        self.sm.add_widget(LoginScreen(name='login'))
        return self.sm

if __name__ == "__main__":
    MainApp().run()
