# Report: Information Collection #
## Name: ZHANG XINJIE Student ID Number: 20M14457 ##

## Contents ##

1.   Information Collection of Accessing GitHub using Command Lines
2.   Information Collection of My own Open Source Software Project
3.   Answers of Exercises 1-3.

---

### Part 1: Information Collection of Accessing GitHub using Command Lines ###

This is the issue URL of work log of Part 1.

[https://github.com/ZxjSamantha/System-Development-Studio/issues/2]

---

### Part 2: Information Collection of Open Source Software Project ###

This is URL to the OSS project:

[https://github.com/ZxjSamantha/System-Development-Studio/tree/main/OSS-project]

This is the issue of work log of Part 2: 

[https://github.com/ZxjSamantha/System-Development-Studio/issues/3]

I am sorry that I was a student majoring in Automation Control. I would consider myself a completely beginner to C/C++ because I have not programmed with C/C++ language for quite a long time. So I have to consider simple C/C++ projects with small volume. 

I like playing video games and I did some game design projects in my undergraduate time. So I considered making a small C/C++ game from scratch. 

I searched with the keyword "C++ projects for beginners" in Chinese, and found a website with a list for C++ beginners. Many projects in the list are about game.

[C/C++ Projects for Beginners](https://zhuanlan.zhihu.com/p/23047091)

Considering the difficulty and development period, I decided to develop a maze game or a reproduction of Google offline dinosaur game. 

---

### Part 3: Answer of Exercises 1-3 ###

1.    Exercise 1: Investigate what is the ASCII code of *#*

  Answer: 35 

  Work log: 

  Search "ASCII code #" on google;

  Find the ASCII code of *#* in the URL [https://www.ascii-code.com/].

  Solution: Use command *man* in terminal to access bulit-in manual.

> man ascii

2.    Exercise 2: Find the command line that compresses the directory *abc* with *tar* and create a file called *abc.tar.gz*

  Answer: tar -zcvf abc.tar.gz abc 

  Work log:

  Search "tar command compress file" on google;

  Find the command line in the URL [https://www.tecmint.com/18-tar-command-examples-in-linux/#:~:text=The%20tar%20command%20used%20to,disk%20or%20machine%20to%20machine.];

  Solution: tar czf abc.tar.gz abc

> man tar

  #man# is a great command line for applying built-in command lines. 

3.    Exercise 3: Compare the program in case of optimization and in case of no optimization. Investigate the effect of optimization.

```
int collatz(int n) {
  if (n == 1) return 1;
  if (n%2) return collatz(3*n + 1);
  else     return collatz(n/2);
}

```

  Answer: I was not able to answer it in time.

  Work log:

  Search "collatz" on Google;

  Check the wiki [https://en.wikipedia.org/wiki/Collatz_conjecture];

  Time passed when I tried to figure out what is Collatz conjecture. 

  I still cannot clearly understand the effect of optimization, but I found a great discussion on stackoverflow with keyword "collatz program optimization compiler" in the following URL:

[https://stackoverflow.com/questions/40354978/why-does-c-code-for-testing-the-collatz-conjecture-run-faster-than-hand-writte]

  I will update my work log in this issue: [https://github.com/ZxjSamantha/System-Development-Studio/issues/1]

  Solution:
  -O3最適化の結果，単に1を返す関数に

```
collatz(int):
        mov     eax, 1
        ret
```






