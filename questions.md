
## 1001

Problem Description

```
Hey, welcome to HDOJ(Hangzhou Dianzi University Online Judge).

In this problem, your task is to calculate SUM(n) = 1 + 2 + 3 + ... + n.

```

Input

```
The input will consist of a series of integers n, one integer per line.

```

Output

```
For each case, output SUM(n) in one line, followed by a blank line. You may assume the result will be in the range of 32-bit signed integer.

```

Sample Input

```
1
100

```

Sample Output

```
1

5050


```

### MyResult

```c
//

```


    
## 1002

Problem Description

```
The highest building in our city has only one elevator. A request list is made up with N positive numbers. The numbers denote at which floors the elevator will stop, in specified order. It costs 6 seconds to move the elevator up one floor, and 4 seconds to move down one floor. The elevator will stay for 5 seconds at each stop.

For a given request list, you are to compute the total time spent to fulfill the requests on the list. The elevator is on the 0th floor at the beginning and does not have to return to the ground floor when the requests are fulfilled.

```

Input

```
There are multiple test cases. Each case contains a positive integer N, followed by N positive numbers. All the numbers in the input are less than 100. A test case with N = 0 denotes the end of input. This test case is not to be processed.

```

Output

```
Print the total time on a single line for each test case. 

```

Sample Input

```
1 2
3 2 3 1
0

```

Sample Output

```
17
41

```

### MyResult

```c
//

```


    
## 1003

Problem Description

```
The least common multiple (LCM) of a set of positive integers is the smallest positive integer which is divisible by all the numbers in the set. For example, the LCM of 5, 7 and 15 is 105.


```

Input

```
Input will consist of multiple problem instances. The first line of the input will contain a single integer indicating the number of problem instances. Each instance will consist of a single line of the form m n1 n2 n3 ... nm where m is the number of integers in the set and n1 ... nm are the integers. All integers will be positive and lie within the range of a 32-bit integer.

```

Output

```
For each problem instance, output a single line containing the corresponding LCM. All results will lie in the range of a 32-bit integer.

```

Sample Input

```
2
3 5 7 15
6 4 10296 936 1287 792 1

```

Sample Output

```
105
10296

```

### MyResult

```c
//

```


    
## 1004

Problem Description

```
A number sequence is defined as follows:

f(1) = 1, f(2) = 1, f(n) = (A * f(n - 1) + B * f(n - 2)) mod 7.

Given A, B, and n, you are to calculate the value of f(n).

```

Input

```
The input consists of multiple test cases. Each test case contains 3 integers A, B and n on a single line (1 <= A, B <= 1000, 1 <= n <= 100,000,000). Three zeros signal the end of input and this test case is not to be processed.

```

Output

```
For each test case, print the value of f(n) on a single line.

```

Sample Input

```
1 1 3
1 2 10
0 0 0

```

Sample Output

```
2
5

```

### MyResult

```c
//

```


    
## 1005

Problem Description

```
There are another kind of Fibonacci numbers: F(0) = 7, F(1) = 11, F(n) = F(n-1) + F(n-2) (n&amp;gt;=2).

```

Input

```
Input consists of a sequence of lines, each containing an integer n. (n < 1,000,000).

```

Output

```
Print the word &quot;yes&quot; if 3 divide evenly into F(n).

Print the word &quot;no&quot; if not.

```

Sample Input

```
0
1
2
3
4
5

```

Sample Output

```
no
no
yes
no
no
no

```

### MyResult

```c
//

```


    
## 1006

Problem Description

```
HOHO，终于从Speakless手上赢走了所有的糖果，是Gardon吃糖果时有个特殊的癖好，就是不喜欢将一样的糖果放在一起吃，喜欢先吃一种，下一次吃另一种，这样；可是Gardon不知道是否存在一种吃糖果的顺序使得他能把所有糖果都吃完？请你写个程序帮忙计算一下。

```

Input

```
第一行有一个整数T，接下来T组数据，每组数据占2行，第一行是一个整数N（0<N<=1000000)，第二行是N个数，表示N种糖果的数目Mi(0<Mi<=1000000)。

```

Output

```
对于每组数据，输出一行，包含一个&quot;Yes&quot;或者&quot;No&quot;。

```

Sample Input

```
2
3
4 1 1
5
5 4 3 2 1

```

Sample Output

```
No
Yes

# HintHint</div>
Please use function scanf

```

### MyResult

```c
//

```


    
## 1007

Problem Description

```
求A^B的最后三位数表示的整数。
说明：A^B的含义是“A的B次方”

```

Input

```
输入数据包含多个测试实例，每个实例占一行，由两个正整数A和B组成（1<=A,B<=10000），如果A=0, B=0，则表示输入数据的结束，不做处理。
```

Output

```
对于每个测试实例，请输出A^B的最后三位表示的整数，每个输出占一行。

```

Sample Input

```
2 3
12 6
6789 10000
0 0

```

Sample Output

```
8
984
1

```

### MyResult

```c
//

```


    
## 1008

Problem Description

```
Given a positive integer N, you should output the most right digit of N^N.

```

Input

```
The input contains several test cases. The first line of the input is a single integer T which is the number of test cases. T test cases follow.
Each test case contains a single positive integer N(1<=N<=1,000,000,000).

```

Output

```
For each test case, you should output the rightmost digit of N^N.

```

Sample Input

```
2
3
4

```

Sample Output

```
7
6

# Hint
In the first case, 3 * 3 * 3 = 27, so the rightmost digit is 7.
In the second case, 4 * 4 * 4 * 4 = 256, so the rightmost digit is 6.
</div>
```

### MyResult

```c
//

```


    
## 1009

Problem Description

```
给定两个正整数，计算这两个数的最小公倍数。
```

Input

```
输入包含多组测试数据，每组只有一行，包括两个不大于1000的正整数.
```

Output

```
对于每个测试用例，给出这两个数的最小公倍数，每个实例输出一行。

```

Sample Input

```
10 14

```

Sample Output

```
70

```

### MyResult

```c
//

```


    
## 1010

Problem Description

```
数列的定义如下：
数列的第一项为n，以后各项为前一项的平方根，求数列的前m项的和。
```

Input

```
输入数据有多组，每组占一行，由两个整数n（n<10000）和m(m<1000)组成，n和m的含义如前所述。
```

Output

```
对于每组输入数据，输出该数列的和，每个测试实例占一行，要求精度保留2位小数。
```

Sample Input

```
81 4
2 2
```

Sample Output

```
94.73
3.41
```

### MyResult

```c
//

```


    