# pr-status 
Python script to generate pull request data of any given repository

Usage
 
pr-status.py repo-owner repo-name

## Authors

- [@neosam01](https://www.github.com/neosam01)
   Samriddha Choudhuri


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`gittoken` : Token for authentication

##Libraries
The following Libraries are required for execution of the code

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests
import sys
import concurrent.futures
import os
from datetime import datetime, timedelta



