# pr-status 
Python script to extract pull request data of any given repository,the script dynamically generates a html file (pull_request_summary.html) which can be viewed in any web broswer.Mail functionality is written but commented due to unavailablity of a SMTP Server,since Google is not allowing any third party app to send emails on it's behalf .

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



