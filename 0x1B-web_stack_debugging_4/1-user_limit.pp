# Still increasing file open numbers
exec { 'increase soft file numbers':
    command => "sed -i '/holberton soft/s/4/65536' /etc/security/limits.conf",
    path    => '/usr/local/bin/:/bin/'
}
exec { 'increase hard file numbers':
    command => "sed -i '/holberton hard/s/5/65536' /etc/security/limits.conf",
    path    => '/usr/local/bin/:/bin/'
}