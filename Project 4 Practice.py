#This is essentially Project 4 for class.
#Import Pandas & Matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

#Read the Life Expectancy csv file & separate it using commas.
life_expect_dataset = pd.read_csv("Life Expectancy.csv", sep=",")

#Drop any missing values from the dataset
life_expect_nonull_dataset = life_expect_dataset.dropna()

#Drop columns with incorrect data. To permanently take out columns, put "inplace = True". Test this out by taking out the Status column.
life_expect_nonull_dataset.drop(['Status'], axis=1, inplace = True)

#Check to see that the Status column did drop.
life_expect_nonull_dataset.columns

#Drop remaining columns with incorrect data.
life_expect_nonull_dataset.drop(['infant deaths', 'percentage expenditure', 'Hepatitis B', 'Measles ', 'under-five deaths ', ' HIV/AIDS', 'GDP', ' thinness  1-19 years', ' thinness 5-9 years'], axis=1, inplace = True)
life_expect_nonull_dataset.drop([' BMI '], axis=1, inplace = True)

#Store the new life expectancy dataframe into a new variable.
new_life_expect = life_expect_nonull_dataset



#THIS IS FOR EXPORTING THE NEW DATAFRAME TO A NEW FILE

root = tk.Tk()

canvas1 = tk.Canvas(root, width=300, height=300, bg='lightsteelblue2', relief='raised')
canvas1.pack()

#This is a global dataframe function. Will be used to export current data to a new csv file.
def exportCSV():
    global df

    export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
    new_life_expect.to_csv(export_file_path, index=False, header=True)

#This is the look of the graphical user interface/dialogue box.
saveAsButton_CSV = tk.Button(text='Export CSV', command=exportCSV, bg='green', fg='white',
                             font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 150, window=saveAsButton_CSV)

root.mainloop()








