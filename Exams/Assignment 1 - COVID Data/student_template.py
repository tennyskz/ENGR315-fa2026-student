import sys

"""
Create a program which will provide answers to the questions posed in the assignment description.
We've provided a function which will parse the NYT covid database file (named "us-counties.csv"); 
however, its correct implementation will be up to you. DO NOT MODIFY THIS FUNCTION.
Your code needs to be successful as well as sufficiently commented/documented to receive full credit.
"""


def parse_nyt_data(file_path=''):
    """
    Parse the NYT covid database and return a list of tuples. Each tuple describes one entry in the source data set.
    Date: the day on which the record was taken in YYYY-MM-DD format
    County: the county name within the State
    State: the US state for the entry
    Cases: the cumulative number of COVID-19 cases reported in that locality
    Deaths: the cumulative number of COVID-19 death in the locality

    :param file_path: Path to data file
    :return: A List of tuples containing (date,county, state, fips, cases, deaths) information

    ____________________ DO NOT MODIFY THIS FUNCTION ___________________
    """
    # data point list
    data=[]

    # open the NYT file path
    try:
        fin = open(file_path)
    except FileNotFoundError:
        print('File ', file_path, ' not found. Exiting!')
        sys.exit(-1)

    # get rid of the headers
    fin.readline()

    # while not done parsing file
    done = False

    # loop and read file
    while not done:
        line = fin.readline()

        if line == '':
            done = True
            continue

        # format is date,county,state,fips,cases,deaths
        (date,county, state, fips, cases, deaths) = line.rstrip().split(",")

        # clean up the data to remove empty entries
        if cases=='':
            cases=0
        if deaths=='':
            deaths=0

        # convert elements into ints
        try:
            entry = (date,county,state, fips, int(cases), int(deaths))
        except ValueError:
            print('Invalid parse of ', entry)

        # place entries as tuple into list
        data.append(entry)


    return data

### YOUR CODE HERE ###

data = parse_nyt_data('../../data/covid/us-counties.csv')   #collect the data from the csv

Hburg_list = [] #create a list for harrisonburg
Rock_list = []  #create a list for rockingham



def day_max(data_list, location):   #function for max day
    max_daily_cases = 0

    for i in range(len(data_list)): #for every entry in the list
        date = data_list[i][0]     #get the date
        cases = data_list[i][4]    #get the number of cases

        if i == 0:                  #the first entry is the first case, so set new_cases to cases
            new_cases = cases
        else:
            new_cases = cases - data_list[i-1][4]      #calculate new cases by subtracting previous day's cases


        #print('Date:', date, 'New cases:', new_cases)   #debugging

        if new_cases > max_daily_cases:         #check if the new daily cases are larger than the current max
            max_daily_cases = new_cases         #save the number and the date
            max_date = date


    print("\n")

    print(location, 'max daily cases:', max_daily_cases, 'on', max_date)


def week_max(data_list, location):   #function for max 7-day window
    weekmax = 0

    for i in range(7 , len(data_list)):     #for every entry starting from the 7th day

        week_amount = data_list[i][4] - data_list[i-7][4]   #calculate the 7-day window of new cases ending on the current day
                                                            #This gives the sum over 7 days since what would be the 8th day [i-7] is subtracted out

        if week_amount > weekmax:       #Check if the current 7-day window is larger than the current max. if so, save it and the start and end date
            weekmax = week_amount
            start_date = data_list[i-6][0]
            end_date = data_list[i][0]

    print("\n")

    print(location, 'max 7-day window:', weekmax, 'from', start_date, 'to', end_date)





for i in data:

    if i[1] == "Harrisonburg city" and i[2] == "Virginia":     #if the entry is for Harrisonburg, add to hburg list
        Hburg_list.append(i)

    elif i[1] == "Rockingham" and i[2] == "Virginia":   #if the entry is for Rockingham, add to rock list
        Rock_list.append(i)


 #the first entry for Hburg & rockingham is the first recorded case, so print the first date for each location
print('The first recorded case in Harrisonburg happened on', Hburg_list[0][0],'\n')

print('The first recorded case in Rockingham happened on', Rock_list[0][0])


#Max days for Harrisonburg and Rockingham
day_max(Hburg_list, 'Harrisonburg')

day_max(Rock_list, 'Rockingham')


#Max 7 day for Harrisonburg and Rockingham
week_max(Hburg_list, 'Harrisonburg')

week_max(Rock_list, 'Rockingham')

