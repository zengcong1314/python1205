# 1  类属性和实例属性的区别是什么？？
#类属性，所有成员都具备的特征,表示：在类定义的下面去定义变量
#实例属性：个体（对象）具备的特征，这些特征可以一样，也可以不一样,在方法里定义的属性
#对象能够获取类属性，类不能获取实例属性
# 2 类属性如何定义？
#在类定义的下面去定义变量
class Car:
    #所有的车都具备的属性
    engine = True
    wheel = True
    material = ["塑料","橡胶"]
# 3 封装一个学生类，(自行分辨定义为类属性还是实例属性)
#  属性：身份(学生)，姓名，年龄，性别，英语成绩，数学成绩，语文成绩， 职责。
# 如果是类属性请提前定义，
# 如果是实例属性请初始化以后添加这个属性的值。
class student:
    #类属性
    identity = "学生"

    def __init__(self,name,age,sex,English_grade,math_grade,language_grade,responsibility):
        # 实例属性
        self.stu_name = name
        self.stu_age = age
        self.stu_sex = sex
        self.EngGrade = English_grade
        self.MathGrade = math_grade
        self.LangGrade = language_grade
        self.job = responsibility
        print("姓名是{},年龄是{}，性别是{}，英语成绩是{}，数学成绩是{}，语文成绩是{}，职责是{}".format(name,age,sex,English_grade,math_grade,language_grade,responsibility))
stu = student("zc","18","女","90,2","98","90","学生会主席")


# 4 给你生活中遇到的 3 种事物分别定义 3 个类，并分别添加几个类属性。
class moneky:
    eat = "banana"
    intest = "climbing tree"


class woman:
    sex = "女"
    interest = "beatiful"


class teacher:
    identity = "teacher_student"
    festival = "Teachers Day"


# 5 定义一个登录的测试用例类LoginTestCase 登录url地址为："http://www.xxxx.com/login" 请求方法为："post" 、 请自行分辨下列属性，应该定义为类属性还是实例属性
# - 属性：用例编号 url地址 请求参数 请求方法 预期结果 实际结果
class LoginTestCase:
    #类属性
    login_url = "http://www.xxxx.com/login"
    method = "post"

    def __init__(self,case_id,data,expected_result,actual_result):
        # 实例属性
        self.caseid = case_id
        self.case_data = data
        self.exresult = expected_result
        self.acresult = actual_result
