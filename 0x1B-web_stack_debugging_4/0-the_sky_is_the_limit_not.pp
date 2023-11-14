# Add the number of files nginx can open
exec { 'increase open file limit':
    command => "sed -i 's/15/65536/g' /etc/default/nginx; sudo service nginx restart",
    path    => ['/bin', '/usr/bin', '/usr/sbin']
}