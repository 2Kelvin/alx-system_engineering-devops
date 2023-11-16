# Still increasing file open numbers
exec { 'increase hard file numbers':
    provider => shell,
    command  => "sudo sed -i 's/nofile 5/nofile 50000/' /etc/security/limits.conf",
    before   => Exec['fileTwo']
}
exec { 'fileTwo':
    provider => shell,
    command  => "sudo sed -i 's/nofile 4/nofile 40000/' /etc/security/limits.conf",
}