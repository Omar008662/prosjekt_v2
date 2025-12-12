from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

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
    if request.method == "POST":
        navn = request.form["navn"]
        brus = request.form["brus"]
        antall = int(request.form.get("antall", 1))

        conn = sqlite3.connect("bestillinger.db")
        c = conn.cursor()
        c.execute("INSERT INTO bestilling (navn, brus, antall) VALUES (?, ?, ?)", (navn, brus, antall))
        conn.commit()
        conn.close()

        return redirect("/")

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

    return render_template("index.html", bestillinger=bestillinger)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
