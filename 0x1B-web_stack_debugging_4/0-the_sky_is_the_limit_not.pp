#Change the open file
exec { 'Open files':
  command => 'sudo sed -i "s/15/4000/" /etc/default/nginx; 
              sudo service nginx restart',
  path    => ['/usr/bin', '/usr/sbin'],
}
