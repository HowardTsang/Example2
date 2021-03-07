#print() the last item from both the year and the pop list to see what the predicted population for the year 2100 is. Use two print() functions.
#Before you can start, you should import matplotlib.pyplot as plt. pyplot is a sub-package of matplotlib, hence the dot.
#Use plt.plot() to build a line plot. year should be mapped on the horizontal axis, pop on the vertical axis. Don't forget to finish off with the show() function to actually display the plot.
# Print the last item from year and pop
print(year)
print(pop)


# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Make a line plot: year on the x-axis, pop on the y-axis
plt.plot(year,pop)

# Display the plot with plt.show()
plt.show()



#Print the last item from both the list gdp_cap, and the list life_exp; it is information about Zimbabwe.
#Build a line chart, with gdp_cap on the x-axis, and life_exp on the y-axis. Does it make sense to plot this data on a line plot?
#Don't forget to finish off with a plt.show() command, to actually display the plot.
# Print the last item of gdp_cap and life_exp
print(gdp_cap)
print(life_exp)

# Make a line plot, gdp_cap on the x-axis, life_exp on the y-axis
plt.plot(gdp_cap,life_exp)

# Display the plot
plt.show()



#Change the line plot that's coded in the script to a scatter plot.
#A correlation will become clear when you display the GDP per capita on a logarithmic scale. Add the line plt.xscale('log').
#Finish off your script with plt.show() to display the plot.
# Change the line plot below to a scatter plot
plt.scatter(gdp_cap, life_exp)

# Put the x-axis on a logarithmic scale
plt.xscale('log')

# Show plot
plt.show()




#Start from scratch: import matplotlib.pyplot as plt.
#Build a scatter plot, where pop is mapped on the horizontal axis, and life_exp is mapped on the vertical axis.
#Finish the script with plt.show() to actually display the plot. Do you see a correlation?
# Import package
import matplotlib.pyplot as plt

# Build Scatter plot
plt.scatter(pop,life_exp)

# Show plot
plt.show()



#Use plt.hist() to create a histogram of the values in life_exp. Do not specify the number of bins; Python will set the number of bins to 10 by default for you.
#Add plt.show() to actually display the histogram. Can you tell which bin contains the most observations?
# Create histogram of life_exp data
plt.hist(life_exp)

# Display histogram
plt.show()





#Build a histogram of life_exp, with 5 bins. Can you tell which bin contains the most observations?
#Build another histogram of life_exp, this time with 20 bins. Is this better?
# Build histogram with 5 bins
plt.hist(life_exp, bins = 5)

# Show and clear plot
plt.show()
plt.clf()

# Build histogram with 20 bins
plt.hist(life_exp, bins = 20)

# Show and clear plot again
plt.show()
plt.clf()



#Build a histogram of life_exp with 15 bins.
#Build a histogram of life_exp1950, also with 15 bins. Is there a big difference with the histogram for the 2007 data?
# Histogram of life_exp, 15 bins
plt.hist(life_exp, bins = 15)

# Show and clear plot
plt.show()
plt.clf()

# Histogram of life_exp1950, 15 bins
plt.hist(life_exp1950, bins = 15)

# Show and clear plot again
plt.show()
plt.clf()




#The strings xlab and ylab are already set for you. Use these variables to set the label of the x- and y-axis.
#The string title is also coded for you. Use it to add a title to the plot.
#After these customizations, finish the script with plt.show() to actually display the plot.
# Basic scatter plot, log scale
plt.scatter(gdp_cap, life_exp)
plt.xscale('log')

# Strings
xlab = 'GDP per Capita [in USD]'
ylab = 'Life Expectancy [in years]'
title = 'World Development in 2007'

# Add axis labels
plt.xlabel(xlab)
plt.ylabel(ylab)

# Add title
plt.title(title)

# After customizing, display the plot
plt.show()




#Use tick_val and tick_lab as inputs to the xticks() function to make the the plot more readable.
#As usual, display the plot with plt.show() after you've added the customizations.
# Scatter plot
plt.scatter(gdp_cap, life_exp)

# Previous customizations
plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')

# Definition of tick_val and tick_lab
tick_val = [1000, 10000, 100000]
tick_lab = ['1k', '10k', '100k']

# Adapt the ticks on the x-axis
plt.xticks(tick_val,tick_lab)

# After customizing, display the plot
plt.show()




#Import the numpy package as np.
#Use np.array() to create a numpy array from the list pop. Call this Numpy array np_pop.
#Double the values in np_pop setting the value of np_pop equal to np_pop * 2. Because np_pop is a Numpy array, each array element will be doubled.
#Change the s argument inside plt.scatter() to be np_pop instead of pop.
# Import numpy as np
import numpy as np

# Store pop as a numpy array: np_pop
np_pop = np.array(pop)

# Double np_pop
np_pop = np_pop * 2

# Update: set s argument to np_pop
plt.scatter(gdp_cap, life_exp, s = np_pop)

# Previous customizations
plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])

# Display the plot
plt.show()




#Add c = col to the arguments of the plt.scatter() function.
#Change the opacity of the bubbles by setting the alpha argument to 0.8 inside plt.scatter(). Alpha can be set from zero to one, where zero is totally transparent, and one is not at all transparent.
# Specify c and alpha inside plt.scatter()
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2 , c = col, alpha = 0.8)

# Previous customizations
plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

# Show the plot
plt.show()




#Add plt.grid(True) after the plt.text() calls so that gridlines are drawn on the plot.
# Scatter plot
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8)

# Previous customizations
plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

# Additional customizations
plt.text(1550, 71, 'India')
plt.text(5700, 80, 'China')

# Add grid() call
plt.grid(True)

# Show the plot
plt.show()




#Use the index() method on countries to find the index of 'germany'. Store this index as ind_ger.
#Use ind_ger to access the capital of Germany from the capitals list. Print it out.
# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# Get index of 'germany': ind_ger
ind_ger = countries.index('germany')

# Use ind_ger to print out capital of Germany
print(capitals[ind_ger])



#With the strings in countries and capitals, create a dictionary called europe with 4 key:value pairs. Beware of capitalization! Make sure you use lowercase characters everywhere.
#Print out europe to see if the result is what you expected.
# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# From string in countries and capitals, create dictionary europe
europe = { 'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Print europe
print(europe)



#Check out which keys are in europe by calling the keys() method on europe. Print out the result.
#Print out the value that belongs to the key 'norway'.
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Print out the keys in europe
print(europe.keys())

# Print out value that belongs to key 'norway'
print(europe['norway'])




#Add the key 'italy' with the value 'rome' to europe.
#To assert that 'italy' is now a key in europe, print out 'italy' in europe.
#Add another key:value pair to europe: 'poland' is the key, 'warsaw' is the corresponding value.
#Print out europe.
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Add italy to europe
europe['italy'] = 'rome'

# Print out italy in europe
print('italy' in europe)

# Add poland to europe
europe['poland'] = 'warsaw'

# Print europe
print(europe)




#The capital of Germany is not 'bonn'; it's 'berlin'. Update its value.
#Australia is not in Europe, Austria is! Remove the key 'australia' from europe.
#Print out europe to see if your cleaning work paid off.
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
          'australia':'vienna' }

# Update capital of germany
europe['germany'] = 'berlin'

# Remove australia
del(europe['australia'])

# Print europe
print(europe)




#Use chained square brackets to select and print out the capital of France.
#Create a dictionary, named data, with the keys 'capital' and 'population'. Set them to 'rome' and 59.83, respectively.
#Add a new key-value pair to europe; the key is 'italy' and the value is data, the dictionary you just built.
# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }


# Print out the capital of France
print(europe['france']['capital'])

# Create sub-dictionary data
data = { 'capital':'rome', 'population':59.83 }

# Add data to europe under key 'italy'
europe['italy'] = data

# Print europe
print(europe)




#Import pandas as pd.
#Use the pre-defined lists to create a dictionary called my_dict. There should be three key value pairs:
#key 'country' and value names.
#key 'drives_right' and value dr.
#key 'cars_per_cap' and value cpc.
#Use pd.DataFrame() to turn your dict into a DataFrame called cars.
#Print out cars and see how beautiful it is.
# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)

# Print cars
print(cars)




#Hit Run Code to see that, indeed, the row labels are not correctly set.
#Specify the row labels by setting cars.index equal to row_labels.
#Print out cars again and check if the row labels are correct this time.
import pandas as pd

# Build cars DataFrame
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
cars_dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
cars = pd.DataFrame(cars_dict)
print(cars)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels

# Print cars again
print(cars)




#To import CSV files you still need the pandas package: import it as pd.
#Use pd.read_csv() to import cars.csv data as a DataFrame. Store this dataframe as cars.
#Print out cars. Does everything look OK?
# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv('cars.csv')

# Print out cars
print(cars)




#Run the code with Run Code and assert that the first column should actually be used as row labels.
#Specify the index_col argument inside pd.read_csv(): set it to 0, so that the first column is used as row labels.
#Has the printout of cars improved now?
# Import pandas as pd
import pandas as pd

# Fix import by including index_col
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out cars
print(cars)




#Use single square brackets to print out the country column of cars as a Pandas Series.
#Use double square brackets to print out the country column of cars as a Pandas DataFrame.
#Use double square brackets to print out a DataFrame with both the country and drives_right columns of cars, in this order.
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out country column as Pandas Series
print(cars['country'])

# Print out country column as Pandas DataFrame
print(cars[['country']])

# Print out DataFrame with country and drives_right columns
print(cars[['country', 'drives_right']])




#Select the first 3 observations from cars and print them out.
#Select the fourth, fifth and sixth observation, corresponding to row indexes 3, 4 and 5, and print them out.
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out first 3 observations
print(cars[0:3])

# Print out fourth, fifth and sixth observation
print(cars[3:6])




#Use loc or iloc to select the observation corresponding to Japan as a Series. The label of this row is JPN, the index is 2. Make sure to print the resulting Series.
#Use loc or iloc to select the observations for Australia and Egypt as a DataFrame. You can find out about the labels/indexes of these rows by inspecting cars in the IPython Shell. Make sure to print the resulting DataFrame.
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out observation for Japan
print(cars.iloc[2])

# Print out observations for Australia and Egypt
print(cars.loc[['AUS', 'EG']])




#Print out the drives_right value of the row corresponding to Morocco (its row label is MOR)
#Print out a sub-DataFrame, containing the observations for Russia and Morocco and the columns country and drives_right.
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out drives_right value of Morocco
print(cars.iloc[5, 2])

# Print sub-DataFrame
print(cars.loc[['RU', 'MOR'], ['country', 'drives_right']])



#Print out the drives_right column as a Series using loc or iloc.
#Print out the drives_right column as a DataFrame using loc or iloc.
#Print out both the cars_per_cap and drives_right column as a DataFrame using loc or iloc.
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out drives_right column as Series
print(cars.iloc[:, 2])

# Print out drives_right column as DataFrame
print(cars.iloc[:, [2]])

# Print out cars_per_cap and drives_right as DataFrame
print(cars.loc[:, ['cars_per_cap', 'drives_right']])




#In the editor on the right, write code to see if True equals False.
#Write Python code to check if -5 * 15 is not equal to 75.
#Ask Python whether the strings "pyscript" and "PyScript" are equal.
#What happens if you compare booleans and integers? Write code to see if True and 1 are equal.
# Comparison of booleans
print(True == False)

# Comparison of integers
print(-5 * 15 != 75)

# Comparison of strings
print("pyscript" == "PyScript")

# Compare a boolean with a numeric
print(True == 1)



#Write Python expressions, wrapped in a print() function, to check whether:
#x is greater than or equal to -10. x has already been defined for you.
#"test" is less than or equal to y. y has already been defined for you.
#True is greater than False.
# Comparison of integers
x = -3 * 6
print(x >= -10)

# Comparison of strings
y = "test"
print("test" <= y)

# Comparison of booleans
print(True > False)



#Using comparison operators, generate boolean arrays that answer the following questions:
#Which areas in my_house are greater than or equal to 18?
#You can also compare two Numpy arrays element-wise. Which areas in my_house are smaller than the ones in your_house?
#Make sure to wrap both commands in a print() statement so that you can inspect the output!
# Create arrays
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than or equal to 18
print(my_house >= 18)

# my_house less than your_house
print(my_house < your_house)




#Write Python expressions, wrapped in a print() function, to check whether:
#my_kitchen is bigger than 10 and smaller than 18.
#my_kitchen is smaller than 14 or bigger than 17.
#double the area of my_kitchen is smaller than triple the area of your_kitchen.
# Define variables
my_kitchen = 18.0
your_kitchen = 14.0

# my_kitchen bigger than 10 and smaller than 18?
print(my_kitchen > 10 and my_kitchen < 18)

# my_kitchen smaller than 14 or bigger than 17?
print(my_kitchen < 14 or my_kitchen > 17)

# Double my_kitchen smaller than triple your_kitchen?
print(my_kitchen * 2 < your_kitchen * 3)



#Generate boolean arrays that answer the following questions:
#Which areas in my_house are greater than 18.5 or smaller than 10?
#Which areas are smaller than 11 in both my_house and your_house? Make sure to wrap both commands in print() statement, so that you can inspect the output.
# Create arrays
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than 18.5 or smaller than 10
print(np.logical_or(my_house > 18.5, my_house < 10))

# Both my_house and your_house smaller than 11
print(np.logical_and(my_house < 11, your_house < 11))




#Examine the if statement that prints out "Looking around in the kitchen." if room equals "kit".
#Write another if statement that prints out "big place!" if area is greater than 15.
# Define variables
room = "kit"
area = 14.0

# if statement for room
if room == "kit" :
    print("looking around in the kitchen.")

# if statement for area
if area > 15 :
    print("big place!")



#Add an else statement to the second control structure so that "pretty small." is printed out if area > 15 evaluates to False.
# Define variables
room = "kit"
area = 14.0

# if-else construct for room
if room == "kit" :
    print("looking around in the kitchen.")
else :
    print("looking around elsewhere.")

# if-else construct for area
if area > 15 :
    print("big place!")
else :
    print("pretty small.")





#Add an elif to the second control structure such that "medium size, nice!" is printed out if area is greater than 10.
# Define variables
room = "bed"
area = 14.0

# if-elif-else construct for room
if room == "kit" :
    print("looking around in the kitchen.")
elif room == "bed":
    print("looking around in the bedroom.")
else :
    print("looking around elsewhere.")

# if-elif-else construct for area
if area > 15 :
    print("big place!")
elif area > 10 :
    print("medium size, nice!")
else :
    print("pretty small.")




#Extract the drives_right column as a Pandas Series and store it as dr.
#Use dr, a boolean Series, to subset the cars DataFrame. Store the resulting selection in sel.
#Print sel, and assert that drives_right is True for all observations.
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Extract drives_right column as Series: dr
dr = cars['drives_right']

# Use dr to subset cars: sel
sel = cars[dr]

# Print sel
print(sel)



#Convert the code on the right to a one-liner that calculates the variable sel as before.
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Convert code to a one-liner
sel = cars[cars['drives_right']]

# Print sel
print(sel)



#Select the cars_per_cap column from cars as a Pandas Series and store it as cpc.
#Use cpc in combination with a comparison operator and 500. You want to end up with a boolean Series that's True if the corresponding country has a cars_per_cap of more than 500 and False otherwise. Store this boolean Series as many_cars.
#Use many_cars to subset cars, similar to what you did before. Store the result as car_maniac.
#Print out car_maniac to see if you got it right.
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Create car_maniac: observations that have a cars_per_cap over 500
cpc = cars['cars_per_cap']
many_cars = cpc > 500
car_maniac = cars[many_cars]

# Print car_maniac
print(car_maniac)



#Use the code sample above to create a DataFrame medium, that includes all the observations of cars that have a cars_per_cap between 100 and 500.
#Print out medium.
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Import numpy, you'll need this
import numpy as np

# Create medium: observations with cars_per_cap between 100 and 500
cpc = cars['cars_per_cap']
between = np.logical_and(cpc > 100, cpc < 500)
medium = cars[between]

# Print medium
print(medium)




#Create the variable offset with an initial value of 8.
#Code a while loop that keeps running as long as offset is not equal to 0. Inside the while loop:
#Print out the sentence "correcting...".
#Next, decrease the value of offset by 1. You can do this with offset = offset - 1.
#Finally, still within your loop, print out offset so you can see how it changes.
# Initialize offset
offset = 8

# Code the while loop
while offset != 0 :
    print("correcting...")
    offset = offset - 1
    print(offset)



#Inside the while loop, complete the if-else statement:
#If offset is greater than zero, you should decrease offset by 1.
#Else, you should increase offset by 1.
#If you've coded things correctly, hitting Submit Answer should work this time.
# Initialize offset
offset = -6

# Code the while loop
while offset != 0 :
    print("correcting...")
    if offset > 0 :
        offset = offset - 1
    else :
        offset = offset + 1
    print(offset)



#Write a for loop that iterates over all elements of the areas list and prints out every element separately.
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for area in areas :
    print(area)




#Adapt the for loop in the sample code to use enumerate() and use two iterator variables.
#Update the print() statement so that on each run, a line of the form "room x: y" should be printed, where x is the index of the list element and y is the actual list element, i.e. the area. Make sure to print out this exact string, with the correct spacing.
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change for loop to use enumerate() and update print()
for index, area in enumerate(areas) :
    print("room " + str(index) + ": " + str(area))




#Adapt the print() function in the for loop on the right so that the first printout becomes "room 1: 11.25", the second one "room 2: 18.0" and so on.
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Adapt the printout
for index, area in enumerate(areas) :
    print("room " + str(index + 1) + ": " + str(area))




#Write a for loop that goes through each sublist of house and prints out the x is y sqm, where x is the name of the room and y is the area of the room.
# house list of lists
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Build a for loop from scratch
for x in house:
    print("the " + x[0] + " is " + str(x[1]) + " sqm")



#Write a for loop that goes through each key:value pair of europe. On each iteration, "the capital of x is y" should be printed out, where x is the key and y is the value of the pair.
# Definition of dictionary
europe = {'spain': 'madrid', 'france': 'paris', 'germany': 'berlin',
          'norway': 'oslo', 'italy': 'rome', 'poland': 'warsaw', 'austria': 'vienna'}

# Iterate over europe
for key, value in europe.items():
    print("the capital of " + str(key) + " is " + str(value))




#Import the numpy package under the local alias np.
#Write a for loop that iterates over all elements in np_height and prints out "x inches" for each element, where x is the value in the array.
#Write a for loop that visits every element of the np_baseball array and prints it out.
# Import numpy as np
import numpy as np

# For loop over np_height
for x in np_height :
    print(str(x) + " inches")

# For loop over np_baseball
for x in np.nditer(np_baseball) :
    print(x)



#Write a for loop that iterates over the rows of cars and on each iteration perform two print() calls: one to print out the row label and one to print out all of the rows contents.
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Iterate over rows of cars
for lab, row in cars.iterrows() :
    print(lab)
    print(row)


#Using the iterators lab and row, adapt the code in the for loop such that the first iteration prints out "US: 809", the second iteration "AUS: 731", and so on.
#The output should be in the form "country: cars_per_cap". Make sure to print out this exact string (with the correct spacing).
#You can use str() to convert your integer data to a string so that you can print it in conjunction with the country label.
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Adapt for loop
for lab, row in cars.iterrows() :
    print(lab + ": " + str(row['cars_per_cap']))



#Use a for loop to add a new column, named COUNTRY, that contains a uppercase version of the country names in the "country" column. You can use the string method upper() for this.
#To see if your code worked, print out cars. Don't indent this code, so that it's not part of the for loop.
# Import cars data
import pandas as pd

cars = pd.read_csv('cars.csv', index_col=0)

# Code for loop that adds COUNTRY column
for lab, row in cars.iterrows():
    cars.loc[lab, "COUNTRY"] = row["country"].upper()

# Print cars
print(cars)




#Replace the for loop with a one-liner that uses .apply(str.upper). The call should give the same result: a column COUNTRY should be added to cars, containing an uppercase version of the country names.
#As usual, print out cars to see the fruits of your hard labor
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Use .apply(str.upper)
cars["COUNTRY"] = cars["country"].apply(str.upper)


#Import numpy as np.
#Use seed() to set the seed; as an argument, pass 123.
#Generate your first random float with rand() and print it out.
# Import numpy as np
import numpy as np

# Set the seed
np.random.seed(123)

# Generate and print random float
print(np.random.rand())



#Use randint() with the appropriate arguments to randomly generate the integer 1, 2, 3, 4, 5 or 6. This simulates a dice. Print it out.
#Repeat the outcome to see if the second throw is different. Again, print out the result.
# Import numpy and set seed
import numpy as np
np.random.seed(123)

# Use randint() to simulate a dice
print(np.random.randint(1,7))

# Use randint() again
print(np.random.randint(1,7))



#Roll the dice. Use randint() to create the variable dice.
#Finish the if-elif-else construct by replacing ___:
#If dice is 1 or 2, you go one step down.
#if dice is 3, 4 or 5, you go one step up.
#Else, you throw the dice again. The number of eyes is the number of steps you go up.
#Print out dice and step. Given the value of dice, was step updated correctly?
# Numpy is imported, seed is set

# Starting step
step = 50

# Roll the dice
dice = np.random.randint(1,7)

# Finish the control construct
if dice <= 2 :
    step = step - 1
elif dice <= 5 :
    step = step + 1
else :
    step = step + np.random.randint(1,7)

# Print out dice and step
print(dice)
print(step)



#Make a list random_walk that contains the first step, which is the integer 0.
#Finish the for loop:
#The loop should run 100 times.
#On each iteration, set step equal to the last element in the random_walk list. You can use the index -1 for this.
#Next, let the if-elif-else construct update step for you.
#The code that appends step to random_walk is already coded.
#Print out random_walk.
# Numpy is imported, seed is set

# Initialize random_walk
random_walk = [0]

# Complete the ___
for x in range(100) :
    # Set step: last element in random_walk
    step = random_walk[-1]

    # Roll the dice
    dice = np.random.randint(1,7)

    # Determine next step
    if dice <= 2:
        step = step - 1
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    # append next_step to random_walk
    random_walk.append(step)

# Print random_walk
print(random_walk)



#Use max() in a similar way to make sure that step doesn't go below zero if dice <= 2.
#Hit Submit Answer and check the contents of random_walk.
# Numpy is imported, seed is set

# Initialize random_walk
random_walk = [0]

for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        # Replace below: use max to make sure step can't go below 0
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)

print(random_walk)




#Add some lines of code after the for loop:

#Import matplotlib.pyplot as plt.
#Use plt.plot() to plot random_walk.
#Finish off with plt.show() to actually display the plot.
# Numpy is imported, seed is set

# Initialization
random_walk = [0]

for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Plot random_walk
plt.plot(random_walk)

# Show the plot
plt.show()



#Fill in the specification of the for loop so that the random walk is simulated 10 times.
#After the random_walk array is entirely populated, append the array to the all_walks list.
#Finally, after the top-level for loop, print out all_walks.
# Numpy is imported; seed is set

# Initialize all_walks (don't change this line)
all_walks = []

# Simulate random walk 10 times
for i in range(10) :

    # Code from before
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)

        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)

    # Append random_walk to all_walks
    all_walks.append(random_walk)

# Print all_walks
print(all_walks)



#Use np.array() to convert all_walks to a Numpy array, np_aw.
#Try to use plt.plot() on np_aw. Also include plt.show(). Does it work out of the box?
#Transpose np_aw by calling np.transpose() on np_aw. Call the result np_aw_t. Now every row in np_all_walks represents the position after 1 throw for the 10 random walks.
#Use plt.plot() to plot np_aw_t; also include a plt.show(). Does it look better this time?
# numpy and matplotlib imported, seed set.

# initialize and populate all_walks
all_walks = []
for i in range(10) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)
    all_walks.append(random_walk)

# Convert all_walks to Numpy array: np_aw
np_aw = np.array(all_walks)

# Plot np_aw and show
plt.plot(np_aw)
plt.show()

# Clear the figure
plt.clf()

# Transpose np_aw: np_aw_t
np_aw_t = np.transpose(np_aw)

# Plot np_aw_t and show
plt.plot(np_aw_t)
plt.show()


#Change the range() function so that the simulation is performed 250 times.
#Finish the if condition so that step is set to 0 if a random float is less or equal to 0.001. Use np.random.rand().
# numpy and matplotlib imported, seed set

# Simulate random walk 250 times
all_walks = []
for i in range(250) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)

        # Implement clumsiness
        if np.random.rand() <= 0.001 :
            step = 0

        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))
plt.plot(np_aw_t)
plt.show()



#To make sure we've got enough simulations, go crazy. Simulate the random walk 500 times.
#From np_aw_t, select the last row. This contains the endpoint of all 500 random walks you've simulated. Store this Numpy array as ends.
#Use plt.hist() to build a histogram of ends. Don't forget plt.show() to display the plot.
# numpy and matplotlib imported, seed set

# Simulate random walk 500 times
all_walks = []
for i in range(500) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        if np.random.rand() <= 0.001 :
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))

# Select last row from np_aw_t: ends
ends = np_aw_t[-1,:]

# Plot histogram of ends, display plot
plt.hist(ends)
plt.show()




















































































































































































































































