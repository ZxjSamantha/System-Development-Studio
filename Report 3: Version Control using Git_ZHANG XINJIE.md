# Report: Verson Control with Git #
 ## Name: ZHANG XINJIE Student ID Number: 20M14457 ##

 ## Contents ##

 1.    Findings of Exercises 1-11. 
 2.    Progress on OSS project. 

 ---
 
 Exercise 1: Create a new repository and commit 3 changes.
 
 Firstly, here is a simple tutorial about git commands created by myself. 
 
 [Information Collection of Accessing GitHub using Command Lines](https://github.com/ZxjSamantha/System-Development-Studio/issues/2)
 
 `git int`: Create a new repository. 
 
 `git add foo`: Stage a file **foo**. 
 
 `git commit -m "msg"`: Commit with message "msg". 
 
 `git log`: Check the history of commits. 
 
 `git status`: Check the current status.
 
```
(base) zhangxinjie@192 Lecture03 % git init Converter
(base) zhangxinjie@192 Converter % echo Xinjie > Converter
(base) zhangxinjie@192 Converter % vi Converter 
(base) zhangxinjie@192 Converter % git add Converter
(base) zhangxinjie@192 Converter % git commit -m "First Change"
[master（根提交） 630a0d2] First Change
 1 file changed, 1 insertion(+)
 create mode 100644 Converter
(base) zhangxinjie@192 Converter % vi Converter 
(base) zhangxinjie@192 Converter % vi Converter
(base) zhangxinjie@192 Converter % git commit -m "Add Name and ID"
位于分支 master
尚未暂存以备提交的变更：
	修改：     Converter

修改尚未加入提交
(base) zhangxinjie@192 Converter % git add Converter 
(base) zhangxinjie@192 Converter % git commit -m "Add Name and ID"
[master 782e173] Add Name and ID
 1 file changed, 1 insertion(+), 1 deletion(-)
(base) zhangxinjie@192 Converter % vi Converter 
(base) zhangxinjie@192 Converter % git add Converter              
(base) zhangxinjie@192 Converter % git commit -m "Delete Name & ID. Add Task." 
[master 0e94365] Delete Name & ID. Add Task.
 1 file changed, 3 insertions(+), 1 deletion(-)
(base) zhangxinjie@192 Converter % git log
commit 0e9436586bd313eae8a82f4f30c7915e6bfac683 (HEAD -> master)
Author: ZxjSamantha <35060339+ZxjSamantha@users.noreply.github.com>
Date:   Thu Oct 29 22:35:32 2020 +0800

    Delete Name & ID. Add Task.

commit 782e173955f7b5dd473cbe7dcc862c316a95bb9d
Author: ZxjSamantha <35060339+ZxjSamantha@users.noreply.github.com>
Date:   Thu Oct 29 22:33:05 2020 +0800

    Add Name and ID

commit 630a0d29a1f9e658281f0f2124374292afacf068
Author: ZxjSamantha <35060339+ZxjSamantha@users.noreply.github.com>
Date:   Thu Oct 29 22:31:22 2020 +0800

    First Change
(base) zhangxinjie@192 Converter % git status
位于分支 master
无文件要提交，干净的工作区

```

 
 ---
 
 Exercise 2: Check the differentiations between each pair of commits.
 
 `git diff commit_A commit_B`: See the differentiations between commit A and commit B
 
 ```
(base) zhangxinjie@192 Converter % git diff 0e9436586bd313eae8a82f4f30c7915e6bfac683 782e173955f7b5dd473cbe7dcc862c316a95bb9d
diff --git a/Converter b/Converter
index 3136c10..04c4e80 100644
--- a/Converter
+++ b/Converter
@@ -1,3 +1 @@
-Task 3: Make a Converter to find W_ij from the energy function.
-       Use 100 or 1,000 Gibbs copies of RNN with probabilistic updating rule.
-       Check if N(x1, x2, x3) follows Boltzmann Distribution. 
+Name:ZHANG XINJIE Student ID Number: 20M14457
 ```
 
 
 `git log --graph --all`: Visualize the commits and merges flow with graph. 
 
 ```
 * commit 0e9436586bd313eae8a82f4f30c7915e6bfac683 (HEAD -> master)
| Author: ZxjSamantha <35060339+ZxjSamantha@users.noreply.github.com>
| Date:   Thu Oct 29 22:35:32 2020 +0800
| 
|     Delete Name & ID. Add Task.
| 
* commit 782e173955f7b5dd473cbe7dcc862c316a95bb9d
| Author: ZxjSamantha <35060339+ZxjSamantha@users.noreply.github.com>
| Date:   Thu Oct 29 22:33:05 2020 +0800
| 
|     Add Name and ID
| 
* commit 630a0d29a1f9e658281f0f2124374292afacf068
  Author: ZxjSamantha <35060339+ZxjSamantha@users.noreply.github.com>
  Date:   Thu Oct 29 22:31:22 2020 +0800
  
      First Change
 ```
 
 ---
 
 Exercise 3: Add a hank using `git add`, and check the two differentiations.
 
`git add -p filename`: Add a small patch of original code to the file. 

```
(base) zhangxinjie@192 Converter % vi Converter 
(base) zhangxinjie@192 Converter % git add -p Converter
diff --git a/Converter b/Converter
index 5cd5a48..2441c5b 100644
--- a/Converter
+++ b/Converter
@@ -6,5 +6,9 @@ class Converter:
 	def __init__(self, alpha, weights, states):
 		self.alpha =  alpha
 		self.weights = weights
-		self.states = state
+		self.states = states
 		print(alpha)
+		print(states)
+
+	def updateStates(weights, currentStates):
+		pass
(1/1) Stage this hunk [y,n,q,a,d,s,e,?]? s
Split into 2 hunks.
@@ -6,5 +6,5 @@
 	def __init__(self, alpha, weights, states):
 		self.alpha =  alpha
 		self.weights = weights
-		self.states = state
+		self.states = states
 		print(alpha)
(1/2) Stage this hunk [y,n,q,a,d,j,J,g,/,e,?]? y
@@ -10 +10,5 @@
 		print(alpha)
+		print(states)
+
+	def updateStates(weights, currentStates):
+		pass
(2/2) Stage this hunk [y,n,q,a,d,K,g,/,e,?]? y

```
 
 `git diff`
 
 ```
(base) zhangxinjie@192 Converter % git diff 7f2efec0ec7059f9a87c03510a5f6c56d7349e9a 255c3c04d0f82116ecb0ed2c3b09e4fa4ec9da09
diff --git a/Converter b/Converter
index 2441c5b..eebc18e 100644
--- a/Converter
+++ b/Converter
@@ -7,8 +7,3 @@ class Converter:
                self.alpha =  alpha
                self.weights = weights
                self.states = states
-               print(alpha)
-               print(states)
-
-       def updateStates(weights, currentStates):
-               pass
(base) zhangxinjie@192 Converter % 
 ```
 
 `git diff --cached`: Check the differentiations between the staging file and the most recent commit.
 
 ```
(base) zhangxinjie@192 Converter % vi Converter 
(base) zhangxinjie@192 Converter % git add Converter 
(base) zhangxinjie@192 Converter % git diff --cached Converter 
diff --git a/Converter b/Converter
index 2441c5b..cfc9a21 100644
--- a/Converter
+++ b/Converter
@@ -10,5 +10,8 @@ class Converter:
                print(alpha)
                print(states)
 
-       def updateStates(weights, currentStates):
+       def updateStates(weights = [], currentStates = []):
+               pass
+
+       def energyFunc(currentStates = []):
                pass

 ```
 
 ---
 
 Exercise 4: Check the file contents at a specific timepoint. 
 
 **What is HEAD?**
 
 **HEAD** is the current commit under operation. 
 
 `git tag `: Add a special label that points to the commit you're currently working on. 
 
 `git checkout`: Switch to the specific commit with HEAD. 
 
 `git checkout HEAD^` and `git checkout HEAD~<num>` :Switch to the previous commits of HEAD. 
 
 ```
(base) zhangxinjie@192 Converter % git checkout 255c3c04d0f82116ecb0ed2c3b09e4fa4ec9da09
注意：正在切换到 '255c3c04d0f82116ecb0ed2c3b09e4fa4ec9da09'。

您正处于分离头指针(Detached HEAD)状态。您可以查看、做试验性的修改及提交，并且您可以在切换
回一个分支时，丢弃在此状态下所做的提交而不对分支造成影响。

如果您想要通过创建分支来保留在此状态下所做的提交，您可以通过在 switch 命令
中添加参数 -c 来实现（现在或稍后）。例如：

  git switch -c <新分支名>

或者撤销此操作：

  git switch -

通过将配置变量 advice.detachedHead 设置为 false 来关闭此建议

HEAD 目前位于 255c3c0 Define Converter
(base) zhangxinjie@192 Converter % git tag Conver
(base) zhangxinjie@192 Converter % git log
commit 255c3c04d0f82116ecb0ed2c3b09e4fa4ec9da09 (HEAD, tag: Conver)
Author: ZxjSamantha <35060339+ZxjSamantha@users.noreply.github.com>
Date:   Fri Oct 30 10:29:06 2020 +0800

    Define Converter

commit 0e9436586bd313eae8a82f4f30c7915e6bfac683
Author: ZxjSamantha <35060339+ZxjSamantha@users.noreply.github.com>
Date:   Thu Oct 29 22:35:32 2020 +0800

    Delete Name & ID. Add Task.

commit 782e173955f7b5dd473cbe7dcc862c316a95bb9d
Author: ZxjSamantha <35060339+ZxjSamantha@users.noreply.github.com>
Date:   Thu Oct 29 22:33:05 2020 +0800

    Add Name and ID

commit 630a0d29a1f9e658281f0f2124374292afacf068
Author: ZxjSamantha <35060339+ZxjSamantha@users.noreply.github.com>
Date:   Thu Oct 29 22:31:22 2020 +0800

    First Change


 ```
 
 `git show`: Check contents of the current commit.
 
 ```
(base) zhangxinjie@192 Converter % git show
commit 255c3c04d0f82116ecb0ed2c3b09e4fa4ec9da09 (HEAD, tag: Conver)
Author: ZxjSamantha <35060339+ZxjSamantha@users.noreply.github.com>
Date:   Fri Oct 30 10:29:06 2020 +0800

    Define Converter

diff --git a/Converter b/Converter
index 3136c10..eebc18e 100644
--- a/Converter
+++ b/Converter
@@ -1,3 +1,9 @@
 Task 3: Make a Converter to find W_ij from the energy function.
        Use 100 or 1,000 Gibbs copies of RNN with probabilistic updating rule.
-       Check if N(x1, x2, x3) follows Boltzmann Distribution. 
+       Check if N(x1, x2, x3) follows Boltzmann Distribution.
+
+class Converter:
+       def __init__(self, alpha, weights, states):
+               self.alpha =  alpha
+               self.weights = weights
+               self.states = states
 ```
 
 The shown contents does not include the following commits.
 
 ---
 
 Exercise 5: Commit some changes to a newly created branch and tag it as `br-a`.
 
 `git branch br-a`: Create a branch under current commit with name **br-a**
 
 `git checkout -b br-b`: Switch to the branch with name **br-b**
 
 `git checkout -b tag-a`: Switch to the branch with name **tag-a**
 
 `git log --graph --all --decorate=full`: Visualize the commits flow.
 
 ```
 (base) zhangxinjie@192 Converter % git log --graph --all --decorate=full 
* commit b379fa91d179f220c61d482d4f89298bff7b2260 (HEAD -> refs/heads/GibbsSampling, tag: refs/tags/Gibbs)
| Author: ZxjSamantha <35060339+ZxjSamantha@users.noreply.github.com>
| Date:   Fri Oct 30 11:16:36 2020 +0800
| 
|     Add Gibbs Sampling
|   
| * commit cbaf5f05a00170f724ef0807d9ce5b598b8569b5 (refs/heads/master)
| | Author: ZxjSamantha <35060339+ZxjSamantha@users.noreply.github.com>
| | Date:   Fri Oct 30 10:57:12 2020 +0800
| | 
| |     Add energy function
| | 
| * commit 7f2efec0ec7059f9a87c03510a5f6c56d7349e9a (tag: refs/tags/v1.0)
|/  Author: ZxjSamantha <35060339+ZxjSamantha@users.noreply.github.com>
|   Date:   Fri Oct 30 10:37:49 2020 +0800
|   
|       Add updateStates
| 
* commit 255c3c04d0f82116ecb0ed2c3b09e4fa4ec9da09 (tag: refs/tags/Conver)
| Author: ZxjSamantha <35060339+ZxjSamantha@users.noreply.github.com>
| Date:   Fri Oct 30 10:29:06 2020 +0800
| 
|     Define Converter
| 
* commit 0e9436586bd313eae8a82f4f30c7915e6bfac683
| Author: ZxjSamantha <35060339+ZxjSamantha@users.noreply.github.com>
| Date:   Thu Oct 29 22:35:32 2020 +0800
| 
|     Delete Name & ID. Add Task.
| 
* commit 782e173955f7b5dd473cbe7dcc862c316a95bb9d
| Author: ZxjSamantha <35060339+ZxjSamantha@users.noreply.github.com>
| Date:   Thu Oct 29 22:33:05 2020 +0800
| 
|     Add Name and ID
| 
* commit 630a0d29a1f9e658281f0f2124374292afacf068
  Author: ZxjSamantha <35060339+ZxjSamantha@users.noreply.github.com>
  Date:   Thu Oct 29 22:31:22 2020 +0800
  
      First Change
 ```
 
 ---
 
 Exercise 6: Merge branch `br-a` to `master`. Add conflicting commits to `br-a` and `master` and then merge them.
 
 Here is a discussion about 3-way merge:
 
 [Gitの3-way mergeとは具体的にどのようなアルゴリズムですか？](https://ja.stackoverflow.com/q/52019)
 
 Here is a tutorial on merging conflicting files:
 
 [How to solve conflicting merges?](https://www.cnblogs.com/ZhangRuoXu/p/6706571.html)
 
 If I merge the conflicting files with `git merge ` on the conflicting_branch, I will receive conflicting warning like this:
 
 ```
(base) zhangxinjie@192 Converter % git merge Gibbs
自动合并 Converter
冲突（内容）：合并冲突于 Converter
自动合并失败，修正冲突然后提交修正的结果。
 ```
 
 `git status`: check the conflicting files. 
 
 ```
(base) zhangxinjie@192 Converter % git status
位于分支 master
您有尚未合并的路径。
  （解决冲突并运行 "git commit"）
  （使用 "git merge --abort" 终止合并）

未合并的路径：
  （使用 "git add <文件>..." 标记解决方案）
	双方修改：   Converter

未跟踪的文件:
  （使用 "git add <文件>..." 以包含要提交的内容）
	.DS_Store
	Figures/

修改尚未加入提交（使用 "git add" 和/或 "git commit -a"）
 ```
The conflicting part is shown as the following:

```
<<<<<<< HEAD

**Contents of HEAD**

=======

**Contents I would like to merge**

>>>>>>> Conflicting contents
```
 
```
Task 3: Make a Converter to find W_ij from the energy function.
        Use 100 or 1,000 Gibbs copies of RNN with probabilistic updating rule.
        Check if N(x1, x2, x3) follows Boltzmann Distribution.

class Converter:
        def __init__(self, alpha, weights, states):
                self.alpha =  alpha
                self.weights = weights
                self.states = states
<<<<<<< HEAD
                print(alpha)
                print(states)

        def updateStates(weights = [], currentStates = []):
                pass

        def energyFunc(currentStates = []):
=======

        def GibbsSampling(neurons):
>>>>>>> Gibbs
                pass
 ```

Fix conflicts in a text editor and save with `git add` and `git commit`, and then merge them.

```
(base) zhangxinjie@192 Converter % vi Converter 
(base) zhangxinjie@192 Converter % git checkout Gibbs
Converter: needs merge
error: 您需要先解决当前索引的冲突
(base) zhangxinjie@192 Converter % git add Converter 
(base) zhangxinjie@192 Converter % git commit -m "Fix conflict"
[master c795ad5] Fix conflict
(base) zhangxinjie@192 Converter % git merge Gibbs
已经是最新的。
```

Check the flow with graph:

```
(base) zhangxinjie@192 Converter % git log --graph --all
*   commit c795ad51457830e47ab9820bcfc1e752a6f03480 (HEAD -> master)
|\  Merge: cbaf5f0 b379fa9
| | Author: ZxjSamantha <35060339+ZxjSamantha@users.noreply.github.com>
| | Date:   Fri Oct 30 11:45:58 2020 +0800
| | 
| |     Fix conflict
| | 
| * commit b379fa91d179f220c61d482d4f89298bff7b2260 (tag: Gibbs, GibbsSampling)
| | Author: ZxjSamantha <35060339+ZxjSamantha@users.noreply.github.com>
| | Date:   Fri Oct 30 11:16:36 2020 +0800
| | 
| |     Add Gibbs Sampling
| | 
* | commit cbaf5f05a00170f724ef0807d9ce5b598b8569b5
| | Author: ZxjSamantha <35060339+ZxjSamantha@users.noreply.github.com>
| | Date:   Fri Oct 30 10:57:12 2020 +0800
| | 
| |     Add energy function
| | 
* | commit 7f2efec0ec7059f9a87c03510a5f6c56d7349e9a (tag: v1.0)
|/  Author: ZxjSamantha <35060339+ZxjSamantha@users.noreply.github.com>
|   Date:   Fri Oct 30 10:37:49 2020 +0800
|   
|       Add updateStates
| 
* commit 255c3c04d0f82116ecb0ed2c3b09e4fa4ec9da09 (tag: Conver)
| Author: ZxjSamantha <35060339+ZxjSamantha@users.noreply.github.com>
| Date:   Fri Oct 30 10:29:06 2020 +0800
| 
|     Define Converter
| 
* commit 0e9436586bd313eae8a82f4f30c7915e6bfac683
| Author: ZxjSamantha <35060339+ZxjSamantha@users.noreply.github.com>
| Date:   Thu Oct 29 22:35:32 2020 +0800
| 
|     Delete Name & ID. Add Task.
| 
* commit 782e173955f7b5dd473cbe7dcc862c316a95bb9d
| Author: ZxjSamantha <35060339+ZxjSamantha@users.noreply.github.com>
| Date:   Thu Oct 29 22:33:05 2020 +0800
| 
|     Add Name and ID
| 
* commit 630a0d29a1f9e658281f0f2124374292afacf068
  Author: ZxjSamantha <35060339+ZxjSamantha@users.noreply.github.com>
  Date:   Thu Oct 29 22:31:22 2020 +0800
  
      First Change
```

`git merge --no-ff`: Fast-forward merge can be used when there is a linear path from the current branch tip to the target branch. 

 ---
 
 Exercise 7: Commit some to `br-b` and `master` and rebase `br-b` to `master`. 
 
 `git cherry-pick COMMIT_ID`: Pick the specific commit on aother branch directly to the master. 
 
 `git checkout br-b` and `git rebase master`: Pick all the commits on the branch, save them temporarily and remove them from the branch. It will look like a smoothier flow with only one temporal order. If conflits happen, use `git rebase --continue` without `git commit`.
 
 ```
 * commit 10bfde0ec6aa0049b3383b7eed9db2bbbb09d4ba (HEAD)
| Author: ZxjSamantha <35060339+ZxjSamantha@users.noreply.github.com>
| Date:   Fri Oct 30 12:07:46 2020 +0800
| 
|     Add eightQueen and BFS
| 
* commit 47f09e08c71b852f1103251ad52bc4e971d06149 (master)
| Author: ZxjSamantha <35060339+ZxjSamantha@users.noreply.github.com>
| Date:   Fri Oct 30 12:01:15 2020 +0800
| 
|     Fix conflict2
|   
| * commit 6c5a296385a965246d2f55d9f71d6706ba9db511 (eightQueen)
| | Author: ZxjSamantha <35060339+ZxjSamantha@users.noreply.github.com>
| | Date:   Fri Oct 30 12:01:15 2020 +0800
| | 
| |     Add BFS
| | 
| * commit b56c7a0ed0c3b3d63c835d87df714bb68cb2fa17
|/  Author: ZxjSamantha <35060339+ZxjSamantha@users.noreply.github.com>
|   Date:   Fri Oct 30 11:59:36 2020 +0800
|   
|       Class eightQueen
|   
*   commit c795ad51457830e47ab9820bcfc1e752a6f03480
|\  Merge: cbaf5f0 b379fa9
| | Author: ZxjSamantha <35060339+ZxjSamantha@users.noreply.github.com>
| | Date:   Fri Oct 30 11:45:58 2020 +0800
| | 
| |     Fix conflict
| | 
| * commit b379fa91d179f220c61d482d4f89298bff7b2260 (tag: Gibbs, GibbsSampling)
| | Author: ZxjSamantha <35060339+ZxjSamantha@users.noreply.github.com>
| | Date:   Fri Oct 30 11:16:36 2020 +0800
| | 
| |     Add Gibbs Sampling
| | 
* | commit cbaf5f05a00170f724ef0807d9ce5b598b8569b5
| | Author: ZxjSamantha <35060339+ZxjSamantha@users.noreply.github.com>
| | Date:   Fri Oct 30 10:57:12 2020 +0800
| | 
| |     Add energy function
| | 
* | commit 7f2efec0ec7059f9a87c03510a5f6c56d7349e9a (tag: v1.0)
|/  Author: ZxjSamantha <35060339+ZxjSamantha@users.noreply.github.com>
|   Date:   Fri Oct 30 10:37:49 2020 +0800
|   
|       Add updateStates
| 
 ```

 
 ---
 
 Exercise 8: Try modifying the commit order and commit message with `git rebase -i` and `git commit --amend`.
 
 `git reflog`: Check which commit the branch pointed to in the past.
 
 ```
 git reflog   
10bfde0 (HEAD) HEAD@{0}: commit: Add eightQueen and BFS
47f09e0 (master) HEAD@{1}: rebase: checkout master
6c5a296 (eightQueen) HEAD@{2}: checkout: moving from master to eightQueen
47f09e0 (master) HEAD@{3}: commit (cherry-pick): Fix conflict2
c795ad5 HEAD@{4}: checkout: moving from eightQueen to master
6c5a296 (eightQueen) HEAD@{5}: commit: Add BFS
b56c7a0 HEAD@{6}: commit: Class eightQueen
c795ad5 HEAD@{7}: checkout: moving from master to eightQueen
c795ad5 HEAD@{8}: commit (merge): Fix conflict
cbaf5f0 HEAD@{9}: checkout: moving from GibbsSampling to master
b379fa9 (tag: Gibbs, GibbsSampling) HEAD@{10}: commit: Add Gibbs Sampling
255c3c0 (tag: Conver) HEAD@{11}: checkout: moving from 7f2efec0ec7059f9a87c03510a5f6c56d7349e9a to GibbsSampling
7f2efec (tag: v1.0) HEAD@{12}: checkout: moving from GibbsSampling to v1.0
255c3c0 (tag: Conver) HEAD@{13}: checkout: moving from 255c3c04d0f82116ecb0ed2c3b09e4fa4ec9da09 to GibbsSampling
255c3c0 (tag: Conver) HEAD@{14}: checkout: moving from master to 255c3c04d0f82116ecb0ed2c3b09e4fa4ec9da09
cbaf5f0 HEAD@{15}: commit: Add energy function
7f2efec (tag: v1.0) HEAD@{16}: commit: Add updateStates
255c3c0 (tag: Conver) HEAD@{17}: commit: Define Converter
0e94365 HEAD@{18}: commit: Delete Name & ID. Add Task.
782e173 HEAD@{19}: commit: Add Name and ID
630a0d2 HEAD@{20}: commit (initial): First Change
 ```
 
 `git rebased -i`: This commond provides a visualization interactive interface to operate the commits, such as modifying the commit messages and changing the commits order. 
 
 ```
 用法：git rebase [-i] [options] [--exec <命令>] [--onto <新基线> | --keep-base] [<上游> [<分支>]]
  或：git rebase [-i] [选项] [--exec <命令>] [--onto <新基线>] --root [<分支>]
  或：git rebase --continue | --abort | --skip | --edit-todo

    --onto <版本>         变基到给定的分支而非上游
    --keep-base           使用上游和分支的合并基线做为当前基线
    --no-verify           允许执行 pre-rebase 钩子
    -q, --quiet           安静。暗示 --no-stat
    -v, --verbose         显示上游变化的差异统计
    -n, --no-stat         不显示上游变化的差异统计
    --signoff             为每一个提交添加一个 Signed-off-by: 签名
    --ignore-whitespace   passed to 'git am'
    --committer-date-is-author-date
                          passed to 'git am'
    --ignore-date         passed to 'git am'
    -C <n>                传递给 'git apply'
    --whitespace <动作>   传递给 'git apply'
    -f, --force-rebase    拣选所有提交，即使未修改
    --no-ff               拣选所有提交，即使未修改
    --continue            继续
    --skip                跳过当前补丁并继续
    --abort               终止并检出原有分支
    --quit                终止但保持 HEAD 不变
    --edit-todo           在交互式变基中编辑待办列表
    --show-current-patch  显示正在应用或合并的补丁文件
    -m, --merge           使用合并策略进行变基
    -i, --interactive     让用户编辑要变基的提交列表
    --rerere-autoupdate   如果可能，重用冲突解决更新索引
    -k, --keep-empty      变基时保留空提交
    --autosquash          在 -i 交互模式下，移动以 squash!/fixup! 开头的提交
    -S, --gpg-sign[=<key-id>]
                          使用 GPG 签名提交
    --autostash           在操作前后执行自动贮藏和弹出贮藏
    -x, --exec <exec>     可编辑列表的每一个提交下面增加一行 exec
    --allow-empty-message
                          允许针对空提交说明的提交变基
    -r, --rebase-merges[=<模式>]
                          尝试对合并提交变基而不是忽略它们
    --fork-point          使用 'merge-base --fork-point' 来优化上游
    -s, --strategy <策略>
                          使用给定的合并策略
    -X, --strategy-option <选项>
                          将参数传递给合并策略
    --root                将所有可达的提交变基到根提交
    --reschedule-failed-exec
                          自动重新安排任何失败的 `exec`
 ```
 
 
 `git commit --amend`: Modifying the commit message. 
 
 ---
 
 Exercise 9: Modify the file using `git add`, and undo `git add` without losing the changes.
 
 `git reset --soft`
 
 `git reset --mixed`
 
 `git reset --hard`
 
 `git stash save`
 
 `git stash pop`
 
 `git stash list`
 
 
 ---
 
 Exercise 10: Find examples of good / bad commit messages on GitHub.
 
 Here is a great blog with introduction on good commits and bad commits.
 
 [How to Write a Git Commit Message](https://chris.beams.io/posts/git-commit/)
 
 The writter gives several examples on good and bad commits. Here are some bad commits: 
 
 ```
e5f4b49 Re-adding ConfigurationPostProcessorTests after its brief removal in r814. @Ignore-ing the testCglibClassesAreLoadedJustInTimeForEnhancement() method as it turns out this was one of the culprits in the recent build breakage. The classloader hacking causes subtle downstream effects, breaking unrelated tests. The test method is still useful, but should only be run on a manual basis to ensure CGLIB is not prematurely classloaded, and should not be run as part of the automated build.

2db0f12 fixed two build-breaking issues: + reverted ClassMetadataReadingVisitor to revision 794 + eliminated ConfigurationPostProcessorTests until further investigation determines why it causes downstream tests to fail (such as the seemingly unrelated ClassPathXmlApplicationContextTests)

147709f Tweaks to package-info.java files

22b25e0 Consolidated Util and MutableAnnotationUtils classes into existing AsmUtils

7f96f57 polishing
 ```
 Each of the commit messages are too redundant or too confusiong. Here are some good exmamples:
 
 ```
5ba3db6 Fix failing CompositePropertySourceTests
84564a0 Rework @PropertySource early parsing logic
e142fd1 Add tests for ImportSelector meta-data
887815f Update docbook dependency and generate epub
ac8326d Polish mockito usage
 ```
 
 In summary, good commits should follow the following: 
 
 1. Separate subject from body with a blank line
 
 2. Limit the subject line to 50 characters
 
 3. Capitalize the subject line

 4. Do not end the subject line with a period

 5. Use the imperative mood in the subject line

 6. Wrap the body at 72 characters

 7. Use the body to explain what and why vs. how


 ---
 
 Exercise 11: Practice Git operatiosn on the practice site. 
 
 [Learn Git Branching](https://learngitbranching.js.org/)
 
 This site provides the visualization of common git operations, by giving learners small tasks and accomplish the tasks with git commands. 
 
 It is quite fun and learnable. However, I am still kind of confused about `git rebase -i` operation some times. 
 
 

