from pages.text_box_page import TextBoxPage


def test_text_box_form(driver):
    page = TextBoxPage(driver)
    page.open()
    page.input_info()
    page.click_btn()

    page._take_screenshot()

    page.get_info()
