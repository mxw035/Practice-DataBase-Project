import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('naudata.csv')

#print(df.corr()) # just gives cohort_type na cohort_type
#print(df.duplicated()) # dosent appear to be any
print(df.info()) # 30832 entries, 0 to 30831, columns 8, non=null count cohort_type = 7794, enrolled_fall_2020 = 18485 

# remove cohort_type null 
#df["COHORT_TYPE"].dropna(inplace = True)#dosent change
#df["ENROLLED_FALL_2020"].dropna(inplace = True)# dosent change 
#df.dropna(inplace = True) 

print("After drop")
print(df.info())# now entries 5613, 0 - 18449, with 8 columns all non-null 5613

#df['FALL_COHORT'].plot(kind = 'hist')# returns over 5000 2019.1
#df['COHORT_TYPE'].plot(kind = 'hist') # no numberic data to plot so wont work 
#df['GENDER'].plot(kind = 'hist') # no numberic data 
#df['N__IPEDS_ETHNICITY'].plot(kind = 'hist') # no numeric data 
#df['ENROLLMENT_STATUS'].plot(kind = 'hist')# no numeric data 
#df['EXCLUSION_ELIGIBLE'].plot(kind = 'hist')# no numeric data 
#df['ENROLLED_FALL_2020'].plot(kind = 'hist') #no numeric data 

#plt.show()

# change data to number 
for x in df.index: 
    if df.loc[x, 'COHORT_TYPE'] == 'FTF':
        df.loc[x, "COHORT_TYPE"] = 1
    elif df.loc[x, 'COHORT_TYPE'] == "LD":
        df.loc[x, "COHORT_TYPE"] = 2
    elif df.loc[x, "COHORT_TYPE"] == "UD":
        df.loc[x, "COHORT_TYPE"] = 3
    else: 
        df.loc[x, "COHORT_TYPE"] = 4 
#df["COHORT_TYPE"].plot(kind = 'hist')
#plt.show()

for y in df.index: 
    if df.loc[y, 'GENDER'] == "F":
        df.loc[y, 'GENDER'] = 1
    else: 
        df.loc[y, 'GENDER'] = 2
#df['GENDER'].plot(kind = 'hist')
#plt.show()

for z in df.index: 
    if df.loc[z, 'N__IPEDS_ETHNICITY'] == "HISPA": 
        df.loc[z, 'N__IPEDS_ETHNICITY'] = 1
    elif df.loc[z, 'N__IPEDS_ETHNICITY'] == "AMIND":
        df.loc[z, 'N__IPEDS_ETHNICITY'] = 2
    elif df.loc[z, 'N__IPEDS_ETHNICITY'] == "ASIAN":
        df.loc[z, 'N__IPEDS_ETHNICITY'] = 3
    elif df.loc[z, 'N__IPEDS_ETHNICITY'] == "BLACK":
        df.loc[z, 'N__IPEDS_ETHNICITY'] = 4
    elif df.loc[z, 'N__IPEDS_ETHNICITY'] == "PACIF":
        df.loc[z, 'N__IPEDS_ETHNICITY'] = 5
    elif df.loc[z, 'N__IPEDS_ETHNICITY'] == "WHITE":
        df.loc[z, 'N__IPEDS_ETHNICITY'] = 6
    elif df.loc[z, 'N__IPEDS_ETHNICITY'] == "TWOMORE":
        df.loc[z, 'N__IPEDS_ETHNICITY'] = 7 
    elif df.loc[z, 'N__IPEDS_ETHNICITY'] == "INTL": 
        df.loc[z, 'N__IPEDS_ETHNICITY'] = 8 
    elif df.loc[z, 'N__IPEDS_ETHNICITY'] == "NSPEC":
        df.loc[z, 'N__IPEDS_ETHNICITY'] = 9 
    else: 
        df.loc[z, 'N__IPEDS_ETHNICITY'] = 0 
    
#df['N__IPEDS_ETHNICITY'].plot(kind = 'hist')
#plt.show()

for a in df.index: 
    if df.loc[a, 'ENROLLMENT_STATUS'] == 'F': 
        df.loc[a, 'ENROLLMENT_STATUS'] = 1
    elif df.loc[a, 'ENROLLMENT_STATUS'] == 'P':
        df.loc[a, 'ENROLLMENT_STATUS'] = 2 
#df['ENROLLMENT_STATUS'].plot(kind = 'hist')
#plt.show()

for b in df.index:
    if df.loc[b, 'EXCLUSION_ELIGIBLE'] == "Y":
        df.loc[b, 'EXCLUSION_ELIGIBLE'] = 1
    else: 
        df.loc[b, 'EXCLUSION_ELIGIBLE'] = 2
#df["EXCLUSION_ELIGIBLE"].plot(kind = 'hist')
#plt.show()

for c in df.index: 
    if df.loc[c, 'ENROLLED_FALL_2020'] == 'Y':
        df.loc[c, 'ENROLLED_FALL_2020'] = 1
    else: 
        df.loc[c, 'ENROLLED_FALL_2020'] = 2
#df["ENROLLED_FALL_2020"].plot(kind = 'hist')
#plt.show()

#df.plot(x = "COHORT_TYPE", y = "ENROLLED_FALL_2020")
#plt.show()
#print("Corr: ", df.corr())