# Installing and configuring nginx puppet style
exec { 'installation':
  command  => 'sudo apt -y update ; sudo apt -y install nginx',
  provider => shell
}

package { 'nginx':
  ensure => 'present'
}

exec { 'pageHello':
  command  => "echo 'Hello World!' | sudo tee /var/www/html/index.html",
  provider => shell
}

exec { 'redirect':
  command  => [
    'sudo',
    'sed',
    '-i',
    '"s/listen 80 default_server;/listen 80 default_server;\\n\\tlocation \/redirect_me {\\n\\t\\treturn 301 https:\/\/www.youtube.com/watch?v=QH2-TGUlwu4\/;\\n\\t}/"',
    '/etc/nginx/sites-available/default',
  ],
  provider => shell
}


exec { 'restart and update nginx':
  command  => 'sudo service nginx restart',
  provider => shell
}
