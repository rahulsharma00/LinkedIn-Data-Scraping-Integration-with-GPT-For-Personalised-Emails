## How it works

This guide outlines the process of integrating the provided Python code with the LinkedIn API to retrieve and process user profile data. The script then extracts information such as name, about, education, skills, and work experience, and saves it to a JSON file. Then it uses OpenAI GPT-3.5 Turbo engine to generate personalized emails based on LinkedIn profile data. The final output comprises JSON files containing structured LinkedIn profile data and text files containing personalized emails.

**Note:** You need to have the following before executing the code
1. OpenAI API
2. LinkedIn email and password


## Prerequisites
1. Make 2 folders called 'profile_data' and 'emails' respectively
2. Execute the following commands before running the application in the following order
   
 `` pip install linkedin_api``

 `` pip install openai``

## Usage instructions
To use the application, execute the following commands in the termial
1. ``python3 json_format.py``
2. Enter the username
3. ``python3 profile_emails.py``
