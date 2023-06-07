# pr-status 

Python script to extract pull request data of any given repository,the script dynamically generates a html file (pull_request_summary.html) which can be viewed in any web broswer.A sample of the output file is provided in the repo.

Mail functionality is written but commented due to unavailablity of a SMTP Server,since Google is not allowing any third party app to send emails on it's behalf.

The script expects an evironment variable(gittoken) to be setup for authentication,in case of using in any pipeline the code needs to be refactored accordingly.

You can use the **EXPORT gittoken="your token"** to set this up

The script also deals with **pagination** as Github has a hard limit of 30 requests per page ,hence for repositories with huge Pull requests the script will take some time to generate the output.For limited number of pull requests it should be completed within seconds.

**Usage**
 
_**pr-status.py repo-owner repo-name**_

**Examples**
>pr-status.py neosam01 pr-status

>pr-status.py docker compose

## Authors

- [@neosam01](https://www.github.com/neosam01)
   Samriddha Choudhuri


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`gittoken` : Token for authentication

## Libraries

The following Libraries are required for execution of the code

smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
requests
sys
concurrent.futures
os
from datetime import datetime, timedelta



