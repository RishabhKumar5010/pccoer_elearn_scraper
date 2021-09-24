# pccoer-elearn-scraper
A scraper and Automation testing utility for pccoerelearning.com website


### What does it do?

This selenium automation scrapes http://pccoerelearning.com/StudentDownload.php and puts the
scraped result into SQLite database.

### How to use?

NOTE :: Before using this code on http://pccoerelearning.com/StudentDownload.php
take necessary permissions from PCCOER (Nilesh Korade Sir).

Class `pccoer_ELearning` does the automatic scraping and automation testing.

Edit the following constructor call in the code as per requirements.

`pccoer_ELearning()`

You can pass upto 6 values to it,

    #depts = ['Computer Engineering'],
    #years = ['Third Year'],
    #courses = ['2015'],
    #semesters = ['First','Second'],
    #subtypes = ['Theory'])
    #subs = ['SEPM'])

All these arguments have to be a 'list' of values to be selected in that category

if any of these arguments aren't passed then all possible combinations for that entry will be considered

Without any argument, that is all possible combinations, the scraping usually takes around 10min to finish.

Once scraped the result would be displayed in the terminal associated with the execution of this program,
and as a `resource` table in `TestDB.db` SQLite output. `TestDB.db` would be generated in the current working
directory.

One can then use the following commands in an SQLite3 console in the same directory as
where `TestDB.db` is generated to view the full formatted table.

```SQL
.open TestDB.db
.mode columns
select * from resource;
```

Note the above works only in an SQLite3 console.

On debian systems to get SQLite:

`sudo apt install sqlite`

and then run

`sqlite3`

in a terminal

Other requirements:
* Firefox geckodriver
* pandas and selenium python packages.

### Features:

* Reattempts queries certain number of times considering both client and server side latencies and network problems.
* Generates offline copy of the fetch as SQL db to reduce load on server side query.
* Can be run multiple times without user to worry about cleaning the workspace.
* Standalone application.

### Use-cases:

* Testing if every selection is working right.
* Command line utility for listing all the resource available.
* Good for admin to track all resource on the site, in one place.
* SQL queries on the data fetched can be done, without risk of altering the
  original database (as this software creates a copy of the original view available to a basic user of the site)


### Automation testing results as of 6 Apr 2021:

* The options in 'year' select tag should be updated based on values chosen in 'dept' select tag.
eg. the website shows year options as 'First Year', 'Second Year', 'Third Year', 'Fourth Year' even if the dept is chosen
as 'First Year'. The automation spends a lot time trying such unfruitful combinations.

* After the user does a query, the site resets the form, which gives a bad UX if user wants to carry
multiple similar queries.

* Some AJAX calls take more than 3 sec for select tag to become active or for options to update.


### Credits:

* Proff. Nilesh Korade (my SEPM teacher)


