import requests
from bs4 import BeautifulSoup
from datetime import datetime
from dateutil import parser

headers ={
     'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}

def login_website(username,password):
    login_data={
        'log':username,
        'pwd':password,
        'wp-submit':'Log In',
        'redirect_to':'http://aitplacements.com/wp-admin/',
        'testcookie':'1'

    }
    with requests.Session() as s:
        url = "http://aitplacements.com/wp-login.php"
        r = s.get(url,headers=headers)
        soup =BeautifulSoup(r.content,'html.parser')
        r = s.post(url, data=login_data, headers=headers)
        soup1=BeautifulSoup(r.content,'html.parser')
        #print(soup1)
        return soup1

def initilize_data():
    global k,title,dates,description
    title=[]
    dates={}
    description={}
    k=0

def send_email(dates,title,description):
    import smtplib, ssl
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "librarycommunity.2020@gmail.com"  # Enter your address
    receiver_email = "gobillamothy85@gmail.com"  # Enter receiver address
    password = 'Apple@123'

    message = MIMEMultipart("alternative")
    message["From"] = sender_email
    message["To"] = receiver_email


    message["Subject"] = "AIT PLACEMENTS NOTIFICATION"
    text = """
    Hello,
    """
    html = """\
    <html>
    <body>
    <p> {} <br>
    There is a new notification about {} <br>
    {} <br>
    <a href="http://aitplacements.com/wp-login.php">Placements Website Link</a>
    </p>
    </body>
    </html>
    """.format(dates,title,description)
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")
    message.attach(part1)
    message.attach(part2)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("mail sent")

def compute_data(soup1):
    global k,title,dates,description
    t=soup1.find_all('div',attrs={'class':'grid-item grid-sm-6 grid-md-4'})
    l=t
    num=len(l)
    print(num)
    m=0
    temp_title=[]
    temp_dates={}
    temp_description={}
    for i in range(0,num):
        if((l[i].find('h4').get_text()) not in title):
            temp_title.append(l[i].find('h4').get_text())
            temp_dates[temp_title[m]]=l[i].find('span').get_text()
            temp_description[temp_title[m]]=l[i].find('p')
            title.append(l[i].find('h4').get_text())
            dates[title[k]]=l[i].find('span').get_text()
            description[title[k]]=l[i].find('p')
            k=k+1
            m=m+1
    print(title)
    return temp_title,temp_dates,temp_description

def main():
    soup1=login_website('gmothy','ait98@abcd')
    #print(soup1)
    temp_title,temp_dates,temp_description=compute_data(soup1)
    print(temp_title)
    for i in range(0,len(temp_title)):
        send_email(temp_dates[temp_title[i]],temp_title[i],temp_description[temp_title[i]])

if __name__=='__main__':
    import time
    i=0
    initilize_data()
    while (1):
        main()
        time.sleep(3600)   # Change this to number of seconds in a day
        if (i == 30):    # make this 30 for a month
            break
            i = i + 1
