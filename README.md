# Teashop

## <i>Description</i>

I realised a *Django project* that has the role of keeping tracks of the available stock of ingredients for a tea shop.
It is connected to a *database* (**MySQL**) so you are everytime updated with all the informations used on the project.


## <i>Prerequisites</i>
### Modules used 
| Name module  |              Description               |
|:------------:|:--------------------------------------:|
|    Django    |        ```pip install Django```        |
|   decouple   |   ```pip install python-decouple```    |
| crispy-forms | ```pip install django-crispy-forms ``` |
| mysqlclient  |     ```pip install mysqlclient```      |

## <i>Informations</i>

[Django module documentation](https://docs.djangoproject.com/en/4.0/)
<br>
[Decouple module documentation](https://pypi.org/project/python-decouple/)
<br>
[Crispy-Forms module documentation](https://pypi.org/project/django-crispy-forms/)
<br>
[MySQLclient module documentation](https://pypi.org/project/mysqlclient/)

### Configs to made
- In the file `.env.default` you will see a template of variables that needs to be put by users to access their informations
- Depending on the above file, you need to create a file `.env`, on the same path as `.env.default` and introduce your specified informations
- You need to insert your secret key for Django in `Teashop/settings.py (line 26)`

### <u>Functions by page</u>

#### *If you are not logged in*
- `Homepage` This is main page of the website with informations about tea
<br><br>
- `Curiosity` Contains polls about the services offered by the company
<br><br>
- `Login` Page to Log In with your account already created
<br><br>
- `Register` Register your account that will be stored in the database
#### *If you are logged in*
- `Homepage` This is main page of the website with informations about tea
<br><br>
- `Curiosity` Contains polls about the services offered by the company
<br><br>
- `Distributors`This page displays all the distributors for the company with all their informations, suchs as name, email, phone number <br>
 On this page you can do more actions:
  1. `ADD NEW DISTRIBUTOR` Add a new distributor with its informations
  2. `UPDATE DISTRIBUTOR` Update informations for distributors
  3. `DELETE DISTRIBUTOR` Delete all the informations about distributors
<br><br>
- `Ingredients` On this page are displayed all the ingredients with their informations and their specific distributor <br>
 On this page you can do more actions:
  1. `ADD NEW INGREDIENT` Add a new ingredient and choose its distributor
  2. `UPDATE QUANTITY` Update the quantity amount of ingredient
  3. `DELETE INGREDIENT` Delete the ingredient from page
  4. By pressing <img src="g_logo.jpg" alt="Google Logo" width="17" height="17"> it will send you on the **email form** to send an email to distributor's email address to warn them that the stock is low <br><br>
- `Recipes` This page will display all the recipes with their amount of quantity available<br>
 On this page you can do more actions:
  1. `ADD NEW RECIPE` Add a new recipe by introducing its name, ingredients used for it, you can upload an image for the recipe and choose the quantity of it
  2. `UPDATE RECIPE` Update the informations for recipe
  3. `PREPARE RECIPE` Prepare a recipe and automatically update the quantity of the ingredient used for recipe
  4. `DELETE RECIPE` Delete the recipe from page
<br><br>
- `Profile of (first name) (last name)` This page will display informations about your created profile, such as `first name`, `last name`, `email`, `username` -> which is not enabled by default, you can enable it from `users/models.py`
<br>
  You can choose your profile image by pressing `CHOOSE FILE`, browse your image, then press `UPLOAD`<br><br>
- `Logout` This option will sign you out from the page