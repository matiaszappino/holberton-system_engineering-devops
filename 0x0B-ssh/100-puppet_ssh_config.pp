# Changes to our configuration file

changepass {"pass_change":
    path  => "/etc/ssh/ssh_config",
    match =>  "PasswordAuthentication yes",
    line  => "    PasswordAuthentication no",
}
changepass {"Identity_file":
    path => "/etc/ssh/ssh_config",
    line => "    IdentityFile ~/.ssh/holberton",
}
