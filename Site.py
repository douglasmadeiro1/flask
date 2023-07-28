from flask import Flask, render_template

app = Flask(__name__)

# primeira pagina
# route -> siteflask.com/homepage
# função -> o que exibir naquela pagina

@app.route("/")
def homepage():
    return render_template("home.html")


# colocar o site no ar 
if __name__ == "__main__":
    app.run(debug=True)