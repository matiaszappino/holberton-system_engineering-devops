# Changes to our configuration file

changepass {"pass_change":
    path  => "/etc/ssh/ssh_config",
    line  => "    PasswordAuthentication no",
    match =>  "PasswordAuthentication yes",
}
changepass {"Identity_file":
    path => "/etc/ssh/ssh_config",
    line => "    IdentityFile ~/.ssh/holberton",
}
