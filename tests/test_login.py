import pytest

@pytest.mark.parametrize("username, password, expected", [
    ("", "", "Please enter username"),  # yoki sizning xatolik matningiz
    ("wronguser", "wrongpass", "Invalid username or password!"),
])

def test_login(login_page, username, password, expected):
    login_page.open()
    login_page.login(username,password)

    if expected:
        assert login_page.get_error_message() == expected

    else:
        color = login_page.get_input_border_color(login_page.USERNAME)
        assert color in ["rgb(220, 53, 69)", "#dc3545"]
