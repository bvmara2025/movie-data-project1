# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 10:19:40 2024

@author: Blessing
"""
"""
import pandas as pd

file = pd.read_csv("movie_dataset.csv")

print(file)
"""

import pandas as pd

df = pd.read_csv("movie_dataset.csv",
                   index_col=0)

column_names=["Rank","Title","Genre","Description","Directors","Actors",
              "Year","Runtime_minutes","Rating","Votes","Revenue_millions",
              "metascore"]

df = pd.read_csv("movie_dataset.csv",
                     index_col=0,
                   header=0,
                   names = column_names)

ave_Year = df["Year"].mean()
df["Year"].fillna(ave_Year, inplace = True)

ave_Runtime_minutes = df["Runtime_minutes"].mean()
df["Runtime_minutes"].fillna(ave_Runtime_minutes, inplace = True)

ave_Rating = df["Rating"].mean()
df["Rating"].fillna(ave_Rating, inplace = True)

ave_Votes = df["Votes"].mean()
df["Votes"].fillna(ave_Votes, inplace = True)


ave_Revenue_millions = df["Revenue_millions"].mean()
df["Revenue_millions"].fillna(ave_Revenue_millions, inplace = True)


ave_metascore = df["metascore"].mean()
df["metascore"].fillna(ave_metascore, inplace = True)

#Questions
# Q1: Highest rated movie

max_Rating = df["Rating"].max()

#max_row_name = df.idxmax().index.values[0]


    
#summary_stats = df.describe()

#print(summary_stats)

highest_rated_movie = df[df["Rating"] == df["Rating"].max()]
highest_rated_movie_title = highest_rated_movie["Title"].iloc[0]

print(f"The highest rated movie is '{highest_rated_movie_title}'.")

#print("Highest rated movie")
print(max_Rating)

#max_value = df.max().max()
#max_row_name = df.idxmax().index.values[0]


#Q2: What is the average revenue of all movies in the dataset?


ave_Revenue_millions = df["Revenue_millions"].mean()
df["Revenue_millions"].fillna(ave_Revenue_millions, inplace = True)

print("Average Revenue is R (millions)")
print(ave_Revenue_millions)

#Q3: Calculate and display the average revenue of movies from 2015 to 2017
movies_2015_to_2017 = df[(df["Year"] >= 2015) & (df["Year"] <= 2017)]
average_revenue_2015_to_2017 = movies_2015_to_2017["Revenue_millions"].mean()
print(f"The average revenue of movies from 2015 to 2017 is: ${average_revenue_2015_to_2017:.2f} million")

#Q4: How many movies were released in the year 2016?

# Count and display the number of movies released in 2016
movies_in_2016_count = df[df['Year'] == 2016].shape[0]
print(f"Number of movies released in 2016 on modified data: {movies_in_2016_count}")

#Q5: How many movies were directed by Christopher Nolan?
nolan_count = df[df["Directors"] == "Christopher Nolan"].shape[0]
print(f"Number of movies directed by Christopher Nolan: {nolan_count}")

#Q6: How many movies in the dataset have a rating of at least 8.0?

# Count and display the number of movies with a rating of at least 8.0
highly_rated_movies_count = df[df["Rating"] >= 8.0].shape[0]
print(f"Number of movies with a rating of at least 8.0: {highly_rated_movies_count}")

#Q7:What is the median rating of movies directed by Christopher Nolan?

#Calculate and display the median rating of Christopher Nolan's movies
nolan_median_rating = df[df['Directors'] == 'Christopher Nolan']['Rating'].median()
print(f"The median rating of movies directed by Christopher Nolan is: {nolan_median_rating}")

#Q8:Find the year with the highest average rating? 

# Find the year with the highest average rating and display it
yearly_average_rating = df.groupby('Year')['Rating'].mean()
year_with_highest_avg_rating = yearly_average_rating.idxmax()
highest_avg_rating = yearly_average_rating.max()
print(f"The year with the highest average rating is {year_with_highest_avg_rating} with an average rating of {highest_avg_rating:.2f}.")

#Q9: What is the percentage increase in number of movies made between 2006 and 2016?

# Calculate and display the percentage increase in the number of movies from 2006 to 2016
movies_in_2006 = df[df['Year'] == 2006].shape[0]
movies_in_2016 = df[df['Year'] == 2016].shape[0]
percentage_increase = ((movies_in_2016 - movies_in_2006) / movies_in_2006) * 100
print(f"Percentage increase in the number of movies from 2006 to 2016: {percentage_increase:.2f}%")

#Q10: Find the most common actor in all the movies?


#Q11: How many unique genres are there in the dataset?

# Calculate and display the number of unique genres in the dataset
all_genres = df['Genre'].str.split(',').explode()
unique_genres = set(all_genres)
number_of_unique_genres = len(unique_genres)
print(f"There are {number_of_unique_genres} unique genres in the dataset.")

#Q12

print("0.3 to 0.5 is low correlation ")
print("0.51 to 0.7 is moderate correlation ")
print("0.71 to 1.0 is high correlation ")


corr1 = df["Rating"].corr(df["Votes"])
print("correlationship between Rating and Votes is:")
print(corr1)


def correlation(corr1):
    if corr1< 0.3:
        return "No correlation"
    elif 0.3 <= corr1 < 0.5:
        return "low correlation"
    elif 0.5 <= corr1 < 0.7:
        return "moderate correlation"
    else:
        return "high correlation"
    
print(correlation(corr1))

#corr2

corr2 = df["Runtime_minutes"].corr(df["Rating"])
print("correlationship between Runtime and Votes is:")
print(corr2)


def correlation(corr2):
    if corr2< 0.3:
        return "No correlation"
    elif 0.3 <= corr2 < 0.5:
        return "low correlation"
    elif 0.5 <= corr2 < 0.7:
        return "moderate correlation"
    else:
        return "high correlation"
    
print(correlation(corr2))
 
#corr3

corr3 = df["Rating"].corr(df["metascore"])
print("correlationship between Rating and metascore is:")
print(corr3)


def correlation(corr3):
    if corr3< 0.3:
        return "No correlation"
    elif 0.3 <= corr3 < 0.5:
        return "low correlation"
    elif 0.5 <= corr3 < 0.7:
        return "moderate correlation"
    else:
        return "high correlation"
    
print(correlation(corr3))
 
#corr4

corr4 = df["Votes"].corr(df["metascore"])
print("correlationship between Rating and metascore is:")
print(corr4)


def correlation(corr4):
    if corr4< 0.3:
        return "No correlation"
    elif 0.3 <= corr4 < 0.5:
        return "low correlation"
    elif 0.5 <= corr4 < 0.7:
        return "moderate correlation"
    else:
        return "high correlation"
    
print(correlation(corr4))
 
#corr5

corr5 = df["Runtime_minutes"].corr(df["Revenue_millions"])
print("correlationship between Runtime_minutes and Revenue_millions is:")
print(corr5)


def correlation(corr4):
    if corr5< 0.3:
        return "No correlation"
    elif 0.3 <= corr5 < 0.5:
        return "low correlation"
    elif 0.5 <= corr5 < 0.7:
        return "moderate correlation"
    else:
        return "high correlation"
    
print(correlation(corr5))


#column_names=["Rank","Title","Genre","Description","Directors","Actors",
#              "Year","Runtime_minutes","Rating","Votes","Revenue_millions",
#              "metascore"]   

#


#


#print(df)