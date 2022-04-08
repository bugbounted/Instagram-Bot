from turtle import width
from selenium import webdriver as wb
from selenium.webdriver.common.keys import Keys
from time import sleep
import random
from tkinter import *

#constants
PATH = 'C:/Users/marxp/OneDrive/Documentos/chromedriver.exe'
URL = 'https://www.instagram.com/'
BGCOLOR = '#fff'


# driver
web = wb.Chrome(executable_path=PATH)

# lists
hashtags = []
with open("hashtags.txt") as file:
    for hashtag in file: 
        hashtag = hashtag.strip() 
        hashtags.append(hashtag) 


comments = []
with open("comments.txt") as file:
    for comm in file: 
        comm = comm.strip() 
        comments.append(comm) 

# functions
def get_user():
    user = varUser.get()
    return user

def get_password():
    password = varPassword.get()
    return password

def login(user, pas):
    username = web.find_element_by_name('username')
    username.send_keys(user)

    passwordname = web.find_element_by_name('password')
    passwordname.send_keys(pas)

    button = web.find_element_by_css_selector('#loginForm > div > div:nth-child(3) > button > div')
    button.click()
    sleep(3)

    try:
        not_now = web.find_element_by_css_selector('#react-root > section > main > div > div > div > div > button')
        not_now.click()

        sleep(3)
        not_now = web.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm')
        not_now.click()
        sleep(2)
    except:
        pass

def start_bot():

    # accessing website
    web.get(URL)
    sleep(2)

    # getting user informations from GUI
    user = get_user()
    password = get_password()

    # Entering on Instagram
    try:
        login(user, password)
    except:
        pass

    search_hashtag()

def like():
    icon = web.find_element_by_xpath('/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button')
    icon.click()
    sleep(2)

def comment():
    web.find_element_by_xpath('/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[2]/button').click()
    sleep(1)
    comment_box = web.find_element_by_xpath('/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea')
    com = random.randint(0,len(comments))
    comment_box.send_keys(comments[com])
    sleep(1)
    comment_box.send_keys(Keys.ENTER)
    sleep(2)
    skip()

def skip():

    skip_button = web.find_element_by_link_text('Avançar')
    skip_button.click()
    sleep(random.randint(2,4))

def search_hashtag():

    for _ in range(0,len(hashtags)):
        
        h = random.randint(0, len(hashtags))
        # searching for the first image of hashtag
        web.get('https://instagram.com/explore/tags/'+hashtags[h]+'/')
        sleep(3)
        click_first = web.find_element_by_xpath('/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')
        click_first.click()
        sleep(random.randint(2,3))

        try:
            # skip
            follow = web.find_element_by_xpath('/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[2]/button').text
            if follow=='seguindo':
                skip() 
            else:   
        
                for _ in range(0,3):
                    # Liking photo
                    like()
                    # Commenting photo
                    comment() 


        except:
            continue


# graphic interface
app = Tk()
app.title('Bot Instagram (v.1)')
app.geometry('220x300')
app.configure(background=BGCOLOR)

# variables
varUser = StringVar()
varPassword = StringVar()

username = Label(app, text='user:', background=BGCOLOR)
username.grid(column=0, row=0, padx=0, pady=20)
username_box = Entry(app, textvariable=varUser)
username_box.grid(column=1, row=0, padx=0, pady=20)

password = Label(app, text='password:', background=BGCOLOR)
password.grid(column=0, row=1, padx=0, pady=0)
password_box = Entry(app, textvariable=varPassword, show='*')
password_box.grid(column=1, row=1, padx=0, pady=0)

button = Button(app, text='           Start           ', command=start_bot)
button.grid(column=1, row=2, padx=0, pady=10)

app.mainloop()




