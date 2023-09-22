# A manifest that kills process killmenow
exec { 'terminateProcess':
  command => 'pkill -9 killmenow'
}
