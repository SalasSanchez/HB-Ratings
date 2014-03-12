from flask import Flask, render_template, redirect, request, flash, session
import model
app = Flask(__name__)
app.secret_key = 'Thisisnotasecretkey'

@app.route("/")
def index():
    user_list = model.session.query(model.User).limit(5).all()
    return render_template("user_list.html", users=user_list)


@app.route("/signup")
def signup():
	html = render_template("signupform.html")
	return html

@app.route("/signup_complete", methods=['POST'])
def signup_complete():
	email =request.form.get('email')
	#print "EMAIL", email
	age = request.form.get('age')
	#print "AGE", age
	zipcode = request.form.get('zipcode')
	#print "ZIPCODE", zipcode
	password = request.form.get('password')
	#print "PASSWORD", password

	existing_users = model.session.query(model.User).filter_by(email=email).all()
	# print "EXISTING USERS", existing_users

	if existing_users == []:
		u = model.User(email=email, age=age, zipcode=zipcode, password=password)
		model.session.add(u)
		model.session.commit()
		flash("User created")
		return "User created"
		# return render_template("signup_complete.html", email=email, 
		# 							  age=age,  #also include message in the html not pass it
		# 							  zipcode=zipcode, 
		# 							  password=password)
	else:
		#flash("This user is already in the database")
		#return render_template("signupform.html")
		return "This user is already in the database"



@app.route("/login")
def log_in():
	return render_template("loginpage.html")

@app.route("/login", methods=['POST'])
def log_in_user():
	email = request.form.get('email')
	password = request.form.get('password')

	user = model.session.query(model.User).filter_by(email=email).one()

	if password == user.password:
		session['user.id']= user.id
		return "You're logged in"
	else:
		return "Incorrect password. Please, try again"



@app.route("/all_users")   #view a list of all users
def all_users():
	all_users = model.session.query(model.User).all()  

	return render_template("all_users.html", all_users=all_users)
	
	

#click on a user and view the list of movies they've rated, 
#as well as the ratings
@app.route("/ratings_by_user")
def ratings_by_user():
	user = request.args.get('user')
	movies_list= model.session.query(model.Rating).filter_by(user_id=user).all()
	return render_template("ratings_by_user.html", movies_list=movies_list)  #or feed user_id=user as an argument directly



#We should be able to, when logged in and viewing a record for a movie, 
#either add or update a personal rating for that movie.




if __name__ == "__main__":
	app.run(debug= True)