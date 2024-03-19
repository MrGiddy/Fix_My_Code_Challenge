# 0x00. Fix my code
# Background Context
```Fix my code``` is a new type of project, where we’ll jump into an existing code base and fix it!

Sometimes you will know the language, sometimes not.

Please download the repository [0x00-Fix_My_Code_Challenge](https://intranet.alxswe.com/rltoken/GLYjW57NUS-s-JEsfjuNFA) and use it as initial files for all solutions.

You should not recode everything, just fix it!

# Requirements
## General
Allowed editors: ```vi```, ```vim```, ```emacs```
All your files will be compiled on Ubuntu 20.04 LTS
All your files should end with a new line
A ```README.md``` file, at the root of the folder of the project is mandatory

# Tasks
## 0. FizzBuzz
Please take a look at my implementation of FizzBuzz in Python: [source code](https://github.com/alx-tools/0x00-Fix_My_Code_Challenge/blob/master/0-fizzbuzz.py)

Something is going wrong….
```
$ ./0-fizzbuzz.py 50
1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 Fizz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 Fizz 31 32 Fizz 34 Buzz Fizz 37 38 Fizz Buzz 41 Fizz 43 44 Fizz 46 47 Fizz 49 Buzz
$
```
```15``` should print ```FizzBuzz``` not ```Fizz```

### Solution
- Refactor the code such that the condition for checking multiples of both 3 and 5 comes before the conditon for checking multiples of 3 alone.

## 1. Print square
Please take a look at my implementation of printing a square in Javascript: [source code](hhttps://github.com/alx-tools/0x00-Fix_My_Code_Challenge/blob/master/1-print_square.js)

Something is going wrong….
```
$ ./1-print_square.js 4
####
####
####
####
$ ./1-print_square.js 10
################
################
################
################
################
################
################
################
################
################
################
################
################
################
################
################
$
```

```./1-print_square.js``` 10 should print a square of size 10…

### Solution
- Change parsing of input number to base 10 instead of base 16

## 2. Sort
Please find here my implementation of sorting arguments in Ruby: [source code](https://github.com/alx-tools/0x00-Fix_My_Code_Challenge/blob/master/2-sort.rb)

Something is going wrong….
```
$ ruby 2-sort.rb 12 41 2 C 9 -9 31 fun -1 32
31
32
12
41
2
9
-9
-1
$
```

## 3. User password
Please find here my implementation of a User class in Python: [source code](https://github.com/alx-tools/0x00-Fix_My_Code_Challenge/blob/master/3-user.py)

Something is going wrong….
```
$ ./3-user.py 
Test User
is_valid_password should return True if it's the right password
$
```
My tests should not print any error…

## 4. Double linked list
Please find here my implementation of a Double linked list in C: [source code](https://github.com/alx-tools/0x00-Fix_My_Code_Challenge/tree/master/4-delete_dnodeint)

Something is going wrong….
```
$ gcc -Wall -pedantic -Werror -Wextra -std=gnu89 main.c free_dlistint.c print_dlistint.c add_dnodeint_end.c delete_dnodeint_at_index.c -o delete_dnodeint
$ ./delete_dnodeint 
0
1
2
3
4
98
402
1024
-----------------
0
1
2
3
4
0
402
1024
-----------------
1
2
3
4
0
402
1024
-----------------
2
3
4
0
402
1024
-----------------
3
4
0
402
1024
-----------------
4
0
402
1024
-----------------
0
402
1024
-----------------
402
1024
-----------------
-----------------
-----------------
-----------------
-----------------
-----------------
-----------------
-----------------
-----------------
-----------------
$
```
It doesn’t look right…
