from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
 {
  "id": 1,
  "title": "Data Analyst",
  "location": "Mwanza, Tanzania",
  "salary": "Tshs 2,000,000"
 },
 {
  "id": 2,
  "title": "UI/UX designer",
  "location": "Arusha, Tanzania",
  "salary": "Tshs 3,000,000"
 }, 
 {
  "id": 3,
  "title": "Full-stack developer",
  "location": "Dar es salaam, Tanzania",
  "salary": "Tshs 2,500,000"
 },
 {
  "id": 4,
  "title": "Database manager",
  "location": "Mwanza, Tanzania",
  "salary": "Tshs 2,000,000"
 },
]

@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name="Dabo")

@app.route("/api/jobs")
def list_jobs():
  return jsonify (JOBS)



if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)