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
        elif "- " in x[0:2]:
            a = x.replace("- ","<li>")
            line_txt[i] = a + "</li>"
        # CUSTOM

        elif x.startswith("§TAGS§ "):
            a = x.replace("§TAGS§ ",'<p id="tags">')
            line_txt[i] = a + "</p>"
        elif x.startswith("§PREVIEW§ "):
            a = x.replace("§PREVIEW§ ",'<p id="preview">')
            line_txt[i] = a + "</p>"

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

def format_article(html):
    while "<h2" in html:
        html = html.replace("<h2",'<h2 id="title"',1)
    while "<h3" in html:
        html = html.replace("<h3",'<h3 id="author"',1)