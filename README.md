# Homework 2: Extracting and storing information with Dictionaries, Working with Functions

Due: 	Monday, October 14, 12:00n 

What to hand in:
* hw2-part1.py program (all your code from part 1)
* hw2-part2.py program (all your code from part 2)
* hw2-feedprocessor.py program (all your code from parts 3-6)

## Part 1: Exercises with Dictionaries
The following code should be at the top of your starter file, hw2-part1.py:

```python
dinocount = {'triceratops': 3, 'tyrannosaurus rex': 1, 'dilophosaurus': 2, 'parasaurolophus': 3, 'gallimimus': 12}
```

The dictionary dinocount represents the number of dinosaurs in a small dinosaur zoo. Complete the exercises embedded in the code. 
Your output should look like:

```
== 1 ==
12
== 2 ==
4
== 3 ==
3
== 4 ==
parasaurolophus: 4
== 5 ==
triceratops
tyrannosaurus rex
dilophosaurus
parasaurolophus
gallimimus
velociraptor
== 6 ==
triceratops: 4
tyrannosaurus rex: 1
dilophosaurus: 2
parasaurolophus: 4
gallimimus: 12
velociraptor: 3
== 7 ==
velociraptor: 3
Sorry, no stegosaurus in the zoo.
== 8 ==
velociraptor: 3
tyrannosaurus rex: 1
brachiosaurus: 0
archaeopteryx: 0
gallimimus: 12
argentinosaurus: 0
=== 9 ===
triceratops,4
tyrannosaurus rex,1
dilophosaurus,2
parasaurolophus,4
gallimimus,12
velociraptor,3
=== 10 ===
```

but please note that the order of dinosaurs may vary; dictionaries have no order.

Your CSV file contents should look like the table below when opened in Excel or another spreadsheet application. Again, order may vary, and your header row won't be bold.

| type | count
| --- | ---
| triceratops	| 3
| tyrannosaurus rex |	1
| dilophosaurus |	2
| parasaurolophus |	4
| gallimimus |	12
| velociraptor |	4

## Part 2: Exercises with Functions
This section will give you some practice with defining and invoking functions. Once complete, your output should look like:
```
=== 1 ===
Wednesday!
nice job!
=== 2 ===
progress?
almost done with part 2??
=== 3 ===
fun
Monday updates
```

## Working with the feed
From th next part in the assignment, we will be working with hw2-feedprocessor.py, which we will use to process the feed in hw2feed.txt. You may also want to open the feed to get a sense of it. 

## Part 3: fieldType() function
In hw2feed.txt, note that there are both posts and replies in this feed. There are also posters. These lines each start with `post:`, `reply:`, and `from:` respectively.

You are probably thinking "it would be really helpful if we had a function that I could use to figure out which type of content a line contains." The good news is that now you will write one. Find the part 3 line in `hw2-feedprocessor.py`. We have included some starter code to define a function `fieldType()`. This function should take a line as a parameter and return the field type (either post, reply, or from).

Note that you will get an error if you run the test code before you fill in `fieldType()`. Once it works, you should get:

```
== part 3 ==
from
post
reply
```

## Part 4: Total number of posts and replies
Find and print the total number posts and replies in the file. Print it as

```
Total posts: <number>
Total replies: <number>
```

## Part 5: Printing posting users
Your next task is to print who posted each post from the Slack channel. See the file for more details.
The first part of the of part 4 should look like (It’s a long list, so I have clipped it!):  

```
Sean Munson
Sean Munson
Jungeun Choi
Sean Munson
Travis Neils
Travis Neils
Travis Neils
Jordan Yoon-Buck
Sean Munson
Sean Munson
Sean Munson
Sean Munson
Sean Munson
```

## Part 6: Counting poster contribution frequency
Your next task in `hw2-feedprocessor.py` is to count how often each user posts or replies to the channel. You will need to use a dictionary to keep a running count of how many times each user posted or replied (a combined count for each) to the channell:
*	The starter code begins by creating an empty dictionary, called pr_count. Note that you will need to open the file again, because looping through its lines in Part 5 will have “consumed” those lines. 
*	Once you’ve extracted a user name (the same thing that you printed out in part 4), think of it as a key in the dictionary, whose value is the number of posts encountered by that user so far. If the key is not in the dictionary, set the value to 1. If the key is already in the dictionary, set its value to 1 more than its current value. (In the language of the accumulation pattern, the count is our accumulator variable for that user.) Hint: You have to handle when you have not seen that user before. You can do that with either `.get()` or with if/else statements. This is your choice.
*	Once your program finishes reading through the file, print how many times each user posted or replied. To do this, create a string of the form: `<name>: <X>`, where <name> is the user’s name, and X is the number of times they posted and replied. (See example screenshot for what it should look like.). Print that string.

The output of part 6 should look like the following, though your usernames may be in different order (recall that dictionaries are in arbitrary order!): 
```
== part 6 ==
== 6a ==
Sean Munson: 11
Jungeun Choi: 1
Travis Neils: 3
Jordan Yoon-Buck: 1
```
 
Then, print the number of unique posters/commenters:
```
4 unique posters
```

## Part 7: Counting word frequency in posts
For part 7, we will count the word frequency in posts (not replies!) to the Slack channel. For this part:
*	Use `stripWordPunctuation()` to remove punctuation from each word. This function will only work if you pass it a word (i.e., not a line).
*	Convert all text to lower case before counting.
* Print only words that appear at least three times.

Put your code in hw2-feedprocessor.py. 

Example output below. It has been trimmed and yours may be in a different order.

```
== part 7 ==
hi: 3
1: 3
it: 10
would: 3
if: 6
we: 4
do: 3
a: 8
with: 3
but: 3
i: 8
to: 21
students: 3
one: 3
you: 17
just: 3
2: 3
should: 5
have: 5
...
```

Note that, depending how you remove punctuation, you *may* have a blank entry. That's okay! So is getting rid of it. Numbers will also count as words.

## Part 8: Counting word frequency in posts or replies
For this part, write a function, `wordFreq()`, that will return the word frequency in either posts or replies as a dictionary
As parameters, it must take a file name and the field type (either post or replies) as a parameter. For example, if I want to get a dictionary of word counts in the posts in hw2feed.txt, I should be able to call:
`wordFreq('hw2feed.txt','post')`

You can use your code from part 7 as a starting point, or if you wrote part 6 using a function, you may simply edit it to meet the requirements for this part.

There are a few lines of code at the end that you can use to test your function. If all goes well, you’ll get:

```
Looks like wordFreq() works fine for posts
Looks like wordFreq() works fine for replies
```

If you are getting errors, check -- in particular -- that you have converted to lowercase, removed punctuation, and removed whitespace.

## P0: Identify an API
Please see a separate assignment on Canvas -> Assignments -> Project (to be introduced in class on Wednesday).

## Just For Fun
Remember, you don’t have to do this. Modify your code from the feed processor to:
1. Separately keep track of replies and posts per user. 
2. For an extra challenge, print the users in alphabetical order by name. 
3. Extra extra challenge: print users by post count, from most to least (we’ll be doing this in future homeworks, so even if you don’t do it – spend a few minutes thinking about what you would need to do).
