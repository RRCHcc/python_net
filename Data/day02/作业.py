"""
 2. 简单的加减法逆波兰表达式
			    * 只包含加减法即可
				* p表示表达式的结束标志
				* 使用链式栈完成
				* 效果类似dc命令
"""
from lstack import *



class ReversePolish:
        @staticmethod
        def reversepolish():

            while True:
                result = input("dc：")
                st = LStack()
                elem = result.split(" ")

                if result =="e":
                    break
                for item in elem:
                    if item == "+":
                        second = st.pop()
                        first = st.pop()
                        total = int(first)+int(second)
                        st.push(str(total))
                    elif item == "-":
                        second = st.pop()
                        first = st.pop()
                        total = int(first) - int(second)
                        st.push(str(total))
                    elif item == "p":
                        print(st.top())
                        st.clear()
                        break
                    else:
                        st.push(item)

re =ReversePolish()
re.reversepolish()
