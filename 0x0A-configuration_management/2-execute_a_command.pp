# Manifest that kills a process named killmenow

exec { "killmenow":
    path => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
    provider => 'shell'
    command => "pkill killmenow",
}