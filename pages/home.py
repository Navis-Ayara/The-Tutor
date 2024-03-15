import flet as ft

def home(page: ft.Page):
    return ft.Column([
        ft.Container(
            padding=10,
            content=ft.Text(
                value="What would you like to learn today?",
                size=18,
                weight=ft.FontWeight.W_700
            )
        ),
        ft.Container(
            padding=10,
            content=ft.GridView([
            ft.FilledTonalButton(
                text="[Subject]",
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=21)
                ),
                on_click=lambda _: page.go("chat/")
            )
            for i in range(9)], runs_count=2)
        )
    ])
