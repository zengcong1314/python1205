import ctypes

class DLL_handle:
    """
    调用dll类。
    交易规则：（交易调用，非占用）->（加载dll）->initDriver-> setPortAttr->操作方法-> deinit->（释放dll）->(交易返回)
    """
    def __init__(self,dllname):
        """
        加载dll
        :param dllname: dll名称
        """
        self.load_dll = ctypes.CDLL(dllname)
        self.load_dll.initDriver()
        self.res_msg = ctypes.create_string_buffer(50)
        self.err_msg = ctypes.create_string_buffer(50)

    def SealInit(self):
        """
        主板初始化
        :return: 成功：设备唯一ID，失败：错误信息
        """
        self.load_dll.SealInit('',self.res_msg,self.err_msg,0,0)
        return self.res_msg.value.decode()

    def GetSealID(self):
        """
        获取印控仪ID号
        :return:设备唯一ID号
        """
        self.load_dll.GetSealID('',self.res_msg,self.err_msg,0,0)
        return self.res_msg.value.decode()

    def SealSetMAC(self,mac):
        """
        印控仪绑定
        :param mac:mac地址。json格式字符串例如：{“mac”:”123456”}
        :return:成功：0 ，失败：非0
        """
        #拼接字符串
        mac1 = '{"mac":"' + mac +'"}'
        #encode('ascii')   python3中，不加入返回的参数只有第一个字母
        mac2 = mac1.encode('ascii')
        self.load_dll.SealSetMAC(mac2,self.res_msg,self.err_msg,0,0)
        return self.res_msg.value.decode()

    def SealCleanMAC(self,mac):
        """
        印控仪解绑
        :param mac:mac地址。 例如：”123456”
        :return:成功：0 ，失败：非0
        """
        mac1 = '{"mac":"' + mac +'"}'
        mac2 = mac1.encode('ascii')
        self.load_dll.SealCleanMAC(mac2,self.res_msg,self.err_msg,0,0)
        return self.res_msg.value.decode()

    def SealGetInformation(self,item):
        """
        查询印控仪信息
        :param item: json格式字符串，字段如下：
        item（需要查询的状态：fixdoorinfo (安全门状态); trayinfo(进纸门状态); lockinfo(锁定状态)）
        :return:status(印控仪状态 0:关闭/未锁定；1:打开/锁定)
        """
        item1 = item.encode('ascii')
        self.load_dll.SealGetInformation(item1,self.res_msg.value,self.err_msg,0,0)
        return self.res_msg.value.decode()

    def SealGetMAC(self):
        """
        印控仪绑定查询
        :return:Json 格式字符串，字段如下：
        mac1(MAC地址1)
        mac2(MAC地址2)
        """
        self.load_dll.SealGetMAC('',self.res_msg,self.err_msg,0,0)
        return self.res_msg.value.decode()

    def SealRelease(self):
        """
        释放dll
        :return:
        """
        self.load_dll.SealRelease('',self.res_msg,self.err_msg,0,0)
        return self.res_msg.value.decode()


if __name__ == '__main__':
    loaddll = DLL_handle("YZJSealMachine.dll")
    loaddll.SealInit()
    # bottles = Bottles1("D4258BD9FD32")
    # selID = loaddll.GetSealID()
    # print(selID)
    # mac = loaddll.SealGetMAC()
    # print(mac)
    # information = loaddll.SealGetInformation("trayinfo")
    # print("状态：{}".format(information))
    # mac = "D4258BD9FD32"
    # setmac = loaddll.SealSetMAC(mac.encode('ascii'))
    # print(setmac)

    # cleanmac = loaddll.SealCleanMAC(mac)
    # print(cleanmac)

    # macz = loaddll.SealGetMAC()
    # print(macz)
    release = loaddll.SealRelease()
    print("释放成功：{}".format(release))