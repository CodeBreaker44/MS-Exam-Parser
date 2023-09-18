from bs4 import BeautifulSoup
import requests
import webbrowser
from pyfiglet import Figlet
import random
import time


COLOR = {
    "HEADER": "\033[95m",
    "BLUE": "\033[94m",
    "GREEN": "\033[92m",
    "RED": "\033[91m",
    "ENDC": "\033[0m",
}
custom_fig1 = Figlet(font='standard')

print(COLOR["GREEN"], custom_fig1.renderText('ExamTopics Parser'), COLOR["ENDC"])

series = input("Enter exam series code, AZ, SC, etc. : ")
exam_number = input("Enter exam number: 200, 300, 400, 500, etc.: ")
y = input("Enter topic number: ")
print("Enter the range of questions")

start_question = int(input("Enter start question: "))
end_question = int(input("Enter end question: "))

user_agents = [
    #  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
     "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    # "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0",
]

for i in range(start_question, end_question+1):
    headers = {
        'Accept' : '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'User-Agent': random.choice(user_agents),
    }
    
    search = f'{series}+{exam_number}+topic+{y}+question+{i}'
    url = 'https://www.google.com/search'
    parameters = {'q': search}

    content = requests.get(url, headers=headers, params=parameters).text
    soup = BeautifulSoup(content, 'html.parser')


    search = soup.find(id='search')
    if search:
        first_link = search.find('a')
        if first_link:
            print(first_link['href'])
            webbrowser.open(first_link['href'])
        else:
            print("No link found in search results.")
    else:
        print("Search element not found.")
    

