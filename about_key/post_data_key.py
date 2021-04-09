##請輸入參數key組合之list[post_data_key]
##請輸入必要參數之list，0為選項；1為必要[require_flag]
##請輸入參數value組合之list[post_data]
post_data_key = ["leagueId","matchId","token"]
require_flag = [0, 0, 1]
post_data = [[4623,""], [54282,[54261,54181,54227,54234,54281,54282,54228,54017,54197,54237],""], ["5TEV2u7T8nFH3Ri78iC0SbubWK80bl9y"]]

#計算程式必要資料
data_num = 0
post_data_num = []
multiple_num = 0
data_num = len(post_data_key)
i = 0
for data in post_data:
    post_data_num.append(len(data))
    if len(data) > 1:
        multiple_num = multiple_num+1
    i = i+1

#格雷碼(Gray Code)
#https://openhome.cc/Gossip/AlgorithmGossip/GrayCode.htm
class Gray:
    def __init__(self, code, isOdd):
        self.code = code
        self.isOdd = isOdd
        
    def lastIndexOf(self, elem):
        return len(self.code) - 1 - self.code[::-1].index(elem)
    
    def next(self):
        i = (len(self.code) if self.isOdd 
                            else self.lastIndexOf(1)) - 1
        return Gray(
            [] if i == -1 \
               else self.code[0:i] + [1 - self.code[i]] + self.code[i + 1:],
               not self.isOdd)
    
    def isEmpty(self):
        return len(self.code) == 0
               
    def __str__(self):
        return str(self.code)
        
def gray(length):
    def successors(gray):
        nx = gray.next()
        return [] if nx.isEmpty() else [nx] + successors(nx)
            
    init = Gray([0] * length, True)
    return [init] + successors(init)

#使用格雷碼產生所有排列組合的情形
code_all = []
for code in gray(data_num):
    code_all.append(str(code)[1:-1].split(", "))
print("步驟1.使用格雷碼產生所有排列組合的情形")
print(code_all)
print("-")

#將格雷碼轉為數字list
i=0
for code in code_all:
    j=0
    for key_flag in code:
        code_all[i][j] = int(key_flag)   
        j = j+1
    i = i+1
print("步驟2.將格雷碼轉為數字list")
print(code_all)
print("-")

#將必要參數之排列組合為0的刪除
code_delete = []
for i in range(len(require_flag)):
    if require_flag[i] == 1:
        for code in code_all:
            if code[i] == 0:
                code_delete.append(code)
list2 = []
for i in code_delete:
    if not i in list2:
        list2.append(i)
for delete in list2:
    code_all.remove(delete)
print("步驟3.將必要參數之排列組合為0的刪除")
print(code_all)
print("-")

#依據各參數案例數量將排列組合產生所有案例排列組合
for loop in range(multiple_num):
    code_append = []
    for i in range(len(post_data_num)):
        for j in range(len(code_all)):
            if code_all[j][i] == 1:
                for k in range(post_data_num[i]):
                    temp = code_all[j].copy()
                    temp[i] = k+1
                    code_append.append(temp)
    code_all = code_append.copy()
list2 = []
code_all = []
for i in code_append:
    if not i in code_all:
        code_all.append(i)
print("步驟4.依據各參數案例數量將排列組合產生所有案例排列組合")
print(code_all)
print("-")
print("步驟5.將各種組合編號，對照參數value與key轉換成文字組合")
#替各種組合編號，一個二進位數字，可以代表一個子集合。
#http://web.ntnu.edu.tw/~algo/Permutation.html
#將各種組合編號，對照參數value與key轉換成文字組合
for i in range(len(code_all)):
    post = []
    count = 0
    for flag in code_all[i]:
        if flag-1 >= 0:
            if(type(post_data[count][flag-1]) == str):
                post.append("\"" + post_data_key[count] + "\": \"" + str(post_data[count][flag-1]) + "\"")
            else:
                post.append("\"" + post_data_key[count] + "\": " + str(post_data[count][flag-1]) + "")
        count += 1
    print("{" + str(post)[2:-2].replace("\'","") + "}")