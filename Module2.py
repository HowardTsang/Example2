#Experiment in the IPython Shell; type 5 / 8, for example.
#Add another line of code to the Python script on the top-right (not in the Shell): print(7 + 10).
#Hit Submit Answer to execute the Python script and receive feedback.

# Example, do not modify!
print(5 / 8)

# Print the sum of 7 and 10

print(7+10)



#Above the print(7 + 10), add the comment
# Division
print(5 / 8)

# Addition
print(7 + 10)



#Suppose you have $100, which you can invest with a 10% return each year. After one year, it's 100X1.1=110 dollars,and after two years it's 100X1.1=121.Add code to calculate how much money you end up with after 7 years, and print the result.
# Addition, subtraction
print(5 + 5)
print(5 - 5)

# Multiplication, division, modulo, and exponentiation
print(3 * 5)
print(10 / 2)
print(18 % 7)
print(4 ** 2)

# Instruction
print(100*1.1**7)

# How much is your $100 worth after 7 years?
print(100*1.1**7)


#Create a variable savings with the value 100.
#Check out this variable by typing print(savings) in the script.
# Create a variable savings
savings = 100

# Print out savings
print(savings)


#Create a variable growth_multiplier, equal to 1.1.
#Create a variable, result, equal to the amount of money you saved after 7 years.
#Print out the value of result.
# Create a variable savings
savings = 100

# Create a variable growth_multiplier
growth_multiplier = 1.1

# Calculate result
result = savings * growth_multiplier ** 7

# Print out result
print (result)



#Create a new string, desc, with the value "compound interest".
#Create a new boolean, profitable, with the value True.
# Create a variable desc
desc = "compound interest"
# Create a variable profitable
profitable = True



#Calculate the product of savings and growth_multiplier. Store the result in year1.
#What do you think the resulting type will be? Find out by printing out the type of year1.
#Calculate the sum of desc and desc and store the result in a new variable doubledesc.
#Print out doubledesc. Did you expect this?
savings = 100
growth_multiplier = 1.1
desc = "compound interest"

# Assign product of growth_multiplier and savings to year1
year1 = savings * growth_multiplier

# Print the type of year1
print(type(year1))


# Assign sum of desc and desc to doubledesc
doubledesc = desc + desc

# Print out doubledesc
print(doubledesc)



#Hit Run Code to run the code. Try to understand the error message.
#Fix the code such that the printout runs without errors; use the function str() to convert the variables to strings.
#Convert the variable pi_string to a float and store this float as a new variable, pi_float.
# Definition of savings and result
savings = 100
result = 100 * 1.10 ** 7

# Fix the printout
print("I started with $" + str(savings) + " and now have $" + str(result) + ". Awesome!")

# Definition of pi_string
pi_string = "3.1415926"

# Convert pi_string into float: pi_float
float(pi_string)




#Create a list, areas, that contains the area of the hallway (hall), kitchen (kit), living room (liv), bedroom (bed) and bathroom (bath), in this order. Use the predefined variables.
#Print areas with the print() function.
# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas
areas = [hall,kit,liv,bed,bath]

# Print areas
print(areas)




#Finish the code that creates the areas list. Build the list so that the list first contains the name of each room as a string and then its area. In other words, add the strings "hallway", "kitchen" and "bedroom" at the appropriate locations.
#Print areas again; is the printout more informative this time?
# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Adapt list areas
areas = ["hallway",hall, "kitchen",kit, "living room",liv,"bedroom",bed,"bathroom", bath]

# Print areas
print(areas)




#Finish the list of lists so that it also contains the bedroom and bathroom data. Make sure you enter these in order!
#Print out house; does this way of structuring your data make more sense?
#Print out the type of house. Are you still dealing with a list?
# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# house information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed],
         ["bathroom", bath]]

# Print out house
print(house)

# Print out the type of house
print(type(house))





#Print out the second element from the areas list (it has the value 11.25).
#Subset and print out the last element of areas, being 9.50. Using a negative index makes sense here!
#Select the number representing the area of the living room (20.0) and print it out.
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print out second element from areas
print(areas[1])

# Print out last element from areas
print(areas[-1])

# Print out the area of the living room
print(areas[5])





#Using a combination of list subsetting and variable assignment, create a new variable, eat_sleep_area, that contains the sum of the area of the kitchen and the area of the bedroom.
#Print the new variable eat_sleep_area.
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Sum of kitchen and bedroom area: eat_sleep_area
eat_sleep_area = areas[3] + areas[-3]

# Print the variable eat_sleep_area
print(eat_sleep_area)





#Use slicing to create a list, downstairs, that contains the first 6 elements of areas.
#Do a similar thing to create a new variable, upstairs, that contains the last 4 elements of areas.
#Print both downstairs and upstairs using print().
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs
downstairs = areas[:6]

# Use slicing to create upstairs
upstairs = areas[-4:]

# Print out downstairs and upstairs
print(downstairs)
print(upstairs)




#Create downstairs again, as the first 6 elements of areas. This time, simplify the slicing by omitting the begin index.
#Create upstairs again, as the last 4 elements of areas. This time, simplify the slicing by omitting the end index.
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Alternative slicing to create downstairs
downstairs = areas[:6]

# Alternative slicing to create upstairs
upstairs = areas[-4:]





#Update the area of the bathroom area to be 10.50 square meters instead of 9.50.
#Make the areas list more trendy! Change "living room" to "chill zone".
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area
areas[-1] = 10.50

# Change "living room" to "chill zone"
areas[4] = "chill zone"




#Use the + operator to paste the list ["poolhouse", 24.5] to the end of the areas list. Store the resulting list as areas_1.
#Further extend areas_1 by adding data on your garage. Add the string "garage" and float 15.45. Name the resulting list areas_2.
# Create the areas list and make some changes
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1
areas_1 = areas + ["poolhouse", 24.5]

# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 + ["garage", 15.45]





#Change the second command, that creates the variable areas_copy, such that areas_copy is an explicit copy of areas. After your edit, changes made to areas_copy shouldn't affect areas. Submit the answer to check this.
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Create areas_copy
areas_copy = list(areas)

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)




#Use print() in combination with type() to print out the type of var1.
#Use len() to get the length of the list var1. Wrap it in a print() call to directly print it out.
#Use int() to convert var2 to an integer. Store the output as out2.
# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1
print(type(var1))

# Print out length of var1
print(len(var1))

# Convert var2 to an integer: out2
out2 = int(var2)




#Use + to merge the contents of first and second into a new list: full.
#Call sorted() on full and specify the reverse argument to be True. Save the sorted list as full_sorted.
#Finish off by printing out full_sorted.
# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first + second

# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse = True)

# Print out full_sorted
print(full_sorted)



#Use the upper() method on place and store the result in place_up. Use the syntax for calling methods that you learned in the previous video.
#Print out place and place_up. Did both change?
#Print out the number of o's on the variable place by calling count() on place and passing the letter 'o' as an input to the method. We're talking about the variable place, not the word "place"!
# string to experiment with: place
place = "poolhouse"

# Use upper() on place: place_up
place_up = place.upper()

# Print out place and place_up
print(place)
print(place_up)

# Print out the number of o's in place
print(place.count('o'))




#Use the index() method to get the index of the element in areas that is equal to 20.0. Print out this index.
#Call count() on areas to find out how many times 9.50 appears in the list. Again, simply print out this number.
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20.0))

# Print out how often 9.50 appears in areas
print(areas.count(9.50))




#Use append() twice to add the size of the poolhouse and the garage again: 24.5 and 15.45, respectively. Make sure to add them in this order.
#Print out areas
#Use the reverse() method to reverse the order of the elements in areas.
#Print out areas once more.
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size
areas.append(24.5)
areas.append(15.45)

# Print out areas
print(areas)

# Reverse the orders of the elements in areas
areas.reverse()

# Print out areas
print(areas)




#Import the math package. Now you can access the constant pi with math.pi.
#Calculate the circumference of the circle and store it in C.
#Calculate the area of the circle and store it in A.
# Definition of radius
r = 0.43

# Import the math package
import math

# Calculate C
C = 2 * r * math.pi

# Calculate A
A = math.pi * r ** 2

# Build printout
print("Circumference: " + str(C))
print("Area: " + str(A))




#Perform a selective import from the math package where you only import the radians function.
#Calculate the distance travelled by the Moon over 12 degrees of its orbit. Assign the result to dist. You can calculate this as r * phi, where r is the radius and phi is the angle in radians. To convert an angle in degrees to an angle in radians, use the radians() function, which you just imported.
#Print out dist.
# Definition of radius
r = 192500

# Import radians function of math package
from math import radians

# Travel distance of Moon over 12 degrees. Store in dist.
dist = r * radians(12)

# Print out dist
print(dist)




#Import the numpy package as np, so that you can refer to numpy with np.
#Use np.array() to create a numpy array from baseball. Name this array np_baseball.
#Print out the type of np_baseball to check that you got it right.
# Create list baseball
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Import the numpy package as np
import numpy as np

# Create a Numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out type of np_baseball
print(type(np_baseball))




#Create a numpy array from height_in. Name this new array np_height_in.
#Print np_height_in.
#Multiply np_height_in with 0.0254 to convert all height measurements from inches to meters. Store the new values in a new array, np_height_m.
#Print out np_height_m and check if the output makes sense.
# height is available as a regular list

# Import numpy
import numpy as np

# Create a numpy array from height_in: np_height_in
np_height_in = np.array(height_in)

# Print out np_height_in
print(np_height_in)

# Convert np_height_in to m: np_height_m
np_height_m = np_height_in * 0.0254

# Print np_height_m
print(np_height_m)



#Create a numpy array from the weight_lb list with the correct units. Multiply by 0.453592 to go from pounds to kilograms. Store the resulting numpy array as np_weight_kg.
#Use np_height_m and np_weight_kg to calculate the BMI of each player. Use the following equation:
# BMI= weight(kg)/ height(m)^2
#Save the resulting numpy array as bmi.
#Print out bmi.
# height and weight are available as regular lists

# Import numpy
import numpy as np

# Create array from height_in with metric units: np_height_m
np_height_m = np.array(height_in) * 0.0254

# Create array from weight_lb with metric units: np_weight_kg
np_weight_kg = np.array(weight_lb) * 0.453592

# Calculate the BMI: bmi
bmi = np_weight_kg / np_height_m ** 2

# Print out bmi
print(bmi)





#Create a boolean numpy array: the element of the array should be True if the corresponding baseball player's BMI is below 21. You can use the < operator for this. Name the array light.
#Print the array light.
#Print out a numpy array with the BMIs of all baseball players whose BMI is below 21. Use light inside square brackets to do a selection on the bmi array.
# height and weight are available as a regular lists

# Import numpy
import numpy as np

# Calculate the BMI: bmi
np_height_m = np.array(height_in) * 0.0254
np_weight_kg = np.array(weight_lb) * 0.453592
bmi = np_weight_kg / np_height_m ** 2

# Create the light array
light = bmi < 21

# Print out light
print(light)

# Print out BMIs of all baseball players whose BMI is below 21
print(bmi[light])




#Subset np_weight_lb by printing out the element at index 50.
#Print out a sub-array of np_height_in that contains the elements at index 100 up to and including index 110.
# height and weight are available as a regular lists

# Import numpy
import numpy as np

# Store weight and height lists as numpy arrays
np_weight_lb = np.array(weight_lb)
np_height_in = np.array(height_in)

# Print out the weight at index 50
print(np_weight_lb[50])

# Print out sub-array of np_height_in: index 100 up to and including index 110
print(np_height_in[100:111])



#Use np.array() to create a 2D numpy array from baseball. Name it np_baseball.
#Print out the type of np_baseball.
#Print out the shape attribute of np_baseball. Use np_baseball.shape.
# Create baseball, a list of lists
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Import numpy
import numpy as np

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the type of np_baseball
print(type(np_baseball))

# Print out the shape of np_baseball
print(np_baseball.shape)




#Use np.array() to create a 2D numpy array from baseball. Name it np_baseball.
#Print out the shape attribute of np_baseball.
# baseball is available as a regular list of lists

# Import numpy package
import numpy as np

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the shape of np_baseball
print(np_baseball.shape)



#Print out the 50th row of np_baseball.
#Make a new variable, np_weight_lb, containing the entire second column of np_baseball.
#Select the height (first column) of the 124th baseball player in np_baseball and print it out.
# baseball is available as a regular list of lists

# Import numpy package
import numpy as np

# Create np_baseball (2 cols)
np_baseball = np.array(baseball)

# Print out the 50th row of np_baseball
print(np_baseball[49,:])

# Select the entire second column of np_baseball: np_weight_lb
np_weight_lb = np_baseball[:,1]

# Print out height of 124th player
print(np_baseball[123, 0])



#You managed to get hold of the changes in height, weight and age of all baseball players. It is available as a 2D numpy array, updated. Add np_baseball and updated and print out the result.
#You want to convert the units of height and weight to metric (meters and kilograms respectively). As a first step, create a numpy array with three values: 0.0254, 0.453592 and 1. Name this array conversion.
#Multiply np_baseball with conversion and print out the result.
# baseball is available as a regular list of lists
# updated is available as 2D numpy array

# Import numpy package
import numpy as np

# Create np_baseball (3 cols)
np_baseball = np.array(baseball)

# Print out addition of np_baseball and updated
print(np_baseball + updated)

# Create numpy array: conversion
conversion = np.array([0.0254, 0.453592, 1])

# Print out product of np_baseball and conversion
print(np_baseball * conversion)



#Create numpy array np_height_in that is equal to first column of np_baseball.
#Print out the mean of np_height_in.
#Print out the median of np_height_in.
# np_baseball is available

# Import numpy
import numpy as np

# Create np_height_in from np_baseball
np_height_in = np_baseball[:,0]

# Print out the mean of np_height_in
print(np.mean(np_height_in))

# Print out the median of np_height_in
print(np.median(np_height_in))



#The code to print out the mean height is already included. Complete the code for the median height. Replace None with the correct code.
#Use np.std() on the first column of np_baseball to calculate stddev. Replace None with the correct code.
#Do big players tend to be heavier? Use np.corrcoef() to store the correlation between the first and second column of np_baseball in corr. Replace None with the correct code.
# np_baseball is available

# Import numpy
import numpy as np

# Print mean height (first column)
avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

# Print median height. Replace 'None'
med = np.median(np_baseball[:,0])
print("Median: " + str(med))

# Print out the standard deviation on height. Replace 'None'
stddev = np.std(np_baseball[:,0])
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column. Replace 'None'
corr = np.corrcoef(np_baseball[:,0], np_baseball[:,1])
print("Correlation: " + str(corr))



#Convert heights and positions, which are regular lists, to numpy arrays. Call them np_heights and np_positions.
#Extract all the heights of the goalkeepers. You can use a little trick here: use np_positions == 'GK' as an index for np_heights. Assign the result to gk_heights.
#Extract all the heights of all the other players. This time use np_positions != 'GK' as an index for np_heights. Assign the result to other_heights.
#Print out the median height of the goalkeepers using np.median(). Replace None with the correct code.
#Do the same for the other players. Print out their median height. Replace None with the correct code.
# heights and positions are available as lists

# Import numpy
import numpy as np

# Convert positions and heights to numpy arrays: np_positions, np_heights
np_positions = np.array(positions)
np_heights = np.array(heights)

# Heights of the goalkeepers: gk_heights
gk_heights = np_heights[np_positions == 'GK']

# Heights of the other players: other_heights
other_heights = np_heights[np_positions != 'GK']

# Print out the median height of goalkeepers. Replace 'None'
print("Median height of goalkeepers: " + str(np.median(gk_heights)))

# Print out the median height of other players. Replace 'None'
print("Median height of other players: " + str(np.median(other_heights)))
































