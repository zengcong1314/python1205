import time

from web.lesson11_pre.pages.home_ba import HomePage
from web.lesson11_pre.data import addclass

class TestAddClass:
    def test_add_class(self,student_login):
        student_driver = student_login
        HomePage(student_driver).add_course(addclass.class_code)
        assert HomePage(student_driver).get_class(addclass.class_name)
        time.sleep(2)
        HomePage(student_driver).delete_course(addclass.pwd)

