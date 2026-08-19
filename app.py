from flask import Flask, request, render_template
import joblib

# Create Flask app
app = Flask(__name__, static_folder="static", template_folder="templates")

# Load trained model
model = joblib.load("boston_prediction")


# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Prediction Route
@app.route("/index", methods=["POST"])
def get_values():
    try:
        rm = float(request.form.get("rm"))
        pt = float(request.form.get("pt"))
        lstat = float(request.form.get("lstat"))

        prediction = model.predict([[rm, pt, lstat]])[0]

        return render_template(
            "result.html",
            prediction=round(prediction, 2),
            rm=rm,
            pt=pt,
            lstat=lstat
        )

    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    app.run(debug=True)