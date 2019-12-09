import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_phpfpm_running_and_enabled(host):
    phpfpm = host.service("php74-php-fpm")
    assert phpfpm.is_running
    assert phpfpm.is_enabled


def test_composer_installed(host):
    assert host.find_command('composer')
