import flet as ft

def main(page: ft.Page):
    page.title = "PUBG Mobile UC"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = 400
    page.window_height = 700

    # Giriş Alanları
    id_input = ft.TextField(label="Oyuncu ID", border_color="yellow", color="white")
    pass_input = ft.TextField(label="Şifre", password=True, can_reveal_password=True, border_color="yellow")
    
    def login_click(e):
        if id_input.value and pass_input.value:
            page.snack_bar = ft.SnackBar(ft.Text("Giriş Yapılıyor... Lütfen Bekleyin."))
            page.snack_bar.open = True
            page.update()
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Lütfen tüm alanları doldurun!"))
            page.snack_bar.open = True
            page.update()

    # Ekran Tasarımı
    page.add(
        ft.Column(
            [
                ft.Image(src="https://upload.wikimedia.org/wikipedia/en/a/ad/Pubg_mobile_logo.png", width=200),
                ft.Text("UC Yükleme Paneli", size=30, weight="bold", color="yellow"),
                id_input,
                pass_input,
                ft.ElevatedButton("Giriş Yap", on_click=login_click, bgcolor="yellow", color="black", width=200),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.app(target=main)
