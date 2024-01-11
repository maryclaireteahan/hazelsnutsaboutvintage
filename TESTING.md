# TESTING

For a proper conclusion to this project several tests were performed.

## TABLE OF CONTENTS

* [RESPONSIVENESS TESTING](#responsiveness-testing)
* [BROWSER COMPABILITY TESTING](#browser-compability-testing)
* [BUGS RESOLVED AND UNRESOLVED](#bugs-resolved-and-unresolved)
* [LIGHTHOUSE TESTING OUTCOMES](#lighthouse-testing-outcomes)
* [CODE VALIDATION](#code-validation)
* [USER STORIES TESTING](#user-stories-testing)
* [FEATURES TESTING](#features-testing)
* [AUTOMATED TESTING](#automated-testing)
* [TEST CASE](#test-case)

Return back to the [README.md](README.md) file.

- - -

## RESPONSIVENESS TESTING

<details>

The deployed application was tested on multiple devices to check for responsiveness issues. 

It works as expected according to the wireframes and no issue was found.

<img src="readme/documentation/responsiveness/amiresponsive.png">

|Device| Screenshot | 
|:---|:---: |
| 1200px |  <img src="readme/documentation/responsiveness/sizes/1200.png">  |
| 992px  |  <img src="readme/documentation/responsiveness/sizes/992.png">  |
| 768px  |  <img src="readme/documentation/responsiveness/sizes/768.png">  |
| 576px  |  <img src="readme/documentation/responsiveness/sizes/576.png"> |
| 320px  |  <img src="readme/documentation/responsiveness/sizes/320.png"> |


</details>

- - -

## BROWSER COMPABILITY TESTING


<details>

The deployed project was tested on multiple browsers to check for compatibility issues and works as expected.

|Browser | Screenshot | 
|:---:|:---: |
| Chrome | <img src="readme/documentation/browser/chrome.png"> |
| Edge  | <img src="readme/documentation/browser/edge.png"> |
| Firefox |  <img src="readme/documentation/browser/firefox.png"> |

</details>

- - -

## BUGS RESOLVED AND UNRESOLVED 

<details>

The issues listed in the table below were indentified during the development of the project.

### Resolved bugs and issues

|N.| Issue |  Action | Status | 
|:---|:--- |:--- |:--- |
|01| Instructions, Ingredients and Category fields weren't required to submit a new recipe | Remove null and blank = True and set a default | Closed | 
|02| edit/delete recipe available to all users | Add condition for user to authenticated and a super user to have edit/delete option render | Closed | 
|03| Brute forcing the URL to edit/delete recipe allowed non superuser to edit/delete recipes | Update views to have non-superusers redirected to 404 error page | Closed | 
|04| Brute forcing the URL to edit/delete comments allowed any user to edit/delete any other users' comments | Update views to have user's who isn't the comment owner redirected to 404 error page | Closed | 
|05| Alert messages wouldn't close when clicking the X | Add javascript to remove the element when the X is clicked | Closed | 
|06| edit/delete recipe available to all users | Add condition for user to authenticated and a super user to have edit/delete option render | Closed |
|09| Inpunt forms don't prepoulate fields with original comment or recipe values when editing | passed the recipe instance as an argument to the form constructor | Closed |
|10| Heroku deployment failing | Removed unused CAB import from msilib | Closed |
|11| Categories weren't rendering | In models.py relevant functions were moved inside catergories class as they were mistakenly sitting outside it | Closed | 
|12| 404 error page wasn't loading | Input handlere404 function to letseat views.py and at the end of relevant conditions in blog views.py   | Closed |
|13| Styles not rendering in live preview | Switch debug to true   | Closed |
|14| Console Error that messageRow is not a valid DOM element however it disappears when the alert message for logging in and out appears. | Delete relevant console.log from script.js | Closed |

### Unresolved bugs and issues

|N.| Issue |  Action | Status | 
|:---|:--- |:--- |:--- |
|01| Ingredients and Instructions do not render in the form of a list even when typed as such in the textareas. | Textarea field in the backend allow lists to be rendered on posted recipe. I have checked the views but isn't clear why the same textareas in the frontend and backend are operating differently | Open |
|02| When a user likes a recipe the like initial icon of a heart outline should fill in to be a solid heart but it doesn't | I have checked the html and views and can't find an obvious reason as to why it isn't changing | Open |

</details>

- - -

## LIGHTHOUSE TESTING OUTCOMES

<details>

The deployed project was tested using the Lighthouse Audit tool to check for any major issues. The results for each page are listed below.

|Page | Screenshot | Notes |
|:---:|:---: |:---: |
|Index Desktop |<img src="readme/documentation/performance/desktop/index.png">||
|Index Mobile |<img src="readme/documentation/performance/mobile/index.png">| Height and width for images stated as reason for lower score. I tried changin them but it made no difference. |
|All Recipes Desktop |<img src="readme/documentation/performance/desktop/all_recipes.png">||
|All Recipes Mobile |<img src="readme/documentation/performance/mobile/all_recipes.png">||
|Single Recipe Desktop |<img src="readme/documentation/performance/desktop/single_recipe.png">||
|Single Recipe Mobile |<img src="readme/documentation/performance/mobile/single_recipe.png">||
|Delete Comment Desktop |<img src="readme/documentation/performance/desktop/comment_delete.png">||
|Delete Comment Mobile |<img src="readme/documentation/performance/mobile/comment_delete.png">||
|Edit Comment Desktop |<img src="readme/documentation/performance/desktop/comment_edit.png">||
|Edit Comment Mobile |<img src="readme/documentation/performance/mobile/comment_edit.png">||
|Add Recipe Desktop |<img src="readme/documentation/performance/desktop/admin_recipe_create.png">||
|Add Recipe Mobile |<img src="readme/documentation/performance/mobile/admin_recipe_create.png">||
|Edit Recipe Desktop |<img src="readme/documentation/performance/desktop/admin_recipe_edit.png">||
|Edit Recipe Mobile |<img src="readme/documentation/performance/mobile/admin_recipe_edit.png">||
|Delete Recipe Desktop |<img src="readme/documentation/performance/desktop/admin_recipe_delete.png">||
|Delete Recipe Mobile |<img src="readme/documentation/performance/mobile/admin_recipe_delete.png">||
|Signup Desktop |<img src="readme/documentation/performance/desktop/signup.png">||
|Signup Mobile |<img src="readme/documentation/performance/mobile/signup.png">||
|Login Desktop |<img src="readme/documentation/performance/desktop/login.png">||
|Login Mobile |<img src="readme/documentation/performance/mobile/login.png">||
|Logout Desktop |<img src="readme/documentation/performance/desktop/logout.png">||
|Logout Mobile |<img src="readme/documentation/performance/mobile/logout.png">||

</details>

- - -

## CODE VALIDATION

<details>

### HTML

The [HTML W3C Validator](https://validator.w3.org/) to validate all HTML files.
In order to properly validate the HTML pages with Jinja syntax, the steps are followed for each file:

- Navigate to the deployed application using Google Chrome,
- Right-click anywhere on the page, and select View Page Source.
- Copy the entire "compiled" code, without any Jinja syntax., and use the validate by input method.

The result for each page are listed bellow:

|Page |Screenshot | Notes  | 
|:---:|:----------------------:|---|
| Index | <img src="readme/documentation/validation/html/index.png"> | No Errors |
| Products | <img src="readme/documentation/validation/html/index.png"> | No Errors |
| Single Product | <img src="readme/documentation/validation/html/product_details.png"> | No Errors |
| Events | <img src="readme/documentation/validation/html/events.png"> | No Errors |
| Single Event | <img src="readme/documentation/validation/html/single_event.png"> | No Errors |
| Add Product | <img src="readme/documentation/validation/html/add_product.png"> | No Errors |
| Edit Product | <img src="readme/documentation/validation/html/edit_product.png"> | No Errors |
| Add Event | <img src="readme/documentation/validation/html/add_event.png"> | No Errors |
| Edit Event | <img src="readme/documentation/validation/html/edit_event.png"> | No Errors |
| Bag | <img src="readme/documentation/validation/html/bag.png"> | No Errors |
| Checkout | <img src="readme/documentation/validation/html/checkout.png"> | No Errors |
| Checkout Success | <img src="readme/documentation/validation/html/checkout_success.png"> | No Errors |
| Coupon | <img src="readme/documentation/validation/html/coupon.png"> | No Errors |
| Feedback | <img src="readme/documentation/validation/html/feedback.png"> | No Errors |
| Single Feedback | <img src="readme/documentation/validation/html/feedback_detail.png"> | No Errors |
| Signup | <img src="readme/documentation/validation/html/signup.png"> | Error with signup form not accessible |
| Login | <img src="readme/documentation/validation/html/signin.png"> | No Errors |
| Logout | <img src="readme/documentation/validation/html/signout.png"> | No Errors |
| 404 | <img src="readme/documentation/validation/html/404.png"> | No Errors |

- - - 

### CSS

The [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator/) was used to validate the CSS file.

| File | Screenshot | Notes |
| --- | --- | --- |
| base.css | <img src="readme/documentation/validation/css/base.png">| No Errors |

- - - 

### JAVASCRIPT

The [JShint Validator](https://jshint.com/) was used to validate the JavaScript file.

| File | Screenshot | Notes |
| --- | --- | --- |
| checkout_stripe_element.js | <img src="readme/documentation/validation/javascript/checkout_stripe_element_1.png"> <img src="readme/documentation/validation/javascript/checkout_stripe_element_2.png">| No Errors |
| profiles_countryfield.js | <img src="readme/documentation/validation/javascript/profiles_countryfield.png"> | No Errors |


- - - 

### PYTHON

The [Code Institute Python Linter](https://pep8ci.herokuapp.com)was used to validate all Python files.

#### Network project

| File | Screenshot  | Notes|
| --- | ------ |:---:|
| settings.py |  <img src="readme/documentation/validation/python/hazelsnutsaboutvintage/settings.png">  | Pass |
| urls.py (main) |  <img src="readme/documentation/validation/python/hazelsnutsaboutvintage/urls.png">  | Pass |
| views.py | <img src="readme/documentation/validation/python/hazelsnutsaboutvintage/views.png">  | Pass |


#### Bag app

| File | Screenshot  | Notes|
| --- | --- | --- |
| bag_tools.py | <img src="readme/documentation/validation/python/bag/bag_tools.png">   | Pass |
| contexts.py | <img src="readme/documentation/validation/python/bag/contexts.png">   | Pass |
| urls.py | <img src="readme/documentation/validation/python/bag/urls.png">   | Pass |
| views.py |  <img src="readme/documentation/validation/python/bag/views.png">  | Pass |

#### Checkout app

| File | Screenshot  | Notes|
| --- | --- | --- |
| admin.py | <img src="readme/documentation/validation/python/checkout/admin.png">   | Pass |
| forms.py | <img src="readme/documentation/validation/python/checkout/forms.png">   | Pass |
| models.py | <img src="readme/documentation/validation/python/checkout/models.png">   | Pass |
| urls.py |  <img src="readme/documentation/validation/python/checkout/urls.png">  | Pass |
| views.py | <img src="readme/documentation/validation/python/checkout/views.png">   | Pass |
| signals.py | <img src="readme/documentation/validation/python/checkout/signals.png">   | Pass |
| webhook_handlers.py |  <img src="readme/documentation/validation/python/checkout/webhook_handlers.png">  | Pass |
| webhooks.py | <img src="readme/documentation/validation/python/checkout/webhooks.png">   | Pass |

#### Coupon app

| File | Screenshot  | Notes|
| --- | --- | --- |
| admin.py | <img src="readme/documentation/validation/python/coupon/admin.png">   | Pass |
| models.py | <img src="readme/documentation/validation/python/coupon/models.png">   | Pass |
| urls.py |  <img src="readme/documentation/validation/python/coupon/urls.png">  | Pass |
| views.py | <img src="readme/documentation/validation/python/coupon/views.png">   | Pass |

#### Events app

| File | Screenshot  | Notes|
| --- | --- | --- |
| admin.py | <img src="readme/documentation/validation/python/events/admin.png">   | Pass |
| forms.py | <img src="readme/documentation/validation/python/events/forms.png">   | Pass |
| models.py | <img src="readme/documentation/validation/python/events/models.png">   | Pass |
| urls.py |  <img src="readme/documentation/validation/python/events/urls.png">  | Pass |
| views.py | <img src="readme/documentation/validation/python/events/views.png">   | Pass |

#### Feedback app

| File | Screenshot  | Notes|
| --- | --- | --- |
| admin.py | <img src="readme/documentation/validation/python/feedback/admin.png">   | Pass |
| forms.py | <img src="readme/documentation/validation/python/feedback/forms.png">   | Pass |
| models.py | <img src="readme/documentation/validation/python/feedback/models.png">   | Pass |
| urls.py |  <img src="readme/documentation/validation/python/feedback/urls.png">  | Pass |
| views.py | <img src="readme/documentation/validation/python/feedback/views.png">   | Pass |


#### Home app

| File | Screenshot  | Notes|
| --- | --- | --- |
| urls.py |  <img src="readme/documentation/validation/python/home/urls.png">  | Pass |
| views.py | <img src="readme/documentation/validation/python/home/views.png">   | Pass |


#### Products app

| File | Screenshot  | Notes|
| --- | --- | --- |
| admin.py | <img src="readme/documentation/validation/python/products/admin.png">   | Pass |
| forms.py | <img src="readme/documentation/validation/python/products/forms.png">   | Pass |
| models.py | <img src="readme/documentation/validation/python/products/models.png">   | Pass |
| urls.py |  <img src="readme/documentation/validation/python/products/urls.png">  | Pass |
| views.py | <img src="readme/documentation/validation/python/products/views.png">   | Pass |
| widgets.py | <img src="readme/documentation/validation/python/products/widgets.png">   | Pass |


#### Profiles app

| File | Screenshot  | Notes|
| --- | --- | --- |
| forms.py | <img src="readme/documentation/validation/python/profiles/forms.png">   | Pass |
| models.py | <img src="readme/documentation/validation/python/profiles/models.png">   | Pass |
| urls.py |  <img src="readme/documentation/validation/python/profiles/urls.png">  | Pass |
| views.py | <img src="readme/documentation/validation/python/profiles/views.png">   | Pass |

</details>

- - -

## USER STORIES TESTING

<details>

The implemented User Stories were tested during the development of this project and also after it was finished.

### Site User

- - -

As a Site User, I want to be able to:

*Must Have*

| User Stories |  Notes|
| --- | --- | 
| view a list of recipes so that I can choose one to read. | Pass |
| click on a recipe post so that I can read the full recipe. |  Pass |
| see how many likes a post has received so that I can see what recipes are most popular. | Pass |
| see who commented what under each post so that I can see what the Site Users think of specific recipes and how they might change them. | Pass |

*Should Have*

| User Stories |  Notes|
| --- | --- | 
| sign up to be a member/ login as an existing member so that I can be a part of the site's community. |  Pass |
| click a like button so that I can like a recipe and then unlike if needed. | Pass |

*Could Have*

| User Stories |  Notes|
| --- | --- | 
| post a comment on a recipe post so that I can interact with the site's community. | Pass |
| edit or delete my comment so that if I made a spelling error or changed my mind about what I said I can edit or delete it. | Pass |


### **Site Admin**

- - -

As Site Admin for the site I want to be able to:

*Must Have*

| User Stories |  Notes|
| --- | --- | 
| create, edit and delete recipe posts so that I can be in control of what content is shown to Site Users. | Pass |
| assign a category to the recipe post so that Site Users will be able to find recipes specific to what they need. | Pass |
| see who commented what under each post so that I can see what the Site Users think of specific recipes and how they might change them. | Pass |
| see how many likes a post has received so that I can see what recipes are most popular. | Pass |

</details>

- - -

## FEATURES TESTING

<details>

| Page | User Action | Expected Result| Notes |
| --- | --- | --- | --- |
| **Index**   |  |  | |
| | Click on Logo | Redirection to Index page | Pass |
| | Click on Nav Toggle | Show Nav items - Home, Recipes, Signup, Login | Pass |
| | Click on Nav Toggle (while logged in) | Show Nav items - Home, Recipes, Logout | Pass |
| | Click on Nav Toggle (while admin logged in) | Show Nav items - Home, Recipes, Logout, Add Recipe | Pass |
| | Click on Home button | Redirection to Index page | Pass |
| | Click on Discover Recipes | Redirection to All Recipes page | Pass |
| | Click on Sign Up button  | Redirection to Sign Up page | Pass |
| | Click on Login button | Redirection to Login page | Pass |
| | Click on Discover Recipes button | Redirection to All Recipes page | Pass |
| **Sign Up** |  |  |  |
| | Click Sign Up button | Username required | Pass |
| | Click Sign Up button (username provided) | Password required | Pass |
| | Click Sign Up button (username and password provided) | Password (again) required | Pass |
| | Click Sign Up button with all valid information | Redirection to Index page and displays message | Pass |
| | Click Sign Up button (username, email (already in use), password, password (again) provided, passwords matching) | Field only accepts new email | Pass |
| | Click Sign Up button (username, password, password (again) provided, passwords matching, using invalid password format) | Field will only accept password format  | Pass |
| | Click Sign Up button (username, password, password (again) provided, passwords not matching) | Passwords required to match | Pass |
| | Click on Login link | Redirection to Login page | Pass |
| | Click Cancel button | Redirection to Index page | Pass |
| **Log In** |  |  |  |
| | Click Login button | Username required | Pass |
| | Click Login button (username provided) | Password required | Pass |
| | Click Login button (valid username and invalid password provided) | Username and/or password incorrect | Pass |
| | Click Login button (invalid username provided) | username and/or password incorrect  | Pass |
| | Enter user email address in username field | field will only accept valid username | Pass |
| | Enter valid password | Field will only accept password format | Pass |
| | Click Login button with all valid information | Redirection to Index page and displays message | Pass |
| | Click on Sign Up link | Redirection to Sign Up page | Pass |
| | Click Cancel button | Redirection to Index page | Pass |
| **Log Out** |  |  |  |
| | click on dropdown menu, then log out | Redirects to log out page | Pass |
| | Click to confirm to sign out  | Redirects to landing page and displays message with the sign out confirmation | Pass |
| | Click Cancel button | Redirection to Index page | Pass |
| **All Recipes** |  |  |  |
| | Click anywhere on a recipe card | User will be redirected to the Single Recipe page | Pass |
| **Single Recipe** |  |  |  |
| | Click the like icon on a recipe if not logged in | Like count remains unchanged | Pass  |
| | Click the like button on a recipe that the user hasn't liked before | Like count will increase by 1 | Pass |
| | Click the like button on a recipe already liked by the user | Like count will decrease by 1 | Pass |
| | Click delete on recipe (only visable to admin)  | User is redirected to Delete Recipe confirmation page | Pass  |
| | Click edit on recipe (only visable to admin) | User is redirected to Edit Recipe page | Pass   |
| | Brute forcing the URL to delete recipe if not logged in | Redirects user to login page | Pass | 
| | Brute forcing the URL to delete recipe while logged in (NOT admin) | Redirects user to error page | Pass |
| | Brute forcing the URL to edit recipe if not logged in | Redirects user to login page | Pass | 
| | Brute forcing the URL to edit recipe while logged in not as (NOT admin) | Redirects user to error page | Pass |
| **Comments on Single Recipe** | | | | 
| | Comment a recipe if not logged in| Feature not available, user promted to log in | Pass |
| | Click submit on new comment form on a recipe | New comment is created | Pass |
| | Click submit on new comment form without adding content | User is prompted to enter something into the field before submitting | Pass |
| | Click edit on own comment (only visable to comment user) | User is redirected to comment edit page | Pass  |
| | Click delete on own comment (only visable to comment user) | User is redirected to comment delete confirmation page | Pass  |
| | Brute forcing the URL to delete another user's comment if not logged in | Redirects user to login page | Pass | 
| | Brute forcing the URL to delete another user's comment while logged in | Redirects user to error page | Pass |
| | Brute forcing the URL to edit another user's comment if not logged in | Redirects user to login page | Pass | 
| | Brute forcing the URL to edit another user's comment while logged in | Redirects user to error page | Pass | 
| **Edit Comment** | | | | 
| | Fill in comment form and click submit | Original comment will be edited User will be redirected to the All Recipes | Pass | 
| | Click on the Cancel button | User will be redirected to All Recipes| Pass | 
| **Delete Comment** | | | | 
| | Click on the Delete button | Comment or reply will be permanently deleted and User will be redirected to All Recipes | Pass | 
| | Click on the Cancel button | User will be redirected to All Recipes | Pass |  
| **Add Recipe** |  |  |  |
| | Click Submit on add recipe form without adding content | User is prompted to enter something into each field before submitting | Pass |
| | Click Cancel on add recipe form | User will be redirected to All Recipes | Pass |
| **Edit Recipe** | | | | 
| | Fill in post form and click submit | Original recipe can be edited and User will be redirected to the All Recipes | Pass | 
| | Click on the Cancel button | User will be redirected to the All Recipes | Pass | 
| **Delete Recipe** | | | | 
| | Click on the Delete button | Recipes will be permanently deleted and User will be redirected to the All Recipes | Pass | 
| | Click on the Cancel button | User will be redirected to the All Recipes | Pass | 
| **Error Pages** | | | | 
| | Click on Home button | User will be redirected to Index page | Pass | 
| **Footer** | | | | 
| | Click on Facebook Icon | Opens new tab to Facebook | Pass |
| | Click on Twitter Icon | Opens new tab to Twitter | Pass |
| | Click on Youtube Icon | Opens new tab to Youtube | Pass |
| | Click on Instagram Icon | Opens new tab to Instagram | Pass |
| | Click on Linkedin Icon | Opens new tab to LinkedIn | Pass |

</details>

- - -

Return back to the [README.md](README.md) file.