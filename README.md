# Jira Automation Guide

This repository is meant to deal with two significant and tedious challenges faced in the frightful world of Jira
project management: bulk operations on multiple or singular fields of Jira issues (epics, stories, bugs), and adding in large amounts of issues
at once.

### Environment File
You will first need to set up an environment file to store sensitive information for authentication purposes, and ***you will need to make sure that you don't push this file to a publicly visible repository***.
I used a .env file with the following information: my Jira instance URL, my Jira account's email address, and [my Jira API token (which you can learn more about here.)](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/)

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
5. **Parent Name**: If you're creating a story or bug, you should include its parent name so that its not orphaned. 
6. **Assignee Display Name**: The lucky person who will be assigned this issue.
7. **Co-Assignee Display Name**: The other lucky person who will be co-assigned this issue.
8. **Story Points**: The dreaded euphemism of all developers. How much time you'll tell your boss you spent on this project
9. **Default Epic Stories**: In case you don't feel like adding in the full project breakdown, or perhaps haven't reached that stage in planning, feel 
free to set this field to true so that the default epic stories will be created (Discovery, Design, Development, UAT, Hypercare.)
10. **Start Date**: When you supposedly started this task.
11. **End Date**: When you supposedly finished this task.
12. **Target Date**: When you're supposed to finish this task

Please Note: All dates must be formatted in the form of YYYY-MM-DD. All names must be the display names you see on Jira.

### Running your program
Please make sure your python environment is set up correctly, including python version, and all packages. You 
can use ```python3 addJiraStoriesWithCSV.py``` to run the program in your terminal or just click the run button in your IDE.



