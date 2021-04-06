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

### Applications:

* Testing if every selection is working right.
* Command line utility for listing all the resource available.
* Good for admin to track all resource on the site, in one place.
* SQL queries on the data fetched can be done, without risk of altering the
  original database (as this software creates a copy of the original view available to a basic user of the site)


### Inspiration:

I have almost never submitted or needed to submit a written assignment. Be it school or college, I try my best
not to submit a written assignment unless it seems worth it or unavoidable. I do however like to approach my
faculties, and ask them if I could submit a small project instead (off syllabus). I maybe lucky to have understanding
teachers in this matter, specially in my engineering college (PCCOER), that I hardly ever need to submit a written assignment.
Infact by what I have observed, my teachers love to have such mini-projects instead of assignments. This is not however
a default culture that is openly encouraged, but kindoff a secret bypass that is available for anyone
that wants to go that way. Again I am lucky to have such faculties in my education journey.

This was created as a substitute to SEPM assignment, and for practicing selenium in python.

### Credits:

* Proff. Nilesh Korade (my SEPM teacher)


