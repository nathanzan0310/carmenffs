# Jira Automation Guide

This repository is meant to deal with two significant and tedious challenges faced in the frightful world of Jira
project management: bulk operations on fields of Jira issues (epics, stories, bugs), and adding in large amounts of complex issues
at once.

_**Notes**_: I created this program for the purpose of streamlining the Jira tracking process for my internship this summer of 2024, so there may be some 
functionalities missing which I did not need to use, but you may need to use. Please feel free to contact me if you have any questions.


### Coding Environment
You will first need to set up an environment file to store sensitive information for Jira authentication purposes, and ***you will need to make sure that you don't push this file to a publicly visible repository***.
I used a .env file with the following information: my Jira instance URL, my Jira account's email address, and [my Jira API token (which you can learn more about here.)](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/)

Please also make sure your python environment is set up correctly, including python version, and all packages. 
The packages I used are **requests, python-dotenv, and pandas**. You can use ```pip3 install <package name>``` or just pip to install the packages.

## Adding Issues To Jira
### Jira Data
In order to add your issues to Jira, you will need to format the breakdowns into a CSV file. I have provided an example called 
[test.csv](test_data/test.csv) that the reader may use for reference. Once your CSV is properly formatted, you will need to drop it 
into the project directory and then change the read in file path in [addJiraStoriesWithCSV.py](addJiraStoriesWithCSV.py).
I will briefly go over each data field you can use below.  

1. **Issue Title**: The name of your issue  
2. **Issue Type**: The type of your issue (Epic, Story, etc.). Don't worry about capitalization, it's been taken care of :)
3. **Description**: How you will describe your issue
4. **Jira Board**: The key of the Jira board in which you want to add your issue
5. **Parent Name**: Parent Name. If you're creating a story or bug, you should include its parent name so that its not orphaned. 
6. **Assignee Display Name**: The lucky person who will be assigned this issue.
7. **Co-Assignee Display Name**: The other lucky person who will be co-assigned this issue.
8. **Story Points**: The euphemism dreaded by all developers. How much time you'll tell your boss you spent on this project
9. **Default Epic Stories**: In case you don't feel like adding in the full project breakdown, or perhaps haven't reached that stage in planning, feel 
free to set this field to true so that the default epic stories will be created (Discovery, Design, Development, UAT, Hypercare.)
10. **Start Date**: When you supposedly started this task.
11. **End Date**: When you supposedly finished this task.
12. **Target Date**: When you're supposed to finish this task

**_Please Note:_** All dates must be formatted in the form of YYYY-MM-DD. All names must be the display names you see on Jira. Summary and title in Jira mean the same thing.

### Running your program
You can use ```python3 addJiraStoriesWithCSV.py``` to run the program in your terminal or just click the run button in your IDE.


## Bulk Operations

If you ever run into a situation where you realize a whole lot of issues need to be changed, and you don't want to do it by hand, then this is for you.

1. Formulate a query in Jira's issue navigator that encompasses all the issues you want to change. 
2. Identify the fields you want to change and what you want to change them to
3. Add them in to the designated location in [bulkEditOnJQLQuery.py](bulkEditOnJQLQuery.py).
4. Run the program with ```python3 bulkEditOnJQLQuery.py```

**_Notes_**: If you want to perform an operation on an existing field, for example if your manager changed the definition of story points from 1 hour to 2 hours, 
you will need to get that particular field from the GET request before you can do that operation. I've included an example in the code.

