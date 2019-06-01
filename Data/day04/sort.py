"""
基本排序算法演示
"""

l = [15, 6, 7, 8, 9, 3, 1,3 , 16]
class Sort:
    def __init__(self,list_):
        self.list_ = list_
    #冒泡排序
    def bubble(self,):
        for r in range(len(self.list_)-1):
            for c in range(len(self.list_)-r-1):
                if self.list_[c] > self.list_[c+1]:
                    l[c],l[c+1] = l[c+1],l[c]
    #选择排序
    def select(self):
        for i in range(len(self.list_)-1):
            min01 = i
            for j in range(i+1,len(self.list_)):
                if self.list_[min01] > self.list_[j]:
                    min01 = j
            if i != min01:
                self.list_[i], self.list_[min01] = \
                self.list_[min01], self.list_[i]
    #插入排序

    def insert(self):
        for i in range(1,len(self.list_)):
            x = self.list_[i]
            j = i
            while j > 0 and self.list_[j-1] > x:
                self.list_[j] = self.list_[j-1]
                j -=1
            self.list_[j]=x


    def sub_sort(self,low,higt):
        key = self.list_[low]
        while low < higt:
            while low < higt and self.list_[higt] >= key:
                higt -= 1
            self.list_[low] = self.list_[higt]
            while low < higt and self.list_[low] < key:
                low += 1
            self.list_[higt] = self.list_[low]
        self.list_[low] = key
        return low


    #快速排列
    def quick(self, low, higt):
        #low 列表开头元素索引
        #high 列表结尾元素索引
        if low < higt:
            key = self.sub_sort(low, higt)
            self.quick(low,key-1)
            self.quick(key+1,higt)


if __name__ =="__main__":
    sr = Sort(l)
    sr.bubble()
    sr.quick(0,len(l)-1)
    print(sr.list_)



