#Fix Too many open files

exec { 'raise limit':
        command  => 'sed -i s/ULIMIT="-n 15"/ULIMIT="-n 4096"/g /etc/default/nginx',
        provider => shell,
}
