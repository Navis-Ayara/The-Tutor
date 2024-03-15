import flet as ft
def change_border_radius(e):
    if len(e.control.value) > 25:
        e.control.border_radius = 15
    else:
        e.control.border_radius = 30

    e.control.update()

def quiz(page: ft.Page):
    return ft.Pagelet(
        expand=True,
        content=ft.Container(
            padding=10,
            expand=True,
            content=ft.Column([
                ft.ListView(

                ),
                ft.Container(
                    padding=10,
                    content=ft.TextField(
                        border_radius=30,
                        filled=True,
                        shift_enter=True,
                        on_change=change_border_radius,
                        max_lines=5
                    )
                )
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
        )
    )