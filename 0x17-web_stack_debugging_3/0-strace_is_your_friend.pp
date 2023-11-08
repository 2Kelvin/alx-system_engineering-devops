# Using strace and tmux to fix wordpress site error
file { '/var/www/html/wp-includes/class-wp-locale.phpp':
    ensure => 'present',
    source => '/var/www/html/wp-includes/class-wp-locale.phpp'
}