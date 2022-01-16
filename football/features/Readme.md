An Aloe test case is called a feature. You program features using two files: a Feature file and a Steps file.

The Feature file consists of statements written in plain English that describe how to configure, execute, and confirm the results of a test. Use the Feature keyword to label the feature and the Scenario keyword to define a user story that you are planning to test. In the example above, the scenario defines a series of steps that explain how to populate the User database table, log a user into the app, and validate the login. All step statements must begin with one of four keywords: Given, When, Then, or And.
The Steps file contains Python functions that are mapped to the Feature file steps using regular expressions.


Run python manage.py harvest and see the following output.


refs : https://testdriven.io/blog/behavior-driven-development-with-django-and-aloe/