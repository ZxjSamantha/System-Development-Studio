# Report 5 Part 1: Pull Request

## Name: ZHANG XINJIE Student ID Number: 20M14457

---
Exercise 5: Swicth to branch `br-dev`, commit several times and make a pull request. 

Making pull requests among the branches in one repository is very common in team-development, which all members can access repository.  

The following operations can be done locally:

`git checkout -b br`: Create a branch `br` and switch to the branch.

Developers can commit to this branch locally and push this branch back.

`git push -u origin br `: For every branch that is up to date or successfully pushed, add upstream (tracking) reference, used by argument-less git-pull and other commands.

Then a new pull request will be made in the repository and can be compared and merged in the repository. 

---

Exercise 6: Comment on the pull request in branch `br-dev`, commit several times and merge it.

It is easy to review the code. 

`LGTM: Looks Good To Me` 


---

Exercise 7: Fork one of the students' repository, clone the repository locally and check the remote.

Here is a good tutorial about making PR between repository. 

[How to PR on others repository](https://blog.csdn.net/qq_33429968/article/details/62219783)

Step 1: Fork the target repository from peer's.

Step 2: Clone the repository to local PC using `git clone ...`

Step 3: Connect with the peer's repository remotely using `git remote add upsteam ...`. The connection can be checked with `git remote -v`.

Step 4: Create a new branch with `git checkout -b branch_name`. The following operations are as same as those in Exercise 5. 

Step 5: Create a new pull request and write commit information. 

Step 6: Wait for getting merged. 

---

Exercise 8: Commit the forked repository and make pull request between the repositories (local and remote). Commit on the received pull request and get merged. 

Thank Mr. Ruixuan Dan very much for he merged my PR! 

---

Exercise 9: Practice git and github operations. 


