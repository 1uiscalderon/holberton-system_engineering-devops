#Change the extension .phpp to .php 
exec { 'Header adition':
  command => 'sudo sed -i "s/phpp/php/" /var/www/html/wp-settings.php',
  path    => ["/usr/bin", "/usr/sbin"],
}
