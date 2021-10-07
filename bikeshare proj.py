import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    while True:
         city = input('please enter the city name chicago - new york city - washington: ')
         city.lower()
        
         if city in CITY_DATA:
             break
         else:
              print("please enter the correct city name chicago or new york city or washington ")
    # ask user to choose filtering by month  or day or both or none          
    filter = input('would you like to filter by month , day, , both or none to not at all: ')
    filter.lower()
    while filter not in['month','day','both','none'] : 
          print('invalid! please enter month, day, both or none')        
          filter = input('would you like to filter by month or day or all')
          filter.lower()
              
    # get user input for month (all, january, february, ... , june)
    if filter == 'month' or filter == 'both':
       while True :
           month = input("please enter the month name: 'january','february','march','april','may','june': ")
           month.lower()
           months =['january','february','march','april','may','june']
           if month not in months:
              print('this is not valid month name ,please enter a valid month name')
           else:
              break
    else:
         month = 'all'
          
    # get user input for day of week (all, monday, tuesday, ... sunday)
    if filter == 'day' or filter == 'both':
      while True :
          day = input("please enter day name :'saturday','sunday','monday','tuesday','wednesday','thursday','friday': ")
          day.title()
          days =['Saturday','sunday','monday','tuesday','wednesday','thursday','friday']
          if day not in days:
             print('please enter a valid day name')
          else:
              break
    else:
        day = 'all'

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
    # file name that will be open
    file_name = CITY_DATA[city]
    df = pd.read_csv(file_name)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    
    df['day_of_week']=df['Start Time'].dt.day_name()
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month']== month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']== day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    #convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    months =['january','february','march','april','may','june']

    # extract month from the Start Time column to create an month column
    df['month']=df['Start Time'].dt.month
    # calculate the most common month
    common_month_n = df['month'].mode()[0]
    common_month =  months[common_month_n-1]
    # display the most common month
    print('Most Popular Start Month:',common_month)

    # extract day of week from the Start Time column 
    # to create an day_of_week column
    df['day_of_week']=df['Start Time'].dt.day
    # calculate the most common month
    common_day = df['day_of_week'].mode()[0]
    # display the most common day of week
    print('Most Popular Start Day:',common_day)



    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # find the most popular hour
    popular_hour = df['hour'].mode()[0]
    # display the most common start hour
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_used_start = df['Start Station'].mode()[0]
    print('most common start station is: ',common_used_start)

    # display most commonly used end station
    common_used_end= df['End Station'].mode()[0]
    print('most common End station is: ',common_used_end)

    # display most frequent combination of start station and end station trip
    common_st_and_end = (df['Start Station']+'to'+df['End Station']).mode()[0]
    print('most common  trip is: ',common_st_and_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('the total travel time: {} second or {} minutes  '.format(total_travel_time,total_travel_time/60))
    print('or{} hour'.format(total_travel_time/60*60))

    # display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print('the average travel time: {} second or {} minutes  '.format(average_travel_time,average_travel_time/60))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('counts of user types')
    # print value counts for each user type
    user_types = df['User Type'].value_counts()
    print(user_types) 

    # Display counts of gender
    if  'Gender' in df:
        gender_counts = df['Gender'].value_counts()
        print("counts of Gender counts is:",gender_counts)

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        
        #the earliest year of birth 
        earliest_year = int(df['Birth Year'].min())
        print("the earliest year of birth is: {}".format(earliest_year))
        
        #the most recent year of birth
        recent_year = int(df['Birth Year'].max())
        print("the recent year of birth is: {}".format(recent_year))
        
        #the most common year of birth

        common_year = int(df['Birth Year'].mode()[0])
        print("the common year of birth is: {}".format(common_year))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_rowdata(df):
    '''
    this function is to display the first 5 rows in row data 
    argument data frame as df 
    returns the first five rows in data fram
       
    
    '''
    row  = 0
    while True:
        display = input('would you like to display the 5 rows in row data yes/no: \n')
        display.lower()
        if display =='no':
           break
        elif display == 'yes':
               print(df.iloc[row:row+5])
               row+=5
               nextfive = input('would you like to display next five?\n')
               nextfive.lower()
               if nextfive == 'yes':
                   continue;
               elif nextfive == 'no':
                   break;
               else:
                   print('not valid answer please answer the question below')
                   continue
                   
        else :
             print('not valid answer please answer the question below')
             
             
             
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_rowdata(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


  if __name__ == "__main__":
	main()




