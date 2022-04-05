import sqlite3
import math
import matplotlib.pyplot as plt
import numpy as np 

db = sqlite3.connect("nau.db")

# functions 


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
    print("num", num)
    print("total", total)
    newnum = math.floor(num/total*100)
    return(newnum)


#main code 

# gets total number of student by counting unique student numbers = 30832
total_students = db.execute("SELECT DISTINCT COUNT(STUDENT_ID) FROM naudata")

for ts in total_students: 
    #assigns that number to a global variable to be used later 
    global num_tot
    num_tot = ts[0]

# looks at general retention vs not retained 
ret = db.execute("SELECT DISTINCT COUNT(STUDENT_ID) FROM naudata WHERE ENROLLED_FALL_2020='Y'")
for r in ret: 
    global gen_ret 
    gen_ret = r[0]
    

notret= db.execute("SELECT DISTINCT COUNT(STUDENT_ID)FROM naudata WHERE ENROLLED_FALL_2020='N/A'")
for nt in notret: 
    global gen_not 
    gen_not = nt[0]

print("Total students Reatained: ") 
num_per(gen_ret, num_tot)

print("Total students Not Retained: ")
#percent(notret, num_tot)
num_per(gen_not, num_tot)
def gen_pie(ret, notret):
        y = np.array([ret, notret])
        mylabels = ["Retained", "Not Retained"]
        plt.pie(y, labels = mylabels)
        plt.legend(title = "General Students")
        plt.show()
        return 
#gen_pie(gen_ret, gen_not)
    

# looks to see total number and percent of females and males as well as retention rates 
female = db.execute("SELECT DISTINCT COUNT(STUDENT_ID) FROM naudata WHERE GENDER='F'")
for f in female: 
    global gen_female 
    gen_female = f[0] 
    
print("Female: ")
femper = num_per(gen_female, num_tot)
femret = get_per_ret("GENDER='F'")
femnot = get_per_not("GENDER='F'")
print(femret, femnot)

male = db.execute("SELECT DISTINCT COUNT(STUDENT_ID) FROM naudata WHERE GENDER='M'")
for m in male: 
    global gen_male
    gen_male = m[0]
print("Male: ") 
maleper = num_per(gen_male, num_tot)
maleret = get_per_ret("GENDER='M'")
malenot = get_per_not("GENDER='M'")

def gender_pie(male, female): 
    y = np.array([male, female])
    mylabels = ["Male", "Female"]
    plt.pie(y, labels= mylabels)
    plt.legend(title= "Gender")
    plt.show()
    return 
#gender_pie(gen_male, gen_female)

def gender_ret(maleret, malenot, femret, femnot):
    y = np.array([maleret, malenot, femret, femnot])
    mylabs = ["Males Retained", "Males Not", "Females Retained", "Females Not"]
    plt.pie(y, labels = mylabs)
    plt.legend(title = "Gender Retention")
    plt.show()
    return 
#gender_ret(maleret, malenot, femret, femnot)

# gets the total number and percent of studnet per cohort FTF, LD and UD and retention rates 
ftf = db.execute("SELECT DISTINCT COUNT(STUDENT_ID) FROM naudata WHERE COHORT_TYPE='FTF'")
print("FTF: ")
for f in ftf: 
    global ftf_num 
    ftf_num = f[0]
ftfper = num_per(ftf_num, num_tot)
ftfret = get_per_ret("COHORT_TYPE='FTF'")
ftfnot = get_per_not("COHORT_TYPE='FTF'")


ld = db.execute("SELECT DISTINCT COUNT(STUDENT_ID) FROM naudata WHERE COHORT_TYPE='LD'")
print("LD: ")
for l in ld: 
    global ld_num 
    ld_num = l[0]
ldper = num_per(ld_num, num_tot)
ldret = get_per_ret("COHORT_TYPE='LD'")
ldnot = get_per_not("COHORT_TYPE='LD'")


ud = db.execute("SELECT DISTINCT COUNT(STUDENT_ID) FROM naudata WHERE COHORT_TYPE='UD'")
print("UD: ")
for u in ud: 
    global ud_num 
    ud_num = u[0]
    
udper = num_per(ud_num, num_tot)
udret = get_per_ret("COHORT_TYPE='UD'")

udnot = get_per_not("COHORT_TYPE='UD'")

na = db.execute("SELECT DISTINCT COUNT(STUDENT_ID) FROM naudata WHERE COHORT_TYPE='N/A'")
for n in na: 
    global na_num
    na_num = n[0]
naper = num_per(na_num, num_tot)
naret = get_per_ret("COHORT_TYPE='N/A'")
nanot = get_per_not("COHORT_TYPE='N/A'")


def cohort_pie(ftf_num, ld_num, ud_num, na_num):
    y = np.array([ftf_num, ld_num, ud_num, na_num])
    mylabs = ["FTF", "LD", "UD", "N/A"]
    plt.pie(y, labels = mylabs)
    plt.legend(title="Cohort Types")
    plt.show()
    return 

#cohort_pie(ftf_num, ld_num, ud_num, na_num)

def cohort_ret(ftfret, ftfnot, ldret, ldnot, udret, udnot, naret, nanot): 
    y = np.array([ftfret, ftfnot, ldret, ldnot, udret, udnot, naret, nanot])
    mylabs = ["FTF Retained", "FTF Not", "LD Retained", "LD Not", "UD Retained", "UD Not", "N/A Retained", "N/A Not"]
    plt.pie(y, labels=mylabs)
    plt.legend(title= "Cohorts Retention", loc='upper left')
    plt.show()
    return 
#cohort_ret(ftfret, ftfnot, ldret, ldnot, udret, udnot, naret, nanot)

def cohort_ret_short(ftfret, ftfnot, ldret, ldnot, udret, udnot): 
    y = np.array([ftfret, ftfnot, ldret, ldnot, udret, udnot])
    mylabs = ["FTF Retained", "FTF Not", "LD Retained", "LD Not", "UD Retained", "UD Not"]
    plt.pie(y, labels=mylabs)
    plt.legend(title= "Cohorts Retention", loc='upper left')
    plt.show()
    return 
#cohort_ret_short(ftfret, ftfnot, ldret, ldnot, udret, udnot)

# gets the total number/percent of students who identify as white and retention rates 
white = db.execute("SELECT DISTINCT COUNT(STUDENT_ID) FROM naudata WHERE N__IPEDS_ETHNICITY='WHITE'")
for w in white: 
    global w_num
    w_num = w[0]
print("White: ", w_num)
whiteper = num_per(w_num, num_tot)
whiteret = get_per_ret("N__IPEDS_ETHNICITY='WHITE'")
whitenot = get_per_not("N__IPEDS_ETHNICITY='WHITE'")

# gets the total nubmer/percentage of students who identify as non white and their retention rates 
non_white = db.execute("SELECT DISTINCT COUNT(STUDENT_ID) FROM naudata WHERE NOT N__IPEDS_ETHNICITY='WHITE'")
for nw in non_white: 
    global nw_num 
    nw_num = nw[0]
    
print("Non-White: ", nw_num)
nwper = num_per(nw_num, num_tot)
nonret = get_per_ret("NOT N__IPEDS_ETHNICITY='WHITE'")

nonnot = get_per_not("NOT N__IPEDS_ETHNICITY='WHITE'")

def eth_pie(w_num, nw_num): 
    y = np.array([w_num, nw_num])
    mylabs = ["White", "Non White"]
    plt.pie(y, labels = mylabs)
    plt.show()
    return 
#eth_pie(w_num, nw_num)

def gen_eth_ret(whiteret, whitenot, nonret, nonnot): 
    y = np.array([whiteret, whitenot, nonret, nonnot])
    mylabs = ["White Students Retained", "White Students Not", "Non White Students Retianed", "Non White Students Not"]
    plt.pie(y, labels = mylabs) 
    plt.show()
    return 
gen_eth_ret(whiteret, whitenot, nonret, nonnot)


#runs ethinicity fxn 
ethnicity()



                       