# A manifest that kills process killmenow
exec { 'terminateProcess':
  command => 'pkill -f killmenow',
  path    => '/usr/bin'
}
