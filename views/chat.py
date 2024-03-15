import flet as ft
import uuid

class ChatView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.page = page

        self.route = "chat/"
        self.appbar = ft.AppBar(
            leading=ft.IconButton(
                icon=ft.icons.ARROW_BACK_ROUNDED,
                on_click=lambda _: page.go("main-view/")
            ),
            title=ft.Text(
                value="[subject]"
            ),
            center_title=True,
            actions=[
                ft.PopupMenuButton(
                    items=[
                        ft.PopupMenuItem(
                            icon=ft.icons.SAVE_ROUNDED,
                            text="Save Session"
                        ),
                        ft.PopupMenuItem(
                            icon=ft.icons.STAR_ROUNDED,
                            text="Start new session"
                        )
                    ]
                )
            ]
        )

        self.controls = [
            ft.Container(
                padding=10,
                content=ft.Column([
                    ft.ListView(
                        
                    ),
                    ft.Container(
                        padding=10,
                        content=ft.TextField(
                            border_radius=50,
                            filled=True,
                            on_change=self.change_border_radius,
                            shift_enter=True,
                            max_lines=5
                        )
                    )
                ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
            )
        ]

    def change_border_radius(self, e):
        if len(e.control.value) > 34:
            e.control.border_radius = 15
        else:
            e.control.border_radius = 30
        e.control.update()
