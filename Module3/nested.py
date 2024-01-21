"""nested.py"""

cat = "harvest"
hunger_level = 25

if cat == "harvest":
    if hunger_level > 100:
        print("MEOW!")
    else:
        print("meow")  # printed
else:
    print("purr")
