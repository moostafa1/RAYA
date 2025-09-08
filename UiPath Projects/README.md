# UiPath Robots

## Robot 1: Web Scraper

This project demonstrates the development of a UiPath robot designed to automate web scraping tasks. The robot performs the following actions:

- Opens Google.
- Searches for the query: **"generate random weather"**.
- Navigates to the appropriate website.
- Selects the required options from dropdown menus.
- Clicks the **Generate** button.
- Extracts the generated weather data and stores it in a string variable in memory.
- Closes the browser.
- Displays the extracted data as a log message.
- Saves the extracted data into a text file.

---

## Key Observations

- Both **Modern** and **Classic** UiPath activities were utilized in this project.
- **Modern activities** can close the browser directly without requiring an explicit **Close Tab** activity, whereas **Classic activities** require it.
- **Classic activities** do not display warnings when using absolute file paths, while **Modern activities** do provide warnings in such cases.

## Project video

- To watch the video, click the image below

- [![Watch the demo](data_to_render/bot_iamge.png)](https://www.youtube.com/watch?v=-lWupisFDuI)
