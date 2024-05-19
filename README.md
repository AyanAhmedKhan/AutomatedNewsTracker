# AutomatedNewsTracker
This Python script is designed to scrape the top stories from Google News using Selenium, a web automation tool. It provides a simple way to fetch headlines and their corresponding links from the top stories section of the Google News website.

Features:
Headline Retrieval: The script retrieves the headlines of the top stories from Google News.
Dynamic Updating: It continuously fetches headlines at regular intervals, providing real-time updates on the news.
Timestamp: Each update is accompanied by a timestamp in the IST (Indian Standard Time) timezone.
Requirements:
Selenium: Ensure you have Selenium installed. You can install it via pip:

pip install selenium
Chrome WebDriver: The script requires Chrome WebDriver to interface with the Chrome browser. Make sure you have Chrome WebDriver installed and its path properly set. Ensure that you use the chromedriver version that matches your Chrome version.

How to Use:
Clone the repository or download the script.

Install the required dependencies.

Run the script using Python:
python news_scraper.py
Sit back and watch as the script fetches the latest headlines from Google News.

Customization:
Time Interval: You can adjust the time interval between each update by modifying the time.sleep() function parameter in the script.
XPath: If Google News' HTML structure changes, you may need to update the XPath expression used to locate the headlines.

Disclaimer:
This script is meant for educational purposes and should be used responsibly. Web scraping may violate the terms of service of websites, so ensure compliance with relevant policies and regulations before using it in a production environment.

Copyright:
Copyright © 2024 Ayan Ahmed Khan. All rights reserved.


