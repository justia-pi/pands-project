# Analysis of Iris dataset
# 1. Program outputs a summary of each variable to a signle file.
# 2. Saves a histogram of each variable to png files.
# 3. Outputs scatter plot of each pair of variable.
# By Justyna Pinkowska
 
import csv
import numpy as np
import matplotlib.pyplot as plt

filename = "iris.csv"
output_filename =  "feature_output.txt"


# Lists to store data for each column
sepal_lengths = []
sepal_widths = []
petal_lengths = []
petal_widths = []
species = []

# Reading Iris dataset
with open(filename, "rt") as csvFile: 
    csvReader = csv.reader(csvFile, delimiter=',')
    for row in csvReader:
        if len(row) == 5: 
            sepal_lengths.append(float(row[0]))
            sepal_widths.append(float(row[1]))
            petal_lengths.append(float(row[2]))
            petal_widths.append(float(row[3]))
            species.append(row[4])
  
# Convert numerical lists to NumPy arrays for calculations
sepal_lengths_np = np.array(sepal_lengths)
sepal_widths_np = np.array(sepal_widths)
petal_lengths_np = np.array(petal_lengths)
petal_widths_np = np.array(petal_widths)

# Calculate features' statistics using dictionaries to store statistics for each feature
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

# Calculate species counts
species_counts = {}
for s in species: # This loop goes through each element s in the species list. 
    if s in species_counts:
        species_counts[s] += 1
    else:
        species_counts[s] = 1 # Gets the count of the species s from the species_counts dictionary. 

    # Write summary to the output file
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

# Creating histogram of each variable (separate histograms)
feature_names = ["sepal_length", "sepal_width", "petal_length", "petal_width"]

# In order to select all the data for the i feature feature_data[:, i], T transposes the array that columns become rows and rows colum
feature_data = np.array([sepal_lengths_np, sepal_widths_np, petal_lengths_np, petal_widths_np]).T 

# Enumerate() helps to go through the list and gives 2 things: position of the item in the list and item itself
for i, feature_name in enumerate(feature_names):

# Plotting hstograms:
   
    plt.figure(figsize=(8, 6))  # Create each histogram separately 8 inches wide and 6 inches tall.
    plt.hist(feature_data[:, i], edgecolor='black', color="red", label=feature_name, alpha=0.7) # feature_data[:, i] all values i colu
    
    # Add a title
    plt.title(f'Histogram of {feature_name}')  
    
    # Add labels, legend and grid
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.legend()
    plt.grid(True)

# Save the histogram of each variable to a png file
    plt.savefig(f'{feature_name}_histogram.png')  







































        
        
