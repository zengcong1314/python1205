from web.lesson11_pre.pages.home_ba import HomePage
from web.lesson11_pre.data import addclass

class TestAddClass:
    def test_add_class(self,student_login):
        student_driver = student_login
        HomePage(student_driver).add_class(addclass.class_code)
        assert HomePage(student_driver).get_class(addclass.class_name)
        HomePage(student_driver).delete_class(addclass.pwd)

