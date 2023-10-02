# Puppet code for http header

exec {'running code in shell':
    command => 'sudo apt -y update;
                sudo apt -y install nginx;
                echo 'Hello World!' > /var/www/html/index.html;
                sed -i "/server_name _;/ a\\\trewrite ^/redirect_me https://www\
                .youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default;
                echo "Ceci n'est pas une page" > /var/www/html/404.html;
                sed -i "0,/}/ s|}|}\n\n\terror_page 404 /404.html;\n\tlocation = /404.html \
                {\n\t\troot /var/www/html/;\n\t\tinternal;\n\t}|" /etc/nginx/sites-available/default;
                sed -i "/server_name _;/ a\\\tadd_header X-Served-By '$HOSTNAME' always;\n" \
                /etc/nginx/sites-available/default;
                sudo service nginx restart',
    provider => shell
}
