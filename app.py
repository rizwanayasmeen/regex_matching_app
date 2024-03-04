from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/results", methods=["POST"])
def results():
    test_string = request.form.get("test_string")
    regex_pattern = request.form.get("regex_pattern")

    # Perform regex matching
    matched_strings = re.findall(regex_pattern, test_string)

    return render_template("index.html", test_string=test_string, regex_pattern=regex_pattern, matched_strings=matched_strings)


@app.route("/email_validation")
def email_validation():
    return render_template("email_validation.html")


@app.route("/validate_email", methods=["POST"])
def validate_email():
    email = request.form.get("email")

    # Perform email validation
    is_valid_email = re.match(r'[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z]+', email) is not None

    return render_template("email_validation.html", email=email, is_valid_email=is_valid_email)



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
