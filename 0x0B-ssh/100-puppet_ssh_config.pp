# Client configuration file using puppet
file_line { 'Private school key location':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/school'
}

file_line { 'No password for school':
  ensure => 'present',
  line   => '    PasswordAuthentication no',
  path   => '/etc/ssh/ssh_config'
}
