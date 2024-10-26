from flask import render_template, request, redirect
import csv
from profile.reader import read_cities

def setup_routes(app):
    @app.route("/", methods=["GET", "POST"])
    def submit_form():
        cities = read_cities()  # Get cities from the Excel file
        if request.method == "POST":

            name = request.form["name"]
            city_id = request.form["city_id"]

            with open("user_profiles.csv", mode="a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([name, city_id])
            return redirect("/")
        return render_template("form.html", cities=cities)