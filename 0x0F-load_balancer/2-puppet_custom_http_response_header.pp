# Configure an Nginx server using Puppet instead of Bash

package { 'nginx':
  ensure => installed,
}

file { 'index.html':
  content => 'Holberton School',
  path    => '/var/www/html/index.html'
}
file_line { 'append instruction':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  after  => 'server_name _;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}
file_line { 'Header instruction':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  after  => 'server_name _;',
  line   => 'add_header X-Served-By "$HOSTNAME";',
  require => Package['nginx'],
}
service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
