class ware:
    def __init__(self):
        self.__xuhao=1
        self.__pinming='苹果'
        self.__danjia=5
        self.__zongshu=10
        self.__shengshu=8

    def display(self):
        print(f'xuhao:{self.__xuhao},pinming:{self.__pinming},danjia：{self.__danjia},zongshu:{self.__zongshu},shengshu:{self.__shengshu}')

    def income(self):
        a=(self.__danjia)
        b=(self.__zongshu)
        c=(self.__shengshu)
        d=b-c
        e=d*a
        print(e)

    def setdata(self,b,c,d,e,f):
        self.__xuhao = b
        self.__pinming = c
        self.__danjia = d
        self.__zongshu = e
        self.__shengshu = f


a=ware()
a.setdata(1,2,3,4,5)
a.display()