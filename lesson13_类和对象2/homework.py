# 一，定义一个手机类，
# 1. 具有打电话和录音的方法
# 2. 打电话的时候可以录音，也可以不录音。（方法调用其他方法）
class mobile_phone:
    def calling(self,record):
        if record == "True":
            self.Recording()
            print("正在打电话")
        else:
            print("正在打电话")

    def Recording(self):
        print("正在录音")

m = mobile_phone()
m.calling("True")

# 二.  简述类方法和实例方法，静态方法
# 类方法：整个类具有的行为,类方法会在类前面加一个声明，@classmethod。类方法可以通过类调用，也可以通过实例调用
# 实例方法：就是一个对象（个体）特有的行为。实例属性。实例方法只能通过实例调用
# 静态方法：（static method）在方法中，不需要用到对象self，又不需要用到类（cls）
# 当你需要把一个普通的函数放在类下面的时候，方便管理。类或对象都可调用

# 三. 简述类属性和实例属性
# 类属性：所有成员都具备的特征，在类定义的下面去定义变量，类属性 == 类变量，获取类属性 类.属性
# 实例属性：个体（对象）具备的特征，这些特征可以一样，也可以不一样

# 四.定义一个 ExcelHandler 类，所有方法不需要实际操作实现（不需要你真的去打开 excel, 不需要你真的把数据读出来。我们练习的是定义类的思维。）
# 1.初始化传入 文件路径。
# 2.定义打开 excel 方法。
# 3.定义获取 sheet 表格方法，根据 名称获取。
# 4.定义读取 sheet 表格数据的方法。 （读取需要先打开，再获取表格。）
# 5.定义关闭文件方法。

class ExcelHandler:
    def __init__(self,filepath):
        self.file_path = filepath

    def openexcel(self,excelname):
        print("正在打开excel")
        pass

    def getsheet(self,sheetname):
        print("getsheet")
        pass

    def readdata(self):
        self.getsheet(self)
        print("readdata")
        pass

    def closefile(self):
        print("closefile")
        pass

doexcel = ExcelHandler("D:\Project\python36\lesson13_类和对象2")
doexcel.getsheet("zx")
doexcel.readdata()
doexcel.closefile()