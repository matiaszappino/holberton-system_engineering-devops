# Changes to our configuration file

file_line {"password_change":
    path  => "/etc/ssh/ssh_config",
    line  => "    PasswordAuthentication no",
    match =>  "PasswordAuthentication yes",
}
file_line {"identity_change":
    path => "/etc/ssh/ssh_config",
    line => "    IdentityFile ~/.ssh/holberton",
}
