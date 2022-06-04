
import numpy as np
import pandas as pd
import time

CITY_DATA = {"chicago": "chicago.csv",
           "new york":"new_york_city.csv",
           "washington":"washington.csv"}



def get_filters():

    print("Hi! want to explore US bikeshare data?.")

    city = None
    while city not in CITY_DATA.keys():
        print("please choose the city you want to explore its data")

        print("\nchoose between "
              "1-chicago "
              "2-new york "
              "3-washington ")
        print("make sure no missing letter from city name")
        city=input("enter the city name : ").lower().strip()

    print("you chose {} city to explore its data".format(city))


    MONTH_DATA= {"january" : 1 ,
                 "february" : 2 ,
                 "march" : 3 ,
                 "april" : 4 ,
                 "may" : 5 ,
                 "june" : 6,
                 "all" : 7}
    month= None
    while month not in MONTH_DATA.keys() :
        print("please choose valid month make sure no missing letter")
        print("example January or january ")
        month =input("enter a month : ").lower().strip()

    print("you chose {}".format(month))


    DAY_DATA = {"monday": 1,
                "tuesday": 2,
                "wednesday": 3,
                "thursday": 4,
                "friday": 5,
                "saturday": 6,
                "sunday": 7,
                "all": 8}

    day = None
    while day not in DAY_DATA.keys():
        print("please enter a valid weekday\na valid weekday contains no missing letters\nexample : Sunday or sunday")
        print("you can also select 'all' to view the whole week data")
        day = input("day name : ").lower().strip()

    print("you chose {}".format(day))
    return city,month,day


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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    common_month = df['month'].mode()[0]
    print('the most common month {}'.format(str(common_month)))

    # TO DO: display the most common day of week

    common_day = df['day_of_week'].mode()[0]
    print('the most common day {}'.format(str(common_day)))

    # TO DO: display the most common start hour
    df['hours']=df['Start Time'].dt.hour
    common_hour = df['hours'].mode()[0]

    print('the most common start hour {}'. format(str(common_hour)))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    start_station = df['Start Station'].mode()[0]
    print('the most frequent {}'.format(str(start_station)))

    # TO DO: display most commonly used end station
    end_station= df['End Station'].mode()[0]
    print('the most common end station {}'.format(str(end_station)))

    # TO DO: display most frequent combination of start station and end station trip
    df['combined'] = df['Start Station'] + df['End Station']
    combination = df['combined'].mode()[0]
    print( 'most common combination {}'.format(str(combination)))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print('number of user type: \n{}'.format(str(user_type)))

    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print('\n\n Type of user by gender as follow :\n{}'.format(str(gender)))
    except:
        print('There is no gender data for this city.')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliset = df['Birth Year'].min()
        most_recent = df['Birth Year'].max()
        most_common = df['Birth Year'].mode()[0]
        print('the earliest year of birth {}. \nThe most recent year of birth {}.\nThe most common year of birth {}.'.format(int(earliset),int(most_recent),int(most_common)))
    except:
        print('There is no birth year data for this city')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df) : 
    """to display 5 rows of the data """
    user_input_list = ['yes','no']
    row_data = None
    counter =0


    while row_data not in user_input_list :
        print('Do you want to view row data?\nPlease choose : \nYes or No ')
        row_data = input().lower().strip()
        if row_data == 'yes':
            print(df.iloc[counter:counter+5])
            counter+=5

        elif row_data == 'no' :
            break
    while row_data == 'yes':
        print("\nDo you want more data ?")
        row_data =input().lower()

        if row_data == 'yes' :
            print(df.iloc[counter:counter+5])
            counter += 5
        elif row_data != 'yes':
            break

    print('-' * 40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()



















































































































































































































































