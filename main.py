import flet as ft
from router import views_handler

def main(page: ft.Page):
    # Window Settings
    page.window_always_on_top = True
    page.padding = 0
    page.window_title_bar_buttons_hidden = True
    page.window_title_bar_hidden = True

    # theming
    page.theme_mode = ft.ThemeMode.DARK

    # -- color theming
    page.theme = ft.Theme(
        color_scheme_seed="#46FFD4",
        color_scheme=ft.ColorScheme(
            primary="#46FFD4"
        ),
        page_transitions=ft.PageTransitionsTheme.linux
    )

    def route_change(route):
        page.views.clear()
        page.views.append(
            views_handler(page)[page.route]
        )

    page.on_route_change = route_change


    page.go("main-view/")


ft.app(target=main, assets_dir="assets")
