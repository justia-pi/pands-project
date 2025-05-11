# Analysis of Iris dataset
# 1. Program outputs a summary of each variable to a signle file.
# 2. Saves a histogram of each variable to png files.
# 3. Outputs scatter plot of each pair of variable.
# 4. Regression line - correlation between varibales: petal length and petal width.
# 5. Boxplots of petal length for each species.
# By Justyna Pinkowska
 
import csv
import numpy as np
import matplotlib.pyplot as plt

filename = "iris.csv"
output_filename =  "feature_output.txt"


# Lists to store data for each column.
sepal_lengths = []
sepal_widths = []
petal_lengths = []
petal_widths = []
species = []

# Reading Iris dataset.
with open(filename, "rt") as csvFile: 
    csvReader = csv.reader(csvFile, delimiter=',')
    for row in csvReader:
        if len(row) == 5: 
            sepal_lengths.append(float(row[0]))
            sepal_widths.append(float(row[1]))
            petal_lengths.append(float(row[2]))
            petal_widths.append(float(row[3]))
            species.append(row[4])
  
# Convert numerical lists to NumPy arrays for calculations.
sepal_lengths_np = np.array(sepal_lengths)
sepal_widths_np = np.array(sepal_widths)
petal_lengths_np = np.array(petal_lengths)
petal_widths_np = np.array(petal_widths)

# Calculate features' statistics using dictionaries to store statistics for each feature.
feature_means = {
    "sepal_length": np.mean(sepal_lengths_np),
    "sepal_width": np.mean(sepal_widths_np),
    "petal_length": np.mean(petal_lengths_np),
    "petal_width": np.mean(petal_widths_np),
}

feature_mins = {
    "sepal_length": np.min(sepal_lengths_np),
    "sepal_width": np.min(sepal_widths_np),
    "petal_length": np.min(petal_lengths_np),
    "petal_width": np.min(petal_widths_np),
}

feature_maxs = {
    "sepal_length": np.max(sepal_lengths_np),
    "sepal_width": np.max(sepal_widths_np),
    "petal_length": np.max(petal_lengths_np),
    "petal_width": np.max(petal_widths_np),
}

feature_stds = {
    "sepal_length": np.std(sepal_lengths_np),
    "sepal_width": np.std(sepal_widths_np),
    "petal_length": np.std(petal_lengths_np),
    "petal_width": np.std(petal_widths_np),
}

feature_medians = {
    "sepal_length": np.median(sepal_lengths_np),
    "sepal_width": np.median(sepal_widths_np),
    "petal_length": np.median(petal_lengths_np),
    "petal_width": np.median(petal_widths_np),
}

# Calculate species counts.
species_counts = {}
for s in species: # This loop goes through each element s in the species list. 
    if s in species_counts:
        species_counts[s] += 1
    else:
        species_counts[s] = 1 # Gets the count of the species s from the species_counts dictionary. 

    # Write summary to the output file.
with open(output_filename, "w") as f:
    f.write("Iris Dataset Variables Summary\n\n")

    for feature in ["sepal_length", "sepal_width", "petal_length", "petal_width"]:
        f.write(f"Feature: {feature}\n")
        f.write(f"  Mean: {feature_means[feature]:.2f}\n")
        f.write(f"  Min: {feature_mins[feature]:.2f}\n")
        f.write(f"  Max: {feature_maxs[feature]:.2f}\n")
        f.write(f"  Standard Deviation: {feature_stds[feature]:.2f}\n")
        f.write(f"  Median: {feature_medians[feature]:.2f}\n\n")

    f.write("Species Distribution:\n")
    for sp, count in species_counts.items():
        f.write(f"  {sp}: {count}\n")

# Creating histogram of each variable (separate histograms).
feature_names = ["sepal_length", "sepal_width", "petal_length", "petal_width"]

# In order to select all the data for the i feature feature_data[:, i], T transposes the array that columns become rows and rows colum.
feature_data = np.array([sepal_lengths_np, sepal_widths_np, petal_lengths_np, petal_widths_np]).T 

# Enumerate() helps to go through the list and gives 2 things: position of the item in the list and item itself.
for i, feature_name in enumerate(feature_names):

# Plotting hstograms:
# Creates each histogram separately 8 inches wide and 6 inches tall.  
    plt.figure(figsize=(8, 6))  
    plt.hist(feature_data[:, i], edgecolor='black', color="red", label=feature_name, alpha=0.7) # feature_data[:, i] all values i column.
    
    # Add a title.
    plt.title(f'Histogram of {feature_name}')  
    
    # Add labels, legend and grid.
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.legend()
    plt.grid(True)

# Save the histogram of each variable to a png file.
    plt.savefig(f'{feature_name}_histogram.png')  

# Scatter plots of each pair:

# Create a figure and an axis.
fig, ax = plt.subplots()
species = ['setosa', 'versicolor', 'virginica']

# First rows 50 is Setosa, 51-100 is Versicolor and 101-150 is Virginica. 
species_names = np.repeat(species, 50) 
color = {"setosa": "red", "versicolor": "green", "virginica": "yellow"}
species_colors = [color[name] for name in species_names]

# Scatter plot of sepal length and sepal width.
ax.scatter(feature_data[:, 0], feature_data[:, 1], c=species_colors, marker=".")
# Labels.
ax.set_xlabel('sepal_length')
ax.set_ylabel('sepal_width')
# Create a legend
handles = [plt.plot([], [], marker=".", linestyle="", color=color[name], label=name)[0] for name in color]
ax.legend(handles=handles, labels=color.keys())
# Save scatter plot.
plt.savefig(f'sepal length and width_scatter_plot.png')


# Scatter plot of sepal length and petal length.
ax.scatter(feature_data[:, 0], feature_data[:, 2], c=species_colors, marker=".")
# Labels.
ax.set_xlabel('sepal_length')
ax.set_ylabel('petal_length')
# Create a legend
handles = [plt.plot([], [], marker=".", linestyle="", color=color[name], label=name)[0] for name in color]
ax.legend(handles=handles, labels=color.keys())
# Save scatter plot.
plt.savefig(f'sepal length and petal length_scatter_plot.png')


# Scatter plot of sepal length and petal width.
ax.scatter(feature_data[:, 0], feature_data[:, 3], c=species_colors, marker=".")
# Labels.
ax.set_xlabel('sepal_length')
ax.set_ylabel('petal_width')
# Create a legend
handles = [plt.plot([], [], marker=".", linestyle="", color=color[name], label=name)[0] for name in color]
ax.legend(handles=handles, labels=color.keys())
# Save scatter plot.
plt.savefig(f'sepal length and petal width_scatter_plot.png')


# Scatter plot of sepal width and petal length.
ax.scatter(feature_data[:, 1], feature_data[:, 2], c=species_colors, marker=".")
# Labels.
ax.set_xlabel('sepal_width')
ax.set_ylabel('petal_length')
# Create a legend
handles = [plt.plot([], [], marker=".", linestyle="", color=color[name], label=name)[0] for name in color]
ax.legend(handles=handles, labels=color.keys())
# Save scatter plot.
plt.savefig(f'sepal width and petal length_scatter_plot.png')

# Scatter plot of sepal width and petal width.
ax.scatter(feature_data[:, 1], feature_data[:, 3], c=species_colors, marker=".")
# Labels.
ax.set_xlabel('sepal_width')
ax.set_ylabel('petal_width')
# Create a legend
handles = [plt.plot([], [], marker=".", linestyle="", color=color[name], label=name)[0] for name in color]
ax.legend(handles=handles, labels=color.keys())
# Save scatter plot.
plt.savefig(f'sepal width and petal width_scatter_plot.png')


# Create a figure and axis.
fig, ax = plt.subplots()
# Scatter plot of petal length and petal width.
ax.scatter(feature_data[:, 2], feature_data[:, 3], c=species_colors, marker=".")
# Labels.
ax.set_xlabel('petal_length')
ax.set_ylabel('petal_width')
# Create a legend
handles = [plt.plot([], [], marker=".", linestyle="", color=color[name], label=name)[0] for name in color]
ax.legend(handles=handles, labels=color.keys())
# Save scatter plot.
plt.savefig(f'petal length and petal width_scatter_plot.png')


# Plotting regression line.https://en.wikipedia.org/wiki/Simple_linear_regression#Line_fitting
# Use polyfit to fit a line to the data.
m, c = np.polyfit(feature_data[:, 2], feature_data[:, 3], 1)
ax.plot(feature_data[:, 2], m * feature_data[:, 2] + c, color = 'red', label = 'Regression line')
# Title.
ax.set_title(f'y = {m:.2f}x + {c:.2f}', color = 'red')
# Legend.
ax.legend()
# Saves scatter plot and regression line.
plt.savefig(f'petal length and petal width_scatter_plot.png')


# Boxplots of petal length for each species:

# Setosa.
set = feature_data[:50, 2]
set_mean = np.mean(set)
set_quant = np.quantile(set, [0.25, 0.5, 0.75], axis=0)
# Create figure, axis.
fig, ax = plt.subplots()
# Create boxplot of Setosa.
ax.boxplot(set)
# Add title.
ax.set_title("Boxplot of Setosa Data")
plt.savefig(f'boxplot_setosa.png')


# Versicolor.
ver = feature_data[51:100, 2]
ver_mean = np.mean(set)
ver_quant = np.quantile(set, [0.25, 0.5, 0.75], axis=0)
# Create figure, axis.
fig, ax = plt.subplots()
# Create boxplot Versicolor.
ax.boxplot(ver)
# Add title.
ax.set_title("Boxplot of Versicolor Data")
plt.savefig(f'boxplot_versicolor.png')

# Virginica.
vir = feature_data[101:150, 2]
vir_mean = np.mean(set)
vir_quant = np.quantile(set, [0.25, 0.5, 0.75], axis=0)
# Create figure, axis.
fig, ax = plt.subplots()
# Create boxplot Virginica
ax.boxplot(vir)
# Add title.
ax.set_title("Boxplot of Virginica Data")
plt.savefig(f'boxplot_virginica.png')

































        
        
