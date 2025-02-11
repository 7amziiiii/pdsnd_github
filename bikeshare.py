"""
Bikeshare Data Analysis

This script allows users to explore US bikeshare data for three cities:
- Chicago
- New York City
- Washington

Users can filter the data by month and day to get insights on:
- The most common travel times
- The most popular stations
- Trip duration statistics
- User demographics
"""

import time
import pandas as pd
import numpy as np

# CITY_DATA = {
#     'chicago': 'C:/Users/Hamza/Desktop/all/chicago.csv',
#     'new york city': 'C:/Users/Hamza/Desktop/all/new_york_city.csv',
#     'washington': 'C:/Users/Hamza/Desktop/all/washington.csv'
# }

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def get_filters():
    """
    Asks user to specify a city, month, and day for analysis.
    Returns:
        (str) city: The chosen city for analysis
        (int) month: Month filter (1-6) or 0 for no filter
        (int) day: Day filter (1-7) or 0 for no filter
    """
    print("Hello! Let's explore some US bikeshare data.")

    # Get user input for city
    while True:
        city = input("Choose a city (chicago, new york city, washington): ").strip().lower()
        if city in CITY_DATA:
            break
        else:
            print("Invalid city name. Please enter one of the available cities.")

    # Get user input for month (1-6) or 0 for no filter
    while True:
        month = input("Select a month as number (1-6) please or 0 for no filter: ").strip()
        if 0 <= int(month) <= 6:
            month = int(month)
            break
        else:
            print("Invalid entry. Please enter a number between 0 and 6.")

    # Get user input for day (1-7) or 0 for no filter
    while True:
        day = input("Select a day (1-7) or 0 for no filter:").strip()
        if 0 <= int(day) <= 7:
            day = int(day)
            break
        else:
            print("Invalid entry. Please enter a number between 0 and 7.")

    print("-" * 40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday + 1  

    if month != 0:  
        df = df[df['month'] == month]

    if day != 0:  
        df = df[df['day_of_week'] == day]

    return df

def time_stats(df):
    """
    Displays statistics on the most frequent times of travel.
    """
    print("\nFinding the most common times of travel...")
    start_time = time.time()

    print(f"Most common month: {df['month'].mode()[0]}")
    print(f"Most common day of the week: {df['day_of_week'].mode()[0]}")
    print(f"Most common start hour: {df['Start Time'].dt.hour.mode()[0]}")

    print(f"This took {time.time() - start_time:.2f} seconds.")
    print("-" * 40)

def station_stats(df):
    """
    Displays statistics on the most popular stations and trip.
    """
    print("\nCalculating popular stations and trip...")
    start_time = time.time()

    print(f"Most common start station: {df['Start Station'].mode()[0]}")
    print(f"Most common end station: {df['End Station'].mode()[0]}")
    df['trip_route'] = df['Start Station'] + " to " + df['End Station']
    print(f"Most common trip route: {df['trip_route'].mode()[0]}")

    print(f"This took {time.time() - start_time:.2f} seconds.")
    print("-" * 40)

def trip_duration_stats(df):
    """
    Displays statistics on the total and average trip duration.
    """
    print("\nAnalyzing trip durations...")
    start_time = time.time()

    print(f"Total travel time: {df['Trip Duration'].sum()} seconds")
    print(f"Average travel time: {df['Trip Duration'].mean():.2f} seconds")

    print(f"This took {time.time() - start_time:.2f} seconds.")
    print("-" * 40)

def user_stats(df):
    """
    Displays statistics on bikeshare users.
    """
    print("\nCalculating user stats...")
    start_time = time.time()

    if 'User Type' in df.columns:
        print("Counts of user types:")
        print(df['User Type'].value_counts())

    if 'Gender' in df.columns:
        print("\nCounts of gender:")
        print(df['Gender'].value_counts())

    if 'Birth Year' in df.columns:
        print(f"\nEarliest birth year: {int(df['Birth Year'].min())}")
        print(f"Most recent birth year: {int(df['Birth Year'].max())}")
        print(f"Most common birth year: {int(df['Birth Year'].mode()[0])}")

    print(f"\nThis took {time.time() - start_time:.2f} seconds.")
    print("-" * 40)

def display_raw_data(df):
    """
    Displays raw data upon user request, 5 rows at a time.
    """
    i = 0
    pd.set_option('display.max_columns', None)  # Show all columns
    while True:
        raw = input("Would you like to see 5 rows of raw data? Enter 'yes' or 'no': ").strip().lower()
        if raw == 'no':
            break
        elif raw == 'yes':
            print(df.iloc[i:i+5])  # Display the next 5 rows
            i += 5
        else:
            print("Invalid input. Please enter only 'yes' or 'no'.")

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)
        restart = input("\nWould you like to restart? Enter 'yes' or 'no': ").strip().lower()
        if restart != 'yes':
            print("Thanks for exploring bikeshare data! Goodbye.")
            break

# just some changes
if __name__ == "__main__":
    main()