###############################################################################
                   Item Catalog Web Application
###############################################################################

1. What Is It?
   -----------
   The Item Catalog Web Application is a Python application that provides a list
   of items within a variety of categories and integrated third party user
   registration and authentication. Authenticated users have the ability to post
   items as well as edit and delete their own items. The application also
   provides JSON endpoints for accessing catalog data.

   This application uses the Flask web application framework and the SQLAlchemy
   Object Relational Mapper. It also uses the oauth2client Python library to
   implement OAuth2 authentication. Users can login to the Item Catalog
   Application using their Google accounts.

   Catalog data can also be accessed via JSON endpoints. Data can be accessed
   from the following URIs:
     All categories:                     /catalog/JSON
     All items from a specific category: /catalog/category/<category_id>/JSON
     Item with the specified ID:         /catalog/item/<item_id>/JSON

   This application was created as partial fulfillment of the Udacity Full
   Stack Web Developer Nanodegree. Specifically, it is Project 5: Item Catalog.

2. Installation
   ------------
   The source code for this application can be obtained from the following
   GitHub repository:
      https://github.com/MickElliott/fsnd-item-catalog.git

   The Item Catalog application consists of the following files:
      application.py
      database_setup.py
      lotsofcategories.py
      catalog.db
      client_secrets.json
      readme.txt
      templates\categories.html
      templates\deleteCategory.html
      templates\deleteItem.html
      templates\editCategory.html
      templates\editItem.html
      templates\header.html
      templates\items.html
      templates\login.html
      templates\main.html
      templates\newCategory.html
      templates\newItem.html
      templates\publicCategories.html
      templates\publicItems.html
      static\styles.css

3. Python Version
   --------------
   This application was developed using Python version 2.7.13

4. Usage
   -----
   1. This application requires that the Flask, SQLAlchemy and oauth2client Python 
      libraries be installed on the user's machine. Alternatively, the user can use
      the virtual machine available in the Udacity OAuth2.0 repository that already 
      contains these libraries. The following steps can be followed to setup this 
      virtual environment:

        a. Clone the following GitHub repository:
            $ git clone https://github.com/Udacity/OAuth2.0.git

        b. Copy the Item Catalog code into the /catalog directory of the OAuth2.0
           repository.

        c. Install Vagrant and VirtualBox. See the following URLs:
            https://www.vagrantup.com/
            https://www.virtualbox.com/
           Instructions for installing these applications can be found on the Udacity
           website:
            https://www.udacity.com/wiki/ud088/vagrant

   2. Launch the virtual machine by typing the following commands from the oath
      directory (containing the VagrantFile file):
        $ vagrant up
        $ vagrant ssh

   4. Change directory to the catalog directory:
        $ cd /vagrant/catalog

   5. Create an empty catalog database:
        $ python database_setup.py

   6. (Optional) Sample catalog data can be added to the database by using the following
      command:
        $ python lotsofcategories.py

   7. The web application can be launched with the following command:
        $ python application.py

   8. The web application can now be accessed by visiting:
        http://localhost:5000
