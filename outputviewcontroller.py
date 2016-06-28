import ui


def viewoutput(html_text: str) -> None:
    v = ui.View()
    v.name = 'Test Web'
    web = ui.WebView()
    v.add_subview(web)
    web.height = 1024
    web.width = 720
    web.load_html(html_text)
    v.present('fullscreen')
