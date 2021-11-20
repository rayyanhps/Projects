#sudo apt-get install postgresql libpq-dev postgresql-client postgresql-client-common
sudo -i -u postgres
createuser maebot -P --interactive
createdb wldb