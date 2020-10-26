# -*- coding:utf-8 -*-
import json
# -------------客户登录->login_kh--------------------------
# paramJson={"password":"NPhcqA7DU9MFK4otOXOgxQ\u003d\u003d","username":"18781972711"}
username = "18781972711"
password_kh = "NPhcqA7DU9MFK4otOXOgxQ\u003d\u003d"
userType_kh = "client"
businessline = "XD"

login_kh_paramJson = {"username": username, "password": password_kh}
login_kh_paramJson = str(login_kh_paramJson).replace('\\\\','\\')       #去除加密密码中的反斜杠

# -----------------------------------------------------------------------------------------
# -------------提交借款申请（正好快贷）--------------------------
# paramJson={"applyType":"FIRSTINLOAN","apply_loan_key":"","businessLine":"XD","canMonthPayMoney":"1000.0","custNo":"664","custType":"1",
#           "facility":"A","loanIntent":"41,其他个人消费","loanMoney":"30000.0","productNo":"56,公积金方案","productTerm":"18","salerNo":"ZHHQ01126"}
apply_loan_key = ""
productNo = [u"55,公务员方案",u"56,公积金方案",u"58,保单方案",u"63,精英方案",u"65,工薪方案",u"66,优房方案",u"701,微粒方案"][0]   #方案类型
product_no = ["55","56","58","63","65","66","701"][0]
productTerm = ["12","18","24","36"][1]   #贷款期限
facility = "A"    #设备类型
loanIntent = [u"41,其他个人消费",u"3,装修",u"9,其他",u"14,个人资金周转",u"30,购物消费",u"35,旅游支出",u"40,员工工资",u"33,婚庆装修",u"32,医疗美容"][0]
applyType = ["FIRSTINLOAN","REVOLVING"][0]   #申请件类型 FIRSTINLOAN:首次进件，REVOLVING:循环贷进件
businessLine = "XD"   #信贷业务线

# 常用修改选项
custNo = "664"  # 用户custNo
salerNo = "ZHHQ01126"  # 业务员账号，经纪人账号
loanMoney = "30000.0"  # 申请借款金额
canMonthPayMoney = "1000"  # 月承受还款额
custType = ["1", "2"][0]  # 1：工薪族，2：企业主

tjsq_paramJson = {"applyType": applyType,"businessLine": businessLine,"canMonthPayMoney": canMonthPayMoney,"custNo": custNo, "custType": custType,"facility": facility,
                  "loanIntent": loanIntent,"loanMoney": loanMoney,"productNo": productNo,"productTerm": productTerm,"product_no": product_no,"salerNo": salerNo}
tjsq_paramJson = json.dumps(tjsq_paramJson, encoding='utf-8', ensure_ascii=False)

# -----------------------------------------------------------------------------------------
# -------------地址信息--------------------------
# paramJson={"isreglive":"1","live_area":"110101,东城区","live_city":"1101,北京市","live_prov":"11,北京市","live_town":"玉林横街19号","reg_area":"110101,东城区",
#           "reg_city":"1101,北京市","reg_prov":"11,北京市","reg_town":"玉林横街19号","apply_loan_key":"${applyloankey}","userType":"client"}
reg_prov = u"11,北京市"  # 户籍省 11为北京市
reg_city = u"1101,北京市"  # 户籍市 11为北京市
reg_area = u"110101,东城区"  # 户籍区 110101为东城区
reg_town = u"玉林横街19号"  # 户籍详细地址
live_prov = u"11,北京市"  # 现住省
live_city = u"1101,北京市"  # 现住市
live_area = u"110101,东城区"  # 现住区
live_town = u"玉林横街19号"  # 现住地址
isreglive = ["1","0"][0]  # 现住址是否与户籍地址相同,1：是

dzxi_paramJson = {"isreglive": isreglive,"live_area": live_area,"live_city": live_city,"live_prov": live_prov,"live_town": live_town,"reg_area": reg_area,
                  "reg_city": reg_city,"reg_prov": reg_prov,"reg_town": reg_town}
dzxi_paramJson = json.dumps(dzxi_paramJson, encoding='utf-8', ensure_ascii=False)

# -----------------------------------------------------------------------------------------
# -------------基本资料--------------------------------------------------------------
# paramJson={"car_value":"30","education":"1,研究生及以上","email":"aa@qq.com","first_entry_date":"2018-02-20","home_mobile":"","house_value":"200","mar_status":"2,未婚",
#           "nation":"1,汉族","qq":"","wechat":"","apply_loan_key":"${applyloankey}","userType":"client"}
car_value = "30"   #汽车价值
house_value = "200"   #房产价值
first_entry_date = "2018-02-24"    #初次入职时间
address_state = "1"

nation = u"1,汉族"  # 民族
wechat = "111"  # 微信号
qq = "222"  # qq号
home_mobile = "015-23454"  # 住宅电话
email = "aa@bb.com"  # 电子邮箱

# 常用修改选项
mar_status = [u"1,已婚", u"2,未婚", u"3,离异", u"4,丧偶", u"5,已婚无法认可", u"6,其他"][0]  # 婚姻状态
education = [u"1,研究生及以上", u"2,大学本科", u"3,大学专科", u"4,高中", u"5,初中及以下"][0]  # 学历
live_type = [u"1,自有产权", u"2,亲属同住", u"3,单位宿舍", u"4,朋友合租"][0]  # 住房性质

jbzl_paramJson = {"address_state": address_state,"car_value": car_value,"education": education,"email": email,"first_entry_date": first_entry_date,"home_mobile": home_mobile,
                  "house_value": house_value,"live_type": live_type,"mar_status": mar_status,"nation": nation,"qq": qq,"wechat": wechat}
jbzl_paramJson = json.dumps(jbzl_paramJson, encoding='utf-8', ensure_ascii=False)

# -----------------------------------------------------------------------------------------
# -------------单位信息---------------------------------------------------------------------------------------------
# paramJson={"apply_loan_key":"${applyloankey}","comp_area":"110101,东城区","comp_city":"1101,北京市","comp_job":"1,一般员工","comp_mobile":"5696-6658569-56",
#           "comp_name":"ZHPH","comp_prov":"11,北京市","comp_town":"玉林横街19号","industry_type":"J1010,金融业&J10101,货币金融服务","landlord_mobile":"",
#           "month_salary":"8000","other_salary":"2000","userType":"client"}
comp_name = "ZHPH"  # 单位名称
comp_mobile = "5696-6658569-56"  # 单位电话
register_date = ""   #注册时间
stock_rate = ""    #占股比例
comp_prov = u"11,北京市"  # 单位的省
comp_city = u"1101,北京市"  # 单位的市
comp_area = u"110101,东城区"  # 单位的区
comp_town = u"玉林横街19号"  # 单位地址
comp_dept = ""    #所在部门
month_salary = "8000"    #月收入
other_salary = "2000"    #其他收入
landlord_mobile = ""     #房东电话
industry_type = [u"J1010,金融业&J10101,货币金融服务", u"O1515,居民服务、修理和其他服务业&O15153,其他服务业"][0]  # 所属行业
comp_job = [u"1,一般员工", u"2,书记", u"3,主任", u"4,科长", u"5,所长", u"6,村长", u"7,校长", u"8,教师", u"9,农民", u"10,其他", u"11,主管", u"12,部门经理",
            u"13,总监", u"14,助理", u"15,副总经理", u"16,总经理/总裁/董事长", u"17,部长", u"18,厂长"][0]  # 职位级别

dwxx_paramJson = {"comp_area": comp_area,"comp_city": comp_city,"comp_job": comp_job,"comp_mobile": comp_mobile,"comp_name": comp_name,
                  "comp_prov": comp_prov,"comp_town": comp_town,"industry_type": industry_type,"landlord_mobile": landlord_mobile,
                  "month_salary": month_salary,"other_salary": other_salary}

dwxx_paramJson = json.dumps(dwxx_paramJson, encoding='utf-8', ensure_ascii=False)

# -----------------------------------------------------------------------------------------
# -------------联系人信息-------------------------------------------------------------------------------------------
# 未婚情况：
# paramJson={"mate":null,
#   "othercontact":[{"contact_mobile":"15736589956","contact_name":"阿三","contact_rel":"1,父母","idcard_no":"","is_known":"1,是","order_index":""},
#           {"contact_mobile":"15198029708","contact_name":"大山","contact_rel":"1,同事","idcard_no":"","is_known":"1,是","order_index":""},
#           {"contact_mobile":"13888888888","contact_name":"李四","contact_rel":"3,子女","idcard_no":"","is_known":"1,是","order_index":""}]}

lxrxx_paramJson = {"mate": {"contact_name": u"王五", "contact_rel": u"2,配偶", "idcard_no": "", "is_known": u"1,是", "contact_mobile": "18793452675","order_index": "0"},
    "othercontact": [{"contact_mobile": "15736589956", "contact_name": u"阿三", "contact_rel": u"1,父母", "idcard_no": "","is_known": u"1,是","order_index": "1"},
        {"contact_mobile": "15198029708", "contact_name": u"大山", "contact_rel": u"1,同事", "idcard_no": "","is_known": u"1,是","order_index": "2"},
        {"contact_mobile": "13888888888", "contact_name": u"李四", "contact_rel": u"3,子女", "idcard_no": "","is_known": u"1,是","order_index": "3"}]}
lxrxx_paramJson = json.dumps(lxrxx_paramJson, encoding='utf-8', ensure_ascii=False)

# -----------------------------------------------------------------------------------------
# -------------负债信息------------------------------------------------------------------------------------------
# paramJson = {"applyLoanKey":"${applyloankey}","custNo":"664","currentDebt":"0","otherPlatformsBorrow_sum":"0","otherPlatformsBorrow_surplus":"",
#              "overdueSituation_sum":"0","overdueSituation_creditCard":"","overdueSituation_houseLoan":"","overdueSituation_other":"",
#              "overdueSituation_sumSurplus":"","userType":"client"}
currentDebt = "0"  # 当前负债
otherPlatformsBorrow_sum = "0"  # 其他网络平台借贷情况,累计借款
otherPlatformsBorrow_surplus = ""  # 其他网络平台借贷情况,待结清
overdueSituation_sum = "0"  # 总逾期金额
overdueSituation_creditCard = ""  # 信用卡逾期金额
overdueSituation_houseLoan = ""  # 购房贷款逾期金额
overdueSituation_other = ""  # 其他贷款逾期金额
overdueSituation_sumSurplus = ""  # 剩余逾期待结清总金额

fzxx_paramJson = {"custNo": custNo,"currentDebt": currentDebt,"otherPlatformsBorrow_sum": otherPlatformsBorrow_sum,"otherPlatformsBorrow_surplus": otherPlatformsBorrow_surplus,
                  "overdueSituation_sum": overdueSituation_sum,"overdueSituation_creditCard": overdueSituation_creditCard,"overdueSituation_houseLoan": overdueSituation_houseLoan,
                  "overdueSituation_other": overdueSituation_other,"overdueSituation_sumSurplus": overdueSituation_sumSurplus}
fzxx_paramJson = json.dumps(fzxx_paramJson, encoding='utf-8', ensure_ascii=False)

# -----------------------------------------------------------------------------------------
# ------------------资产信息----------------------------------------------------------------------------------------
# paramJson={"apply_loan_key":"${applyloankey}","house_mortg_amt":"0","house_quantity":"0","car_mortg_amt":"0","house_mortg_quantity":"0",
#           "car_quantity":"0","car_mortg_quantity":"0"}
house_mortg_amt = "0"  # 房产按揭金额
house_quantity = "0"  # 房产总数量
house_mortg_quantity = "0"  # 房产按揭数量
car_mortg_amt = "0"  # 车辆按揭金额
car_quantity = "0"  # 车辆总数量
car_mortg_quantity = "0"  # 车辆按揭金额

zcxx_paramJson = {"house_mortg_amt":house_mortg_amt,"house_quantity":house_quantity,"car_mortg_amt":car_mortg_amt,
                 "house_mortg_quantity":house_mortg_quantity,"car_quantity":car_quantity,"car_mortg_quantity":car_mortg_quantity}
zcxx_paramJson = json.dumps(zcxx_paramJson, encoding='utf-8', ensure_ascii=False)

# ------------------运营商、电商征信授权------------------------------------------------------------------------
# ------------------提交借款------------------------------------------------------------------------------------

# ------------------经纪人登录->login_qm---------------------------------------------------------------------------
# paramJson={"username":"ZHTS0005","password":"NPhcqA7DU9MFK4otOXOgxQ==","userType":"saler"}

salerNo = "ZHTS0005"   # 经纪人账号
password_jjr = "NPhcqA7DU9MFK4otOXOgxQ=="   # 经纪人密码
userType_jjr = "saler"

login_qm_paramJson = {"username": salerNo, "password": password_jjr, "userType": userType_jjr}

# -----------------------------------------------------------------------------------------
# ------------------提交审核----------------------------------------------------------------------------------
# paramJson={"apply_loan_key":"${applyloankey}","loan_memo":"","bank_water_cardno":"","processResult":"","isPatch":false}
loan_memo = ""
bank_water_cardno = ""
processResult = ""
isPatch = "false"

tjsh_paramJson = {"loan_memo": loan_memo, "bank_water_cardno": bank_water_cardno,"processResult": processResult,"isPatch": isPatch}
tjsh_paramJson = json.dumps(tjsh_paramJson, encoding='utf-8', ensure_ascii=False)

# -----------------------------------------------------------------------------------------
# -------------------审批人登录->login_sale--------------------------------------------------------------------------
loginAudit = "ZHHQ00014"    #审批账号
auditPasswd = "a654321."    #审批账号密码

# -----------------------------------------------------------------------------------------
# -------------------初审/复审/复核审核分单-----------------------------------------------------------------------------
#在中央审批库的zhph_sys_user表中查询账号userId
activitiStatus_cs = "HEAD_OFFICE_TRIAL"    #初审分单
activitiStatus_fs = "HEAD_OFFICE_REVIEW"    #复审分单
auditStatus = "SIGN_REVIEW"    #复核审核分单
userId = "4A1EC3FF5BEC4661E05332C8A8C0AB77"   #审批用户ID

# -----------------------------------------------------------------------------------------
# -------------------总部初审/复审------------------------------------------------------------------------------
productTerm = ["12","18","24","36"][1]    #贷款期数
loanProduct = ["55","56","58","63","65","66","701"][0]    #正好快贷产品编号 55,公务员方案,56,公积金方案,58,保单方案,63,精英方案,65,工薪方案,66,优房方案,701,微粒方案
grantAmount = "500"    #批准额度
loanStatus = "APPLICATION_PASS"    #初审/复审状态

# -----------------------------------------------------------------------------------------
# -------------------销售登录------------------------------------------------------------------------------
loginSale = "ZHHQ01080"    #销售账号
salePasswd = "a654321."    #销售账号密码

# -----------------------------------------------------------------------------------------
# -------------------注册授权------------------------------------------------------------------------------
realName = u"张洪嘉"
mobile = "18781972711"
custcertNo = "510322199206123475"   #客户身份证号

bankcardNo = "6228410334569010273"   #银行卡号
openBankCode = u"招商银行"   #开户银行
bankDescribe = u"成都支行"   #银行支行
