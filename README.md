# Raihana_blog
Specification:

  python 3.9.7
  
  django 4.0.4

Application Setup


1. Clone the repository

2. Create a virtual environment to install dependencies in and activate it

3. Then install the dependencies:

  (env)$ pip install -r requirements.txt

  - Note the (env) in front of the prompt. This indicates that this terminal session operates in a virtual environment.

  - Once pip has finished downloading the dependencies:

  (env)$ cd project

  (env)$ python manage.py runserver

 4. And navigate to http://127.0.0.1:8000/

# Home 

url = http://127.0.0.1:8000/

View list of all the posts created by all the users

Navigation bar - Home,About,Login,Register


# Login
If already have an account, Enter username ,password and click on login

else click on Sign up now link below login button

# Register

Register page is for adding a new user. Once we head to the register page,
we need to enter the username, emailid and password then on clicking the sign up
button, the user will be registered

# View/Update Profile (logged in users)
Click on Profie link in the navigation bar.
Profile page contains the details about the user.
We can update in the emailid, username and the profile picture of the logged in user from profile page.

# Create Post (logged in users)
The page will have the forms to be filled to create a new blog.It includes title, content fields and a post button

# Update/Delete Post (logged in users)
On clicking the title of a blog from home page, we can head to blog update
or delete.logged in user can update/delete blog post and repost


# Bulk import (logged in users)
Bulk import page have the field to upload csv file which contains the bulk details about cars. From the field we can browse through the folders
in computer and select the correct csv file. Once clicked on the upload button,the data will be reflected in the home page.

# Logout

CLock on logout nav-link to logout user.

# Admin page:
Create a super user from the shell
python manage.py createsuperuser

provide the username and password and go to the below url

http://localhost:8000/admin

-Admin can create/update/delete users,posts,bulk import posts

# Dataset
#User dataset:

  - dataset/user_dataset.csv
  
  - it should containg comma seperated values
  
  - columns:title,content [column header should not be included in the file]
  
  - author will automatically updated with current logged in user

#Admin dataset:

  - dataset/admin_dataset.csv
  
  - it should containg comma seperated values
  
  - columns:title,content,author [column header should be included in the file]
  
  - author should be a valid user name, else the post will get ignored
  
#Table data set

  - dataset/table data.xlsx
  - columns:title,content
  - copy the table and paste in to text area
  
  # Table entry
  - user should be logged in
  - user can paste the excel table data in the text area
  - click on generate table button to view the table
  - click on Bulk Post button to Post the entire data to the blog
  
  
  
  



