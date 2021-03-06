hxpro.phpfpm
============

[![Build Status](https://travis-ci.org/hxpro/ansible-role-phpfpm.svg?branch=master)](https://travis-ci.org/hxpro/ansible-role-phpfpm)

Install and configure php-fpm.

This role is under development. Use it on your own risk. Pull requests are welcome.

Requirements
------------

The ipaddr filter requires python's netaddr be installed on the ansible controller

```bash
  pip install netaddr
```

Role Variables
--------------
```
phpfpm_composer_version: "1.9.1"
phpfpm_composer_checksum: "sha256:1f210b9037fcf82670d75892dfc44400f13fe9ada7af9e787f93e50e3b764111"

phpfpm_version: 74
phpfpm_pkg:
  - fpm
  - opcache
  - cli
  - xml
  - common
  - mysqlnd
  - gd
  - pear
  - soap
  - mbstring
  - pdo
  - process
  - pecl-zip

phpfpm_ini:
  - section: PHP
    option: short_open_tag
    value: 'On'
  - section: Date
    option: date.timezone
    value: Europe/Prague

phpfpm_pid: "/run/php-fpm/php-fpm.pid"

phpfpm_user: "apache"
phpfpm_group: "apache"
phpfpm_log_path: "/var/log/php-fpm/"
phpfpm_error_log: "/var/log/php-fpm/error.log"
phpfpm_log_level: "notice"

phpfpm_emergency_restart_threshold: 0
phpfpm_emergency_restart_interval: 0
phpfpm_process_control_timeout: 0

phpfpm_process_max: 128
phpfpm_process_priority:

phpfpm_daemonize: yes

phpfpm_systemd_interval: 10

# phpfpm_rlimit_files:
# phpfpm_rlimit_core:

phpfpm_pools:
  - name: www
    user: apache
    group: apache

    request_slowlog_timeout: 10
    slowlog: "/var/log/php-fpm/www-slow.log"
    request_terminate_timeout: 0
    rlimit_files: 1024
    rlimit_core: 0

    chroot:
    chdir: "/var/www"

    catch_workers_output: yes
    clear_env: no
    security:
      limit_extensions: ".php .php3 .php4 .php5 .php7"

    env:
      HOSTNAME: "$HOSTNAME"
      PATH: "/opt/remi/php{{ phpfpm_version }}/root/usr/bin:/usr/local/bin:/usr/bin:/bin"
      LD_LIBRARY_PATH: "/opt/remi/php{{ phpfpm_version }}/root/usr/lib64"
      TMP: "/tmp"
      TEMP: "/tmp"
      TMPDIR: "/tmp"

    listen:
      address: '127.0.0.1:9000'
      allowed_clients: '127.0.0.1'

    # Process Manager settings
    pm:
      dynamic:
      max_children: 50
      start_servers: 5
      min_spare_servers: 5
      max_spare_servers: 35
      status_path: "/status"
      max_requests: 0

    ping:
      path: "/ping"
      response: "pong"

    php_admin_value:
#      sendmail_path: '/usr/sbin/sendmail -t -i -f www@example.com'
      error_log: "/var/log/php-fpm/www-error.log"
      memory_limit: 128M

    php_flag:
      display_errors: off
      log_errors: on

    php_value:
      session.save_handler: files
      session.save_path: "/var/opt/remi/php{{ phpfpm_version }}/lib/php/session"
      soap.wsdl_cache_dir: "/var/opt/remi/php{{ phpfpm_version }}/lib/php/wsdlcache"
      opcache.file_cache: "/var/opt/remi/php{{ phpfpm_version }}/lib/php/opcache"

```

Known Issues
------------

 - Folders /var/opt/remi/php{{ phpfpm_version }}/lib/php/{opcache,session,wsdlcache} are installed by php-fpm rpm package and them group is set to apache. Do not use this default paths if you would not use group apache.

Dependencies
------------

 - hxpro.epel

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```
- hosts: servers
  roles:
    - role: hxpro.phpfpm
      vars:
        phpfpm_version: 74
```

License
-------

WTFPL

Author Information
------------------

Matěj Koudelka <matej@hxpro.cz>
