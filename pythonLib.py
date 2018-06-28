import csv
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
import os
import time
import requests
import json


def request_fun(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html5lib')
    return soup


## Read From CSV (First Col in done)
def read_col_csv(filename,ind):
    done = []
    ind = int(ind)
    if (os.path.exists(filename)):
        with open(filename, 'rb') as f:
            reader = csv.reader(f)
            for row in reader:
                try:
                    done.append(row[ind])
                except IndexError:
                    continue
    return done

## Read From CSV (First Col in done)
def read_done_csv(filename):
    done = []
    if (os.path.exists(filename)):
        with open(filename, 'rb') as f:
            reader = csv.reader(f)
            for row in reader:
                try:
                    done.append(row[3])
                except IndexError:
                    continue
    return done

## Read From CSV (all Col in csv file)
def read_full_csv(filename,category):
    done = []
    if (os.path.exists(filename)):
        with open(filename, 'rb') as f:
            reader = csv.reader(f)
            for row in reader:
                try:
                    if row[0] == category:
                        done.append([row[0],row[1],row[2],row[3]])
                    else:
                        pass
                    
                except IndexError:
                    continue
    return done


## Read From CSV (all Col in csv file)
def read_full_csv_error(filename):
    done = []
    if (os.path.exists(filename)):
        with open(filename, 'rb') as f:
            reader = csv.reader(f)
            c = 0
            for row in reader:
                try:
                    if c == 0:
                        pass
                    else:
                        
                        done.append([row[0],row[1],row[2],row[3]])
                    
                except IndexError:
                    continue
                c = c + 1
    return done



## Save to CSV
def save_to_csv(filename,data):

    new_data = []
    with open(filename, 'ab') as f:
        writer = csv.writer(f)
        try:
            writer.writerow(data)
        except:
            try:
                for x in data:
                    try:
                        x.encode('utf-8')
                    except:
                        try:
                            x.decode('utf-8')
                        except:
                            x = ''
                    new_data.append(x)
            except:
                pass
            new_data = [x.encode('ascii', 'replace') for x in new_data]
            writer.writerow(new_data)


##  Clicks element
def click(driver,elem):
    actions = ActionChains(driver)
    actions.move_to_element(elem)
    actions.click(elem)
    actions.perform()
    
##  Clicks elem & types sendinfo in it
def click_send(driver,elem,sendinfo):
    elem.click()
    actions = ActionChains(driver)
    actions.move_to_element(elem)
    actions.click(elem)
    
    actions.send_keys(sendinfo)
    actions.perform()


def click_dropdown(elem,optiontext):
    for option in elem.find_elements_by_tag_name('option'):
        if option.text == optiontext:
            option.click() # select() in earlier versions of webdriver
            break



