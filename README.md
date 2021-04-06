# pccoer-elearn-scrapper
A scrapper for pccoerelearning.com website


### What does it do?

This selenium automation scrapes http://pccoerelearning.com/StudentDownload.php and puts the
scraped result into SQLite database.

### How to use?

Just call this class

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


### Applications:

* Testing if every selection is working right.
* Command line utility for listing all the resource available.
* Good for admin to track all resource on the site, in one place.
* SQL queries on the data fetched can be done, without risk of altering the
  original database (as this software creates a copy of the original view available to a basic user of the site)

