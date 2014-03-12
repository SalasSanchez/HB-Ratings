from flask import Flask, render_template, redirect, request, flash
import model
app = Flask(__name__)

@app.route("/")
def index():
    user_list = model.session.query(model.User).limit(5).all()
    return render_template("user_list.html", users=user_list)


@app.route("/signup")
def signup():
	html = render_template("signup.html")
	return html




	# email =request.form('email')
	# age = request.form('age')
	# zipcode = request.form('zipcode')
	# password = request.form('password')

	# model.User(email=email, age=age, zipcode=zipcode, password=password)

	# return render_template("signup.html", email=email, 
	# 									  age=age, 
	# 									  zipcode=zipcode, 
	# 									  password=password)


# @app.route("/log_in")
# def log_in():
# 	pass


# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if valid_login(request.form['username'],
#                        request.form['password']):
#             return log_the_user_in(request.form['username'])
#         else:
#             error = 'Invalid username/password'
#     # the code below is executed if the request method
#     # was GET or the credentials were invalid
#     return render_template('login.html', error=error)


# @app.route("all_users")
#We should be able to view a list of all users



#We should be able to click on a user and view the list of movies they've rated, 
#as well as the ratings

#We should be able to, when logged in and viewing a record for a movie, 
#either add or update a personal rating for that movie.




if __name__ == "__main__":
	app.run(debug= True)