# Author -- Chris Silos
# EM 624

# Exercise 06

# This is a program that processes a file about Stevens SSE Courses and displays some properties of the dataset through 4 different graphs
# Each plot will be saved as an html file to the folder that this script is ran in

# The program outputs the following information for the file
# 1. Number of students in EM Courses by semester (Line chart)
# 2. Number of Students in EM Courses vs Number of students in SYS courses (Scatter plot)
# 3. Average enrollment by program (bar chart)
# 4. Enrollment for each program in 2020 (pie chart)

# Import libraries
from matplotlib.pyplot import bar
import pandas as pd
from bokeh.plotting import figure, show, output_file, save
from bokeh.layouts import row
import numpy as np

# Read file into pandas dataframe
df = pd.read_csv("SSE_Courses.csv") 
df = df.rename(columns={"Unnamed: 0":"Course"}) # Rename first column to 'Course'
df = df.set_index('Course') # Set the 'Course' column as the index of the dataframe

# ----- PART 1 -----

# Create list for x axis ticks
x = [1,2,3,4,5,6]
# Create list for y axis values
y = list(df.loc['EM'])

output_file(filename="EM_Students_by_Semester.html", title="EM Students by Semester")

# Create a new plot with a title and axis labels
line_plot = figure(title="EM Students by Semester", x_axis_label="Semester", y_axis_label="EM Enrollments")

# Add a line renderer with legend and line color
line_plot.line(x, y, legend_label="# of Students", line_width=2, line_color='green')

# Customize the values of the tickers on the x axis
line_plot.xaxis.ticker = x
line_plot.xaxis.major_label_overrides = {1: 'Spring 18', 2: 'Fall 18', 3: 'Spring 19', 4:'Fall 19', 5:'Spring 20', 6:'Fall 20'}

# Import library to manually set y axis limits
from bokeh.models import Range1d
line_plot.y_range = Range1d(50,250)
save(line_plot)


# ----- PART 2 -----

output_file(filename="EM_vs_SYS_Students.html", title="EM vs SYS Students")

# Create a new plot with a title and axis labels
scatter_plot = figure(title="EM vs SYS Students", x_axis_label="EM", y_axis_label="SYS")

# Plot EM data for x values and SYS data for y values
scatter_plot.circle(list(df.loc['EM']), list(df.loc['SYS']), size=10, color="red", alpha=1)

# Create limits for y axis
scatter_plot.y_range = Range1d(0,500)

save(scatter_plot)


# ----- PART 3 -----

# Calculate average enrollment for each course type
avg_EM = np.mean(df.loc['EM'])
avg_ES = np.mean(df.loc['ES'])
avg_ISE = np.mean(df.loc['ISE'])
avg_SSW = np.mean(df.loc['SSW'])
avg_SYS = np.mean(df.loc['SYS'])

output_file(filename="Average_Enrollment_by_Course.html", title="Average Enrollment by Program")

# Create list of courses and average enrollment per course
courses = list(df.index)
counts = [avg_EM, avg_ES, avg_ISE, avg_SSW, avg_SYS]

bar_chart = figure(x_range=courses, title="Average Enrollment by Program",
           toolbar_location=None, tools="", y_axis_label='# of Students', x_axis_label='Program')

bar_chart.vbar(x=courses, top=counts, width=0.9)

bar_chart.xgrid.grid_line_color = None
bar_chart.y_range.start = 0

save(bar_chart)


# ----- PART 4 -----

# Import libraries for pie chart
from math import pi
from bokeh.palettes import Category10
from bokeh.transform import cumsum

# Calculate total enrollment for 2020 for each of the courses
em_2020 = df.loc['EM']["Spring '20"] + df.loc['EM']["Fall '20"]
es_2020 = df.loc['ES']["Spring '20"] + df.loc['ES']["Fall '20"]
ise_2020 = df.loc['ISE']["Spring '20"] + df.loc['ISE']["Fall '20"]
ssw_2020 = df.loc['SSW']["Spring '20"] + df.loc['SSW']["Fall '20"]
sys_2020 = df.loc['SYS']["Spring '20"] + df.loc['SYS']["Fall '20"]

x = {
    'EM': em_2020,
    'ES': es_2020,
    'ISE': ise_2020,
    'SSW': ssw_2020,
    'SYS': sys_2020,
}

# Organize data into a form appropriate for plotting in a pie chart
data = pd.Series(x).reset_index(name='value').rename(columns={'index': 'Course'})
# Calculate the angle for each category in the pie chart
data['angle'] = data['value']/data['value'].sum() * 2*pi
data['color'] = Category10[len(x)]

output_file(filename="Total_2020_Enrollment_by_Course.html", title="Total 2020 Enrollment by Course")

# Create the pie chart
pie_chart = figure(title="Total 2020 Enrollment by Course", toolbar_location=None,
           tools="hover", tooltips="@Course: @value", x_range=(-0.5, 1.0))

# Create the wedges for the pie chart
pie_chart.wedge(x=0, y=1, radius=0.4,
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', legend_field='Course', source=data)


pie_chart.axis.axis_label = None
pie_chart.axis.visible = False
pie_chart.grid.grid_line_color = None

save(pie_chart)

##
# The code for the pie chart was based off the code from the Bokeh documentation shown below
#https://docs.bokeh.org/en/latest/docs/gallery/pie_chart.html