from greenlet import greenlet

def test01():
    print("执行test01")
    gr2.switch()
    print("结束test01")

def test02():
    print("执行test02")
    gr1.switch()
    print("结束test02")


    #将函数变为协程函数
gr1 = greenlet(test01)
gr2 = greenlet(test02)
gr1.switch()        #执行协程test01
gr2.switch()