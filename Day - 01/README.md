# About my Algorithms

Problem: https://adventofcode.com/2021/day/1

## PART - 1

For the proper algorithm we need to loop either `from 1 to end of list` or `from 0 to end of list - 1` <br>
For idea 1 you need to check if the list element at the current index if higher then the list element at current index  - 1. <br>
For idea 2 you need to check if the list element at the current index + 1 if higher then the list element at current index. <br>
Count all the occurrence mentioned above and your are done with part one. <br>

## PART - 2

![kép](https://user-images.githubusercontent.com/60004480/184424333-90a7f2e5-1655-4f94-8a4f-af12635da2ac.png)
<br>
As you can see we don't need to sum the numbers. <br>
We just need to check if the last B number (210) is higher then the first A number (199). <br>
It works because the (200) and (208) numbers can be found in **both sum A and B** and these numbers **do not affact** the result . <br>

For the proper algorithm we need to loop from 0 to end of list - 2. <br>
And we check if the `list element at the current index + 2` is higer then the `element at the current index`. <br>
Count all the occurrence mentioned above and your are done with part two. <br>
