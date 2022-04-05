# Assignment-5
DATA 1202 - Assignment #5, Professor Omar Al-Trad


![Assignment_#5](https://user-images.githubusercontent.com/103003890/161653591-84319dba-5d17-4d4b-ac74-2398d0c1593b.png)


## Table of Contents

* [Purpose of project]
* [Introduction]
* [Steps Invlolved]
* [Conclusion]
* [References]


## Purpose 
This project deals with a challenge about extracting the data records from a huge dataset called as "Youtube_dataset" and putting it into a different dataset.
Our concerned column for this would be "Channel type"


## Introduction 
This project is done on Python 3 using different python libraries and visualisation packages.
The question/challenge was to: 
- Creating a function to calculate the distribution of channeltype from the top 1000
records.

## Steps invloved 
1) The project was started by importing the python libraries. Our project has used pandas, numpy and also 2 visualisation packages called seaborn and matplotlib.
   
    1.1 We can utilise the capacity of %matplotlib inline to make the inline plotting more strong, where the plots/charts will be shown just underneath the cell where we write our plotting command. (Kumar, 2021)

2) After importing the libraries, we loaded and imported our dataset, using "pd.read_csv" this function. 
pd.read_csv was utilized to stack the youtube_dataset as a dataframe with an
encoding of "cp1252" which takes into account characters, for example, "€" which was essential for
the dataset.
3) Next step was about using the subset function or loc() function. This function basically allows us to create a subset of the dataframe considering a particular row/column. 


    3.1 
    <img width="271" alt="image" src="https://user-images.githubusercontent.com/103003890/161672386-ee84da28-1393-4447-aa2d-fe5ba30ec2ca.png">
This "first row" & "last row" was entered as input.
4) Other function called, "groupby" was put in use to find the distribution.

## Conclusion
The distribution of the highest 1000 channel types were found by employing a variety of functions in
Python. This was then exported as a csv file.

## References
Kumar, B. (2021, August 16). What is matplotlib inline. pythonguides.com. https://pythonguides.com/what-is-matplotlib-inline/


# Thank You
