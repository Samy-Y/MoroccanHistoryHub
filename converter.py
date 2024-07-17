ab = """# The Humble Potato 🥔

Potatoes are one of the most versatile and widely consumed vegetables worldwide. Whether mashed, fried, or baked, they find their way into countless dishes. Let's explore some interesting facts about this humble tuber:

## Origins and History

- **Origin**: Potatoes (Solanum tuberosum) originated in the Andes region of South America, where they were cultivated by indigenous peoples thousands of years ago.
- **Introduction to Europe**: Spanish explorers brought potatoes to Europe in the 16th century. Initially met with suspicion, they eventually gained popularity due to their nutritional value and ability to thrive in various climates.

## Culinary Uses

- **Mashed Potatoes**: Creamy, __buttery__ mashed potatoes are a staple side dish in many cuisines.
- **French Fries**: Thinly sliced and deep-fried, French fries are beloved by people of all ages.
- **Baked Potatoes**: Baking potatoes in the oven results in a crispy skin and fluffy interior.
- **Potato Salad**: A refreshing *salad* made with boiled potatoes, herbs, and dressing.

## Nutritional Benefits

- Potatoes are an excellent source of vitamin C, potassium, and dietary fiber.
- They are naturally gluten-free and low in fat.
- However, avoid consuming green or sprouted potatoes, as they can contain toxic compounds.

Remember to enjoy your potatoes without moderation! 🌟
"""

def convert_markdown(txt):
    line_txt = txt.split("\n")

    for i,x in enumerate(line_txt):
        if "# " in x[0:2]:
            a = x.replace("# ","<h1>")
            line_txt[i] = a + "</h1>"
        elif "# " in x[0:3]:
            a = x.replace("## ","<h2>")
            line_txt[i] = a + "</h2>"
        elif "# " in x[0:4]:
            a = x.replace("### ","<h3>")
            line_txt[i] = a + "</h3>"
        elif "# " in x[0:5]:
            a = x.replace("#### ","<h4>")
            line_txt[i] = a + "</h4>"
        elif "* " in x[0:2]:
            a = x.replace("* ","<li>")
            line_txt[i] = a + "</li>"
        elif x.startswith("- "):
            a = x.replace("- ","<li>")
            line_txt[i] = a + "</li>"

    for i,x in enumerate(line_txt):
        if "**" in x:
            while "**" in x:
                x = x.replace("**", "<b>", 1)
                x = x.replace("**", "</b>", 1)
            line_txt[i] = x

    for i,x in enumerate(line_txt):
        if "__" in x:
            while "__" in x:
                x = x.replace("__", "<u>", 1)
                x = x.replace("__", "</u>", 1)
            line_txt[i] = x

    for i,x in enumerate(line_txt):
        if "*" in x and (x[x.index("*") + 1] != "*" or x[x.index("*") - 1] != "*"):
            while "*" in x:
                x = x.replace("*", "<i>", 1)
                x = x.replace("*", "</i>", 1)
            line_txt[i] = x

    return "\n".join(line_txt)