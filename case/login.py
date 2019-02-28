import requests
import json
import xlrd
import os
# 可选择的配置测试环境
url1 = 'https://pre.bldz.com'
url2 = 'https://test.bldz.com'
# 获取excel文件存放地址
case_excel = os.path.join(os.getcwd(), 'case/login.xlsx')
dt = xlrd.open_workbook(case_excel)
# 获取第一个表
tables = dt.sheets()[0]
# 获取行数
all_nrows = tables.nrows-1#第一行不是用例，所以减去1
# 创建一个空list，存放测试结果
test_result =[]
for i in range(all_nrows):
    # 获取用例名称
    case_name = tables.cell_value(i+1, 1)
    # 获取请求地址
    address = tables.cell_value(i+1, 3)
    url = url1+address
    # 获取请求头
    h = tables.cell_value(i+1, 5)
    h = eval(h)#从str转dict
    print(type(h))
    # 获取求情参数
    request_data = tables.cell_value(i+1, 6)
    request_data = eval(request_data)#从str转dict
    # 获取期望值
    h_r = tables.cell_value(i+1, 7)
    h_r = eval(h_r)#从str转dict
    # 获取测试用例编号
    case_num = tables.cell_value(i+1, 0)
    case_num = str(case_num)
    # 获取请求方式
    request_type = tables.cell_value(i+1, 4)
    if request_type == 'post':
        response = requests.post(url,headers = h,data = json.dumps(request_data))
    elif request_type == 'get':
        response = requests.get(url,headers = h,data = json.dumps(request_data))
    else:
        assert(),'请求方式错误'
    print (response.text)#用.text转换成str后打印返回值
    n_r = json.loads(response.text)#获取返回值，并通过json.loads转换成dict
    for key in h_r:#通过循环‘期望值’的key，来判断返回值是否正确
        print(h_r[key],n_r[key])
        if n_r[key]==h_r[key]:
            print('测试通过')
        else:
            information = '第'+case_num+'条，'+case_name+'有问题'#断言失败时，把错误信息记录好并存放在test_result里
            test_result.append(information)
if test_result!=[]:
    test_result = set(test_result)#list中去重
    assert(),test_result
else:
    pass