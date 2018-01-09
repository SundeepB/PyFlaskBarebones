rm -rf migrations
rm -f ./barebones.db
flask db init
flask db migrate
flask db upgrade
