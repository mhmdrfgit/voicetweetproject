# Raihana_blog
Specification:

  python 3.9.7
  
  django 4.0.4
  
  db: postgre sql
  sso: google authentication

Application Setup


1. Clone the repository

2. Create a virtual environment to install dependencies in and activate it

3. Then install the dependencies:

  (env)$ pip install -r requirements.txt

  - Note the (env) in front of the prompt. This indicates that this terminal session operates in a virtual environment.

  - Once pip has finished downloading the dependencies:

  (env)$ cd project

  (env)$ python manage.py runserver
  
 4. Configure the database in settings.py
 
 5. do migraions

 6. And navigate to http://127.0.0.1:8000/




# Home 

url = http://127.0.0.1:8000/

View list of all the posts created by all the users

Navigation bar - Home,About,Login,Register


# Login
login with google
or login with credentials creted while registering 

# Register

Register page is for adding a new user. Once we head to the register page,
we need to enter the username, emailid and password then on clicking the sign up
button, the user will be registered

# View/Update Profile (logged in users)
Click on Profie link in the navigation bar.
Profile page contains the details about the user.
We can update in the emailid, username and the profile picture of the logged in user from profile page.

# Create Tweet (logged in users)
The page will have the forms to be filled to create a new blog.It includes title, voice file and a tweet button

# Add Comment(logged in users)
add comment under the associated tweet 


# Logout

CLock on logout nav-link to logout user.

# Admin page:
Create a super user from the shell
python manage.py createsuperuser

provide the username and password and go to the below url

http://localhost:8000/admin

-Admin can create/update/delete users,posts etc
  
  
  
  



