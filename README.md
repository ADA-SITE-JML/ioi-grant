# IOI GRANT RESEARCH PROJECT

The repository is a working ground of the ongoing research on 2019 IOI participants data. The aim is to analyze the whole competition data to derive useful information such as correlations and causations.

## INSIGHTS

Insights folder consists of 4 directories each of which describes contestant behavior from different aspect. Each folder contains SQL scripts, which can be run on the contest's 
PostgreSQL database, and the corresponding output data. Names of these folders and a short description for each of them are listed below:
1.  **Contestant requests statistics:** Gets contestant request count for each type of request at intervals of 30 min
2.  **Daily submission statistics:** There are 4 similar SQL scripts. First one gets submission count for each task at 30 min intervals. Others get count of the submissions which scored more than 0, 20, and 50 at 30 min intervals accordingly. 
3.  **Solution approaches:** Finds how much time each participant spend for each task before swithcing to another task.
4.  **WC requests statistics:** Finds how many times, contestants used a WC request within 45 minutes after asking for banana, apple, cupcake, chocolate, and water.

## DATABASE

The database folder consists of a README.md and an images folder. The importance of the readme file is to have all the ERD schema of the contest database in a neat form. The images folder consists of 2 files one is the general iconic image that has been used in the readme file and the latter one is the ERD schema in a format of png. This makes it easy to see the whole schema at once.

## AUTOMATION SCRIPTS

