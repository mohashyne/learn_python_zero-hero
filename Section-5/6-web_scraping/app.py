""" web scraping using BeautifulSoup """
# install the required packages
# pipenv install requests
# pipenv install beautifulsoup4

import requests
from bs4 import BeautifulSoup

response = requests.get("https://stackoverflow.com/questions", timeout=10)
# print(response.text, response.status_code, response.reason)
soup = BeautifulSoup(response.text, "html.parser")  # parse the html content
questions = soup.select(".s-post-summary")  # select the questions
print(type(questions[0]))  # <class 'bs4.element.Tag'>   # first question
# attributes of the first question  # {'class': ['s-post-summary']}
print(questions[0].attrs)
# {'id': 'question-summary-79317748',
# 'class': ['s-post-summary', 'js-post-summary'],
# 'data-post-id': '79317748', 'data-post-type-id': '1'}

# we can use the get method to get the value of the attribute
# so that if the id attribute is not present, it will return None
# print(questions[0].get("id"))  # question-summary-79317748

# print(questions[0].select(".s-link"))  # [<a class="s-link" href="/questions/79317748/what-is-the-difference-between-keras-and-tensorflow-in-terms-of-implementation">What is the difference between Keras and TensorFlow in terms of implementation?</a>]

# we use the select_one method to get the first element, and avoid searching for all the elements
# print(questions[0].select_one(".s-link").getText()) # What is the difference between Keras and TensorFlow in terms of implementation?

for question in questions:
    print(question.select_one(".s-link").getText()) # get text of all the question

# How to run SQL migrations to create tables in PostgreSQL from a .NET app without using EF Core in Docker?
# CachedNetworkImage is not working in Carousel Slider
# How to do priori calculations for rust iterators only once
# Pull request proposed for pandas overflow with timestamp normalize
# How to pass request parameters to an Angular component in SSR (Angular 18) and view logs in the browser?
# Hide inherited getters on hover in VS Code (node)
# ToC generation when building pdf using QuestPdf library
# I want %matplotlib notebook not %matplotllib widget or %matplotlib ipympl : Javascript Error: IPython is not defined
# Why is my Angular app not receiving Server-Sent Events (SSE) from a WebFlux backend?
# How to diagnose water-damaged Asus Zenbook UX425 and test mainboard functionality? [closed]
# EF many to many relationship in Web Api using swagger
# watchOS timer app freezes UI in dimmed state while haptics continue working
# munin plugin memory: graph draws the wrong total memory
# How to change input text position (the text inside an input ) using css or sass [duplicate]
# How to convert Type to C#-parseable string
# telebot handler not being triggered and selenium not working in Python bot
# Vmware exporter for Prometheus to scrap VM Disk I/O and NIC Data transfer
# PostgreSQL privilege to only select a limited number of rows
# Workspace as a Task Webhook - pretty common
# Is there a way to stop mixing console.group()s when script use async functions?
# How do I correctly send a binary file over POST to an ESP32 device from a React Native app?
# How to get the origins of rays in NeRF properly?
# Display actual key order in VS Code in Debug mode (javascript)
# lombok @SuperBuilder changing one of my field names?
# Rust and Sqlx which approach is more resource efficient?
# Webgl shadows implemetation trouble
# How to fix Google CLS issue - "A late network request adjusted the page layout"
# How to properly store state in child components? [closed]
# How is data integration in geopandas?
# SpdLog, RuntimeError: async log: thread pool doesn't exist anymore
# Copy certain cells over to another sheet when the script is running
# Clang: constexpr variable must be initialized by a constant expression, but function is constexpr
# Use Azure Devops REST API to get YAML defintion of Release (steps)
# Test if image is compliant to guideline
# Nodemailer in Google Cloud Function - spontaneous connection timeout
# KServe endpoint ui showing revision failed in kubeflow
# Make columns of calculator appear as example [closed]
# 3ddv Venue Map issue
# how to reset password wazuh in docker
# Can I remove/delete all inline keyboards when user types a "start" command?
# Falco Talon Integration
# In need to neglect play console tablets screenshots
# Bison: howto handle optiobal ';' after statement
# How to group a prometheus metric by day?
# Maui NET8 ANDROID Modify the color of a section of an SVG image
# what are the best practices to use the BOM APIs in React component
# ADF Pipelines performance i particular Web activity
# Is it possible to query an Amazon RDS instance directly from Step function?
# Java with JPA and vectorscale: SQL Error [42704]: ERROR: type "vectorscale" does not exist
# Users Unable to Login via Firebase Authentication in Google Play Installed App     



    print(question.select_one(".s-post-summary--stats-item").getText()) # get text of all the question
    
# .NET microservices on AWS ECS with inter-service communication using service connect grpc

# 0
# votes

# Solr highlight several search words in long text

# 0
# votes

# Angular: Replace placeholder with input box inside a html table at runtime

# 0
# votes

# ROS2 running on a docker container in WSL cannot communicate to remote machines

# 0
# votes

# Handling stale SSE connection response objects in Node js(Nest js)

# 0
# votes

# Push an item in deeply nested array if no exists (MongoDB with C# Driver)

# 0
# votes

# PowerShell Script to Check If Chrome Profiles Are Running Not Working As Expected

# 0
# votes

# how to sort dropdown items in angular checked item first

# 0
# votes

# Azure EventGrid batching delay

# 0
# votes

# How to run SQL migrations to create tables in PostgreSQL from a .NET app without using EF Core in Docker?

# 0
# votes

# CachedNetworkImage is not working in Carousel Slider

# 0
# votes

# How to do priori calculations for rust iterators only once

# 1
# vote

# Pull request proposed for pandas overflow with timestamp normalize

# 0
# votes

# How to pass request parameters to an Angular component in SSR (Angular 18) and view logs in the browser?

# 1
# vote

# Hide inherited getters on hover in VS Code (node)

# 0
# votes

# ToC generation when building pdf using QuestPdf library

# 0
# votes

# I want %matplotlib notebook not %matplotllib widget or %matplotlib ipympl : Javascript Error: IPython is not defined

# 0
# votes

# Why is my Angular app not receiving Server-Sent Events (SSE) from a WebFlux backend?

# 1
# vote

# How to diagnose water-damaged Asus Zenbook UX425 and test mainboard functionality? [closed]

# -1
# votes

# EF many to many relationship in Web Api using swagger

# 0
# votes

# watchOS timer app freezes UI in dimmed state while haptics continue working

# 0
# votes

# munin plugin memory: graph draws the wrong total memory

# 0
# votes

# How to change input text position (the text inside an input ) using css or sass [duplicate]

# -1
# votes

# How to convert Type to C#-parseable string

# 0
# votes

# telebot handler not being triggered and selenium not working in Python bot

# -1
# votes

# Vmware exporter for Prometheus to scrap VM Disk I/O and NIC Data transfer

# -1
# votes

# PostgreSQL privilege to only select a limited number of rows

# 0
# votes

# Workspace as a Task Webhook - pretty common

# 0
# votes

# Is there a way to stop mixing console.group()s when script use async functions?

# 0
# votes

# How do I correctly send a binary file over POST to an ESP32 device from a React Native app?

# 1
# vote

# How to get the origins of rays in NeRF properly?

# 0
# votes

# Display actual key order in VS Code in Debug mode (javascript)

# 0
# votes

# lombok @SuperBuilder changing one of my field names?

# 0
# votes

# Rust and Sqlx which approach is more resource efficient?

# 0
# votes

# Webgl shadows implemetation trouble

# 0
# votes

# How to fix Google CLS issue - "A late network request adjusted the page layout"

# 0
# votes

# How to properly store state in child components? [closed]

# -1
# votes

# How is data integration in geopandas?

# 0
# votes

# SpdLog, RuntimeError: async log: thread pool doesn't exist anymore

# 0
# votes

# Copy certain cells over to another sheet when the script is running

# 0
# votes

# Clang: constexpr variable must be initialized by a constant expression, but function is constexpr

# 0
# votes

# Use Azure Devops REST API to get YAML defintion of Release (steps)

# 0
# votes

# Test if image is compliant to guideline

# 0
# votes

# Nodemailer in Google Cloud Function - spontaneous connection timeout

# 0
# votes

# KServe endpoint ui showing revision failed in kubeflow

# 0
# votes

# Make columns of calculator appear as example [closed]

# -6
# votes

# 3ddv Venue Map issue

# 0
# votes

# how to reset password wazuh in docker

# 0
# votes

# Can I remove/delete all inline keyboards when user types a "start" command?

# -1
# votes

# Falco Talon Integration

# 0
# votes
    
    
