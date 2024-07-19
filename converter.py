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

def format_input(rawdict):
    title = "<h2 id='title'>"
    author = "<h3 id='author'> "
    tags = "<p id='tags'>"
    preview = "<p id='preview'>"
    img = '<img id="article-thumbnail"'
    content = ""

    title += rawdict["title"] + "</h2>"
    author += rawdict['author'] + "</h3>"
    tags += rawdict["tags"] + "</p>"
    img += " src='" + rawdict['image'] + "'>"
    preview += rawdict['preview'] + "</p>"
    content += "<p>" + convert_markdown(rawdict['content']) + "</p>"
    
    final_html = f"""<!doctype html>
<html>
    <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Moroccan History Hub</title>
    <link rel="stylesheet" type="text/css" href="../../static/styles.css">
    
    </head>
    <body>
        <nav>
            <div class="logo">
                <img src="../assets/logo-white.svg" alt="Logo">
                <h1>Moroccan History Hub</h1> 
            </div>
            <ul class="nav-links">
                <li><a href="{{ url_for('index')}}">HOME</a></li>
                <li><a href="../about.html">ABOUT</a></li>
                <li><a href="#">ARTICLES</a></li>
            </ul>
        </nav>
        <div class="articletxt">
            <div class="main-article">
                {title}
                {author}
                {tags}
                {preview}
                {img}
                {content}
            </div>
        </div>
        <footer>
            <div class="social-icons">
                <a href="#" aria-label="Facebook"><img src="../assets/facebook-logo.png"></a>
                <a href="#" aria-label="YouTube"><img src="../assets/youtube-logo.png"></a>
            </div>
            <div class="credits">
                Moroccan History Hub, 2024.
            </div>
        </footer>
    </body>
</html>
"""
    return final_html