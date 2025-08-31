from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def risk_calculator():
    risk_level = None
    likelihood = 0
    impact = 0

    if request.method == "POST":
        # Collect all values
        factors = [int(value) for value in request.form.values()]

        # First 8 = Likelihood, Last 8 = Impact
        likelihood = sum(factors[:8]) / 8
        impact = sum(factors[8:]) / 8

        risk_score = (likelihood + impact) / 2

        if risk_score < 3:
            risk_level = "Low"
        elif risk_score < 6:
            risk_level = "Medium"
        elif risk_score < 9:
            risk_level = "High"
        else:
            risk_level = "Critical"

    return render_template("index.html", risk=risk_level, likelihood=likelihood, impact=impact)

if __name__ == "__main__":
    app.run(debug=True)
