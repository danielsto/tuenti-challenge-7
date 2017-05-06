# tuenti-challenge-7
My solutions on the Tuenti Challenge 7 by Tuenti using Python

[Introduction]()  
[Challenge 1 - Pizza Love](https://github.com/danielsto/tuenti-challenge-7#challenge-1---pizza-love)  
[Challenge 2 - Bowling]()  
[Challenge 3 - Board games]()  
[Challenge 4 - Help Pythagoras Junior]()  
[Challenge 5 - Ghost in the HTTP]()  
[Challenge 6 - The Tower]()  
[Challenge 7 - Word Soup Challenge]()  

## Introduction
This is my approach to the programming contest Tuenti Challenge 7 organized by Tuenti in 2017.
Most of the code was written in Python 3.5 and is available in this repository.
There are also files containing input and output data for each challenge.

I had some problems submitting a couple of output files so I was not properly ranked
(I sent output from one challenge to two different challenges). Nevertheless I was #327 out of 1428 contestants.
 
 More on my experience in this [blog post]() in spanish.

## Challenge 1 - Pizza Love
Only modules from The Python Standard Library were used to solve this challenge.
These modules were [math](https://docs.python.org/3/library/math.html) for mathematical functions
and [os](https://docs.python.org/3/library/os.html) to interact with the operating system.

This one was pretty easy. Details can be found [here](https://contest.tuenti.net/Challenges). For each case in the input file, 
pizzas slices were added to a total which then was divided by 8 (number of slices per 
pizza). Then math.ceil() function was applied to that sum so that there was enough pizza 
for everyone, even though this may cause some leftovers.

Run time: ~0.07 seconds including file reading and writing.  
Number of lines: 17 including module imports. Main algorithm is 8 lines.
## Challenge 2 - Bowling
Only one module from The Python Standard Library was used to solve this challenge.
This module was [os](https://docs.python.org/3/library/os.html) to enable interaction
with the operating system.

This one was a little bit more tricky because I had no idea how bowling was scored.
## Challenge 3 - Board games
Only modules from The Python Standard Library were used to solve this challenge.
These modules were [math](https://docs.python.org/3/library/math.html) for mathematical functions
and [os](https://docs.python.org/3/library/os.html) to interact with the operating system.

Challenge 3 was all about really understanding what it was being asked and that was
a bit hard for me.

Coding the solution was easy though. For each case smallest nearest integer of log2(points) is found
and then added 1. Thus, we get the minimum number of cards necessary to represent all the points in that case.

Runtime:  ~0.001 s including file reading and writing
Number of lines:  12, main algorithm is 5 lines long 
## Challenge 4 - Help Pythagoras Junior
Only modules from The Python Standard Library were used to solve this challenge.
These modules were [math](https://docs.python.org/3/library/math.html) for mathematical functions, 
[os](https://docs.python.org/3/library/os.html) to interact with the operating system and to interact
with the operating system and [itertools](https://docs.python.org/2/library/itertools.html) to generate
combinatoric iterators.

For this challenge a little bit of mathematical theory was needed, geometry to be precise.
According to the [Triangle Inequality Theorem](), "the sum of two side lengths of a triangle is 
always greater than the third side".
 
It would have seemed obvious to iterate over all the possible combinations of sides and get the smallest
perimeter of them. And it worked (a bit slow)  with the testInput.txt because it contained only 71 cases
which greatest number of sides was 100. It definitely didn't work that way with the submitInput.txt, with 130 cases
of 1000 sides each.

That's where the magic happened. Only by sorting the list (for obvious reasons) it became much more efficient and actually
ended in a reasonable time.

Run time: ~2.25 s including file reading and writing (more than 2 hours without sorting and not even finishing)   
Number of lines: 31, main algorithm is 8 lines long

## Challenge 5 - Ghost in the HTTP
I still have NO IDEA how was this done but plan to research in write-ups and blogs.
It had something to do with HTTP/2.

## Challenge 6 - The Tower
TODO
## Challenge 7 - Word Soup Challenge
TODO