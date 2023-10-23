## Pizza Order

# Instructions

Small Pizza: $15
Mediun Pizza: $20
Large Pizza: $25
Pepperoni for small pizza: +$2
Pepperoni for Medium or Large Pizza: +$3
Extra cheese for any size pizza: +$1

## Love Calculator

# Instructions

Write a program that tests the compatibility between two people.
Use the super scientific method recommended by BuzzFeed.

To work out the love score between two people:

> **_Take both people's names and check for the number of times the letters in the word_** >**_True occurs. Then check for the number of times the letters in the word LOVE occurs._** >**_Then combine these numbers to make a 2 digit number._**

For love Scores **less than 10** or **greater than 90**, the message should be:
"Your score is x, you go together like coke and mentos."

For Love Score **between 40** and **50**, the mesage should be:
"Your score is **y,** you are alright together."

Otherwise the message will just be their score e.g.
"Your score is **z.**"

hint:

1. The lower() function changes all the letters ina string to lower case.
   https://stackoverflow.com/questions/6797984/how-do-i-lowercase-a-string-in-python

2. The count() function will give you the number of times a letter occurs in a string.
   https://stackoverflow.com/questions/1155617/count-the-number-of-occurrences-of-a-character-in-a-string
