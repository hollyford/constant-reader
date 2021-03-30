# [Constant Reader](https://github.com/hollyford/constant-reader)

## Contents
1. [Summary](#summary)
1. [UX](#ux)
    1. [Strategy](#strategy)
    1. [Scope](#scope)
    1. [Structure](#structure)
    1. [Skeleton](#skeleton)
    1. [Surface](#surface)
1. [Features](#features)
    1. [Existing Features](#existing-features)
    1. [Features left to implement](#left-to)
1. [Bugs](#bugs)
1. [Technologies used](#tech)
1. [Testing](#testing)
1. [Deployment](#deployment)
    1. [Github Pages](#github)
    1. [heroku](#heroku)
1. [Credits](#credits)
    1. [Content](#content)
    1. [Additional Content](#add-cont)
    1. [Acknowledgements](#acks)

# <a name="summary"></a> Summary
This site is an e-commerce store selling books. The title of the website was inspired by Stephen King who refers to his readers as ‘Constant Reader’. He writes to the Constant Reader at the end of each of his books.

This site provides an array of books which can be searched, viewed by standard users, favourited by users which create a profile and added to, edited and deleted by store admin.


# <a name="ux"></a> UX
## <a name="Strategy"></a> Strategy
### **New site user's goals:**
* As a new site user, I want to be able to browse and search for books
* As a new site user, I want to be able to view the details of individual books
* As a new site user, I want to be able to understand the intent of the page
* As a new site user, I want to understand easily how to navigate the page and access the facilities provided
* As a new site user, I want to be able to make a purchase without needing to create a profile
* As a new site user, I want to be able to be able to easily create a profile
* As a new site user, I want to be able to be able to sort products on a page
* As a new site user, I want to be able to be able to sort by specific categories
* As a new site user, I want to be able to be able to be able to amend the items in my bag including quantities and removing them entirely
### **Returning user's goals**
* As a returning site user, I want to be able to log in and out
* As a returning site user, I want to be able to recover a forgotten password
* As a returning site user, I want to be able to have a personalised profile
* As a returning site user, I want to be able to view my past orders

### **Site owner'as goals:**
* As a site owner, I want to be able to create, edit and delete books
* As a site owner, I want to the ability to create, edit and delete books to be limited to superusers

## <a name="scope"></a> Scope
**Functional requirements:**
#### For ease of use:
* Navigation bar which is simple and easy to navigate
* A search Function
#### To ensure the database is up to date and editable:
* Function to add a book
* Function to edit a book
* Function to delete a book
* For the books to be only editable by a superuser

**Content requirements:**
#### To ensure the site is visually appealing and to draw the user's eye:
* Images of books
* Clear soft colours intending to draw the user into the site and to be soft on the eye whilst not detracting from or make the text unreadable

### For usability
* For links to be clear and for the page to be constructed in a way which is instructive enabling the user to instinctively navigate the page

## <a name="structure"></a> Structure
**Interaction design:**
* User friendly interface to ensure usability and to encourage the user to return
* Responsive and visible links which change on hover to provide user feedback as they navigate the site
* Ability to exit pop ups so a user is not forced to use the browser navigation tools

**Information Architecture:**
* Navigation bar at the top of the page
* Responsive navigation bar - adjusting for mobile for ease of use
* Responsive images to ensure they fit within the designated spaces, no matter what device is being used or the size of the screen
* All features appropriate size and responsive for mobile and desktop viewing
* All information is appropriate and relative to the subject and not misleading or hard to find

## <a name="skeleton"></a> Skeleton
Please click the below link to view the wireframe mock up of the website in mobile, tablet and desktop sizing

[Wireframe](/workspace/constant-reader/wireframes/constant-reader-wireframes.pdf)

## <a name="surface"></a> Surface
The intention of the website is to be whimsycal 

* The font family chosen is 'Mirza' as this has a whimsycal touch, close to a typewriter style text whilst also being clear and easy to read
* The colour scheme selected is a shade of yellow with a consistant cover image throughout the site. For ease of viewing the content, there is an opaque attribute added to all but the main home page cover image
* The cover image was selected as it shows the site is all about books whilst also providing some clear space for text and not being too distracting as a cover image with content over the top of it

# <a name="features"></a> Features
## <a name="existing-features"></a> Existing Features
Feature | Details
--------|--------
Log in | The user can register and log into their own account with personalised features
Log out | There is a log out functionality on the page - this is especially important for users of a shared device
Add books | Superusers can add books to the site 
Edit books | Superusers are able to edit books
Delete books | Superusers are able to delete books
Search function | The users are able to search the book database. This function is available whether a user is logged in/registered or not

## <a name="left-to"></a> Features left to implement
Feature | Details
--------|--------
Multipe genres per book | The fixtures were set up to enable the use of mutiple genres however, due to issues in loading this data to the heroku database, the items needed to have only one genre
A filter for sale items | The fixtures were set up with a boolean field showing if the item was on sale or not to enable items to be filtered by whether they are on sale
A facility to save 'favourited' books | Links on each book page allowing a user to save books to their favourite list within their profile
# <a name="bugs"></a> Bugs
Bug | Fix
--------|--------
was unable to load models with multiple genres for an individual book | Although I was unable to resolve this issue, a fix was to change this so that each book only had one genre attached to it
An error occured when attempting to deploy the site in Heroku jango.core.exceptions.ImproperlyConfigured: You're using the staticfiles app without having set the STATIC_ROOT setting | I added STATIC_ROOT to settings.py to solve the collect static error when deploying to Heroku


# <a name="tech"></a> Technologies Used
* https://getbootstrap.com/
* JavaScript
* https://fonts.google.com/
* www.validator.w3.org
* http://www.css-validator.org/
* Git
* Gitpod
* GitHub
* Google Chrome
* http://www.responsinator.com/
* Chrome Dev Tools
* Python
* Django
* Amazon AWS S3
* Heroku
* Jinja
* Favicon.io
* Balsamiq

# <a name="testing"></a> Testing
### **New site user testing:**
# <a name="testing"></a> Testing
### **New site user testing:**
* As a new site user, I want to be able to browse and search for books
    1. Upon entering the site, users are automatically greeted with the page title and sub navigation bar
    1. There is a clear call to action to browse the books
* As a new site user, I want to be able to view the details of individual books
    1. Each book can be opened in an individual page with more information available than on the main page
* As a new site user, I want to be able to understand the intent of the page
    1. Upon entering the page, it is clear the site is designed around books. The main cover image shows a stack of books and all links are clear and book related
* As a new site user, I want I want to understand easily how to navigate the page and access the facilities provided
    1. The navigation bar has clear and easy to understand links
* As a new site user, I want to be able to make a purchase without needing to create a profile
    1. A user can checkout without the need to create a profile
* As a new site user, I want to be able to be able to easily create a profile
    1. A user can create a profile using the link in the nav bar
* As a new site user, I want to be able to be able to sort products on a page
    1. When viwing books, a select box is available at the top of the page to sort the books in several different ways
* As a new site user, I want to be able to be able to sort by specific categories
    1. On the nav bar, there is a drop down box which allows the user to select specific genres
* As a new site user, I want to be able to be able to be able to amend the items in my bag including quantities and removing them entirely
    1. The shopping bag has amend and delete buttons and the ability to increase the quantity

### **Returning user testing**
* As a returning site user, I want to be able to log in and out
    1. Upon entering the site, there is the option in the nav bar to register and log in
* As a returning site user, I want to be able to recover a forgotten password
    1. By using the Django all auth packages, this facility is available to users with a profile
* As a returning site user, I want to be able to have a personalised profile
    1. Users have a profile within which they can update their personal details
* As a returning site user, I want to be able to view my past orders
    1.  Within the profile page, there is a list of past orders 
    1. users can click on these orders to view the full details

### **Site owner testing:**
* As a site owner, I want to be able to create, edit and delete books
    1. There is a delete button on each book
    1. There is an edit button on each book which takes the user to a form where they can edit the content
    1. There is a form available from the nav bar to allow the creation of new books
* As a site owner, I want to the ability to create, edit and delete books to be limited to superusers
    1. The create edit and delete function is limited in two ways. Jinja logic is used within the html code and the @login_required decorator is used within the views. py document

### **Performance testing:**
1. Tested website responsiveness using http://www.responsinator.com/
    1. Results: The website is responsive to all device sizes without any unnecessary x-scroll
1. Tested the image size to ensure no image is to large and impacting the website loading times. I used the Google Dev Tools - Network
    1. Results: The site loading time is appropriate. The total website loading time is 1.1s is acceptable
1. Tested the images on the all books page using Google Dev Tools - Lighthouse
    1. Results: It was recommended that the images used were of a smaller size to improve download speed and cause less data consumption.
1. All HTML and CSS were tested using https://jigsaw.w3.org/css-validator/validator
    1. All but the templates resulted in errors that the Lang Doctype and Title were missing. This was to be expected as the details were being extended from the base template to did not need to be added
    1. All HTML pages resulted in errors where the Jinja template language was used
    1. None of these are actual errors within the code
	1. Some CSS errors were observed. However, the items highlighted were added intentionally to the CSS files and did create the desired affect
1. Tested the website on the Google Chrome browser Version 89.0.4389.90 (Official Build) (64-bit)
    1. Results: The website was responsive and the elements performed in the way they were intended to
1. Tested the website on the Microsoft Edge browser Version 89.0.774.63 (Official build) (64-bit)
    1. Results: The website was responsive and the elements performed in the way they were intended to
1. Tested the website on the Firefox browser Version 82.0.3 (64-bit)
    1. Results: The website was responsive and the elements performed in the way they were intended to
1. Tested adding items to the bag
    1. Results: Successfully able to add an item to the bag
1. Tested increasing the quantity of items in the bag
    1. Results: Successfully able to increase the quantity of an item in the bag
1. Tested removing items from the bag
    1. Results:Successfully removed an item from the bag
1. Tested the stripe process using 4242 4242 4242 4242 which should be successful
    1. Results: Order completed successfully and the confirmation page appears
1. Tested the stripe process using 4000 0027 6000 3184 which will request authorisation - completed authentication
    1. Results: Authorisation screen appears then the order completed successfully and the confirmation page appears
1. Tested the stripe process using 4000 0027 6000 3184 which will request authorisation - selected declined
    1. Results: The payment fails and the user is returned to the checkout page. The appropriate error message appears
1. Tested the profile page and that the orders placed above show correctly
	1. Results: The two successful orders made during testing appeared on the right hand side of the screen

# <a name="deployment"></a> Deployment
## <a name="github"></a> Github Pages
1. Create a new repository or access an existing repository
1. Click the green Gitpod button to launch the project in Gitpod
1. Create an index.html file
1. Add the file to the staging area using the git add Functional
1. Commit the file using the git commit function, adding an appropriate commentary
1. Push the file to GitHub using the git commit and git push functions
1. Refresh your GitHub repository and click the 'Settings' tab
1. Scroll to the GitHub Pages section and select a publishing source
1. Click 'Save'
1. Click the URL created within the Settings - GitHub Pages section

**To clone the repository for local deployment:** 
1. On the main page of the repository, click the down arrow Code button
1. Click the download icon under the relevant section to clone with either HTTPS, SSH or GitHub CLI 
1. In Git Bash, change the current directory to the location you want the directory to be stored
1. Type git clone and then paste the URL you copied in step 2
    1. An example for HTTPS: `git clone https://github.com/hollyford/constant-reader`
1. Press enter - that's it, your clone has been completed! 

**To fork the repository:**
1. Navigate to the main page of the repository you wish to fork
1. Click the Fork button on the top right hand side of the page
## <a name="heroku"></a> Heroku
### How to deploy to Heroku

To deploy the app to Heroku from its [GitHub repository](https://github.com/hollyford/constant-reader), the following steps were taken:

1. From the GitPod terminal, create **requirements.txt** and **Procfile** using these commands:

```console
pip3 freeze --local > requirements.txt
echo web: python app.py > Procfile
```

2. **Push** these files to GitHub
3. **Log In** to [Heroku](https://id.heroku.com/login)
4. Select **Create new app** from the dropdown in the Heroku dashboard
5. Choose a unique name ('recipe-nation') for the app and the location nearest to you
6. Go to the **Deploy** tab and under **Deployment method** choose GitHub
7. In **Connect to GitHub** enter your GitHub repository details and once found, click **Connect**
8. Go to the **Settings** tab and under **Config Vars** choose **Reveal Config Vars**
9. Enter the following keys and values, which must match those in the settings.py file:

|**Key**|**Value**|
|:-----|:-----|
AWS_ACCESS_KEY_ID|'AWS_ACCESS_KEY_ID'
AWS_SECRET_ACCESS_KEY | 'AWS_SECRET_ACCESS_KEY'
|DATABASE_URL|'DATABASE_URL'|
|EMAIL_HOST_PASS|'EMAIL_HOST_PASS'|
|EMAIL_HOST_USER|'EMAIL_HOST_USER'|
|SECRET_KEY|'SECRET_KEY'|
|STRIPE_PUBLIC_KEY|'STRIPE_PUBLIC_KEY'|
|STRIPE_SECRET_KEY|'STRIPE_SECRET_KEY'|
|STRIPE_WH_SECRET|'STRIPE_WH_SECRET'|
|USE_AWS|True|

10. Go back to the **Deploy** tab and under **Automatic deploys** choose **Enable Automatic Deploys**
11. Under **Manual deploy**, select **master** and click **Deploy Branch**
12. Once the app has finished building, click **Open app** from the header row of the dashboard

# <a name="credits"></a> Credits
## <a name="content"></a> Book Content

ISBN | URL
--------|--------
1408855652| https://www.amazon.co.uk/Harry-Potter-Philosophers-Stone/dp/1408855658/ref=sr_1_1?dchild=1&keywords=9781408855652&qid=1615124430&s=books&sr=1-1
1408855666| https://www.amazon.co.uk/Harry-Potter-Chamber-Secrets/dp/1408855666/ref=pd_bxgy_2/258-8126162-1694237?_encoding=UTF8&pd_rd_i=1408855666&pd_rd_r=2c62b488-0802-40cb-8d83-6552d5553769&pd_rd_w=BZjnr&pd_rd_wg=5sWcS&pf_rd_p=dcf35746-0212-418b-a148-30395d107b2d&pf_rd_r=P6F60GMSCCAAMFPN4QRS&psc=1&refRID=P6F60GMSCCAAMFPN4QRS
1408855674|	https://www.amazon.co.uk/Harry-Potter-Prisoner-Azkaban/dp/1408855674/ref=pd_bxgy_2/258-8126162-1694237?_encoding=UTF8&pd_rd_i=1408855674&pd_rd_r=86048960-f59a-4060-ad98-83728d4a7d95&pd_rd_w=PF3XI&pd_rd_wg=Wqvln&pf_rd_p=dcf35746-0212-418b-a148-30395d107b2d&pf_rd_r=6B3F7Q0S2RY5KMEAVS4J&psc=1&refRID=6B3F7Q0S2RY5KMEAVS4J
0241486106|	https://www.amazon.co.uk/Tomorrow-Will-Good-Day-Autobiography/dp/0241486106/ref=sr_1_2?crid=30G4W6I4DMCZF&dchild=1&keywords=biography+books&qid=1615126397&s=books&sprefix=bio%2Cstripbooks%2C195&sr=1-2
1688967486|	https://www.amazon.co.uk/Freddie-Mercury-Life-His-Words/dp/1688967486/ref=sr_1_5?crid=30G4W6I4DMCZF&dchild=1&keywords=biography+books&qid=1615126397&s=books&sprefix=bio%2Cstripbooks%2C195&sr=1-5
1788701984|	https://www.amazon.co.uk/Right-Said-Fred-Entertaining-Enjoyable/dp/1788701984/ref=sr_1_11?crid=30G4W6I4DMCZF&dchild=1&keywords=biography+books&qid=1615126397&s=books&sprefix=bio%2Cstripbooks%2C195&sr=1-11
0008297193|	https://www.amazon.co.uk/Guest-List-Lucy-Foley/dp/0008297193/ref=lp_72_1_12
1538702738|	https://www.amazon.co.uk/Boy-Woods-Harlan-Coben/dp/1538702738/ref=tmm_hrd_swatch_0?_encoding=UTF8&qid=1615127552&sr=1-21
0140569324|	https://www.amazon.co.uk/Very-Hungry-Caterpillar-Eric-Carle/dp/0140569324/ref=sr_1_15?qid=1615128090&rnid=1025612&s=books&sr=1-15
1407170716|	https://www.amazon.co.uk/Stick-Man-Julia-Donaldson/dp/1407170716/ref=sr_1_19?dchild=1&qid=1615128118&rnid=1025612&s=books&sr=1-19
1787133672|	https://www.amazon.co.uk/Chinese-Takeaway-Cookbook-re-create-favourites/dp/1787133672/ref=sr_1_17?dchild=1&qid=1615128454&rnid=1025612&s=books&sr=1-17
1787134636|	https://www.amazon.co.uk/Curry-Guy-Bible-curryhouse-favourites/dp/1787134636/ref=sr_1_30?dchild=1&qid=1615128454&rnid=1025612&s=books&sr=1-30
1785945076|	https://www.amazon.co.uk/Mary-Berrys-Simple-Comforts-Berry/dp/1785945076/ref=sr_1_36?dchild=1&qid=1615128516&rnid=1025612&s=books&sr=1-36
0099590085|	https://www.amazon.co.uk/Sapiens-Humankind-Yuval-Noah-Harari/dp/0099590085?ref_=Oct_s9_apbd_otopr_hd_bw_b3El4&pf_rd_r=YKFDBQDDQFYPNAQYDSMB&pf_rd_p=8428d2f8-f7eb-5209-aa69-c422ee9b7764&pf_rd_s=merchandised-search-10&pf_rd_t=BROWSE&pf_rd_i=771718
1782941975|	https://www.amazon.co.uk/KS2-Discover-Learn-History-Britain/dp/1782941975?ref_=Oct_s9_apbd_oup_hd_bw_b3El4&pf_rd_r=YKFDBQDDQFYPNAQYDSMB&pf_rd_p=9b946017-b2a2-5f42-a4bd-b03ce461f8a1&pf_rd_s=merchandised-search-10&pf_rd_t=BROWSE&pf_rd_i=771718
1648450660|	https://www.amazon.co.uk/Great-Book-Badass-Women-Inspirational/dp/1648450660?ref_=Oct_s9_apbd_omg_hd_bw_b3El4&pf_rd_r=YKFDBQDDQFYPNAQYDSMB&pf_rd_p=388cbd1d-c4fe-51a3-b7ee-6bfcd37daf0c&pf_rd_s=merchandised-search-10&pf_rd_t=BROWSE&pf_rd_i=771718
1473676398|	https://www.amazon.co.uk/Outsider-Stephen-King/dp/1473676398?ref_=Oct_s9_apbd_oup_hd_bw_b11&pf_rd_r=5A43NYXYNH51DJZCKQBX&pf_rd_p=e5f5770b-b23a-5d6b-ac4d-6290381dff9c&pf_rd_s=merchandised-search-10&pf_rd_t=BROWSE&pf_rd_i=63
1444720730|	https://www.amazon.co.uk/Stand-Stephen-King/dp/1444720732?ref_=Oct_s9_apbd_obs_hd_bw_b2Anm&pf_rd_r=99M34EHZ3WTX188KY7NP&pf_rd_p=1d70d2e5-357c-5c8d-9bdf-f7fe34a67e88&pf_rd_s=merchandised-search-10&pf_rd_t=BROWSE&pf_rd_i=518182
0141196886|	https://www.amazon.co.uk/Dracula-Bram-Stoker/dp/0141196882?ref_=Oct_s9_apbd_omwf_hd_bw_b2Anm&pf_rd_r=99M34EHZ3WTX188KY7NP&pf_rd_p=c8b90d51-22c9-5956-867c-9d63f84139c1&pf_rd_s=merchandised-search-10&pf_rd_t=BROWSE&pf_rd_i=518182
1788689135|	https://www.amazon.co.uk/Lonely-Planets-Ultimate-Travel-List/dp/1788689135/ref=sr_1_1?dchild=1&qid=1615130141&refinements=p_n_feature_fourteen_browse-bin%3A16368282031&rnid=16368267031&s=books&sr=1-1
1786892737|	https://www.waterstones.com/book/the-midnight-library/matt-haig/9781786892737
0857839442|	https://www.waterstones.com/book/together/luke-adam-hawker/9780857839442
1529105100|	https://www.waterstones.com/book/the-boy-the-mole-the-fox-and-the-horse/charlie-mackesy/9781529105100

## <a name="add-cont"></a> Additional Content

File Name|Used For|URL
---|------|-----
colour-book-pile.jpg|	Cover image|	https://buddhify.com/what-mindfulness-and-meditation-books-should-i-add-to-my-summer-reading-list/
no-image.png|	No images available|	https://commons.wikimedia.org/wiki/File:No-image-available.png

## <a name="acks"></a> Acknowledgements
* Ed Bradley - I also used this readme as an example of how to deploy Heroku
    * https://github.com/Edb83/self-isolution

* My mentor Antonio Rodriguez who has provided me with guidance and support through the project
