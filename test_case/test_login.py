import pytest
from common_lib.handle_data import handle_csv_data
from page.web import Web
import sys


class TestDemo:
    def setup(self):
        self.web = Web()
        self.login = self.web.start().to_login_page()

    @pytest.mark.parametrize("username,password,expected", handle_csv_data(sys.path[0] + "\\test_data\\login_data.csv"))
    def test_login(self, username, password, expected):
        self.login.login(username, password)
        assert self.login.login_fail_message() == expected, "失败"

    def teardown(self):
        self.web.stop()