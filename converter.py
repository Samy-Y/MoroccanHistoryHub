markdown = "## aa \n* Abab ## bb"
print(markdown)

md = {}

for i in markdown.index("##"):
    md["h2"] = markdown[i,markdown.index("\n")]

md["h2"] = markdown[markdown.index("##"),markdown.index("\n")]

print("Final result:\n"+md)