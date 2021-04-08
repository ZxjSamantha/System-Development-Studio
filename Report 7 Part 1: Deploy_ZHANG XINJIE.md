# Report 7 Part 1: Deploy
## Name: ZHANG XINJIE Student ID Number: 20M14457

---

Exercise 1: Create a branch in the repository for exercise, and publish it as GitHub Pages. 

[About GitHub Pages](https://docs.github.com/cn/free-pro-team@latest/github/working-with-github-pages/about-github-pages)

[Creating a GitHub Pages Site](https://docs.github.com/cn/free-pro-team@latest/github/working-with-github-pages/creating-a-github-pages-site)

And this is my GitHub Page for the branch: 

[System Development Studio from ZxjSamantha](https://zxjsamantha.github.io/System-Development-Studio/)

I followed this tutorial: [Deploy Static Web Page with GitHub Pages](https://zhuanlan.zhihu.com/p/38480155)

Step 1: I firstly choosed `ghp-delpoy` branch as the source of GitHub Pages in the setting. 

`index.html`: 

```
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Github Page demo</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" media="screen" href="main.css" />
    <script src="index.js"></script>
</head>
<body>
    <div id="main-content">

    </div>
</body>
</html>
```

`index.js`:

```
window.onload = function() {
  document.getElementById('main-content').innerHTML = 'Hello, github pages :)'
}
```

`main.css`:

```
#main-content {
  font-size: 36px;
  font-weight: bold;
  padding: 16px;
}
```

Step 2: I cloned the project into the local pc, and committed several files, and pushed the repository. 

Step 3: I can check the change on the web page with my commits to the repository through CircleCI directly.

---

Exercise 2: Deploy the repository for the exercise with CircleCI to GitHub Pages. 

This exercise is to generate a dymanic file in the CircleCI and add it to GitHub Pages. Ideally, I should be able to deploy the files into the GitHub Pages automatically with CircleCI. 

Step 1: Add an ssh deploy key to CircleCI.

Here is the tutorial of adding the ssh key to CircleCI.

[Adding an SSH Key to CircleCI](https://circleci.com/docs/2.0/add-ssh-key/)

Step 2: The expect of this step is to push the generated file from program `a.c` to the GitHub Pages in the branch `ghp-deploy`. 

The code of `a.c`:

```
#include <stdio.h>

int fib(int i) {
  if (i <= 1) {
    return i;
  }
  return fib(i - 2) + fib(i - 1);
}

int main() {
  printf("fib(10) = %d\n", fib(10));
}
```

The deploy script:

```
target_branch="ghp-deploy"
git config --global user.name "CircleCI deployer"
git config --global user.email "<>"
git checkout $target_branch
git reset --hard origin/main

gcc -o a.out a.c
echo "output of a.out: $(./a.out)" > a.txt

git add a.out a.txt
git commit -m "[skip ci] updates GitHub Pages"
if [ $? -ne 0 ]; then
  echo "nothing to commit"
  exit 0
fi
git remote set-url origin "https://github.com/ZxjSamantha/System-Development-Studio.git"
git push -f origin $target_branch
```

I failed to deploy the file a.txt to the GitHub Pages though I successfully builded the project in CircleCI. The output in CircleCI is as the following:

```
Already on 'ghp-deploy'
HEAD is now at 8121525 Rename RNN.py to OSS-project/RNN.py
./deploy.sh: line 9: gcc: command not found
./deploy.sh: line 10: ./a.out: No such file or directory
fatal: pathspec 'a.out' did not match any files
On branch ghp-deploy
Untracked files:
  (use "git add <file>..." to include in what will be committed)
	a.txt
	deploy.sh

nothing added to commit but untracked files present (use "git add" to track)
nothing to commit
CircleCI received exit code 0
```

The failure may be caused by the configurations of my pc, since I changed to use this pc temporarily and many configurations had not been set. 

CircleCI provides an automated deployment, from fetching a repository into local pc, automatically running the gievm operations, adding the generated files and pushing them back to the given branches in the origin repository. It will save a lot of time and works for coders from mannually deploying and testing, especially for large scale development.   

--- 

Exercise 3: List some non-idempotent operations and explain when they are not idempotent.

Idempotence is a mathematical property that f(x) = f(f(x)). In programming, methods can also have the property of “idempotence” in that (aside from error or expiration issues) the side-effects of N > 0 identical requests is the same as for a single request.

[Tutorial of Idempotence](https://www.jianshu.com/p/475589f5cd7b)

[What is an idempotent opration](https://stackoverflow.com/questions/1077412/what-is-an-idempotent-operation)

For example, in the operations of database, **insert** and **update** are not idempotent, because they will affect the system and produce different results when taking single operation and multiple operations. 

The necessecity of idempotence and methods to guarantee idempotence are discussed in this blog. 

[What is idempotence?](https://www.modb.pro/db/13517)

The definition of idempotence:

1. Idempotence is more than just one (or multiple) requests without side effects on resources.

2. Idempotence also includes side effects on resources when the first request is made, but subsequent requests will no longer have side effects on resources.

3. Idempotent is concerned with whether the subsequent multiple requests will have side effects on the resource, but not the result.

4. Problems such as network timeout are not the scope of idempotent discussion.

Idempotence is a promise (rather than realization) of system services to the outside world, which promises that as long as the interface is successfully called, the impact of multiple external calls on the system is consistent. Services declared as idempotent will consider external call failures to be normal, and there must be retry after failure.

How to guarantee idempotence? Here are two commonly used methods. 

1. Create a unique index

2. Use the token to prevent repeated submissions. 



