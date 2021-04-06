from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.select import Select
import pandas as pd
import io

import sqlite3

driver = webdriver.Firefox()

driver.get('http://pccoerelearning.com/StudentDownload.php')

driver.implicitly_wait(10)

conn = sqlite3.connect('TestDB.db')
c = conn.cursor()

try:
    c.execute('drop table resource')
    #conn.commit()
except:
    pass

try:
    c.execute('create table resource (Department varchar(30), Year char(2), Course char(4),\
            Semester varchar(10), SubjectType varchar(15), Subject varchar(30), Unit varchar(2), FileName varchar(30),\
            FacultyName varchar(30))')
except:
    pass

class pccoer_ELearning:
    def __init__(self,
            depts = 'dept',
            years = 'year',
            courses = 'course',
            semesters = 'sem',
            subtypes = 'subtype',
            subs = 'subject'):

        self.depts = depts
        self.years = years
        self.courses = courses
        self.semesters = semesters
        self.subtypes = subtypes
        self.subs = subs

        self.fill_up()

    @staticmethod
    def choose(Id,val=None):
        for i in range(10):
            try:
                sel = Select(driver.find_element_by_xpath(f'//select[@id="{Id}"]'))

                if val:
                    sel.select_by_visible_text(val)
                else:
                    options = list(map(lambda x:x.text, sel.options))
                    try:
                        options.remove('')
                    except:
                        pass
                    if len(options)==0:
                        raise Exception('Option not loaded')
                    return options
                break
            except Exception as e:
                print('reattempting (option not loaded) :',i,e.args)
            sleep(1)
        return []


    def fill_up(self):

        select = lambda x:x if isinstance(x,list) else self.choose(x)

        for dept in select(self.depts):
            self.choose('dept',dept)

            for year in select(self.years):
                self.choose('dept',dept)
                self.choose('year',year)

                for course in select(self.courses):
                    self.choose('dept',dept)
                    self.choose('year',year)
                    self.choose('course',course)

                    for semester in select(self.semesters):
                        self.choose('dept',dept)
                        self.choose('year',year)
                        self.choose('course',course)
                        self.choose('sem',semester)

                        for subtype in select(self.subtypes):
                            self.choose('dept',dept)
                            self.choose('year',year)
                            self.choose('course',course)
                            self.choose('sem',semester)
                            self.choose('subtype',subtype)

                            for subject in select(self.subs):

                                print('================')
                                self.choose('dept',dept)
                                print(dept)
                                self.choose('year',year)
                                print(year)
                                self.choose('course',course)
                                print(course)
                                self.choose('sem',semester)
                                print(semester)
                                self.choose('subtype',subtype)
                                print(subtype)
                                self.choose('subject',subject)
                                print(subject)


                                driver.find_element_by_id('listall').click()
                                sleep(1)
                                self.extract_table()

    @staticmethod
    def extract_table():
        for i in range(10):
            try:
                data =[]
                table = driver.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/article/table')
                for tr in table.find_elements_by_tag_name('tr'):
                    row = []
                    for td in tr.find_elements_by_tag_name('td'):
                        row.append(td.text)
                    if row:data.append(row)

                if not data:
                    raise Exception('Table not loaded')
                else:
                    pccoer_ELearning.to_sqlDB(data)
                    break
            except Exception as e:
                if 'No Data Found' in driver.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/article').text:
                    break
                print('reattempting (table not loaded) :',i,e.args)
            sleep(1)

    @staticmethod
    def to_sqlDB(data):
        for i in data:
            c.execute('insert into resource values("{}")'.format('","'.join(i)))


web = pccoer_ELearning()
            #depts = ['Computer Engineering'],
            #years = ['Third Year'],
            #courses = ['2015'],
            #semesters = ['First'],
            #subtypes = ['Theory'])
            #subs = ['SEPM'])


df = pd.read_sql_query("SELECT * FROM resource", conn)

pd.set_option('display.max_rows', df.shape[0]+1)

print(df['FacultyName'])

conn.commit()
conn.close()
driver.quit()

