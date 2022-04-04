import sqlite3
import math


db = sqlite3.connect("nau.db")

# functions 

# percent fxn takes the ouput from a sql argument 
def percent(sql): 
    for x in sql:
        # assigns the out put to num
        num = x[0]
        print(num)
        # gets the percentage for num out of total students 
        print("Percent of total", math.floor((num/30832)*100),"%")
    return 

# ethnicity retention or not takes the ethnicity name as e , then the total number of students who identify with that ethnicity as num 

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
# function ethnicity 
def ethnicity():
    # gets ethnicity names 
    eth = db.execute("SELECT DISTINCT N__IPEDS_ETHNICITY FROM naudata")
    for e in eth: 
        #print("Eth: ", e)
        #gets the total amount of students who identify as that ethnicity
        eth_num = db.execute("SELECT DISTINCT COUNT(STUDENT_ID) FROM naudata WHERE N__IPEDS_ETHNICITY=?", e)
        for ep in eth_num:
            #gets the  percentage of students per ethnicity 
            per = math.floor((ep[0]/30832)*100)
            if per < 1: 
                per = "less than one"
                print("Eth: ", e, ep, per,"%")
            else: 
                print("Eth: ", e, ep, per,"%")
            # takes the ethnicity name (e) and the total number of students who identify as that ethnicity (ep[0]) and plugs them in to the eth_R_NOT fxn to get retention vs non retention numbers and percentage. 
            eth_R_NOT(e, ep[0])
    return 
# fxn get_per_ret gets total number of students (total) takes a str as argument and looks at the retention rate for students specified
def get_per_ret(getstr): 
    total = ("SELECT DISTINCT COUNT(STUDENT_ID) FROM naudata")
    ret_per = ("SELECT DISTINCT COUNT(STUDENT_ID) FROM naudata WHERE ENROLLED_FALL_2020='Y' AND ")
    newstr = ret_per + getstr
    newtotal = total + getstr
    answer = db.execute(newstr)
    for x in answer: 
        print(getstr, "Retained", x)
    return 
# same as get_per_ret but now changed for not retained. 
def get_per_not(getstr): 
    ret_per = ("SELECT DISTINCT COUNT(STUDENT_ID) FROM naudata WHERE ENROLLED_FALL_2020='N/A' AND ")
    newstr = ret_per + getstr
    answer = db.execute(newstr)
    for x in answer: 
        print(getstr, "Not: ", x)
    return 

#main code 

# gets total number of student by counting unique student numbers = 30832
total_students = db.execute("SELECT DISTINCT COUNT(STUDENT_ID) FROM naudata")

# looks to see total number of females and males 
female = db.execute("SELECT DISTINCT COUNT(STUDENT_ID) FROM naudata WHERE GENDER='F'")
print("Female: ")
percent(female)
male = db.execute("SELECT DISTINCT COUNT(STUDENT_ID) FROM naudata WHERE GENDER='M'")
print("Male: ")
percent(male)

# looks at the male/females and the numbers for retain vs not retained 
get_per_ret("GENDER='F'")
get_per_not("GENDER='F'")
get_per_ret("GENDER='M'")
get_per_not("GENDER='M'")

# gets the total number of studnet per cohort FTF, LD and UD 
ftf = db.execute("SELECT DISTINCT COUNT(STUDENT_ID) FROM naudata WHERE COHORT_TYPE='FTF'")
print("FTF: ")
# gets percent of ftf students 
percent(ftf)
ld = db.execute("SELECT DISTINCT COUNT(STUDENT_ID) FROM naudata WHERE COHORT_TYPE='LD'")
print("LD: ")
# gets percent of ld students 
percent(ld)
ud = db.execute("SELECT DISTINCT COUNT(STUDENT_ID) FROM naudata WHERE COHORT_TYPE='UD'")
print("UD: ")
# gets percent of ud students 
percent(ud)

# gets the total number of students who identify as white and their percentage 
white = db.execute("SELECT DISTINCT COUNT(STUDENT_ID) FROM naudata WHERE N__IPEDS_ETHNICITY='WHITE'")
print("White: ")
percent(white)

# gets the total nubmer of students who identify as non white and their percentage 
non_white = db.execute("SELECT DISTINCT COUNT(STUDENT_ID) FROM naudata WHERE NOT N__IPEDS_ETHNICITY='WHITE'")
print("Non-White: ")
percent(non_white)

# looks at general retention vs not retained 
ret = db.execute("SELECT DISTINCT COUNT(STUDENT_ID) FROM naudata WHERE ENROLLED_FALL_2020='Y'")

notret= db.execute("SELECT DISTINCT COUNT(STUDENT_ID)FROM naudata WHERE ENROLLED_FALL_2020='N/A'")

print("Reatained: ")
percent(ret)
print("Not Retained: ")
percent(notret)

#runs ethinicity fxn 
ethnicity()



                       
