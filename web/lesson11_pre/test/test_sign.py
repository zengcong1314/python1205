"""老师登录，学生登录，学生需要加入课程（课程码，加入课程）
老师要创建签到码，获取签到码，学生签到"""
from web.lesson11_pre.data import home
from web.lesson11_pre.pages.class_page import ClassPage
from web.lesson11_pre.pages.home_ba import HomePage


class TestSignClass:
    def test_sign_success(self,teacher_login,student_login):
        """测试步骤：
        1、老师登录
        2、学生登录
        3、老师需要进入课堂
        4、创建签到码
        5、并且获取签到码
        6、学生进入课堂
        7、实行签到
        """

        teacher_driver,student_driver = teacher_login,student_login
        # 有一个课程
        # 手工创建，自动化创建
        # 老师进入课堂
        HomePage(teacher_driver).enter_class(home.class_name)
        # 获取签到码
        sign_code = ClassPage(teacher_driver).get_class_code()
        # 学生签名之前获取一次多少人签到
        # 获取加课码
        class_code = ClassPage(student_driver).get_addclass_code()
        # 学生加入课堂
        HomePage(student_driver).add_class(class_code)
        # 学生进入课堂
        HomePage(student_driver).enter_class(home.class_name)
        # 课程页面，学生签到
        ClassPage(student_driver).sign(sign_code)
        # 怎么断言 日期校验
        #