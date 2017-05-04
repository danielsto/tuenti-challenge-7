from selenium import webdriver
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

firefox_capabilities = DesiredCapabilities.FIREFOX
url = 'http://52.49.91.111:8036/word-soup-challenge'
driver = webdriver.Firefox(executable_path='C:/Users/danie/Downloads/geckodriver-v0.16.1-win64/geckodriver.exe', capabilities=firefox_capabilities)
driver.get(url)
time.sleep(2)
html = driver.page_source

words_list = []
words = driver.find_element_by_id('words').find_elements_by_css_selector('*')
for word in words:
    if word.get_attribute('id') != 'time1' and word.get_attribute('id') != 'time-left' and word.tag_name != 'h1':
        # print("INSERTANDO", word.get_attribute('innerHTML'))
        words_list.append(word.get_attribute('innerHTML'))

rows = driver.find_elements_by_tag_name('tr')

soup = []
for row in rows:
    row_val = []
    cols = row.find_elements_by_tag_name('td')
    for col in cols:
        row_val.append(col.get_attribute('innerHTML'))
    soup.append(row_val)
driver.quit()


def get_up_letter(i, j, soup):
    return soup[i-1][j]


def get_down_letter(i, j, soup):
    return soup[i+1][j]


def get_left_letter(i, j, soup):
    return soup[i][j-1]


def get_right_letter(i, j, soup):
    return soup[i][j+1]

def find_word(word):
    res = ''
    for c in word:
        for i, s in enumerate(soup):
            for j, ss in enumerate(s):
                if c == ss:
                    print(c, "IS EQUAL TO", ss)
                    res += ss
                    print(res)
                j += 1
            i += 1

for i, word in enumerate(words_list):
    if i == len(words_list)-1:
        break
    else:
        find_word(word)