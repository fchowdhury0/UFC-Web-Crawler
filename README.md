# UFC-Web-Crawler
Parses the web and collects information for all fighters currently in contract with the UFC, outputting the data into a usable .csv file.


To run:

   python crawler.py


Function: Goes through list of fighter links and collects fighter data.

Data Collected: firstname, lastname, nickname, height, weight, reach, stance, record (wins, losses, draws), and if they're a current champion

Implementation: The immediate goal is to create a chrome web extension that will display fighter statistics on user mouseover.
Intended Audience: UFC fans, UFC betting enthusiasts 
Future Implementation: The end goal is to create a (hopefully reliable) fighter model with the data collected by the crawler.

To Fix/Add:
- more usable data types
  - change height value from imperial string to double metric form 
  - change reach from string into a double type 
  - remove f_link column 
  - bool_curr_belt to curr_belt(bool type)
  - new table on mariadb 
- automation
  - run at regular intervals
  - auto updates to maria db
- collecting other fighter data
  - more detailed statistics (significant strike avg, defensive and offensive statistics, opponent style evaluation, etc.)
