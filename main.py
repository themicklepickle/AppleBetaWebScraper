import requests
from bs4 import BeautifulSoup
import webbrowser
import os

def notify(title, text):
    os.system(f'osascript -e \'display notification "{text}" with title "{title}" sound name "Ping"\'')

url = "https://beta.apple.com/sp/betaprogram/"	
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
html = list(soup.children)[7]
comingSoon = soup.find("h2").contents[0]

if comingSoon == "Coming Soon":
	notify("Apple Beta Program", "No changes yet.")
else:
	notify("Apple Beta Program", "Beta available!")
	webbrowser.open_new_tab(url)