import pytest


@pytest.mark.parametrize("username, password, expected", [
    ("", "", "Please enter username"),  # yoki sizning xatolik matningiz
    ("wronguser", "wrongpass", "Invalid username or password!"),
])
def test_login(login_page, username, password, expected):
    login_page.open()
