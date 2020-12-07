# Manifest that kills a process named killmenow.
exec { 'killmenow':
  command  => 'pkill killmenow',
  provider => 'shell',
  returns  => [0, 1],
}
