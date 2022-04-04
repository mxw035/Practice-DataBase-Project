import sqlite3
import math


db = sqlite3.connect("nau.db")

def percent(sql): 
    for x in sql:
        num = x[0]
        print(num)
        
        print("Percent of total", math.floor((num/30832)*100),"%")
    return 

total_students = db.execute("SELECT DISTINCT COUNT(STUDENT_ID) FROM naudata")

female = db.execute("SELECT DISTINCT COUNT(STUDENT_ID) FROM naudata WHERE GENDER='F'")
print("Female: ")
percent(female)
male = db.execute("SELECT DISTINCT COUNT(STUDENT_ID) FROM naudata WHERE GENDER='M'")
print("Male: ")
percent(male)
ftf = db.execute("SELECT DISTINCT COUNT(STUDENT_ID) FROM naudata WHERE COHORT_TYPE='FTF'")
print("FTF: ")
percent(ftf)
ld = db.execute("SELECT DISTINCT COUNT(STUDENT_ID) FROM naudata WHERE COHORT_TYPE='LD'")
print("LD: ")
percent(ld)
ud = db.execute("SELECT DISTINCT COUNT(STUDENT_ID) FROM naudata WHERE COHORT_TYPE='UD'")
print("UD: ")
percent(ud)

white = db.execute("SELECT DISTINCT COUNT(STUDENT_ID) FROM naudata WHERE N__IPEDS_ETHNICITY='WHITE'")
print("White: ")
percent(white)

non_white = db.execute("SELECT DISTINCT COUNT(STUDENT_ID) FROM naudata WHERE NOT N__IPEDS_ETHNICITY='WHITE'")
print("Non-White: ")
percent(non_white)

ret = db.execute("SELECT DISTINCT COUNT(STUDENT_ID) FROM naudata WHERE ENROLLED_FALL_2020='Y'")

notret= db.execute("SELECT DISTINCT COUNT(STUDENT_ID)FROM naudata WHERE ENROLLED_FALL_2020='N/A'")

print("Reatianed: ")
percent(ret)
print("Not Retained: ")
percent(notret)

def eth_R_NOT(e, num):
    eth_r = db.execute("SELECT DISTINCT COUNT(STUDENT_ID) FROM naudata WHERE N__IPEDS_ETHNICITY=? AND ENROLLED_FALL_2020='Y'", e)
    eth_not = db.execute("SELECT DISTINCT COUNT(STUDENT_ID) FROM naudata WHERE N__IPEDS_ETHNICITY=? AND ENROLLED_FALL_2020='N/A'", e)
    for r in eth_r: 
        for rn in eth_not: 
            num = int(num)
            r = int(r[0])
            rn = int(rn[0])
            print("Eth: ", e, "Ret: ", r, "Not: ", rn)
            print("Ret per: ", math.floor((r/num)*100), "%")
            print("Not per: ", math.floor((rn/num)*100), "%")
            
    return

def ethnicity():
    eth = db.execute("SELECT DISTINCT N__IPEDS_ETHNICITY FROM naudata")
    for e in eth: 
        #print("Eth: ", e)
        eth_num = db.execute("SELECT DISTINCT COUNT(STUDENT_ID) FROM naudata WHERE N__IPEDS_ETHNICITY=?", e)
        for ep in eth_num:
            per = math.floor((ep[0]/30832)*100)
            if per < 1: 
                per = "less than one"
                print("Eth: ", e, ep, per,"%")
            else: 
                print("Eth: ", e, ep, per,"%")
        
            eth_R_NOT(e, ep[0])
    return 
ethnicity()

def get_per_ret(getstr): 
    total = ("SELECT DISTINCT COUNT(STUDENT_ID) FROM naudata")
    ret_per = ("SELECT DISTINCT COUNT(STUDENT_ID) FROM naudata WHERE ENROLLED_FALL_2020='Y' AND ")
    newstr = ret_per + getstr
    newtotal = total + getstr
    answer = db.execute(newstr)
    for x in answer: 
        print(getstr, "Retained", x)
    return 

def get_per_not(getstr): 
    ret_per = ("SELECT DISTINCT COUNT(STUDENT_ID) FROM naudata WHERE ENROLLED_FALL_2020='N/A' AND ")
    newstr = ret_per + getstr
    answer = db.execute(newstr)
    for x in answer: 
        print(getstr, "Not: ", x)
    return 

get_per_ret("GENDER='F'")
get_per_not("GENDER='F'")
get_per_ret("GENDER='M'")
get_per_not("GENDER='M'")
                       