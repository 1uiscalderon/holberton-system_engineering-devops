# Set up your client SSH configuration file so that you can connect to a server without typing a password.
file_line { 'add identity file':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/holberton',
  match  => '^*IdentityFile ~/.ssh/holberton*',
}
file_line {'change pswrd aut':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no',
  match  => '^*PasswordAuthentication*',
}
