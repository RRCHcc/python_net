"""
练习：检测括号是否为成出现，如果不是则报错
"""
from sstack import *
data = "adf) (asd(fasd) {fa)sd [af] fasd} fa)s asd sd as "

parens = "()[]{}"
left_parens = "([{"
opposite ={")": "(", "]": "[", "}": "{"}

def parent(text):
    #i 记录字符串索引
    i,text_len = 0,len(text)
    while True:
        #逐个遍历字符串，如果没到结尾并且不是括号就向后遍历
        while i < text_len and text[i] not in parens:
            i +=1
        if i >= text_len:
            return
        else:
            yield text[i],i
            i += 1


st = SStack()
for pr, i in parent(data):
    if pr in left_parens:
        st.push((pr, i))
    elif st.is_empty() or st.pop()[0] != opposite[pr]:
        print("Unmatching is found at %d for %s" %(i, pr))
        break
else:
    #循环正常结束
    if st.is_empty():
        print("All parenthese are matched")
    else:
        e = st.pop()
        parent("Unmatching is found at %d for %s" % (e[1], e[0]))




