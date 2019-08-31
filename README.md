ETL PROJECT

We decided to focus our data search on Kaggle.com for the world major marathon winners. We were able to pull csv files that contained a list of all previous winners. The world major marathons are in Boston, Tokyo, New York, Chicago, Berlin and London. For our ETL project we focused on the male and female winners in Boston. 
For extraction we downloaded the csv files from kaggle.com. From the raw csv files, we created a Jupyter Notebook to be able to manipulate the data accordingly. During the read portion of loading the csv files we encountered encoding issues with the extraction Unicode transformation format. After much research we were able to utilize ISO8859_15 to help extract and read the file. Cleaning the data involved dropping all N/A fields and the columns titled note and state. After data was cleaned, we set index to year. 
The final database was created using PostgreSQL. The database contains two tables Table 1: Female Boston and Table 2: Male Boston. We used PostgreSQL because it is a relational database that allows us to collaborate and standardize diverse data sets. PostgreSQL also safeguards our data with password protected user accounts. Lastly, it enabled us to store data that can be queried later and increases data accuracy.

Summary of steps to create and access database: 
•	Go to Kaggle.com and search world major marathons 
•	Download csv files 
•	Create a Jupyter Notebook
•	Import dependencies: sqlalchemy pandas
•	Import/Read csv files using ISO8859_15 and pandas 
•	Create a data frame for each csv file
•	Drop Notes and States columns to keep more runner year information. 
•	Open PostgreSQL and create a new table to hold csv information
•	Establish a connection on Jupyter Notebook with PostgreSQL 
•	Load in csv files 
•	Check in Jupyter Notebook that table was created, and information was loaded by querying each respective table name 
