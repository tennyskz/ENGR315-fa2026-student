"""
CULMINATING ASSIGNMENT 2: RSI

Create a program which will provide answers to the tasks posed in the assignment description.

For this assignment, you will start from scratch with this blank template.
It is your reponsibility to include all necessary program components in this file.
Your code needs to be successful as well as sufficiently commented/documented to receive full credit.

The relevant data file is named "all_participant_data_rsi.csv" and is located in data > drop-jump.

All file paths need to be relative and execute from this file's directory;
the Visual Studio Code setting "Python > Terminal: Execute in File Dir" 
must be enabled in File > Preferences > Settings.

See Canvas for additional requirements.
"""

import numpy as np
import pandas as pd
from scipy.stats import ttest_1samp, ttest_rel, norm, ttest_ind, t, sem, chisquare, chi2
import matplotlib.pyplot as plt




path = "../../data/drop-jump/all_participant_data_rsi.csv"


alpha = 0.05    #given alpha value
confidence = 0.95   #given confidence level

df = pd.read_csv(path)

force_plate = df['force_plate_rsi']     #take out force plate and accelerometer columns
accelerometer = df['accelerometer_rsi']

participant_f = df[df['trial'].str.startswith('F', na=False)]   #take out the data for participant F and avoid crashes for NaN values

Accelerometer_f = participant_f['accelerometer_rsi']    #get accelerometer data for participant F
force_plate_f = participant_f['force_plate_rsi']    #get force plate data for participant F


def paired_t_test(data1, data2):    #perform paired t-test on the two data columns and return the t-stat and p-value
    t_stat, p_value = ttest_rel(data1, data2)
    return t_stat, p_value


def expected_normal_counts(_bins, _mu, _std, _num_samples):     #calculate the expected counts for a normal distribution


    expected_prob = np.diff(norm.cdf(_bins, loc=_mu, scale=_std))   #calculate the probability of a value being in each bin

    expected_counts = expected_prob *_num_samples   #multiply the probability by the number of samples to get the expected count for each bin
    return expected_counts


def normal_fit_test(_samples, _alpha):      #perform a chi-square test to determine if the samples fit a normal distribution


    fitted_mean, fitted_std = norm.fit(_samples)    #fit a normal distribution to the data and return the mean and standard deviation
    min_val = np.min(_samples)                      #find the min and max for the bins
    max_val = np.max(_samples)
    bins1 = np.linspace(min_val, max_val, 9)        #create 8 bins between the min and max values
    bins = np.r_[-np.inf, bins1, np.inf]        #add -inf and inf to the bins to catch all values

    
    
    observed_counts = np.histogram(_samples, bins=bins)[0]      #make a histogram of the samples and return the counts for each bin
    expected_counts = expected_normal_counts(bins, fitted_mean, fitted_std, len(_samples))  #calculate the expected counts for a normal distribution with the fitted mean and standard deviation


    chi_stat, p_value = chisquare(observed_counts, f_exp=expected_counts, ddof=2)   #find the chi2, ddof = 2 because we are estimating two parameters (mean and std) from the data
    reject = p_value < _alpha

    return chi_stat, p_value, reject

def plotting(_samples, _bins):
    
    _mean, _std = norm.fit(_samples)    #find the mean and standard deviation of the normal 

    count, bins, ignored = plt.hist(_samples, bins=_bins, density=True, edgecolor='black', label='Accelerometer RSI Data')  #plot the samples


    x = np.linspace(min(_samples), max(_samples), 100)
    plt.plot(x, norm.pdf(x, loc=_mean, scale=_std), linewidth=2, color='r', label='Expected Normal Distribution')   #plot the expected normal distribution

    plt.title('Histogram of Accelerometer RSI Data with Fitted Normal Distribution')
    plt.xlabel('Accelerometer RSI Value')
    plt.ylabel('Density')
    plt.legend()
    plt.show()

def get_stats(data, name):
    n = len(data)               #number of samples
    mean_f = np.mean(data)      #calculate mean and standard error
    std_error_f = sem(data)
    ci_lower, ci_upper = t.interval(0.95, df=n-1, loc=mean_f, scale=std_error_f)    #find the 95% confidence interval around the mean with the scale being the standard error
    print(name)
    print(f"Mean: {mean_f:.4f}, Standard Error: {std_error_f:.4f}, sample size: {n}") #display the data
    print(f"95% CI: ({ci_lower}, {ci_upper:.4f})\n")                                  #and the confidence interval

    return ci_lower, ci_upper


t_test_results = paired_t_test(force_plate, accelerometer)          #find and print the t-test results

print(f"T-test results: t-stat = {t_test_results[0]}, p-value = {t_test_results[1]}")

if t_test_results[1] < alpha:                         #determine if the t-test results are significant and print the appropriate message

    print("P < 0.05: Reject the null hypothesis, There is a significant difference between the two groups.")

else:
    
    print("P >= 0.05: Fail to reject the null hypothesis, There is no significant difference between the two groups.")

print("\n")

normal_fit_results = normal_fit_test(accelerometer, alpha)              #find and print the normal fit test results

print(f"Normal fit test results: chi2-stat = {normal_fit_results[0]}, p-value = {normal_fit_results[1]}")

if normal_fit_results[1] < alpha:                  #determine if the normal fit test results are significant and print the appropriate message

    print("P < 0.05: Reject the null hypothesis, The accelerometer data does not follow a normal distribution.")

else:
    
    print("P >= 0.05: Fail to reject the null hypothesis, The accelerometer data follows a normal distribution.")
print("\n")

plotting(accelerometer, 8)  #plot the accelerometer date with 8 bins

print(participant_f)    #print the data for participant F
print("\n")

get_stats(Accelerometer_f, "Accelerometer 95% confidence interval for Participant F")   #print the 95% confidence interval for the accelerometer data for participant F
get_stats(force_plate_f, "Force Plate 95% confidence interval for Participant F")       #print the 95% confidence interval for the force plate data for participant F