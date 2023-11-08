#  Using strace and tmux to fix wordpress site error
$correct_fname = '/var/www/html/wp-settings.php'
exec { 'fix file'
    command => "sed -i 's/phpp/php/g' ${correct_fname}",
    path    => ['/bin', '/usr/bin']
}