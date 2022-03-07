# Author -- Chris Silos
# EM 624

# Exercise 05

# This is a program that processes a file about COVID-19 corobidities and displays basic information through a bar chart and pie chart

# The program outputs the following information for the file
# 1. The corobidity with the highest number of deaths below the age of 35
# 2. Bar chart displaying the number of deaths by each age group
# 3. Pie chart with the same information as #2

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Read file into pandas dataframe
df = pd.read_csv('covid_comorbidities_USsummary.csv') 

# Drop all rows with COVID-19 as the condition (these rows have no comorbidity)
df_without_covid = df.drop(df[df['Condition']=='COVID-19'].index) 

# Create dataframe that only holds rows with ages below 35
younger_than_35 = df_without_covid[(df_without_covid['Age Group'] == '0-24') | (df_without_covid['Age Group'] == '25-34')]

# Create a new dataframe ordered by number of deaths
ordered_by_deaths = younger_than_35.groupby(['Condition']).sum().sort_values(by='COVID-19 Deaths', ascending=False).reset_index()
max_deaths = ordered_by_deaths['COVID-19 Deaths'][0] # Select the maximum number of deaths from the dataframe
max_deaths_condition = ordered_by_deaths['Condition'][0] # Select the condition with the maximum number of deaths from the dataframe
print(f'\nThe comorbidity with the highest amount of deaths below age 35 was "{max_deaths_condition}" with {max_deaths} deaths\n') # Print results

# Create dataframe with number of deaths by age group
deaths_by_age_group = df_without_covid.groupby(['Age Group']).sum() 
# Remove 'All Ages' and 'Not stated'
deaths_by_age_group = deaths_by_age_group[deaths_by_age_group.index != 'All Ages']
deaths_by_age_group = deaths_by_age_group[deaths_by_age_group.index != 'Not stated']
print(deaths_by_age_group)

# Create list of names and values for the bar chart
names = list(deaths_by_age_group.index)
values = list(deaths_by_age_group['COVID-19 Deaths'])

# Create bar chart
f = plt.figure(figsize = (16,12))
f.suptitle ('COVID-19 Comorbidity Death Counts by Age Group (USA)', fontsize=26)
ax = f.add_subplot(221)
ax.bar(names, values)
ax.set_xlabel('Age Group', fontsize=16)
ax.set_ylabel('Deaths', fontsize=16)

# Re-order name and value lists to avoid putting slices with small percentages next to each other (poor visibility)
values_pie = [values[1],values[4],values[2],values[3],values[0],values[5],values[6],values[7]]
names_pie = [names[1],names[4],names[2],names[3],names[0],names[5],names[6],names[7]]

# Create pie chart
ax2 = f.add_subplot(222)
ax2.pie(values_pie, labels=names_pie, autopct='%.1f%%', pctdistance=0.8, labeldistance=1.1)
ax2.legend(loc='upper left', labels=names_pie, title='Age Group')
plt.show()