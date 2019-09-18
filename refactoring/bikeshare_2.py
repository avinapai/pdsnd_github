import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
# Created a new mapping data for Days of week
DAY_DATA = { '1': 'Sunday', '2': 'Monday', '3': 'Tuesday', '4': 'Wednesday', '5': 'Thursday',
              '6': 'Friday', '7': 'Saturday' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Would you like to see data for chicago, new york city, or washington? \n")
    # This is to get the user choose only a City name provided and show a notice message if an incorrect choice is made
    while city not in ['chicago', 'new york city', 'washington']:
        print("Please make sure you enter either of the following: chicago, new york city, or washington? \n")
        city = input("Would you like to see data for chicago, new york city, or washington? \n")

    filterCriteria = input("Would you like to filter the data by month, day, both or not at all? Type 'none' for no time filter. \n")

    # TO DO: get user input for month (all, january, february, ... , june)
    # If user chooses "both" option, get user to input month and day value
    if filterCriteria in ['both']:
        month = input("Which month: january, february, march, april, may or june? \n")
        # This is to get the user choose only the Month provided and show a notice message if an incorrect choice is made
        while month not in ['january', 'february', 'march', 'april', 'may', 'june']:
            print("Please make sure you enter either of the following: january, february, march, april, may or june? \n")
            month = input("Which month: january, february, march, april, may or june? \n")

        day = input("What day? Please type your response as an integer (e.g, 1 =  Sunday.) \n")
        # This is to get the user choose only the day value provided and show a notice message if an incorrect choice is made
        while day not in ['1', '2', '3', '4', '5', '6', '7']:
            print("Please make sure you enter a valid day: (e.g, 1 =  Sunday.)? \n")
            day = input("What day? Please type your response as an integer (e.g, 1 =  Sunday.) \n")

    elif filterCriteria in ['month']:
        month = input("Which month: january, february, march, april, may or june? \n")
        # This is to get the user choose only the Month provided and show a notice message if an incorrect choice is made
        while month not in ['january', 'february', 'march', 'april', 'may', 'june']:
            print("Please make sure you enter either of the following: january, february, march, april, may or june? \n")
            month = input("Which month: january, february, march, april, may or june? \n")
        day = 'all'

    elif filterCriteria in ['day']:
        day = input("What day? Please type your response as an integer (e.g, 1 =  Sunday.) \n")
        # This is to get the user choose only the day value provided and show a notice message if an incorrect choice is made
        while day not in ['1', '2', '3', '4', '5', '6', '7']:
            print("Please make sure you enter a valid day: (e.g, 1 =  Sunday.)? \n")
            day = input("What day? Please type your response as an integer (e.g, 1 =  Sunday.) \n")
        month = 'all'

    elif filterCriteria in ['none']:
        day = 'all'
        month = 'all'
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    # Already handled above as part of the If condition...

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime to identify month and day of the week
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month

    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month_of_year = ['january', 'february', 'march', 'april', 'may', 'june']
        month = month_of_year.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

     # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == DAY_DATA[day]]

    # give user the ability to view 5 rows of data until the user chooses not to
    user_data_view = input("Would you like to see the first 5 rows of data (yes/no) ? \n")
    count = 0
    while user_data_view in ['yes', 'Yes', 'YES']:
        print(df[count: 5 + count])
        user_data_view = input("Would you still like to see the next 5 rows of data (yes/no) \n")
        count += 5

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    #print(df.head())
    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Popular Month:', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Popular Day of the Week:', popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Station:', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Popular End Station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    popular_start_end_station = (df['Start Station'] + df['End Station']).mode()[0]
    print('Most Popular Start and End Station:', popular_start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('The total travel time is :', df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('The average travel time is :', df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    if 'User Type' in df.columns:
        print('\nThe counts of user types are:\n', df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print('\nThe counts of Gender are:\n', df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('\nThe earliest year of birth :', df['Birth Year'].min().astype(int))
        print('\nThe most recent year of birth :', df['Birth Year'].max().astype(int))
        print('\nThe most common year of birth :', df['Birth Year'].mode()[0].astype(int))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    #washington csv does not have the data set for Gender and year of Birth

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
