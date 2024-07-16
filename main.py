from flask import Flask, render_template, abort
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import os
import re

articles_data = {}

html_files = [f for f in os.listdir('templates/publications') if f.endswith('.html')]

options = webdriver.ChromeOptions()
options.add_argument('--headless="new"')
driver = webdriver.Chrome(options=options)
for g in html_files:
    script_directory = os.path.dirname(os.path.realpath(__file__))
    script_directory = script_directory.replace("\\","/")
    full_url = f"{script_directory}/templates/publications/{g}"
    driver.get(full_url)
    try:
        #title
        element_title = driver.find_element(By.ID, "title")
        element_title_text = element_title.text
        #author
        element_author = driver.find_element(By.ID, "author")
        element_author_text = element_author.text
        #tags
        element_tags = driver.find_element(By.ID, "tags")
        element_tags_text = element_tags.text
        element_tags_text = element_tags_text.split(',')
        #preview
        element_preview = driver.find_element(By.ID, "preview")
        element_preview_text = element_preview.text
        #img
        element_img = driver.find_element(By.ID, "article-thumbnail")
        element_img_src = element_img.get_attribute("src")

        match = re.search(r"static/.*", element_img_src)
        if match:
            element_img_src_final = match.group()
        else:
            element_img_src_final = ""

        articles_data[g] = {}
        articles_data[g]["title"] = element_title_text
        articles_data[g]["author"] = element_author_text
        articles_data[g]["tags"] = element_tags_text
        articles_data[g]["preview"] = element_preview_text
        articles_data[g]["image"] = element_img_src_final
    except NoSuchElementException:
        print(f"This page is incomplete: {full_url}")
        continue  # Skip to the next page

driver.quit()

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/')
def index():
    return render_template('index.html', css="static/styles.css", articles_data=articles_data)

@app.route('/articles')
def articles():
    return render_template('articles.html', css="static/styles.css")

@app.route('/admin')
def admin():
    return render_template('admin.html', css="static/admin.css")

@app.route('/admin/create')
def create():
    return render_template("create.html", css="static/admin.css")


def generate_article_route(filename):
    def render_article():
        if filename in html_files:
            return render_template(f'publications/{filename}', css="static/styles.css")
        else:
            abort(404)
    return render_article

# Dynamically create routes for each HTML file
for x in html_files:
    route = f"/articles/{x}"
    endpoint = f"article_{x.replace('.html', '')}"
    app.add_url_rule(route, endpoint, generate_article_route(x))

if __name__ == '__main__':
    app.run(debug=True)

#reload comment : aa