# Travex(Website for people to anonymously share their travel expiriences)

#### Video Demo: https://www.youtube.com/watch?v=eqRxZAaqFYc&ab_channel=BT_Coding
#### Description: 
Travex is a webpage that allows it's users to anoymously post about their travels and adventures, how they felt during the, where they went and how much did it cost them.

### How it works:
After you register into the webiste using a not already taken username, and a strong password you can go to either the home page, or your account page or to create post so you can create your first post and share it to the world, explain a vacation you went to, where did you, how did it go, was it cheap or expensive, where did you stay, what fun acitivies you did and so on. After you finish create your post and go the homepage so you can see it along other people's post which are all completely anonymous and noone will be able to criticize you. If you don't like your post you can always click the delete button under the post when you are in your account and boom the post is gone. Share your thoughts.

### Technologies I used:
```
Python
Flask
Jinja
HTML
CSS
CSS Bootstrap
SQLite
I didn't use Javascript because I did not see it fiting anywere
```

## template files and their app.py route functions:

### all files inside my final project
```
static/styles.cc
templates/login.html
templates/register.html
templates/layout.html
templates/index.html
templates/myaccount.html
templates/home.html
templates/create.html
templates/apology.html
app.db
app.py
helpers.py
```

### login.html / app.py login route
This is the first file I have created in the project, It contains a login form which upon completion gets checked by the server and if it passes all the conditions: it checks if the user has typed anythin in the box if not it returns an apology, checks if the password is typed if not it returns an apology. The next checks are validations, It checks if the username is within the database, if it is then checks if the hashes of the typed password and the one in the database are matching, if they do it logs in the user and redirects them to the index page.

### register.html / app.py login route
This the second file, if the user does not have an account they click on the register link so it can redirect them here, after redireciton the user sees a form with an username input field and 2 password fields. Once typed and clicks the register button, the server does a couple of checks before continuing. First it checks if there is a name, and passwords if not it returns an apology, Then it checks if the name is already in the database, if it is it returns an apology saying the username is already taken, then checks if both password are matching if they are not it returns an apology saying the passwords do not match. If it passes all the checks it creates a hash for the password and then stores the name and the hash for the password inside the table users in the database app.db.

### layout.html 
Layout made by Jinja, so I don't have to type the navbar in all the HTML files. There is an if statement inside that file so It checks if the user is logged in by checking if there is a session["user_id"] if there is the navbar will show logged in user navbar if not it will show log in and register navbar.

### index.html / app.py index
Takes only one paramter the user's username which is displayed ontop of the page welcoming the user. Under the greeting there are 2 links, One for the user to go back to his profile and One to go home and check other people's posts.

### myaccount.html / app.py myacc
In the myaccount page, The user's name is shows and also all if the user's posts.
This is achieved by a for loop inside the Jinja templates which loops trough all the posts inside the databse with user_id as one of their columns in the table, and displayes the needed information inside the user's account, If there are no posts it displays no posts to show. For style sake the delete button under the posts which deletes a post is shown only inside the user's account, and not in the homepage.

### home.html / app.py home
Inside the homepage the 10 most recent post are shown, the usernames of the accounts are not shown because Travex let's the users publish their expiriences privately. In the Jinja template Im looping trough all of the posts which I am taking from the database and Im taking the TOP 10 in Descending order of post_id's So the post will always refresh themselves and not stay on the first 10 ever created, if there are no posts it displays no posts to show.

### create.html / app.py create
The create page is where a user creates their posts, Inside is a form with a location field which if not typed returns an apology, same for the description field. 2 Selection fields, one so the user can share the price of their adventure from cheap to expensive, and one for their mood during the vacation from Bad to Amazing. The location field so the user can type where they went and a description text-field so the user can tell the world how their vacation went how did they feel, where they stayed and other things. After they finished they click the create post button which pushes the data inside the post table in the database, and redirects the user to their account page so they can see their post displayed.

### delete route in app.py 
The delete route takes it's information from a form that I made inside each user's post. The form's submit button is the delete button, it takes the post_id from there so it accuretly execute the DELETE command inside the database without hurting the database but only deleting the post with that id which is exclusive.

### logout route in app.py
The logout function clears the current user session and redirects the user back to the login page.

### @login required in the helpers.py
The login required function checks if the user_id inside the session is None, if it is it returns the user to the login page.

### apology.html and the apology function in helpers.py
The apology function in helpers.py makes a custom error with the ERROR CODE 400, so I can only use apology(), and not a whole render_template so I can render every single mistake the user does, I always do it in the apology fucntion.

### app.db 
In the database there are 2 tables, users and posts. The user has 3 fields and the first is ID which is automaticaly incremented by SQL starting from 1 and the secodn is the username and the third is the password hash generated from app.py register.
The posts table has 6 columns but only 2 are more important, the 4 that are just basic are the location, the price, the mood and the description of the user's expirience. The post_id is auto incremented from 1 and it plays a key role in the deletion algorithm, and the user_id which is a FOREIGN KEY from users takes a key role in displaying the post in the correct accounts.

### How to activate on your own mashine.
1. Either clone this repository using git_clone and taking the HTTP clone or Just download it from the dropdown menu which displays when hovering over the green button code and downloading as ZIP.
2. After downloading open it in VSCODE and be sure you have downloaded flask using pip3 install inside a virtually managed enviorment or you might get an error.
3. Use the command flask run in the terminal.
4. You are ready to go.