# Using strace and tmux to fix wordpress site error
exec { 'fix file':
    command  => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
    provider => shell,
}