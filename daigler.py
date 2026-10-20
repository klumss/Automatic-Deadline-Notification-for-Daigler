
import pandas as pd
import requests
from playwright.sync_api import sync_playwright
import datetime
import os
from dotenv import load_dotenv


url = "https://daigler25.addu.edu.ph/login/index.php"
load_dotenv()
username = os.getenv("USER")
password = os.getenv("PASS")

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(url)
    
    #login
    page.locator("#username").fill(username)
    page.locator("#password").fill(password)
    page.click("#loginbtn")
    
    #data
    data = []
    
    #extraction
    container = page.locator("div.calendarwrapper")
    for card in container.locator("div.event > div.overflow-auto").all():
        title = card.locator("h4.d-flex > a.text-truncate").inner_text()
        datetitle = card.locator("div.date > a").get_attribute("title")
        data.append({
            "title" : title,
            "date" : datetitle
        })
    
    
    #check
    #page.wait_for_url("**/my/")
    
    #close
    browser.close()

df = pd.DataFrame(data)
df["title"] = df["title"].replace(r"\bis due\b", "",regex=True)

markdown_df = df.to_markdown(index=False, colalign=("left", "right"))
markdown_df = markdown_df[226:]


formatted_markdown = markdown_df.split("\n")

formatted = [f"{row}\n\n" for row in formatted_markdown]
formatted = "\n".join(formatted)
formatted = formatted + "\n---------------------------------"

#The notification sender

topic = "YOUR TOPIC NAME HERE"
url = f"https://ntfy.sh/{topic}"
datetoday = datetime.date.today()

post = requests.post(
    url,
    data=formatted,
    headers={
        "Title" : f"Daigler Deadlines as of {datetoday}"
    }
)

print(f"Sent Notification. {datetime.datetime.now()}")


