#  Using strace and tmux to fix wordpress site error
file { '/var/www/html/wp-includes/class-wp-locale.phpp':
    ensure => 'present',
    owner  => 'apache2',
    group  => 'apache2',
    mode   => '0644',
    source => 'puppet:///modules/wordpress/locale/class-wp-locale.phpp'
}
service { 'apache2':
    ensure => running
}