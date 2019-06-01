"""
１．创建技能类(编号，技能名称，冷却时间，攻击力，消耗法力)
　　创建技能列表．
　　－－　定义函数：查找编号是１０１的技能对象
　　－－　定义函数：查找冷却时间为０的所有技能对象
　　－－　定义函数：查找攻击力大于５的所有技能对象
　　－－　定义函数：查找攻击力大于１０，并且不需要消耗法力的所有技能．
    使用列表推导式，与生成器表达式完成
    通过调试断点体会程序执行过程，两项技术的差异
"""
class Skill():
    def __init__(self,id,name,cd,atk,mp):
        self.id = id
        self.name = name
        self.cd =cd
        self.atk =atk
        self.mp =mp

    def __str__(self):
        return "%d--%s--%d--%d--%d"%(self.id,self.name,self.cd,self.atk,self.mp
                                     )
list = [
    Skill(101,"降龙十八掌",15,80,30),
    Skill(102,"佛山无影脚",12,60,20),
    Skill(103,"还我漂漂拳",0,15,0),
    Skill(104,"呵呵哈哈哈或",1,3,0),
    Skill(105,"上山打老虎",0,12,3)
]

result01 = [item for item in list if item.id == 101]
for item in result01:
    print(item)
result02 = (item for item in list if item.id == 101)
for item in result02:
    
    print(item)

result01=[item for item in list if item.cd == 0]
for item in result01:
    print(item)
result02 = (item for item in list if item.cd == 0)
for item in result02:
    print(item)

result01 = [item for item in list if item.atk > 5]
for item in result01:
    print(item)
result02 = (item for item in list if item.atk > 5)
for item in result02:
    print(item)

result01 = [item for item in list if item.atk > 10and item.mp == 0]
for item in result01:
    print(item)
result02 = (item for item in list if item.atk > 10and item.mp == 0)
for item in result02:
    print(item)