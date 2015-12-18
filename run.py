from flask import Flask, render_template, url_for
from app import app
from app import views


if __name__ == '__main__':
    app.run(debug=True)

