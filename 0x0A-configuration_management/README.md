0x0A Configuration management
=============================

* Foundations - System engineering & DevOps ― CI/CD
* By Sylvain Kalache, co-founder at Holberton School
* Ongoing project - started 03-31-2021, must end by 04-06-2021 (in 1 day) - you're done with 0% of tasks.
* Checker was released at 04-04-2021 09:36 AM
* QA review fully automated.

Background Context
------------------

[![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2019/6/6a0a8024f2b1c47a9d1e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210405%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210405T024650Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=cab76af560163bc9f77b813acc60d3927ef8a26abed919870ca3da70ff768ff9)](https://youtu.be/ogYLFyp68cI)

When I was working for SlideShare, I worked on an auto-remediation tool called [Skynet](/rltoken/ftFvBjxNPLoWcF9eHaK8yw "Skynet") that monitored, scaled and fixed Cloud infrastructure. I was using a parallel job-execution system called MCollective that allowed me to execute commands to one or multiple servers at the same time. I could apply an action to a selected set of servers by applying a filter such as the server’s hostname or any other metadata we had (server type, server environment…). At some point, a bug was present in my code that sent `nil` to the filter method.

There were 2 pieces of bad news:

1.  When MCollective receives `nil` as an argument for its filter method, it takes this to mean ‘all servers’
2.  The action I sent was to terminate the selected servers

I started the parallel job-execution and after some time, I realized that it was taking longer than expected. Looking at logs I realized that I was shutting down SlideShare’s entire document conversion environment. Actually, 75% of all our conversion infrastructure servers had been shut down, resulting in users not able to convert their PDFs, powerpoints, and videos… Pretty bad!

Thanks to Puppet, we were able to restore our infrastructure to normal operation in under 1H, pretty impressive. Imagine if we had to do everything manually: launching the servers, configuring and linking them, importing application code, starting every process, and obviously, fixing all the bugs (you should know by now that complicated infrastructure always goes sideways)…

Obviously writing Puppet code for your infrastructure requires an investment of time and energy, but in the long term, it is for sure a must-have.

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/292/4i8il3B.gif)

That was me ^_^‘: [https://twitter.com/devopsreact/status/836971570136375296](/rltoken/uHU1llO2UZXg8_funEgpJA "https://twitter.com/devopsreact/status/836971570136375296")

Resources
---------

**Read or watch**:

* [Intro to Configuration Management](/rltoken/r-NmkYO8bxIKp2qEx2ZjKQ "Intro to Configuration Management")
* [Puppet resource type: file](/rltoken/fuhnsI9_1_F4GrHwGT3GxA "Puppet resource type: file") (_check “Resource types” for all manifest types in the left menu_)
* [Puppet’s Declarative Language: Modeling Instead of Scripting](/rltoken/Fqmb5rnChQgYAypvKoTxAQ "Puppet's Declarative Language: Modeling Instead of Scripting")
* [Puppet lint](/rltoken/oezu0m_hJ8nEVA6a9o17Tw "Puppet lint")
* [Puppet emacs mode](/rltoken/N70cVw8mG3707He-OxjP1w "Puppet emacs mode")

Requirements
------------

### General

* All your files will be interpreted on Ubuntu 14.04 LTS
* All your files should end with a new line
* A `README.md` file at the root of the folder of the project is mandatory
* Your Puppet manifests must pass `puppet-lint` version 2.1.1 without any errors
* Your Puppet manifests must run without error
* Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about
* Your Puppet manifests files must end with the extension `.pp`

Note on Versioning
------------------

Your Ubuntu 14.04 VM should have Puppet 3.4 preinstalled.

You do **not** need to attempt to upgrade versions. This project is simply a set of tasks to familiarize you with the basic level syntax which is virtually identical in newer versions of Puppet.

The linked documentation is to Puppet 3.8 because the 3.4 documentation has been archived and is therefore more challenging to navigate. If you would like to upgrade anyway, [click here](/rltoken/e6imCENcgeeIw6JV5ltSkw "click here") (this will not affect how your code is checked). [Puppet 5 Docs](/rltoken/_xOod_Lzz8WKTbhpG5SWLQ "Puppet 5 Docs")

### Install `puppet-lint`

    $ apt-get install -y ruby
    $ gem install puppet-lint -v 2.1.1
    

Tasks
-----

### 0\. Create a file

mandatory

Using Puppet, create a file in `/tmp`.

Requirements:

* File path is `/tmp/holberton`
* File permission is `0744`
* File owner is `www-data`
* File group is `www-data`
* File contains `I love Puppet`

Example:

    root@6712bef7a528:~# puppet-lint --version
    puppet-lint 2.1.1
    root@6712bef7a528:~# puppet-lint 0-create_a_file.pp
    root@6712bef7a528:~# 
    root@6712bef7a528:~# puppet apply 0-create_a_file.pp
    Notice: Compiled catalog for 6712bef7a528.ec2.internal in environment production in 0.04 seconds
    Notice: /Stage[main]/Main/File[holberton]/ensure: defined content as '{md5}f1b70c2a42a98d82224986a612400db9'
    Notice: Finished catalog run in 0.03 seconds
    root@6712bef7a528:~#
    root@6712bef7a528:~# ls -l /tmp/holberton
    -rwxr--r-- 1 www-data www-data 13 Mar 19 23:12 /tmp/holberton
    root@6712bef7a528:~# cat /tmp/holberton
    I love Puppetroot@6712bef7a528:~#
    

**Repo:**

* GitHub repository: `holberton-system_engineering-devops`
* Directory: `0x0A-configuration_management`
* File: `0-create_a_file.pp`

Done?! Help

×

#### Students who are done with "0. Create a file"

Check your code

×

#### Correction of "0. Create a file"

Start a new test

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

  Get a sandbox

×

####   Sandboxes

Each sandbox will be available for 8 months max

**Ubuntu 14.04 - 292**

You have reached the limit of sandboxes you can spawn (5)  
Please terminate a running sandbox before starting a new one

[My sandboxes](/dashboards/my_containers)

| Access from anywhere | Access from campus | Detailed port mapping |
| --- | --- | --- |
| * **HTTP:**<br>    <br>* **HTTPS:**<br>* **User:**<br>* **Password:**<br>* **SSH:**<br>* **SFTP:**<br>* **SCP:** | * **HTTP:**<br>    <br>* **HTTPS:**<br>* **User:**<br>* **Password:**<br>* **SSH:** |     |

**Ports mapping**  
Each exposed port is mapped to another one. Example: the port SSH **22** is mapped to the port **33511**.

### 1\. Install a package

mandatory

Using Puppet, install `puppet-lint`.

Requirements:

* Install `puppet-lint`
* Version must be `2.1.1`

Example:

    root@d391259bf577:/# puppet apply 1-install_a_package.pp
    Notice: Compiled catalog for d391259bf577.hsd1.ca.comcast.net in environment production in 0.10 seconds
    Notice: /Stage[main]/Main/Package[puppet-lint]/ensure: created
    Notice: Finished catalog run in 2.83 seconds
    root@d391259bf577:/# gem list
    
    *** LOCAL GEMS ***
    
    puppet-lint (2.1.1)
    root@d391259bf577:/#
    

**Repo:**

* GitHub repository: `holberton-system_engineering-devops`
* Directory: `0x0A-configuration_management`
* File: `1-install_a_package.pp`

Done?! Help

×

#### Students who are done with "1. Install a package"

Check your code

×

#### Correction of "1. Install a package"

Start a new test

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

  Get a sandbox

×

####   Sandboxes

Each sandbox will be available for 8 months max

**Ubuntu 14.04 - 292**

You have reached the limit of sandboxes you can spawn (5)  
Please terminate a running sandbox before starting a new one

[My sandboxes](/dashboards/my_containers)

| Access from anywhere | Access from campus | Detailed port mapping |
| --- | --- | --- |
| * **HTTP:**<br>    <br>* **HTTPS:**<br>* **User:**<br>* **Password:**<br>* **SSH:**<br>* **SFTP:**<br>* **SCP:** | * **HTTP:**<br>    <br>* **HTTPS:**<br>* **User:**<br>* **Password:**<br>* **SSH:** |     |

**Ports mapping**  
Each exposed port is mapped to another one. Example: the port SSH **22** is mapped to the port **33511**.

### 2\. Execute a command

mandatory

Using Puppet, create a manifest that kills a process named `killmenow`.

Requirements:

* Must use the `exec` Puppet resource
* Must use `pkill`

Example:

Terminal #0 - starting my process

    root@d391259bf577:/# cat killmenow
    #!/bin/bash
    while [[ true ]]
    do
        sleep 2
    done
    
    root@d391259bf577:/# ./killmenow
    

Terminal #1 - executing my manifest

    root@d391259bf577:/# puppet apply 2-execute_a_command.pp
    Notice: Compiled catalog for d391259bf577.hsd1.ca.comcast.net in environment production in 0.01 seconds
    Notice: /Stage[main]/Main/Exec[killmenow]/returns: executed successfully
    Notice: Finished catalog run in 0.10 seconds
    root@d391259bf577:/# 
    

Terminal #0 - process has been terminated

    root@d391259bf577:/# ./killmenow
    Terminated
    root@d391259bf577:/#
    

**Repo:**

* GitHub repository: `holberton-system_engineering-devops`
* Directory: `0x0A-configuration_management`
* File: `2-execute_a_command.pp`

Done?! Help

×

#### Students who are done with "2. Execute a command"

Check your code

×

#### Correction of "2. Execute a command"

Start a new test

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

  Get a sandbox

×

####   Sandboxes

Each sandbox will be available for 8 months max

**Ubuntu 14.04 - 292**

You have reached the limit of sandboxes you can spawn (5)  
Please terminate a running sandbox before starting a new one

[My sandboxes](/dashboards/my_containers)

| Access from anywhere | Access from campus | Detailed port mapping |
| --- | --- | --- |
| * **HTTP:**<br>    <br>* **HTTPS:**<br>* **User:**<br>* **Password:**<br>* **SSH:**<br>* **SFTP:**<br>* **SCP:** | * **HTTP:**<br>    <br>* **HTTPS:**<br>* **User:**<br>* **Password:**<br>* **SSH:** |     |

**Ports mapping**  
Each exposed port is mapped to another one. Example: the port SSH **22** is mapped to the port **33511**.