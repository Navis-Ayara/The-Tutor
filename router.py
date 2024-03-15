import flet as ft
from views.main_view import Home
from views.login import LoginView
from views.chat import ChatView

def views_handler(page: ft.Page):
    return {
        "main-view/": Home(page),
        "login/": LoginView(page),
        "chat/": ChatView(page)
    }
