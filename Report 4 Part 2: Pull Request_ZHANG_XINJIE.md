# Report 4 Part 2: Pull Request

## Name: ZHANG XINJIE Student ID Number: 20M14457



Exercise 1: Copy the Git repository on your local machine to another directory and check the origin

```
(base) zhangxinjie@zhangxinjiedeMacBook-Air Lecture04 % git clone https://github.com/ZxjSamantha/System-Development-Studio.git cloned
正克隆到 'cloned'...
remote: Enumerating objects: 25, done.
remote: Counting objects: 100% (25/25), done.
remote: Compressing objects: 100% (20/20), done.
remote: Total 25 (delta 1), reused 0 (delta 0), pack-reused 0
展开对象中: 100% (25/25), 6.56 KiB | 149.00 KiB/s, 完成.
(base) zhangxinjie@zhangxinjiedeMacBook-Air Lecture04 % cd cloned 
(base) zhangxinjie@zhangxinjiedeMacBook-Air cloned % ls
OSS-project	README.md
(base) zhangxinjie@zhangxinjiedeMacBook-Air cloned % git remote -v
origin	https://github.com/ZxjSamantha/System-Development-Studio.git (fetch)
origin	https://github.com/ZxjSamantha/System-Development-Studio.git (push)
```

---

Exercise 2: `pull` the commits from remote repository using `git pull` and `push` local commits to the origin remote repository. 

```
(base) zhangxinjie@zhangxinjiedeMacBook-Air OSS-project % git add Probabilistic\ and\ Binary\ Model.c
(base) zhangxinjie@zhangxinjiedeMacBook-Air OSS-project % git commit -m "Delete notes"
[main 5950bbd] Delete notes
 1 file changed, 4 insertions(+), 4 deletions(-)
(base) zhangxinjie@zhangxinjiedeMacBook-Air OSS-project % git push
枚举对象: 7, 完成.
对象计数中: 100% (7/7), 完成.
使用 4 个线程进行压缩
压缩对象中: 100% (4/4), 完成.
写入对象中: 100% (4/4), 465 字节 | 465.00 KiB/s, 完成.
总共 4 （差异 1），复用 0 （差异 0）
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/ZxjSamantha/System-Development-Studio.git
   cca4bd7..5950bbd  main -> main 
```

---

Exercise 3: Experiment with two strategies of `pull` between replicated repositories.

I have different commits on local repository and remote repository. The warning is shown in the following:

```
(base) zhangxinjie@zhangxinjiedeMacBook-Air OSS-project % git pull --rebase
remote: Enumerating objects: 7, done.
remote: Counting objects: 100% (7/7), done.
remote: Compressing objects: 100% (4/4), done.
remote: Total 4 (delta 2), reused 0 (delta 0), pack-reused 0
展开对象中: 100% (4/4), 780 字节 | 86.00 KiB/s, 完成.
来自 https://github.com/ZxjSamantha/System-Development-Studio
   2a88326..468bb63  main       -> origin/main
首先，回退头指针以便在其上重放您的工作...
应用：Change the initial states
使用索引来重建一个（三方合并的）基础目录树...
M	OSS-project/Deterministic Binary Neuron Model.py
回落到基础版本上打补丁及进行三方合并...
自动合并 OSS-project/Deterministic Binary Neuron Model.py
冲突（内容）：合并冲突于 OSS-project/Deterministic Binary Neuron Model.py
error: 无法合并变更。
打补丁失败于 0001 Change the initial states
提示：用 'git am --show-current-patch' 命令查看失败的补丁
Resolve all conflicts manually, mark them as resolved with
"git add/rm <conflicted_files>", then run "git rebase --continue".
You can instead skip this commit: run "git rebase --skip".
To abort and get back to the state before "git rebase", run "git rebase --abort".
```

```
if __name__ == "__main__":
<<<<<<< HEAD
    initialStates = [0, 0, 0, 0]
    #initialStates = [1, 1, 1, 1]
    #initialStates = [0,1,0,1]
=======
    #initialStates = [0, 0, 0, 0]
    #initialStates = [1, 1, 1, 1]
    initialStates = [0,1,0,1]
>>>>>>> Change the initial states
    currentStates = initialStates
    energy = []
    while(energyFunc(currentStates) > 0):
        currentStates = statesUpdate(currentStates)
        print(currentStates)
        energy.append(energyFunc(currentStates))
    print(energy)

```

After resolving the conflict, use `git rebase --continue`. 

---

Exercise 4: Create an empty repository on GitHub and push the repository you built locally.

```
(base) zhangxinjie@zhangxinjiedeMacBook-Air PRML % git remote add origin https://github.com/ZxjSamantha/System-Development-Studio.git
(base) zhangxinjie@zhangxinjiedeMacBook-Air PRML % git push -u origin master
枚举对象: 3, 完成.
对象计数中: 100% (3/3), 完成.
写入对象中: 100% (3/3), 240 字节 | 240.00 KiB/s, 完成.
总共 3 （差异 0），复用 0 （差异 0）
remote: 
remote: Create a pull request for 'master' on GitHub by visiting:
remote:      https://github.com/ZxjSamantha/System-Development-Studio/pull/new/master
remote: 
To https://github.com/ZxjSamantha/System-Development-Studio.git
 * [new branch]      master -> master
分支 'master' 设置为跟踪来自 'origin' 的远程分支 'master'
```

