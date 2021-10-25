#==============================#
#       python 內置函數        #
#==============================#

#==============================#
#       AAAAAAAAAAAAAAA        #
#==============================#

# abs()
# 絕對值

'''
print abs(-1)

返回絕對值，可輸入整數、小數、複數((a^2+b^2) 開根號)
'''

# ascii()
# 回傳參數的ASCII可印出形式，若非ASCII格式，則以\x、\u、\U等跳脫字元顯示
'''
print(ascii("Hello 你好"))

輸出：
'Hello \u4f60\u597d'
'''
# all()
# 檢查給定的可迭代參數是否都為true

'''
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True

若元素內有空、0、False返回False，否則返回True
有點像AND GATE
'''

# any()
# 檢查給定的可迭代參數是否都為False

'''
def any(iterable):
    for element in iterable:
        if element:
            return True
    return False

若元素內都為空、0、False返回False，否則返回True
有點像OR GATE
'''

#==============================#
#       BBBBBBBBBBBBBBB        #
#==============================#

# bin()
# 返回一個int/long int的二進制表示法

'''
bin(int/long int)

print(bin(10))
輸出：
0b1010

>>> 可採用字串擷取的方式去掉0b
print(bin(10)[2:])
輸出：
1010
'''

# bool()
# 將給定參數轉換為布林代數
# 整數、小數皆可填入，只有0會被判別為False
# 且bool是int的sub class
'''
print(bool(0))
輸出：
False
'''

# breakpoint()
# 設定中斷點並進入除錯模式(Pdb)
'''
b— 新增breakpoint
p — 印出變數值 # p 變數名稱，例如 p varName
l — 印出目前所在 function/frame上下 11 行的程式碼
ll — 印出目前所在 function/frame 的所有程式碼
c — 持續執行程式碼直到遇到下一個中斷點
unt — 持續執行程式直到某一行 #
q — 離開 pdb
'''

# bytearray()
# 返回一個新字節數組，數組內的元素是可變的，且每個元素的值範圍:0 <= x < 256

'''
class bytearray([source[, encoding[, errors]]])

如果 source 为整数，则返回一个长度为 source 的初始化数组；
如果 source 为字符串，则按照指定的 encoding 将字符串转换为字节序列；
如果 source 为可迭代类型，则元素必须为[0 ,255] 中的整数；
如果 source 为与 buffer 接口一致的对象，则此对象也可以被用于初始化 bytearray。
如果没有输入任何参数，默认就是初始化数组为0个元素。

print(bytearray())
輸出：
bytearray(b'')

print(bytearray([1,2,3]))
輸出：
bytearray(b'\x01\x02\x03')

print(bytearray('runoob', 'utf-8'))
輸出：
bytearray(b'runoob')
'''

#==============================#
#       CCCCCCCCCCCCCCC        #
#==============================#
