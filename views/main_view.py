import flet as ft
from pages.home import home
from pages.quiz import quiz
from pages.profile import profile

class Home(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.page = page
        self.padding = 0
        self.route = "main-view/"
        self.scroll = ft.ScrollMode.ALWAYS
        
        self.appbar = ft.AppBar(
            leading=ft.Container(
                margin=ft.margin.only(left=10),
                content=ft.CircleAvatar()
            ),
            actions=[
                ft.Container(
                    margin=ft.margin.only(right=10),
                    content=ft.IconButton(
                        icon=ft.icons.MENU_ROUNDED,
                        style=ft.ButtonStyle(
                            side=ft.BorderSide(width=0.9, color=ft.colors.OUTLINE),
                            shape=ft.RoundedRectangleBorder(radius=10)
                        ),
                        on_click=self.show_drawer
                    )
                )
            ]
        )

        self.drawer = ft.NavigationDrawer(
            elevation=40,
            indicator_shape=ft.StadiumBorder(),
            selected_index=-1,
            controls=[
                ft.Container(height=12),
                ft.NavigationDrawerDestination(
                    label="Item 1",
                    icon=ft.icons.ABC,
                    selected_icon_content=ft.Icon(ft.icons.ACCESS_ALARM),
                ),
                ft.Divider(thickness=2),
                ft.NavigationDrawerDestination(
                    icon_content=ft.Icon(ft.icons.MAIL),
                    label="Item 2",
                    selected_icon=ft.icons.PHISHING,
                ),
                ft.Container(
                    height=10
                ),
                ft.NavigationDrawerDestination(
                    icon_content=ft.Icon(ft.icons.PHONE),
                    label="Item 3",
                    selected_icon=ft.icons.PHISHING,
                ),
            ],
        )

        self.navigation_bar = ft.NavigationBar(
            on_change=self.navigate,
            elevation=0,
            label_behavior=ft.NavigationBarLabelBehavior.ONLY_SHOW_SELECTED,
            destinations=[
                ft.NavigationDestination(  
                    label="Home",
                    icon_content=ft.Container(
                        content=ft.Image(
                            src="icons/Home.svg",
                            color=ft.colors.OUTLINE_VARIANT,
                            width=32
                        )
                    ),
                    selected_icon_content=ft.Container(
                        content=ft.Image(
                            src="icons/Home.svg",
                            color=ft.colors.ON_BACKGROUND,
                            width=32
                        )
                    )
                ),
                ft.NavigationDestination(
                    label="Quiz",
                    icon_content=ft.Container(
                        content=ft.Image(
                            src="icons/Sun.svg",
                            color=ft.colors.OUTLINE_VARIANT,
                            width=32
                        )
                    ),
                    selected_icon_content=ft.Container(
                        content=ft.Image(
                            src="icons/Sun.svg",
                            color=ft.colors.ON_BACKGROUND,
                            width=32
                        )
                    )
                ),
                ft.NavigationDestination(
                    label="History",
                    icon_content=ft.Container(
                        content=ft.Image(
                            src="icons/Clock.svg",
                            color=ft.colors.OUTLINE_VARIANT,
                            width=32
                        )
                    ),
                    selected_icon_content=ft.Container(
                        content=ft.Image(
                            src="icons/Clock.svg",
                            color=ft.colors.ON_BACKGROUND,
                            width=32
                        )
                    )
                ),
                ft.NavigationDestination(
                    label="Profile",
                    icon_content=ft.Container(
                        content=ft.Image(
                            src="icons/User.svg",
                            color=ft.colors.OUTLINE_VARIANT,
                            width=32
                        )
                    ),
                    selected_icon_content=ft.Container(
                        content=ft.Image(
                            src="icons/User.svg",
                            color=ft.colors.ON_BACKGROUND,
                            width=32
                        )
                    )
                )
            ]
        )

        self.controls = [home(self.page)]

    def show_drawer(self, e):
        self.drawer.open = True
        self.update()

    def navigate(self, e):
        match e.control.selected_index:
            case 0:
                self.appbar = ft.AppBar(
                    leading=ft.Container(
                        margin=ft.margin.only(left=10),
                        content=ft.CircleAvatar()
                    ),
                    actions=[
                        ft.Container(
                            margin=ft.margin.only(right=10),
                            content=ft.IconButton(
                                icon=ft.icons.MENU_ROUNDED,
                                style=ft.ButtonStyle(
                                    side=ft.BorderSide(width=0.9, color=ft.colors.OUTLINE),
                                    shape=ft.RoundedRectangleBorder(radius=10)
                                ),
                                on_click=self.show_drawer
                            )
                        )
                    ]
                )

                self.controls.clear()
                self.controls.append(
                    home(self.page)
                )

                self.page.update()

            case 1:
                self.appbar = ft.AppBar(
                    automatically_imply_leading=False,
                    title=ft.Text(
                        value="Quiz"
                    )
                )

                self.controls.clear()
                self.controls.append(
                    quiz(self.page)
                )
                self.page.update()

            case 2:
                self.appbar = ft.AppBar(
                    title=ft.Text(
                        value="Sessions History",
                        size=20,
                        weight=ft.FontWeight.BOLD
                    ),
                    center_title=True,
                    automatically_imply_leading=False,
                )

                self.controls.clear()
                self.page.update()

            case 3:
                self.appbar = ft.AppBar(
                    elevation=10,
                    leading=ft.Container(
                        margin=ft.margin.only(left=10),
                        content=ft.CircleAvatar()
                    ),
                    title=ft.Text(
                        value="Profile",
                        size=20,
                        weight=ft.FontWeight.BOLD
                    ),
                    center_title=True
                )

                self.controls.clear()
                self.controls.append(
                    profile(self.page)
                )

                self.page.update()