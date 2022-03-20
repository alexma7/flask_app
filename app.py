import flask #, request, render_template, jsonify
#from flask.wrappers import Response
#from py.prime import makePrime
#from galton import galtonboard
#import git # GitPython library
#import os

app = flask.Flask(__name__)

#Route for the GitHub webhook
# @app.route('/git_update', methods=['POST'])
# def git_update():
#   repo = git.Repo('./flask_app')
#   origin = repo.remotes.origin
#   repo.create_head('main', 
#   origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
#   origin.pull()
#   return '', 200

@app.route("/")
def hello_world():
    return flask.render_template('index.html')

@app.route("/about")
def about():
    return flask.render_template('about.html')

@app.route("/welcome")
def welcome():
    weeks = 5
    course = 'Flask'
    group = 'ПО-09'
    return flask.render_template(
        'welcome.html', 
        weeks=weeks,  
        course=course, 
        group=group
    )

@app.route('/students/<int:student_id>')
def students(student_id):
    students = {
      1: 'Петров Иван Иванович',
      2: 'Иванов Иван Иванович',
      3: 'Сидоров Иван Иванович',
      4: 'Кукухин Иван Иванович',
    }
    student_name = students.get(student_id)
    if student_name is None:
        flask.abort(404)
    return flask.render_template('students.html', student_name=student_name)

if __name__ == '__main__':
  app.run(debug=True)
 
