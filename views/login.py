import flet as ft

class LoginView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.route = "login/"
        self.page = page

        self.vertical_alignment = ft.MainAxisAlignment.CENTER

        self.controls = [
            ft.Column([
                ft.Column([
                    ft.TextField(
                        hint_text="Username or Email",
                        border_radius=50,
                        focused_border_color=ft.colors.PRIMARY,
                        max_length=30
                    ),
                    ft.TextField(
                        hint_text="Password",
                        password=True,
                        border_radius=50,
                        focused_border_color=ft.colors.PRIMARY,
                    ),
                ], spacing=0),
                ft.ElevatedButton(
                    text="Login",
                    on_click=lambda _: page.go("main-view/")
                ),
                ft.Text(
                    value="or"
                ),
                ft.Column([
                    ft.FilledButton(
                        text="Continue with Google",
                        width=300
                    )
                ])
            ], spacing=25, horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER, expand=True)
        ]
