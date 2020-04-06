Step 1:

MENU
sandwiches:
  Chang's Veggie Delight: Swiss Cheese and avocado, with mayo, tomato, lettuce, onion, carrot, and cucumber.
  BLT: Lettuce, Tomatoes, Bacon.
  Black Forest Ham: Lettuce, Tomatoes, Cucumbers, Green Peppers, Red Onions, Spinach, Black Forest Ham.
  Chicken Caesar Melt: Provolone, Tomatoes, Red Onions, Spinach, Caesar, Rotisserie-Style Chicken.
breads: rye, wheat, Italian, 9-Grain
spreads: cheese, butter, mayonnaise(mayo), mustard
options: 6 inches/1-foot(12 inches), toasted or not, double spreads
exceptions: no onions, hold the mayo, no tomatoes

DEFAULT SERVINGS
Chang's Veggie Delight: Italian, mayo, 6 inches, non toasted, no exceptions
BLT: Italian, butter, 6 inches, non toasted, no exceptions
Black Forest Ham: 9-Grain, mayo, 6 inches, non toasted, no exceptions
Chicken Caesar Melt: Italian, mayo, 6 inches, non toasted, no exceptions

Step2:

The list of terms you treat as equivalent:
["Chang's Veggie Delight", "CVD", "C.V.D.", "Chang's", "Changs", "Veggie", "Veg", "Vegetarian", "Veggie Delight"]
["BLT", "B.L.T."]
["Black Forest Ham", "BFH", "B.F.H.", "Black Forest"]
[ "Chicken Caesar Melt", "CCM", "C.C.M.", "Chicken Caesar"]
["rye"]
["wheat"]
["Italian", "Italy", "Italy's"]
[ "9-Grain", "Grain", "nine_Grain", "Grain-9", "Grain9"]
[ "cheese", "cheeses"]
["butter"]
["mayo", "mayonnaise"]
["mustard", "mustards"]

The list of terms like “Please” etc. that you will ignore.
{"please", "thank you", "thanks", "i'd like", "i would like",  "i would like to",
                 "i want", "i want to ", "i need", "i need to", "hi", "how are you", "hello",
                 "hey", "what's up", "could i please", "could i have", "may i", "could i"}

The different ways you will allow customers to specify exceptions like “Hold the mayo”.
hold the mayo
I don't want the mayo
I do not want mayo
I do not need mayo
no mayo
without mayo
leave the mayo
remove the mayo

Step 3:

Language:
Python

How to run?
Just run sandwich.py directly.

Files:
sandwich.py    main program. Parse user input and print order detail.
constants.py   all the constants used while parsing user input.

Step 4:

Example 1:
hello, what do you want to eat today?
>>>hi how are you, can i see the menu?
MENU
sandwiches:
  Chang's Veggie Delight: Swiss Cheese and avocado, with mayo, tomato, lettuce, onion, carrot, and cucumber.
  BLT: Lettuce, Tomatoes, Bacon.
  Black Forest Ham: Lettuce, Tomatoes, Cucumbers, Green Peppers, Red Onions, Spinach, Black Forest Ham.
  Chicken Caesar Melt: Provolone, Tomatoes, Red Onions, Spinach, Caesar, Rotisserie-Style Chicken.

breads: rye, wheat, Italian, 9-Grain

spreads: cheese, butter, mayonnaise(mayo), mustard

options: 6 inches/1-foot(12 inches), toasted or not, double spreads

exceptions: no onions, hold the mayo, no tomatoes

Hi, here is the menu, what do you want to eat?
>>>ok, I want to eat Veggie with rye, with mayo on it and please give me 12 inches one, non toasted.
Also without onions, thank you!
Order detail:

1. Sandwich: Chang's Veggie Delight

2. Usual ingredients: Swiss Cheese and avocado, with mayo, tomato, lettuce, onion, carrot, and cucumber

3. Bread-type: rye

4. Spreads: mayonnaise

5. Options: 12 inches,non toasted

6. Exceptions: no onion


Irrelevant exceptions:

Hi, is this what you are ordering? Press enter to confirm.
Otherwise, enter one of 1,3,4,5,6 and reenter.


Thank you for ordering! Please stand by, your sandwich is coming soon!

Example 2:
hello, what do you want to eat today?
>>>hi what are my choices?
MENU
sandwiches:
  Chang's Veggie Delight: Swiss Cheese and avocado, with mayo, tomato, lettuce, onion, carrot, and cucumber.
  BLT: Lettuce, Tomatoes, Bacon.
  Black Forest Ham: Lettuce, Tomatoes, Cucumbers, Green Peppers, Red Onions, Spinach, Black Forest Ham.
  Chicken Caesar Melt: Provolone, Tomatoes, Red Onions, Spinach, Caesar, Rotisserie-Style Chicken.

breads: rye, wheat, Italian, 9-Grain

spreads: cheese, butter, mayonnaise(mayo), mustard

options: 6 inches/1-foot(12 inches), toasted or not, double spreads

exceptions: no onions, hold the mayo, no tomatoes

Hi, here is the menu, what do you want to eat?
>>>emm, i WANT BLT with cheese, 6-inches and please hold the mayo. Thank you
Either bread not found or not specified. This sandwich usually comes with Italian bread. Press return to accept
this choice of bread, or choose one of the other alternatives:
1. rye bread.
2. wheat bread.
3. 9-Grain bread.
>>>2
Order detail:

1. Sandwich: BLT

2. Usual ingredients: Lettuce, Tomatoes, Bacon

3. Bread-type: wheat

4. Spreads: cheese

5. Options: 6 inches,non toasted

6. Exceptions:

Irrelevant exceptions: These are invalid exceptions. Either it can not be removed or we didn't add it in the
 food in the first place:
no mayo


Hi, is this what you are ordering? Press enter to confirm.
Otherwise, enter one of 1,3,4,5,6 and reenter.


Thank you for ordering! Please stand by, your sandwich is coming soon!

Example 3:
hello, what do you want to eat today?
>>>hi give me Chicken Caesar Melt with Italian bread. double spread and no Tomatoes please.
Either spread not found or not specified. This sandwich usually comes with mayonnaise spread. Press return
to accept this choice of spread, or choose one of the other alternatives:
1. cheese spread.
2. butter spread.
3. mustard spread.

Order detail:

1. Sandwich: Chicken Caesar Melt

2. Usual ingredients: Provolone, Tomatoes, Red Onions, Spinach, Caesar, Rotisserie-Style Chicken

3. Bread-type: Italian

4. Spreads: mayonnaise

5. Options: 6 inches,non toasted, double spread

6. Exceptions: no tomato


Irrelevant exceptions:

Hi, is this what you are ordering? Press enter to confirm.
Otherwise, enter one of 1,3,4,5,6 and reenter.

>>>6
Please input new exceptions, including:
no onions, hold the mayo, no tomatoes.
>>>no onions, and no apples, no bananas
Order detail:

1. Sandwich: Chicken Caesar Melt

2. Usual ingredients: Provolone, Tomatoes, Red Onions, Spinach, Caesar, Rotisserie-Style Chicken

3. Bread-type: Italian

4. Spreads: mayonnaise

5. Options: 6 inches,non toasted, double spread

6. Exceptions: no onion


Irrelevant exceptions: These are invalid exceptions. Either it can not be removed or we didn't add
 it in the food in the first place:
no apples
no bananas


Hi, is this what you are ordering? Press enter to confirm.
Otherwise, enter one of 1,3,4,5,6 and reenter.

>>>3
Please choose a new bread type:
rye
wheat
Italian
9-Grain
>>>wheat
Order detail:

1. Sandwich: Chicken Caesar Melt

2. Usual ingredients: Provolone, Tomatoes, Red Onions, Spinach, Caesar, Rotisserie-Style Chicken

3. Bread-type: wheat

4. Spreads: mayonnaise

5. Options: 6 inches,non toasted, double spread

6. Exceptions: no onion


Irrelevant exceptions: These are invalid exceptions. Either it can not be removed or we didn't add it in the 
food in the first place:
no apples
no bananas


Hi, is this what you are ordering? Press enter to confirm.
Otherwise, enter one of 1,3,4,5,6 and reenter.


Thank you for ordering! Please stand by, your sandwich is coming soon!

Example 4:

Below is an example of ordering Meatball Marinara(which we don't serve).
The system ask the user to re-choose a sandwich and all the other requests are reserved.
Also user can modify the order during the confirming period.

hello, what do you want to eat today?
>>>what's on the menu
MENU
sandwiches:
  Chang's Veggie Delight: Swiss Cheese and avocado, with mayo, tomato, lettuce, onion, carrot, and cucumber.
  BLT: Lettuce, Tomatoes, Bacon.
  Black Forest Ham: Lettuce, Tomatoes, Cucumbers, Green Peppers, Red Onions, Spinach, Black Forest Ham.
  Chicken Caesar Melt: Provolone, Tomatoes, Red Onions, Spinach, Caesar, Rotisserie-Style Chicken.

breads: rye, wheat, Italian, 9-Grain

spreads: cheese, butter, mayonnaise(mayo), mustard

options: 6 inches/1-foot(12 inches), toasted or not, double spreads

exceptions: no onions, hold the mayo, no tomatoes

Hi, here is the menu, what do you want to eat?
>>>Meatball Marinara with cheese and 9-grain. Without tomatoes
Sandwich not found, please reenter:
Chang's Veggie Delight: Swiss Cheese and avocado, with mayo, tomato, lettuce, onion, carrot, and cucumber.
BLT: Lettuce, Tomatoes, Bacon.
Black Forest Ham: Lettuce, Tomatoes, Cucumbers, Green Peppers, Red Onions, Spinach, Black Forest Ham.
Chicken Caesar Melt: Provolone, Tomatoes, Red Onions, Spinach, Caesar, Rotisserie-Style Chicken.
>>>BFH
Order detail:

1. Sandwich: Black Forest Ham

2. Usual ingredients: Lettuce, Tomatoes, Cucumbers, Green Peppers, Red Onions, Spinach, Black Forest Ham

3. Bread-type: 9-Grain

4. Spreads: cheese

5. Options: 6 inches,non toasted

6. Exceptions: no tomato


Irrelevant exceptions:

Hi, is this what you are ordering? Press enter to confirm.
Otherwise, enter one of 1,3,4,5,6 and reenter.

>>>5
Please input new customized options, including:
6 inches/1-foot(12 inches), toasted or not, double spreads.
>>>12-inches 2x spread
Order detail:

1. Sandwich: Black Forest Ham

2. Usual ingredients: Lettuce, Tomatoes, Cucumbers, Green Peppers, Red Onions, Spinach, Black Forest Ham

3. Bread-type: 9-Grain

4. Spreads: cheese

5. Options: 12 inches,non toasted, double spread

6. Exceptions: no tomato


Irrelevant exceptions:

Hi, is this what you are ordering? Press enter to confirm.
Otherwise, enter one of 1,3,4,5,6 and reenter.


Thank you for ordering! Please stand by, your sandwich is coming soon!

Step 5:
a. the easiest part is to design the sentences that the system give to users.
b. the hardest part is to think of strategies of how to use re module to do regex matching and how to handle
options and exceptions and irrelevant requests from user. Also it is a little difficult to design the
"confirm" logic.
c. NLP is difficult even with simplest regex method.