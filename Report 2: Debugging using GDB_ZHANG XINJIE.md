
# Report: Debugging using GDB #
## Name: ZHANG XINJIE Student ID Number: 20M14457 ##

## Contents ##

1.    Findings of Exercises 1-6 Using Given Cases

---

### Part 1: Findings of Exercises 1-6 Using Given Cases ###

1.    Exercise 1: Examine the OSS project using UB sanitizer.

   **What is Undefined Behavior?**

   I searched definition of undefined behavior at first, and I found an good article  written by John Regehr giving definition of UB, the classifications of UB and discussions of UB. 

   [A Guide to Undefined Behavior in C and C++, Part 1](https://blog.regehr.org/archives/213)

   The definition of Undefined Behavior is as the following: The program may fail to compile, or it may execute incorrectly (crashing; generating incorrect results), or it may fortuitously do exactly what the programmer intended.

   If any step in a program's execution has undefined behavior, then the entire execution is without meaning. John Regehr gives several approaches to deal with undefined behavior:

   - Enable and heed compiler warnings, preferably using multiple compilers

   - **Use static analyzers (like Clang’s, Coverity, etc.) to get even more warnings**

   - Use compiler-supported dynamic checks; for example, gcc’s -ftrapv flag generates code to trap signed integer overflows

   - Use tools like Valgrind to get additional dynamic checks

   - When functions are “type 2” as categorized above, document their preconditions and postconditions

   - Use assertions to verify that functions’ preconditions are postconditions actually hold

   - Particularly in C++, use high-quality data structure libraries

   In the given case, clang is used to get warning from programs with undefined behavior.The documentation of Undefined Behavior Sanitizer is given in the following:

   [Clang 12 documentation: UndefinedBehaviorSanitizer](https://clang.llvm.org/docs/UndefinedBehaviorSanitizer.html)

   The used command is:

   > clang -fsanitize=undefined program.c 

   `-fsanitize=undefined` will print a verbose error report and continue execution.

   I tested a example given in [A Guide to Undefined Behavior in C and C++, Part 1]

```
#include<limits.h>
#include <stdio.h>

int main(void) {
    printf("%d\n", (INT_MAX+1) < 0);
    return 0;
}
```

   The report given using `clang -fsanitize=undefined UBSanitizer.c` is in the following:

```shell
UBSanitizer.c:5:28: warning: overflow in expression; result is -2147483648 with type 'int' [-Winteger-overflow]
    printf("%d\n", (INT_MAX+1) < 0);
                           ^
1 warning generated.
1
```

   The warning emphasizes undefined behavior happened in the line **5** and charater **28**. 

   More examples of undefined behaviors are given in the following blog:

   [Examples of Undefined Behaviors](https://en.cppreference.com/w/cpp/language/ub)


2.    Exercise 2: Set checkpoints in the OSS project using GDB to check values of variables. & Exercise 5: Observe the changes of variables in the OSS project using watchpoints.

   I would like to put the exercise 2 & 5 together since breakpoints and watchpoints are usually working together during debugging.

   I am a Mac user. The equivalent debugger with same functions like gdb on Mac is **lldb**. There are some tiny differences between commands but most of them are same. 

   Here is a documentation listing commands with same functions in gbd and lldb:

   [GDB to LLDB command map](https://lldb.llvm.org/use/map.html)
    
   And a tutorial documentation for lldb:
    
   [Tutorial of lldb](https://lldb.llvm.org/use/tutorial.html)

   Here is a simple tutorial I found using lldb to debug program in C:

   [Debugging C with clang compiler and lldb](https://www.developerfiles.com/debugging-c-with-clang-compiler-and-lldb/)

**Step 1:**

```
clang -g breakpoint.c -o breakpoint
lldb breakpoint
(lldb) target create "breakpoint"
Current executable set to 'breakpoint' (x86_64).
```



**Step 2: Operate on breakpoints and start debugging**

The breakpoints can be added using:

`b line_number`

`b function_name`

`b program_name.c: line_number/function_name`

   output:

```
(lldb) b breakpoint.c:10
Breakpoint 1: where = breakpoint`main + 51 at breakpoint.c:11:28, address = 0x0000000100000f43
```
   Start debugging:

`run`

   Output: 

```
Process 83390 launched: 'breakpoint.c'
Process 83390 stopped
* thread #1, queue = 'com.apple.main-thread', stop reason = breakpoint 1.1
    frame #0: 0x0000000100000f43 breakpoint`main at breakpoint.c:11:28
   8        x += 1;
   9        x += y;
   10       
-> 11       printf("Name is %s\n", name);
   12       printf("Number x is %d\n", x); 
   13   }
Target 0: (breakpoint) stopped.
```

   There are several commands for further debugging:
    
   - `p variable_name`: displaying specific variable
    
```
(lldb) p name
(char *) $0 = 0x0000000100000f96 "Jimmy"
(lldb) p &name
(char **) $1 = 0x00007ffeefbff5f0
```
 
   - `next` or `n`: Step to the next line.

   Step to the next line with `n`. The output is:
    

```
(lldb) n
Name is Jimmy
Process 83390 stopped
* thread #1, queue = 'com.apple.main-thread', stop reason = step over
    frame #0: 0x0000000100000f55 breakpoint`main at breakpoint.c:12:32
   9        x += y;
   10       
   11       printf("Name is %s\n", name);
-> 12       printf("Number x is %d\n", x); 
   13   }
Target 0: (breakpoint) stopped.
```


   `printf("Name is %s\n", name);` is executed. 

   - `step` or `s`: Step into current's line function.
    

```
(lldb) s
Number x is 16
Process 83390 stopped
* thread #1, queue = 'com.apple.main-thread', stop reason = step in
    frame #0: 0x0000000100000f6e breakpoint`main at breakpoint.c:13:1
   10       
   11       printf("Name is %s\n", name);
   12       printf("Number x is %d\n", x); 
-> 13   }
Target 0: (breakpoint) stopped.
```

   - `continue` or `c`: Continue until the next breakpoint.

```
(lldb) c
Process 83390 resuming
Process 83390 exited with status = 0 (0x00000000) 
```
   - `finish`: Finish excecuting the current function and then pauses

```
(lldb) finish
error: invalid thread
```

   - `br list `: List all existing breakpoints. 

```
(lldb) br list
Current breakpoints:
1: file = 'breakpoint.c', line = 10, exact_match = 0, locations = 1, resolved = 1, hit count = 1
  1.1: where = breakpoint`main + 51 at breakpoint.c:11:28, address = 0x0000000100000f43, resolved, hit count = 1 
```

   - `br del breakpint_id_number`: Delete breakponit with specific id number. `br del` will delete all breakpoints.
    
```
(lldb) br del 1
1 breakpoints deleted; 0 breakpoint locations disabled.
```
    
   For a function that may be called more than once in the program, the sequence of nested functions calls is needed. `br` can be the tool to know the backtrace. 
   
   As breakpoints are for programs, watchpoints are for data.

   The differences between a software watchpoint and a hardware watch point are explained in the following:

   [Difference of software and hardware watchpoint](https://stackoverflow.com/questions/48695665/difference-software-and-hardware-watchpoint)
   
   In general, hardware watchpoints can monitor memory read/write as a CPU function, while software watchpoints are used when hardware watchpoints are not available, normally to monitor memory changes and in a slow speed. 
   
   Here are common commands of using watchpoints by command `help watchpoint`. 

```
(lldb) help watchpoint
     Commands for operating on watchpoints.

Syntax: watchpoint <subcommand> [<command-options>]

The following subcommands are supported:

      command -- Commands for adding, removing and
                 examining LLDB commands executed when
                 the watchpoint is hit (watchpoint
                 'commands').
      delete  -- Delete the specified watchpoint(s).  If
                 no watchpoints are specified, delete
                 them all.
      disable -- Disable the specified watchpoint(s)
                 without removing it/them.  If no
                 watchpoints are specified, disable them
                 all.
      enable  -- Enable the specified disabled
                 watchpoint(s). If no watchpoints are
                 specified, enable all of them.
      ignore  -- Set ignore count on the specified
                 watchpoint(s).  If no watchpoints are
                 specified, set them all.
      list    -- List all watchpoints at configurable
                 levels of detail.
      modify  -- Modify the options on a watchpoint or
                 set of watchpoints in the executable. 
                 If no watchpoint is specified, act on
                 the last created watchpoint.  Passing
                 an empty argument clears the
                 modification.
      set     -- Commands for setting a watchpoint.

For more help on any particular subcommand, type 'help <command> <subcommand>'.
```

   Debugging by setting breakpoints and watchpoints:
   
```
(lldb) target create "./breakpoint"
Current executable set to 'breakpoint'
(lldb) b 7
Breakpoint 2: where = breakpoint`main + 33 at breakpoint.c:8:7, address = 0x0000000100000f31
(lldb) run
Process 85402 launched: 'breakpoint'
Process 85402 stopped
* thread #1, queue = 'com.apple.main-thread', stop reason = breakpoint 2.1
    frame #0: 0x0000000100000f31 breakpoint`main at breakpoint.c:8:7
   5        int y = 5;
   6        char *name = "Jimmy";
   7   
-> 8        x += 1;
   9        x += y;
   10       
   11       printf("Name is %s\n", name);
Target 0: (breakpoint) stopped.
(lldb) watch set var x
Watchpoint created: Watchpoint 2: addr = 0x7ffeefbff5fc size = 4 state = enabled type = w
    declare @ '/Users/zhangxinjie/Desktop/3Q讲义/System Developmen Studio/Lecture02/breakpoint.c:4'
    watchpoint spec = 'x'
    new value: 10
```

  - `watch modify -c '(var in condition)'` command means using `(lldb) c` to continue until variable satisifies the specified condition.
  - `watch l` or `watchpoint list` commands can get set watchpoints.
  
```
(lldb) watch modify -c '(x == 16)'
(lldb) watch l
Number of supported hardware watchpoints: 4
Current watchpoints:
Watchpoint 2: addr = 0x7ffeefbff5fc size = 4 state = enabled type = w
    declare @ 'breakpoint.c:4'
    watchpoint spec = 'x'
    new value: 10
    condition = '(x == 16)'
    
(lldb) c
Process 85402 resuming

Watchpoint 2 hit:
old value: 10
new value: 16
Process 85402 stopped
* thread #1, queue = 'com.apple.main-thread', stop reason = watchpoint 2
    frame #0: 0x0000000100000f43 breakpoint`main at breakpoint.c:11:28
   8        x += 1;
   9        x += y;
   10       
-> 11       printf("Name is %s\n", name);
   12       printf("Number x is %d\n", x); 
   13   }
Target 0: (breakpoint) stopped.
```
  
The program stopped at when `x == 16` as the set condition. 


3.    Exercise 3: Try debugging with a core dump.

   **What is Core dump?**
   
   In the case of Mac, there are some extra steps needed to access core files. 
   
   [How to generate core dumps in Mac OS X?](https://stackoverflow.com/questions/9412156/how-to-generate-core-dumps-in-mac-os-x/12118329)
  

   Step 1: Activate the generation of core dump file. 
   
   `ulimit -c unlimited`
   
   Step 2:Compile the target program. 
   
   `clang -g program.c -o program`
   
   Step 3: Run the target program.
   
   `./program`
   
   Output: 
   
   `segmentation fault  ./program`
   
   Step 4:
   
   `lldb `
   
   Step 5:
   
   I tested core dump with following code:
   
   ```
#include<stdio.h>

int main(int argc, char** argv){
    int *p = NULL;
    *p = 0;

    printf("Bad!\n");
    return 0; 
}
   ```
   
   Firstly, I generated coredump file in the following flow:
   
```
ulimit -c unlimited
clang -c coredump.c -o coredump
./coredump
```

Output:

```
segmentation fault  ./coredump
```

However, I did not found the core file. 

I will update my progress on debugging with core dump in the following issue:

[Debug with Core Dump (core file not found)](https://github.com/ZxjSamantha/System-Development-Studio/issues/4)

4.    Exercise 4: Try debugging by embedding int3 command in the OSS project.

**What is int3?**

**INT** is an assembly language instruction for x86 processors that generates a software interrupt. When written in assembly language, the instruction is written like `INT X`, where `X` is the software interrupt that should be generated (0-255). 

**INT 3** instruction is a one-byte-instruction defined for use to temporarlly replace an instruction in a runnning program in order to set a code breakpoint.  

I found a tutorial about debugging with int 3 in Chinese. 

[int 3 Interupt and Debugging](https://blog.csdn.net/trochiluses/article/details/20209593)

INT 3 is a one-byte-instruction to support debugging, by replacing an instruction in a running program in order to set a code breakpoint. 


The debugging process using given case is shown in the following:

```
#include <stdio.h>

int main(){
    printf("debug\n");
    asm("int3");
    printf("debug2\n");
    printf("debug3\n");
}
```

The debugging is like debugging with breakpoints:

```

clang -g int3command.c -o int3command
lldb int3command
(lldb) target create "int3command" 'int3command'
(lldb) r
Process 86245 launched: 'int3command'
Process 86245 stopped
* thread #1, queue = 'com.apple.main-thread', stop reason = EXC_BREAKPOINT (code=EXC_I386_BPT, subcode=0x0)
    frame #0: 0x0000000100000f47 int3command`main at int3command.c:6:5
   3    int main(){
   4        printf("debug\n");
   5        asm("int3");
-> 6        printf("debug2\n");
   7        printf("debug3\n");
   8    }
Target 0: (int3command) stopped.
(lldb) frame info
frame #0: 0x0000000100000f47 int3command`main at int3command.c:6:5
(lldb)  x/10i $rip-20
    0x100000f33: e5 48                 inl    $0x48, %eax
    0x100000f35: 83 ec 10              subl   $0x10, %esp
    0x100000f38: 48 8d 3d 57 00 00 00  leaq   0x57(%rip), %rdi          ; "debug\n"
    0x100000f3f: b0 00                 movb   $0x0, %al
    0x100000f41: e8 30 00 00 00        callq  0x100000f76               ; symbol stub for: printf
    0x100000f46: cc                    int3   
->  0x100000f47: 48 8d 3d 4f 00 00 00  leaq   0x4f(%rip), %rdi          ; "debug2\n"
    0x100000f4e: 89 45 fc              movl   %eax, -0x4(%rbp)
    0x100000f51: b0 00                 movb   $0x0, %al
    0x100000f53: e8 1e 00 00 00        callq  0x100000f76               ; symbol stub for: printf
```

When we set breakpoints with debugger (e.g., gdb, lldb), the debugger will save the first character of original command and rewrite an `INT 3`command. 

