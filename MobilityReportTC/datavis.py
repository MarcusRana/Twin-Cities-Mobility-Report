import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def dataVis(State,County):
    df = pd.read_csv("2020_US_Region_Mobility_Report.csv")
    print("ReadCSV")
    df = df[df["sub_region_1"]==State]
    df = df[df["sub_region_2"]==County]
    df.loc[:, "date"] = pd.to_datetime(df.loc[:, "date"], format="%Y-%m-%d")
    makeData(df,"retail_and_recreation_percent_change_from_baseline","RetailRec",County)
    makeData(df,"grocery_and_pharmacy_percent_change_from_baseline","Grocery",County)
    makeData(df,"workplaces_percent_change_from_baseline","WorkPlace",County)

def makeData(df,category,x_title,County):
    y_values = df.loc[:, category]
    y_values = df.loc[:, category]
    x_values = np.linspace(0,1,len(df.loc[:, category]))
    poly_degree = 9

    coeffs = np.polyfit(x_values, y_values, poly_degree)
    poly_eqn = np.poly1d(coeffs)
    y_hat = poly_eqn(x_values)

    plt.figure(figsize=(12,8))
    plt.plot(df.loc[:, "date"], df.loc[:,category], "ro")
    plt.plot(df.loc[:, "date"],y_hat)
    plt.title('Twin Cities Mobility Report')
    plt.ylabel(x_title)
    plt.xlabel('Date')
    plt.savefig(f"mobility-report-{County}-{x_title}.png")

dataVis("Minnesota","Hennepin County")
dataVis("Minnesota","Ramsey County")