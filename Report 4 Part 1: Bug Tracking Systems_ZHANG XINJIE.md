# Report 4 Part 1: Bug Tracking System

## Name: ZHANG XINJIE Student ID Number: 20M14457


---

Exercise 1: Use BTS to find several bugs in the ususally used OSS projects. 

Bug Tracking System is a software application that keeps track of reported software bugs in software development projects. IBM gives a summary of BTS in the following URL:

[What is bug tracking?](https://www.ibm.com/topics/bug-tracking)


A BTS generally includes the following functions:

1. Bug tracking.

2. Feature request / Question. 

3. Bug search.

4. Version control.

Bug tracking is the process of logging and monitoring bugs or errors during software developing and testing. The bugs need to be evaluated, monitored and prioritized for debugging.  A bug may go through several stages or states. They include:

 – Active: Investigation is underway
 
 – Test: Fixed and ready for testing
 
 – Verified: Retested and verified
 
 – Closed: Can be closed after it is verified and it is not considered to be a bug
 
 – Reopened: Not fixed and reactivated
 
A good guide is provided by GitHub Guides about mastering issues in the following URL:

[Mastering Issues](https://guides.github.com/features/issues/)
 
Keras is a open-source high-level deep learning API written in Python, running on top of the machine learning platform Tensorflow. The keras team welcomes contributions world-wide. Currently, there are over 3,100 issues are submitted. The issues are categorized by **Author**, **Label**, **Projects**, **Milestones**, **Assignee**, and further sorting. 

[Keras: Deep Learning for humans](https://github.com/keras-team/keras)

The following issue is found using **sort** and **most recommmended**. 

[model.save and load giving different result](https://github.com/keras-team/keras/issues/4875)

This issue has been open since 30 Dec, 2016. It reported an issue about built-in function to ouput the trained and saved deep learning sequential models, that the function `model.save` did not work as users expected. 

This issue has not been addressed officially, but many contributors tried different ways to solve this problem. And a most recent reply is given by one of contributors and it seems to work well.

[Comments from akbaramed](https://github.com/keras-team/keras/issues/4875#issuecomment-712633281)


---

Exercise 2: Find examples of good bug report and bad bug report.

Some OSS projects will give the issue templates for contributors to sumbit readable bug report or feature request. 

A Good bug report should include:

1. Title

2. Environments details

3. Steps to Reproduce

4. Expected Behavior

5. Actual Behavior

Here is good article about writing good bug report in the following URL, and a bug report template is given:

[How to write good bug report?](https://www.softwaretestinghelp.com/how-to-write-good-bug-report/)

```
SAMPLE BUG REPORT
Bug Name: Application crash on clicking the SAVE button while creating a new user.
Bug ID: (It will be automatically created by the BUG Tracking tool once you save this bug)
Area Path: USERS menu > New Users
Build Number: Version Number 5.0.1
Severity: HIGH (High/Medium/Low) or 1
Priority: HIGH (High/Medium/Low) or 1
Assigned to: Developer-X
Reported By: Your Name
Reported On: Date
Reason: Defect
Status: New/Open/Active (Depends on the Tool you are using)
Environment: Windows 2003/SQL Server 2005

Description:
Application crash on clicking the SAVE button while creating a new
the user, hence unable to create a new user in the application.

Steps To Reproduce:
1) Login into the Application
2) Navigate to the Users Menu > New User
3) Filled all the user information fields
4) Clicked on the ‘Save’ button
5) Seen an error page “ORA1090 Exception: Insert values Error…”
6) See the attached logs for more information (Attach more logs related to bug..IF any)
7) And also see the attached screenshot of the error page.

Expected Result: On clicking SAVE button, should be prompted to a success message “New User has been created successfully”.


```

Here is a fun blog I found about bug report that tells readers (or developers) a bad template of bug report. 

[How to Make Your Developer Hate You](https://blog.ubertesters.com/how-to-make-your-developer-hate-you-or-7-tips-on-bad-bug-reporting/)

I made a converse summary about what the author mentioned as bad bug report: 

1. Readable and sufficient description.

2. State the priority of bug.

3. Report a new bug even there is a similar old one.

4. Do not combine multiple bugs into one bug report.

5. Note the issues are features, improvements or bugs clearly. 

In the case of Keras development, I would consider the following issue as a relatively unreadable issue, because the title is vague, no environment information is provided, and no expected result is provided.  

[Keras and multiple labels](https://github.com/keras-team/keras/issues/10983)

---

Exercise 3: Post issues to your own OSS project. 

I found a tutorial in Chinese about submit issues with several specific keywords. 

[How to manage an OSS software project with Issue?](http://www.ruanyifeng.com/blog/2017/08/issue.html)

An issue will be closed when the following commands:

`git commit -m "msg_fix, fix/fixes/fixed #issue_number"`

`git commit -m "msg_close, close/closes/closed #issue_number"`

`git commit -m "msg_resolve, resolve/resolves/resolved #issue_number"`

I submitted an issue about how to accessing GitHub using command lines before, now I would like to close the following issue (documentation) using git commands because it should be considered as a documentation and it has been finished.

https://github.com/ZxjSamantha/System-Development-Studio/issues/2

