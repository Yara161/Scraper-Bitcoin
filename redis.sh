wget http://download.redis.io/redis-stable.tar.gz
tar xvzf redis-stable.tar.gz
cd redis-stable
make
make test

cd src
sudo apt install redis-server
j
redis-server
redis-cli ping
redis-cli
ping


