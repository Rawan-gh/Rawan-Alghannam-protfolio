from flask import Flask, render_template

app = Flask(__name__)
projects = [{
    'id':
    1,
    'project':
    'Web Scrapping',
    'skills':
    'urllib python , Python Requests ,Selenium,Beautiful Soupe'
}, {
    'id': 2,
    'project': 'AI model for flare mointoring',
    'skills': 'Python Pandas, matblotlib, microsoft azure, Pychatgpt'
}, {
    'id': 3,
    'project': 'AI model for flare mointoring',
    'skills': 'Python Pandas, matblotlib, microsoft azure, Pychatgpt'
}]


@app.route('/')
def hello_world():
  return render_template('home.html', myskills=projects, myname = 'Rawan Alghannam')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=True)  #run flask server
