import os
from dotenv import load_dotenv
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    send_from_directory,
)

load_dotenv()
print(f"FLASK_APP: {os.environ.get('FLASK_APP')}")
print(f"FLASK_ENV: {os.environ.get('FLASK_ENV')}")
print(f"TEST_BOTH: {os.environ.get('TEST_BOTH')}")
print(f"FLASK_DEBUG: {os.environ.get('FLASK_DEBUG')}")
print(f"FLASK_RUN_HOST: {os.environ.get('FLASK_RUN_HOST')}")
print(f"FLASK_RUN_PORT: {os.environ.get('FLASK_RUN_PORT')}")

page_title = "Hello World"
page_subtitle = "Well hello, wonderful world!"
app = Flask(__name__)
app_static_url_path = app.static_url_path
app_static_folder = app.static_folder
print(f"app: {app}")
# print(f"app.config: {app.config}")
print(f"app.debug: {app.debug}")
print(f"app.static_url_path: {app.static_url_path}")
print(f"app.static_folder: {app.static_folder}")


@app.route("/")
def root() -> "html":
    return render_template(
        "index.html",
        page_title=page_title,
        page_subtitle=page_subtitle,
        app_static_url_path=app_static_url_path,
        app_static_folder=app_static_folder,
    )


# If module name: app.py
# When starting with 'python app.py' __name__ is "__main__"
# When starting with 'flask run' __name__ is "app"

# If module name: hello.py
# When starting with 'python hello.py' __name__ is "__main__"
# When starting with 'FLASK_APP=hello flask run' __name__ is "hello"

# Start the Flask app if the current, active module is __main__.
print(f"__name__: {__name__}")
if __name__ == "__main__":
    print(
        f"Running app on host {os.environ.get('FLASK_RUN_HOST')} on port {os.environ.get('FLASK_RUN_PORT')}"
    )
    # app.run(debug=True)
    # app.run()
    # app.run(port=os.environ.get('FLASK_RUN_PORT'))
    app.run(
        host=os.environ.get("FLASK_RUN_HOST"), port=os.environ.get("FLASK_RUN_PORT")
    )
