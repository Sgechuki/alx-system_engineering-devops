#Fix Apache is returning a 500 error

exec { 'delete a letter':
        command  => 'sed -i s/class-wp-locale.phpp/class-wp-locale.php/g /var/www/html/wp-settings.php',
        provider => shell,
}
