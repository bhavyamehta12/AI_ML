from flask import Flask,render_template

app= Flask(__name__)

@app.route("/")
def student_profile():
    return render_template(
        "Profile.html",
        name="Arun",
        is_topoper=True,
        subjects=["Maths","science","History"]
    )
if __name__=="__main__":
    app.run(debug=True)