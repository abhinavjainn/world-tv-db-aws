# World TV Database
A backend flask RESTful API application deployed on AWS.

[Application URL(AWS)](http://python-wowtv.eba-ppa7mzyg.eu-west-2.elasticbeanstalk.com/) | Up time 07:00-23:00 GMT everyday.

[Previous instance](https://github.com/abhinavjainn/qmul_cloud-computing-mini-project) of the application was deployed on [Heroku](https://world-tv-db.herokuapp.com/).

# Application Overview

The application “World TV Database” has following main features:

    1. Anyone can use the application to browse the TV shows. Response may be used to read the plot summary, view cast, check reviews etc.
    2. Interested users can create their account and save their own list of TV shows which, for instance, may be used as a watchlist.
    3. Registered users can view or modify their list of TV shows. 
    4. Admin users can delete users, for example, users which have been idle for a long time.

# Application endpoints

1. /browse
2. /register
3. /login
4. /logout
5. /add-to-list
6. /delete-from-list
7. /view-list
8. /delete-user
