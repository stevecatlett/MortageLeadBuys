import pandas as pd
import seaborn as sns
import datetime
from matplotlib import pyplot as plt

#import the data from the excel file
df = pd.read_excel(r'C:\Users\catle\OneDrive\Documents\New folder\Better_Case_Raw_Data.xlsx')
#print(df)

#Change Dataframe to only include leads that received an application
app = df[df['APPLICATION'] == 1]
# print(app.head().to_string())

#Calculate average Cost of all leads
avgcost = df["COST"].mean()
# print(avgcost)

#Print Avgerage Cost of Lead with an Application
appavgcost = app["COST"].mean()
print("Original Cost Per Application $" + str(appavgcost))

#Calculate Average Cost Per Fund
fund= app[app["FUND"] == 1]
fundavgcost = fund["COST"].mean()
print("Original Cost Per Fund $" + str(fundavgcost))

#Calculate the Average Cost Per Application based on Credit Score
FairCreditCost=[] #LEss than 670
GoodCreditCost=[] #Between 670 and 740
VeryGoodcreditCost=[] #Between 740 and 800
ExCreditCost = [] #Greater than 800
for i in range(len(app)):
    if (app["EST_CREDIT_SCORE"].iloc[i] <= 670):
        FairCreditCost.append(app["COST"].iloc[i])

    elif (app["EST_CREDIT_SCORE"].iloc[i] > 670) & (app["EST_CREDIT_SCORE"].iloc[i] <= 740):
        GoodCreditCost.append(app["COST"].iloc[i])

    elif (app["EST_CREDIT_SCORE"].iloc[i] > 740) & (app["EST_CREDIT_SCORE"].iloc[i] <= 800):
        VeryGoodcreditCost.append(app["COST"].iloc[i])

    elif app["EST_CREDIT_SCORE"].iloc[i] > 800:
        ExCreditCost.append(app["COST"].iloc[i])

# print(FairCreditCost)
# print(GoodCreditCost)
# print(VeryGoodcreditCost)
# print(ExCreditCost)

Faircreditapp = sum(FairCreditCost)/len(FairCreditCost)
GoodCreditapp = sum(GoodCreditCost)/len(GoodCreditCost)
VeryGoodCreditapp = sum(VeryGoodcreditCost)/len(VeryGoodcreditCost)
ExceptionalCreditapp = sum(ExCreditCost)/len(ExCreditCost)

print("Fair Credit Cost Per Application $" + str(Faircreditapp))
print("Good Credit Cost Per Application $" + str(GoodCreditapp))
print("Very Good Credit Cost Per Application $" + str(VeryGoodCreditapp))
print("Exceptional Credit Cost Per Application $" + str(ExceptionalCreditapp))

#Calculate the Average Cost Per Application based on Loan Value
SmallLoanCost=[] #Less than 500K
MediumLoanCost=[] #Between 500k and 1M
LargeLoanCost=[] #Over 1M

for i in range(len(app)):
    if (app["LOAN_AMT"].iloc[i] <= 500000):
        SmallLoanCost.append(app["COST"].iloc[i])

    elif (app["LOAN_AMT"].iloc[i] > 500000) & (app["LOAN_AMT"].iloc[i] <= 1000000):
        MediumLoanCost.append(app["COST"].iloc[i])

    elif (app["LOAN_AMT"].iloc[i] > 1000000):
        LargeLoanCost.append(app["COST"].iloc[i])

# print(SmallLoanCost)
# print(MediumLoanCost)
# print(LargeLoanCost)

SmallLoanapp = sum(SmallLoanCost)/len(SmallLoanCost)
MediumLoanapp = sum(MediumLoanCost)/len(MediumLoanCost)
LargeLoanapp = sum(LargeLoanCost)/len(LargeLoanCost)


print("Small Loan Cost Per Application $" + str(SmallLoanapp))
print("Medium Loan Cost Per Application $" + str(MediumLoanapp))
print("Large Loan Cost Per Application $" + str(LargeLoanapp))

#Calculate the Average Cost Per Application based on Loan to Value Ratio
LVR60=[]
LVR60_80=[]
LVR80_100=[]

for i in range(len(app)):
    if (app["LOAN_TO_VALUE"].iloc[i] <= 60):
        LVR60.append(app["COST"].iloc[i])

    elif (app["LOAN_TO_VALUE"].iloc[i] > 60) & (app["LOAN_TO_VALUE"].iloc[i] <= 79):
        LVR60_80.append(app["COST"].iloc[i])

    elif (app["LOAN_TO_VALUE"].iloc[i] > 79):
        LVR80_100.append(app["COST"].iloc[i])

LVR60app = sum(LVR60)/len(LVR60)
LVR60_80app = sum(LVR60_80)/len(LVR60_80)
LVR80_100app = sum(LVR80_100)/len(LVR80_100)


print("Loan to Value Ratio Less than 60 Cost Per Application $" + str(LVR60app))
print("Loan to Value Ratio Between 60 and 80 Cost Per Application $" + str(LVR60_80app))
print("Loan to Value Ratio Greater than 80 Cost Per Application $" + str(LVR80_100app))



# Sorting Cost By Month
app['LEAD_CREATED_TIMESTAMP'] = pd.to_datetime(app['LEAD_CREATED_TIMESTAMP'])

app["month"]=pd.DatetimeIndex(app['LEAD_CREATED_TIMESTAMP']).month
app["year"]=pd.DatetimeIndex(app['LEAD_CREATED_TIMESTAMP']).year
print(app[['month','LEAD_CREATED_TIMESTAMP']])
MonthlyCost=app.groupby(['month',"year"])["COST"].sum()
Monthlyapp=app.groupby(['month','year'])["APPLICATION"].sum()

#Calculate the Average Monthly Applications and MOnthly costs
averagemonthlycost=sum(MonthlyCost)/len(MonthlyCost)
averagemonthlyapp=sum(Monthlyapp)/len(Monthlyapp)
print(averagemonthlycost)
print(averagemonthlyapp)


# Plotting Data to check for skewness in loan amount with respect to cost of lead
sns.scatterplot(x=app["COST"],y=app["LOAN_AMT"])
plt.xlabel('Cost')
plt.ylabel("Loan Amount")
plt.title("Cost vs. Loan Amount")
plt.show()

