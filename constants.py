# to identify that the customer wants a menu
MENU_WORD = {"menu", "choices", "choice", "selections", "selection", "recommend", "recommendation",
             "recommendations", "have", "provide"}

# words to ignore
UNVALID_WORDS = {"please", "thank you", "thanks", "i'd like", "i would like",  "i would like to",
                 "i want", "i want to ", "i need", "i need to", "hi ", "hi,", "how are you", "hello",
                 "hey", "what's up", "could i please", "could i have", "may i", "could i"}

# menu content
MENU = """MENU
sandwiches:
  Chang's Veggie Delight: Swiss Cheese and avocado, with mayo, tomato, lettuce, onion, carrot, and cucumber.
  BLT: Lettuce, Tomatoes, Bacon.
  Black Forest Ham: Lettuce, Tomatoes, Cucumbers, Green Peppers, Red Onions, Spinach, Black Forest Ham.
  Chicken Caesar Melt: Provolone, Tomatoes, Red Onions, Spinach, Caesar, Rotisserie-Style Chicken.

breads: rye, wheat, Italian, 9-Grain

spreads: cheese, butter, mayonnaise(mayo), mustard

options: 6 inches/1-foot(12 inches), toasted or not, double spreads

exceptions: no onions, hold the mayo, no tomatoes
"""

# sandwiches and default servings
CVD = ("Chang's Veggie Delight", "Swiss Cheese and avocado, with mayo, tomato, lettuce, onion, carrot, and cucumber",
       "Italian", "mayonnaise")
BLT = ("BLT", "Lettuce, Tomatoes, Bacon", "Italian", "butter")
BFH = ("Black Forest Ham", "Lettuce, Tomatoes, Cucumbers, Green Peppers, Red Onions, Spinach, Black Forest Ham",
       "9-Grain", "mayonnaise")
CCM  = ("Chicken Caesar Melt", "Provolone, Tomatoes, Red Onions, Spinach, Caesar, Rotisserie-Style Chicken",
        "Italian", "mayonnaise")
SANDWICH_LIST = ["Chang's Veggie Delight: Swiss Cheese and avocado, with mayo, tomato, lettuce, onion,"
                 " carrot, and cucumber.", "BLT: Lettuce, Tomatoes, Bacon.", "Black Forest Ham: Lettuce, "
                "Tomatoes, Cucumbers, Green Peppers, Red Onions, Spinach, Black Forest Ham.",
                 "Chicken Caesar Melt: Provolone, Tomatoes, Red Onions, Spinach, Caesar, Rotisserie-Style Chicken."]
SANDWICHES = {"Chang's Veggie Delight": CVD,
              "CVD": CVD,
              "C.V.D.": CVD,
              "Chang's": CVD,
              "Changs": CVD,
              "Veggie": CVD,
              "Veg": CVD,
              "Vegetarian": CVD,
              "Veggie Delight": CVD,

              "BLT": BLT,
              "B.L.T.": BLT,

              "Black Forest Ham": BFH,
              "BFH": BFH,
              "B.F.H.": BFH,
              "Black Forest": BFH,

              "Chicken Caesar Melt": CCM,
              "CCM": CCM,
              "C.C.M.": CCM,
              "Chicken Caesar": CCM}

# breads
RYE = "rye"
WHEAT = "wheat"
ITALIAN = "Italian"
GRAIN9 = "9-Grain"
BREAD_LIST = [RYE, WHEAT, ITALIAN, GRAIN9]
BREADS = {
    "rye": RYE,

    "wheat": WHEAT,

    "Italian": ITALIAN,
    "Italy": ITALIAN,
    "Italy's": ITALIAN,

    "9-Grain": GRAIN9,
    "Grain": GRAIN9,
    "nine_Grain": GRAIN9,
    "Grain-9": GRAIN9,
    "Grain9": GRAIN9
}

# spreads
CHEESE = "cheese"
BUTTER = "butter"
MAYO = "mayonnaise"
MUSTARD = "mustard"
SPREAD_LIST = [CHEESE, BUTTER, MAYO, MUSTARD]
SPREADS = {
    "cheese": CHEESE,
    "cheeses": CHEESE,

    "butter": BUTTER,

    "mayo": MAYO,
    "mayonnaise": MAYO,

    "mustard": MUSTARD,
    "mustards": MUSTARD
}

# exceptions
EXCEs = ["onion", "mayo", "tomato"]

# prompts for irrelevant exceptions
IRRE_EXCE = "These are invalid exceptions. Either it can not be removed or we didn't add it " \
                   "in the food in the first place:\n"