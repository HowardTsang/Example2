#Import pandas and seaborn using the standard naming conventions.
#The path to the csv file is stored in the grant_file variable.
#Use pandas to read the file.
#Store the resulting DataFrame in the variable df.
# import all modules
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read in the DataFrame
df = pd.read_csv(grant_file)




#Use the pandas' plot.hist() function to plot a histogram of the Award_Amount column.
# Display pandas histogram
df['Award_Amount'].plot.hist()
plt.show()

# Clear out the pandas histogram
plt.clf()




#Use Seaborn's distplot() function to plot a distribution plot of the same column.
# Display a Seaborn distplot
sns.distplot(df['Award_Amount'])
plt.show()

# Clear the distplot
plt.clf()




#Create a distplot for the data and disable the KDE.
#Explicitly pass in the number 20 for the number of bins in the histogram.
#Display the plot using plt.show().
# Create a distplot
sns.distplot(df['Award_Amount'],
             kde=False,
             bins=20)

# Display a plot
plt.show()




#Create a distplot of the Award_Amount column in the df.
#Configure it to show a shaded kde (using the kde_kws dictionary).
#Add a rug plot above the x axis.
#Display the plot.
# Create a distplot of the Award Amount
sns.distplot(df['Award_Amount'],
             hist=False,
             rug=True,
             kde_kws={'shade':True})

# Plot the results
plt.show()




#The data is available in the dataframe called df.
#Create a regression plot using regplot() with "insurance_losses" on the x axis and "premiums" on the y axis.
# Create a regression plot of premiums vs. insurance_losses
sns.regplot(data=df,
            x="insurance_losses",
            y="premiums")

# Display the plot
plt.show()



#Create a regression plot of "premiums" versus "insurance_losses" using lmplot().
#Display the plot.
# Create an lmplot of premiums vs. insurance_losses
sns.lmplot(data=df,
           x="insurance_losses",
           y="premiums")

# Display the second plot
plt.show()




#Use lmplot() to look at the relationship between insurance_losses and premiums.
#Plot a regression line for each Region of the country.
# Create a regression plot using hue
sns.lmplot(data=df,
           x="insurance_losses",
           y="premiums",
           hue="Region")

#Show the results
plt.show()




#Use lmplot() to look at the relationship between insurance_losses and premiums.
#Create a plot for each Region of the country.
#Display the plots across multiple rows.
# Create a regression plot with multiple rows
sns.lmplot(data=df,
           x="insurance_losses",
           y="premiums",
           row="Region")

# Show the plot
plt.show()




#Plot a pandas histogram without adjusting the style.
#Set Seaborn's default style.
#Create another pandas histogram of the fmr_2 column which represents fair market rent for a 2-bedroom apartment.
# Plot the pandas histogram
df['fmr_2'].plot.hist()
plt.show()
plt.clf()

# Set the default seaborn style
sns.set()

# Plot the pandas histogram again
df['fmr_2'].plot.hist()
plt.show()
plt.clf()




#Create a distplot() of the fmr_2 column in df using a dark style. Use plt.clf() to clear the figure.
# Plot with a dark style
sns.set_style('dark')
sns.distplot(df['fmr_2'])
plt.show()

# Clear the figure
plt.clf()




#Create the same distplot() of fmr_2 using a whitegrid style. Clear the plot after showing it.
# Plot with a whitegrid style
sns.set_style('whitegrid')
sns.distplot(df['fmr_2'])
plt.show()

# Clear the figure
plt.clf()




#Use a white style for the plot.
#Create a lmplot() comparing the pop2010 and the fmr_2 columns.
#Remove the top and right spines using despine().
# Set the style to white
sns.set_style('white')

# Create a regression plot
sns.lmplot(data=df,
           x='pop2010',
           y='fmr_2')

# Remove the spines
sns.despine()

# Show the plot and clear the figure
plt.show()
plt.clf()




#Set the default Seaborn style and enable the matplotlib color codes.
#Create a distplot for the fmr_3 column using matplotlib's magenta (m) color code.
# Set style, enable color code, and create a magenta distplot
sns.set(color_codes=True)
sns.distplot(df['fmr_3'], color='m')

# Show the plot
plt.show()




#Create a for loop to show the difference between the bright and colorblind palette.
#Set the palette using the set_palette() function.
#Use a distplot of the fmr_3 column.
# Loop through differences between bright and colorblind palettes
for p in ['bright', 'colorblind']:
    sns.set_palette(p)
    sns.distplot(df['fmr_3'])
    plt.show()

    # Clear the plots
    plt.clf()




#Create and display a Purples sequential palette containing 8 colors.
# Create the Purples palette
sns.palplot(sns.color_palette("Purples", 8))
plt.show()



#Create and display a palette with 10 colors using the husl system.
# Create the husl palette
sns.palplot(sns.color_palette("husl", 10))
plt.show()



#Create and display a diverging palette with 6 colors coolwarm.
# Create the coolwarm palette
sns.palplot(sns.color_palette("coolwarm", 6))
plt.show()




#Use plt.subplots() to create a axes and figure objects.
#Plot a distplot of column fmr_3 on the axes.
#Set a more useful label on the x axis of "3 Bedroom Fair Market Rent".
# Create a figure and axes
fig, ax = plt.subplots()

# Plot the distribution of data
sns.distplot(df['fmr_3'], ax=ax)

# Create a more descriptive x axis label
ax.set(xlabel="3 Bedroom Fair Market Rent")

# Show the plot
plt.show()




#Create a distplot of the fmr_1 column.
#Modify the x axis label to say "1 Bedroom Fair Market Rent".
#Change the x axis limits to be between 100 and 1500.
#Add a descriptive title of "US Rent" to the plot.
# Create a figure and axes
fig, ax = plt.subplots()

# Plot the distribution of 1 bedroom rents
sns.distplot(df['fmr_1'], ax=ax)

# Modify the properties of the plot
ax.set(xlabel="1 Bedroom Fair Market Rent",
       xlim=(100,1500),
       title="US Rent")

# Display the plot
plt.show()





#Create a figure and axes.
#Plot the fmr_1 column distribution.
#Add a vertical line using axvline for the median and mean of the values which are already defined.
# Create a figure and axes. Then plot the data
fig, ax = plt.subplots()
sns.distplot(df['fmr_1'], ax=ax)

# Customize the labels and limits
ax.set(xlabel="1 Bedroom Fair Market Rent", xlim=(100,1500), title="US Rent")

# Add vertical lines for the median and mean
ax.axvline(x=median, color='m', label='Median', linestyle='--', linewidth=2)
ax.axvline(x=mean, color='b', label='Mean', linestyle='-', linewidth=2)

# Show the legend and plot the data
ax.legend()
plt.show()




#Create two axes objects, ax0 and ax1.
#Plot fmr_1 on ax0 and fmr_2 on ax1.
#Display the plots side by side.
# Create a plot with 1 row and 2 columns that share the y axis label
fig, (ax0, ax1) = plt.subplots(nrows=1, ncols=2, sharey=True)

# Plot the distribution of 1 bedroom apartments on ax0
sns.distplot(df['fmr_1'], ax=ax0)
ax0.set(xlabel="1 Bedroom Fair Market Rent", xlim=(100,1500))

# Plot the distribution of 2 bedroom apartments on ax1
sns.distplot(df['fmr_2'], ax=ax1)
ax1.set(xlabel="2 Bedroom Fair Market Rent", xlim=(100,1500))

# Display the plot
plt.show()




#Create a stripplot of the Award_Amount with the Model Selected on the y axis with jitter enabled.
# Create the stripplot
sns.stripplot(data=df,
              x='Award_Amount',
              y='Model Selected',
              jitter=True)

plt.show()



#Create a swarmplot() of the same data, but also include the hue by Region.
# Create and display a swarmplot with hue set to the Region
sns.swarmplot(data=df,
              x='Award_Amount',
              y='Model Selected',
              hue='Region')

plt.show()




#Create and display a boxplot of the data with Award_Amount on the x axis and Model Selected on the y axis.
# Create a boxplot
sns.boxplot(data=df,
            x='Award_Amount',
            y='Model Selected')

plt.show()
plt.clf()





#Create and display a similar violinplot of the data, but use the husl palette for colors.
# Create a violinplot with the husl palette
sns.violinplot(data=df,
               x='Award_Amount',
               y='Model Selected',
               palette='husl')

plt.show()
plt.clf()





#Create and display an lvplot using the Paired palette and the Region column as the hue.
# Create a lvplot with the Paired palette and the Region column as the hue
sns.lvplot(data=df,
           x='Award_Amount',
           y='Model Selected',
           palette='Paired',
           hue='Region')

plt.show()
plt.clf()




#Create a countplot with the df dataframe and Model Selected on the y axis and the color varying by Region.
# Show a countplot with the number of models used with each region a different color
sns.countplot(data=df,
              y="Model Selected",
              hue="Region")

plt.show()
plt.clf()






#Create a pointplot with the df dataframe and Model Selected on the x-axis and Award_Amount on the y-axis.
#Use a capsize in the pointplot in order to add caps to the error bars.
# Create a pointplot and include the capsize in order to show caps on the error bars
sns.pointplot(data=df,
              y='Award_Amount',
              x='Model Selected',
              capsize=.1)

plt.show()
plt.clf()




#Create a barplot with the same data on the x and y axis and change the color of each bar based on the Region column.
# Create a barplot with each Region shown as a different color
sns.barplot(data=df,
            y='Award_Amount',
            x='Model Selected',
            hue='Region')

plt.show()
plt.clf()




#Plot a regression plot comparing Tuition and average SAT scores(SAT_AVG_ALL).
#Make sure the values are shown as green triangles.
# Display a regression plot for Tuition
sns.regplot(data=df,
            y='Tuition',
            x="SAT_AVG_ALL",
            marker='^',
            color='g')

plt.show()
plt.clf()




#Use a residual plot to determine if the relationship looks linear.
# Display the residual plot
sns.residplot(data=df,
              y='Tuition',
              x="SAT_AVG_ALL",
              color='g')

plt.show()
plt.clf()





#Plot a regression plot of Tuition and PCTPELL.
# Plot a regression plot of Tuition and the Percentage of Pell Grants
sns.regplot(data=df,
            y='Tuition',
            x="PCTPELL")

plt.show()
plt.clf()




#Create another plot that breaks the PCTPELL column into 5 different bins.
# Create another plot that estimates the tuition by PCTPELL
sns.regplot(data=df,
            y='Tuition',
            x="PCTPELL",
            x_bins=5)

plt.show()
plt.clf()



#Create a final regression plot that includes a 2nd order polynomial regression line.
# The final plot should include a line using a 2nd order polynomial
sns.regplot(data=df,
            y='Tuition',
            x="PCTPELL",
            x_bins=5,
            order=2)

plt.show()
plt.clf()




#Create a regplot of Tuition and UG and set the fit_reg parameter to False to disable the regression line.
# Create a scatter plot by disabling the regression line
sns.regplot(data=df,
            y='Tuition',
            x="UG",
            fit_reg=False)

plt.show()
plt.clf()




#Create another plot with the UG data divided into 5 bins.
# Create a scatter plot and bin the data into 5 bins
sns.regplot(data=df,
            y='Tuition',
            x="UG",
            x_bins=5)

plt.show()
plt.clf()




#Create a regplot() with the data divided into 8 bins.
# Create a regplot and bin the data into 8 bins
sns.regplot(data=df,
         y='Tuition',
         x="UG",
         x_bins=8)

plt.show()
plt.clf()




#Use pandas' crosstab() function to build a table of visits by Group and Year.
#Print the pd_crosstab DataFrame.
#Plot the data using Seaborn's heatmap().
# Create a crosstab table of the data and print it
pd_crosstab = pd.crosstab(df["Group"], df["YEAR"])
print(pd_crosstab)

# Plot a heatmap of the table
sns.heatmap(pd_crosstab)

# Rotate tick marks for visibility
plt.yticks(rotation=0)
plt.xticks(rotation=90)

plt.show()





#Create a crosstab table of Group and YEAR
#Create a heatmap of the data using the BuGn palette
#Disable the cbar and increase the linewidth to 0.3
# Create the crosstab DataFrame
pd_crosstab = pd.crosstab(df["Group"], df["YEAR"])

# Plot a heatmap of the table
sns.heatmap(pd_crosstab, cbar=False, cmap="BuGn", linewidths=.3)

# Rotate tick marks for visibility
plt.yticks(rotation=0)
plt.xticks(rotation=90)

# Show the plot
plt.show()
plt.clf()




#Create a FacetGrid that shows a point plot of the Average SAT scores SAT_AVG_ALL.
#Use row_order to control the display order of the degree types.
# Create FacetGrid with Degree_Type and specify the order of the rows using row_order
g2 = sns.FacetGrid(df,
                   row="Degree_Type",
                   row_order=['Graduate', 'Bachelors', 'Associates', 'Certificate'])

# Map a pointplot of SAT_AVG_ALL onto the grid
g2.map(sns.pointplot, 'SAT_AVG_ALL')

# Show the plot
plt.show()
plt.clf()





#Create a factorplot() that contains a boxplot (box) of Tuition values varying by Degree_Type across rows.
# Create a factor plot that contains boxplots of Tuition values
sns.factorplot(data=df,
         x='Tuition',
         kind='box',
         row='Degree_Type')

plt.show()
plt.clf()




#Create a factorplot() of SAT Averages (SAT_AVG_ALL) facetted across Degree_Type that shows a pointplot (point).
#Use row_order to order the degrees from highest to lowest level.
# Create a facetted pointplot of Average SAT_AVG_ALL scores facetted by Degree Type
sns.factorplot(data=df,
        x='SAT_AVG_ALL',
        kind='point',
        row='Degree_Type',
        row_order=['Graduate', 'Bachelors', 'Associates', 'Certificate'])

plt.show()
plt.clf()





#Create a FacetGrid() with Degree_Type columns and scatter plot of UG and PCTPELL.
# Create a FacetGrid varying by column and columns ordered with the degree_order variable
g = sns.FacetGrid(df, col="Degree_Type", col_order=degree_ord)

# Map a scatter plot of Undergrad Population compared to PCTPELL
g.map(plt.scatter, 'UG', 'PCTPELL')

plt.show()
plt.clf()




#Create a lmplot() using the same values from the FacetGrid().
# Re-create the plot above as an lmplot
sns.lmplot(data=df,
        x='UG',
        y='PCTPELL',
        col="Degree_Type",
        col_order=degree_ord)

plt.show()
plt.clf()



#Create a facetted lmplot() comparing SAT_AVG_ALL to Tuition with columns varying by Ownership and rows by Degree_Type.
#In the lmplot() add a hue for Women Only Universities.
# Create an lmplot that has a column for Ownership, a row for Degree_Type
# and hue based on the WOMENONLY column and columns defined by inst_order
sns.lmplot(data=df,
           x='SAT_AVG_ALL',
           y='Tuition',
           col="Ownership",
           row='Degree_Type',
           row_order=['Graduate', 'Bachelors'],
           hue='WOMENONLY',
           col_order=inst_ord)

plt.show()
plt.clf()





#Compare "fatal_collisions" to "premiums" by using a scatter plot mapped to a PairGrid().
# Create a PairGrid with a scatter plot for fatal_collisions and premiums
g = sns.PairGrid(df, vars=["fatal_collisions", "premiums"])
g2 = g.map(plt.scatter)

plt.show()
plt.clf()



#Create another PairGrid but plot a histogram on the diagonal and scatter plot on the off diagonal.
# Create the same PairGrid but map a histogram on the diag
g = sns.PairGrid(df, vars=["fatal_collisions", "premiums"])
g2 = g.map_diag(plt.hist)
g3 = g2.map_offdiag(plt.scatter)

plt.show()
plt.clf()




#Recreate the pairwise plot from the previous exercise using pairplot().
# Create a pairwise plot of the variables using a scatter plot
sns.pairplot(data=df,
             vars=["fatal_collisions", "premiums"],
             kind='scatter')

plt.show()
plt.clf()




#Create another pairplot using the "Region" to color code the results.
#Use the RdBu palette to change the colors of the plot.
# Plot the same data but use a different color palette and color code by Region
sns.pairplot(data=df,
             vars=["fatal_collisions", "premiums"],
             kind='scatter',
             hue='Region',
             palette='RdBu',
             diag_kws={'alpha':.5})

plt.show()
plt.clf()




#Create a pair plot that examines fatal_collisions_speeding and fatal_collisions_alc on the x axis and premiums and insurance_losses on the y axis.
#Use the husl palette and color code the scatter plot by Region.
# Build a pairplot with different x and y variables
sns.pairplot(data=df,
             x_vars=["fatal_collisions_speeding", "fatal_collisions_alc"],
             y_vars=['premiums', 'insurance_losses'],
             kind='scatter',
             hue='Region',
             palette='husl')

plt.show()
plt.clf()




#Build a pairplot() with kde plots along the diagonals. Include the insurance_losses and premiums as the variables.
#Use a reg plot for the the non-diagonal plots.
#Use the BrBG palette for the final plot.
# plot relationships between insurance_losses and premiums
sns.pairplot(data=df,
             vars=["insurance_losses", "premiums"],
             kind='reg',
             palette='BrBG',
             diag_kind = 'kde',
             hue='Region')

plt.show()
plt.clf()




#Use Seaborn's "whitegrid" style for these plots.
#Create a JointGrid() with "hum" on the x-axis and "total_rentals" on the y.
#Plot a regplot() and distplot() on the margins.
# Build a JointGrid comparing humidity and total_rentals
sns.set_style("whitegrid")
g = sns.JointGrid(x="hum",
                  y="total_rentals",
                  data=df,
                  xlim=(0.1, 1.0))

g.plot(sns.regplot, sns.distplot)

plt.show()
plt.clf()




#Re-create the plot using a jointplot().
# Create a jointplot similar to the JointGrid
sns.jointplot(x="hum",
        y="total_rentals",
        kind='reg',
        data=df)

plt.show()
plt.clf()





#Create a jointplot with a 2nd order polynomial regression plot comparing temp and total_rentals.
# Plot temp vs. total_rentals as a regression plot
sns.jointplot(x="temp",
         y="total_rentals",
         kind='reg',
         data=df,
         order=2,
         xlim=(0, 1))

plt.show()
plt.clf()




#Use a residual plot to check the appropriateness of the model.
# Plot a jointplot showing the residuals
sns.jointplot(x="temp",
              y="total_rentals",
              kind='resid',
              data=df,
              order=2)

plt.show()
plt.clf()




#Create a jointplot with a scatter plot comparing temp and casual riders.
#Overlay a kdeplot on top of the scatter plot.
# Create a jointplot of temp vs. casual riders
# Include a kdeplot over the scatter plot
g = (sns.jointplot(x="temp",
                   y="casual",
                   kind='scatter',
                   data=df,
                   marginal_kws=dict(bins=10, rug=True))
     .plot_joint(sns.kdeplot))

plt.show()
plt.clf()




#Build a similar plot for registered users.
# Replicate the above plot but only for registered riders
g = (sns.jointplot(x="temp",
             y="registered",
             kind='scatter',
             data=df,
             marginal_kws=dict(bins=10, rug=True))
    .plot_joint(sns.kdeplot))

plt.show()
plt.clf()





































































































































































































































































































































































































































































