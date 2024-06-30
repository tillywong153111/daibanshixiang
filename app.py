# app.py
from flask import Flask, render_template
import requests
from markdown2 import markdown

app = Flask(__name__)

@app.route("/")
def index():
    github_url = "https://raw.githubusercontent.com/tillywong153111/recordeverything/master/待办事项.md"
    response = requests.get(github_url)

    if response.status_code == 200:
        md_content = response.text
        html_content = markdown(md_content)
    else:
        html_content = "<p>无法加载数据，请稍后再试。</p>"

    return render_template("index.html", content=html_content)

if __name__ == "__main__":
    app.run(debug=True)
