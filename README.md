# selenium-py-example
Sample code based on the tutorial: Page Object with Selenium Webdriver
You can find the tutorial here: https://www.youtube.com/watch?v=BURK7wMcCwU

Thanks to Raghav Pal for the excelent explanation :)

Project structure:
- Reports: HTML reports created by HTMLTestRunner for each test excecution

- POMObjectDemo:
  -Locators: Contains the element ID's that you need to find elements inside the webpage.
  -Pages: Contains the action methods in order to interact with the webpage elements.
  -Tests: Here you can find the main class "login.py". You can run the tests on command line with the line: python -m       POMObjectDemo.Tests.login
