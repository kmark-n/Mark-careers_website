from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id':1,
    'title':'Data Scientist',
    'location':'Florida, USA'
  },
  {
    'id':2,
    'title':'Data Analyst',
    'location':'San Fransisco, USA'
  },
  {
    'id':3,
    'title':'Front-end developer',
    'location':'Mumbai, India'
  },
  {
    'id':4,
    'title':'Software Engineer',
    'location':'Atlanta, Georgia'
  }
]
@app.route("/")
def mark_careers():
  return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
  
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)