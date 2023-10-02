# Puppet code for http header

exec { 'run my shell code':
  command  => 'sudo apt -y update;
               sudo apt -y upgrade;
               sudo apt -y install nginx;
               sudo /var/www/html/index.nginx-debian.html;
               echo "Hello World" >> /var/www/html/index.nginx-debian.html;
               /etc/nginx/sites-enabled/default/sudo sed -i /server_name _;/ a \\trewrite\
             ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
               sudo sed -i "11i \\\t add_header X-Served-By $HOSTNAME always;\n" /etc/nginx/nginx.conf;
               sudo service nginx restart',
  provider => shell,
}
