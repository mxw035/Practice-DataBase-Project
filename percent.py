import sqlite3
import math


db = sqlite3.connect("nau.db")

# functions 

# percent fxn takes the ouput from a sql argument and the total number 
def percent(sql, total): 
    for x in sql:
        # assigns the out put to num
        num = x[0]
        total = int(total[0])
        # gets the percentage for num out of total students 
        print("Total: ", num, "Percentage: ", math.floor((num/total)*100),"%")
    return(num)

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
    ret_per = ("SELECT DISTINCT COUNT(STUDENT_ID) FROM naudata WHERE ENROLLED_FALL_2020='Y' AND ")
    newstr = ret_per + getstr
    answer = db.execute(newstr)
    for x in answer: 
        print(getstr, "Retained", x[0])
    return(x[0])

# same as get_per_ret but now changed for not retained. 
def get_per_not(getstr): 
    ret_per = ("SELECT DISTINCT COUNT(STUDENT_ID) FROM naudata WHERE ENROLLED_FALL_2020='N/A' AND ")
    newstr = ret_per + getstr
    answer = db.execute(newstr)
    for x in answer: 
        print(getstr, "Not: ", x[0])
    return(x[0])

# takes two numbers and gives back a percentage 
def num_per(num, total):
    newnum = math.floor(num/total*100)
    return(newnum)


#main code 

# gets total number of student by counting unique student numbers = 30832
total_students = db.execute("SELECT DISTINCT COUNT(STUDENT_ID) FROM naudata")

for ts in total_students: 
    #assigns that number to a global variable to be used later 
    global num_tot
    num_tot = ts

# looks at general retention vs not retained 
ret = db.execute("SELECT DISTINCT COUNT(STUDENT_ID) FROM naudata WHERE ENROLLED_FALL_2020='Y'")

notret= db.execute("SELECT DISTINCT COUNT(STUDENT_ID)FROM naudata WHERE ENROLLED_FALL_2020='N/A'")

print("Total students Reatained: ") 
percent(ret, num_tot)

print("Total students Not Retained: ")
percent(notret, num_tot)


# looks to see total number and percent of females and males as well as retention rates 
female = db.execute("SELECT DISTINCT COUNT(STUDENT_ID) FROM naudata WHERE GENDER='F'")
print("Female: ")
femnum = percent(female, num_tot)
femret = get_per_ret("GENDER='F'")
print("Percent: ", num_per(femret, femnum), "%")
femnot = get_per_not("GENDER='F'")
print("Percent: ", num_per(femnot, femnum), "%")

male = db.execute("SELECT DISTINCT COUNT(STUDENT_ID) FROM naudata WHERE GENDER='M'")
print("Male: ") 
malenum = percent(male, num_tot)
maleret = get_per_ret("GENDER='M'")
print("Percent: ", num_per(maleret, malenum), "%")
malenot = get_per_not("GENDER='M'")
print("Percent: ", num_per(malenot, malenum), "%")


# gets the total number and percent of studnet per cohort FTF, LD and UD and retention rates 
ftf = db.execute("SELECT DISTINCT COUNT(STUDENT_ID) FROM naudata WHERE COHORT_TYPE='FTF'")
print("FTF: ")
ftftot = percent(ftf, num_tot)
ftfret = get_per_ret("COHORT_TYPE='FTF'")
print("Percentage: ", num_per(ftfret, ftftot), "%")

ftfnot = get_per_not("COHORT_TYPE='FTF'")
print("Percentage: ", num_per(ftfnot, ftftot), "%")


ld = db.execute("SELECT DISTINCT COUNT(STUDENT_ID) FROM naudata WHERE COHORT_TYPE='LD'")
print("LD: ")
ldtot = percent(ld, num_tot)
ldret = get_per_ret("COHORT_TYPE='LD'")
print("Percentage: ", num_per(ldret, ldtot), "%")

ldnot = get_per_not("COHORT_TYPE='LD'")
print("Percentage: ", num_per(ldnot, ldtot), "%")


ud = db.execute("SELECT DISTINCT COUNT(STUDENT_ID) FROM naudata WHERE COHORT_TYPE='UD'")
print("UD: ")
udtot = percent(ud, num_tot)
udret = get_per_ret("COHORT_TYPE='UD'")
print("Percentage: ", num_per(udret, udtot), "%")

udnot = get_per_not("COHORT_TYPE='UD'")
print("Percentage: ", num_per(udnot, udtot), "%")

# gets the total number/percent of students who identify as white and retention rates 
white = db.execute("SELECT DISTINCT COUNT(STUDENT_ID) FROM naudata WHERE N__IPEDS_ETHNICITY='WHITE'")
print("White: ")
whitetot = percent(white, num_tot)
whiteret = get_per_ret("N__IPEDS_ETHNICITY='WHITE'")
print("Percentage: ", num_per(whiteret, whitetot), "%")
whitenot = get_per_not("N__IPEDS_ETHNICITY='WHITE'")
print("Percentage: ", num_per(whitenot, whitetot), "%")

# gets the total nubmer/percentage of students who identify as non white and their retention rates 
non_white = db.execute("SELECT DISTINCT COUNT(STUDENT_ID) FROM naudata WHERE NOT N__IPEDS_ETHNICITY='WHITE'")
print("Non-White: ")
nonwhitetot = percent(non_white, num_tot)
nonret = get_per_ret("NOT N__IPEDS_ETHNICITY='WHITE'")
print("Percentage: ", num_per(nonret, nonwhitetot), "%")

nonnot = get_per_not("NOT N__IPEDS_ETHNICITY='WHITE'")
print("Percentage: ", num_per(nonnot, nonwhitetot), "%")





#runs ethinicity fxn 
ethnicity()



                       
