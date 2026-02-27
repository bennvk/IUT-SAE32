"""Flask web application for document search."""

from flask import Flask, render_template, request
from search_engine import search_in_directory
from config import SERVER_HOST, SERVER_PORT

app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)

@app.route("/", methods=["GET", "POST"])
def index():
    grouped_results = {}
    total_matches = 0
    total_files = 0

    if request.method == "POST":
        keyword = request.form.get("keyword")
        grouped_results, total_matches, total_files = search_in_directory(keyword)

    return render_template(
        "index.html",
        results=grouped_results,
        total_matches=total_matches,
        total_files=total_files
    )


if __name__ == "__main__":
    app.run(host=SERVER_HOST, port=SERVER_PORT, debug=True)