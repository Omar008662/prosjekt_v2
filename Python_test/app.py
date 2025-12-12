from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "superhemmelig"  # Trengs for session

# Opprett database dersom den ikke finnes
def init_db():
    conn = sqlite3.connect("bestillinger.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS bestilling (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            navn TEXT NOT NULL,
            brus TEXT NOT NULL,
            antall INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()

@app.route("/", methods=["GET", "POST"])
def index():
    if "handlekurv" not in session:
        session["handlekurv"] = []

    if request.method == "POST":
        brus = request.form["brus"]
        antall = int(request.form.get("antall", 1))
        # Legg til i handlekurv
        session["handlekurv"].append({"brus": brus, "antall": antall})
        session.modified = True  # Viktig, ellers oppdateres ikke session
        return redirect("/")

    return render_template("index.html", handlekurv=session["handlekurv"])

@app.route("/bestill", methods=["POST"])
def bestill():
    navn = request.form["navn"]
    handlekurv = session.get("handlekurv", [])

    if not handlekurv:
        return redirect("/")

    conn = sqlite3.connect("bestillinger.db")
    c = conn.cursor()
    for item in handlekurv:
        c.execute("INSERT INTO bestilling (navn, brus, antall) VALUES (?, ?, ?)",
                  (navn, item["brus"], item["antall"]))
    conn.commit()
    conn.close()

    # Tøm handlekurv
    session["handlekurv"] = []

    return redirect("/")

@app.route("/oversikt")
def oversikt():
    # Hent bestillinger og summer antall per person og brus
    conn = sqlite3.connect("bestillinger.db")
    c = conn.cursor()
    c.execute("""
        SELECT navn, brus, SUM(antall) as total
        FROM bestilling
        GROUP BY navn, brus
        ORDER BY navn
    """)
    bestillinger = c.fetchall()
    conn.close()
    return render_template("oversikt.html", bestillinger=bestillinger)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
