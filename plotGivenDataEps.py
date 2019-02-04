#
# This file was written for an assignment on epsilon differential privacy
#
# (Course: CSC 591 - Privacy at NCSU, Spring 2019)
#
# Draw Histograms for data from a CSV file...
# ..with epsilon = 0.01, 1, 10
#

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Function to read given CSV file and store salaries into an array
def find_salaries():
	data = pd.read_csv('IL_employee_salary.csv', sep=',',header=None, index_col =0, skipinitialspace=True)
	salaries = []
	i=1
	while(i<len(data[2])):
		s = data[2][i]
		s = s.replace("$","")
		s = s.replace(",","")
		salaries.append(float(s))
		i+=1
	return salaries

# Function to set the bins for the histogram
def set_bin_arr(bin_max):
	i=0
	bins_arr = []
	while(i<=bin_max):
		bins_arr.append(i)
		i+=10000
	return bins_arr

# Plot the sets of data on histogram
def plot_histogram(data,bin_max):
	plt.hist(data,bins=set_bin_arr(bin_max),edgecolor='black',linewidth=1,color=['green','blue','orange','red'],
		label=['Actual','epsilon=0.1','epsilon=1','epsilon=10'])
	plt.ylabel('Number of Employees')
	plt.xlabel('Salary (in thousands of dollars)')
	plt.title('Number of employees in different salary brackets')
	plt.xticks(range(0,bin_max,10000))
	plt.xticks(rotation=90)
	plt.yticks(range(0,42,2))
	plt.legend()
	plt.show()

# find noise based on epsilon
def get_noise(epsilon):
	loc,scale = 0.,float(2/epsilon)
	return np.random.laplace(loc,scale,1)

# with given epsilon, add noise to each salary 
def get_noisy_salaries(salaries,epsilon):
	epsilon_salaries = []
	for salary in salaries:
		appended_val = salary+get_noise(epsilon)
		epsilon_salaries.append(appended_val)
	return epsilon_salaries

def main():
	salaries = find_salaries()
	salaries_01 = get_noisy_salaries(salaries,0.1)
	salaries_1 = get_noisy_salaries(salaries,1)
	salaries_10 = get_noisy_salaries(salaries,10)
	bin_max = int(np.amax([np.amax(salaries),np.amax(salaries_01),np.amax(salaries_1),np.amax(salaries_10)]))
	plot_histogram([salaries,salaries_01,salaries_1,salaries_10],bin_max)

main()