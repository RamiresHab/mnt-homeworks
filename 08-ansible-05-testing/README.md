# Домашнее задание к занятию "5. Тестирование roles"

## Подготовка к выполнению
1. Установите molecule: `pip3 install "molecule==3.5.2"`
2. Выполните `docker pull aragast/netology:latest` -  это образ с podman, tox и несколькими пайтонами (3.7 и 3.9) внутри

## Основная часть

Наша основная цель - настроить тестирование наших ролей. Задача: сделать сценарии тестирования для vector. Ожидаемый результат: все сценарии успешно проходят тестирование ролей.

### Molecule

1. Запустите  `molecule test -s centos7` внутри корневой директории clickhouse-role, посмотрите на вывод команды.

<details>
<summary><b>ansible-clickhouse git:(master) ✗ molecule test -s centos_7</b></summary>

```
INFO     centos_7 scenario test matrix: dependency, lint, cleanup, destroy, syntax, create, prepare, converge, idempotence, side_effect, verify, cleanup, destroy
INFO     Performing prerun with role_name_check=0...
INFO     Set ANSIBLE_LIBRARY=/Users/ro.khabibullin/.cache/ansible-compat/b9a93c/modules:/Users/ro.khabibullin/.ansible/plugins/modules:/usr/share/ansible/plugins/modules
INFO     Set ANSIBLE_COLLECTIONS_PATH=/Users/ro.khabibullin/.cache/ansible-compat/b9a93c/collections:/Users/ro.khabibullin/.ansible/collections:/usr/share/ansible/collections
INFO     Set ANSIBLE_ROLES_PATH=/Users/ro.khabibullin/.cache/ansible-compat/b9a93c/roles:/Users/ro.khabibullin/.ansible/roles:/usr/share/ansible/roles:/etc/ansible/roles
INFO     Using /Users/ro.khabibullin/.cache/ansible-compat/b9a93c/roles/alexeysetevoi.clickhouse symlink to current repository in order to enable Ansible to find the role using its expected full name.
INFO     Running centos_7 > dependency
WARNING  Skipping, missing the requirements file.
WARNING  Skipping, missing the requirements file.
INFO     Running centos_7 > lint
WARNING  Listing 79 violation(s) that are fatal
fqcn[action-core]: Use FQCN for builtin module actions (set_fact).
handlers/main.yml:3 Use `ansible.builtin.set_fact` or `ansible.legacy.set_fact` instead.

schema[meta]: 2.8 is not of type 'string'
meta/main.yml:1  Returned errors will not include exact line numbers, but they will mention
the schema name being used as a tag, like ``schema[playbook]``,
``schema[tasks]``.

This rule is not skippable and stops further processing of the file.

If incorrect schema was picked, you might want to either:

* move the file to standard location, so its file is detected correctly.
* use ``kinds:`` option in linter config to help it pick correct file type.


fqcn[action-core]: Use FQCN for builtin module actions (include_role).
molecule/centos_7/converge.yml:5 Use `ansible.builtin.include_role` or `ansible.legacy.include_role` instead.

fqcn[action-core]: Use FQCN for builtin module actions (assert).
molecule/centos_7/verify.yml:8 Use `ansible.builtin.assert` or `ansible.legacy.assert` instead.

fqcn[action-core]: Use FQCN for builtin module actions (include_role).
molecule/centos_8/converge.yml:5 Use `ansible.builtin.include_role` or `ansible.legacy.include_role` instead.

fqcn[action-core]: Use FQCN for builtin module actions (assert).
molecule/centos_8/verify.yml:8 Use `ansible.builtin.assert` or `ansible.legacy.assert` instead.

schema[inventory]: None is not of type 'object'
molecule/resources/inventory/hosts.yml:1  Returned errors will not include exact line numbers, but they will mention
the schema name being used as a tag, like ``schema[playbook]``,
``schema[tasks]``.

This rule is not skippable and stops further processing of the file.

If incorrect schema was picked, you might want to either:

* move the file to standard location, so its file is detected correctly.
* use ``kinds:`` option in linter config to help it pick correct file type.


fqcn[action-core]: Use FQCN for builtin module actions (include_role).
molecule/resources/playbooks/converge.yml:5 Use `ansible.builtin.include_role` or `ansible.legacy.include_role` instead.

fqcn[action-core]: Use FQCN for builtin module actions (include_role).
molecule/ubuntu_focal/converge.yml:5 Use `ansible.builtin.include_role` or `ansible.legacy.include_role` instead.

fqcn[action-core]: Use FQCN for builtin module actions (assert).
molecule/ubuntu_focal/verify.yml:8 Use `ansible.builtin.assert` or `ansible.legacy.assert` instead.

fqcn[action-core]: Use FQCN for builtin module actions (set_fact).
tasks/configure/db.yml:2 Use `ansible.builtin.set_fact` or `ansible.legacy.set_fact` instead.

jinja[spacing]: Jinja2 spacing could be improved: clickhouse-client -h 127.0.0.1 --port {{ clickhouse_tcp_secure_port | default(clickhouse_tcp_port) }}{{' --secure' if clickhouse_tcp_secure_port is defined else '' }} -> clickhouse-client -h 127.0.0.1 --port {{ clickhouse_tcp_secure_port | default(clickhouse_tcp_port) }}{{ ' --secure' if clickhouse_tcp_secure_port is defined else '' }} (warning)
tasks/configure/db.yml:2 Jinja2 template rewrite recommendation: `clickhouse-client -h 127.0.0.1 --port {{ clickhouse_tcp_secure_port | default(clickhouse_tcp_port) }}{{ ' --secure' if clickhouse_tcp_secure_port is defined else '' }}`.

no-free-form: Avoid using free-form when calling module actions. (set_fact)
tasks/configure/db.yml:2 Task/Handler: Set ClickHose Connection String

fqcn[action-core]: Use FQCN for builtin module actions (command).
tasks/configure/db.yml:5 Use `ansible.builtin.command` or `ansible.legacy.command` instead.

fqcn[action-core]: Use FQCN for builtin module actions (command).
tasks/configure/db.yml:11 Use `ansible.builtin.command` or `ansible.legacy.command` instead.

no-changed-when: Commands should not change things if nothing needs doing.
tasks/configure/db.yml:11 Task/Handler: Config | Delete database config

fqcn[action-core]: Use FQCN for builtin module actions (command).
tasks/configure/db.yml:20 Use `ansible.builtin.command` or `ansible.legacy.command` instead.

no-changed-when: Commands should not change things if nothing needs doing.
tasks/configure/db.yml:20 Task/Handler: Config | Create database config

fqcn[action-core]: Use FQCN for builtin module actions (template).
tasks/configure/dict.yml:2 Use `ansible.builtin.template` or `ansible.legacy.template` instead.

fqcn[action-core]: Use FQCN for builtin module actions (file).
tasks/configure/sys.yml:2 Use `ansible.builtin.file` or `ansible.legacy.file` instead.

fqcn[action-core]: Use FQCN for builtin module actions (file).
tasks/configure/sys.yml:17 Use `ansible.builtin.file` or `ansible.legacy.file` instead.

fqcn[action-core]: Use FQCN for builtin module actions (file).
tasks/configure/sys.yml:26 Use `ansible.builtin.file` or `ansible.legacy.file` instead.

fqcn[action-core]: Use FQCN for builtin module actions (template).
tasks/configure/sys.yml:35 Use `ansible.builtin.template` or `ansible.legacy.template` instead.

fqcn[action-core]: Use FQCN for builtin module actions (template).
tasks/configure/sys.yml:45 Use `ansible.builtin.template` or `ansible.legacy.template` instead.

fqcn[action-core]: Use FQCN for builtin module actions (template).
tasks/configure/sys.yml:54 Use `ansible.builtin.template` or `ansible.legacy.template` instead.

fqcn[action-core]: Use FQCN for builtin module actions (template).
tasks/configure/sys.yml:65 Use `ansible.builtin.template` or `ansible.legacy.template` instead.

fqcn[action-core]: Use FQCN for builtin module actions (template).
tasks/configure/sys.yml:76 Use `ansible.builtin.template` or `ansible.legacy.template` instead.

fqcn[action-core]: Use FQCN for builtin module actions (lineinfile).
tasks/configure/sys.yml:87 Use `ansible.builtin.lineinfile` or `ansible.legacy.lineinfile` instead.

fqcn[action-core]: Use FQCN for builtin module actions (apt_key).
tasks/install/apt.yml:5 Use `ansible.builtin.apt_key` or `ansible.legacy.apt_key` instead.

fqcn[action-core]: Use FQCN for builtin module actions (apt_repository).
tasks/install/apt.yml:12 Use `ansible.builtin.apt_repository` or `ansible.legacy.apt_repository` instead.

fqcn[action-core]: Use FQCN for builtin module actions (apt_repository).
tasks/install/apt.yml:20 Use `ansible.builtin.apt_repository` or `ansible.legacy.apt_repository` instead.

fqcn[action-core]: Use FQCN for builtin module actions (apt).
tasks/install/apt.yml:27 Use `ansible.builtin.apt` or `ansible.legacy.apt` instead.

fqcn[action-core]: Use FQCN for builtin module actions (apt).
tasks/install/apt.yml:36 Use `ansible.builtin.apt` or `ansible.legacy.apt` instead.

fqcn[action-core]: Use FQCN for builtin module actions (copy).
tasks/install/apt.yml:45 Use `ansible.builtin.copy` or `ansible.legacy.copy` instead.

risky-file-permissions: File permissions unset or incorrect.
tasks/install/apt.yml:45 Task/Handler: Hold specified version during APT upgrade | Package installation

fqcn[action-core]: Use FQCN for builtin module actions (rpm_key).
tasks/install/dnf.yml:5 Use `ansible.builtin.rpm_key` or `ansible.legacy.rpm_key` instead.

fqcn[action-core]: Use FQCN for builtin module actions (yum_repository).
tasks/install/dnf.yml:12 Use `ansible.builtin.yum_repository` or `ansible.legacy.yum_repository` instead.

fqcn[action-core]: Use FQCN for builtin module actions (dnf).
tasks/install/dnf.yml:24 Use `ansible.builtin.dnf` or `ansible.legacy.dnf` instead.

fqcn[action-core]: Use FQCN for builtin module actions (dnf).
tasks/install/dnf.yml:33 Use `ansible.builtin.dnf` or `ansible.legacy.dnf` instead.

fqcn[action-core]: Use FQCN for builtin module actions (yum_repository).
tasks/install/yum.yml:5 Use `ansible.builtin.yum_repository` or `ansible.legacy.yum_repository` instead.

fqcn[action-core]: Use FQCN for builtin module actions (yum).
tasks/install/yum.yml:16 Use `ansible.builtin.yum` or `ansible.legacy.yum` instead.

fqcn[action-core]: Use FQCN for builtin module actions (yum).
tasks/install/yum.yml:25 Use `ansible.builtin.yum` or `ansible.legacy.yum` instead.

fqcn[action-core]: Use FQCN for builtin module actions (include_vars).
tasks/main.yml:3 Use `ansible.builtin.include_vars` or `ansible.legacy.include_vars` instead.

fqcn[action-core]: Use FQCN for builtin module actions (include_tasks).
tasks/main.yml:14 Use `ansible.builtin.include_tasks` or `ansible.legacy.include_tasks` instead.

name[missing]: All tasks should be named.
tasks/main.yml:14 Task/Handler: include_tasks precheck.yml

fqcn[action-core]: Use FQCN for builtin module actions (include_tasks).
tasks/main.yml:17 Use `ansible.builtin.include_tasks` or `ansible.legacy.include_tasks` instead.

name[missing]: All tasks should be named.
tasks/main.yml:17 Task/Handler: include_tasks params.yml

fqcn[action-core]: Use FQCN for builtin module actions (include_tasks).
tasks/main.yml:20 Use `ansible.builtin.include_tasks` or `ansible.legacy.include_tasks` instead.

name[missing]: All tasks should be named.
tasks/main.yml:20 Task/Handler: include_tasks file={{ lookup('first_found', params) }} apply={'tags': ['install'], '__line__': 22, '__file__': PosixPath('tasks/main.yml')}

fqcn[action-core]: Use FQCN for builtin module actions (include_tasks).
tasks/main.yml:32 Use `ansible.builtin.include_tasks` or `ansible.legacy.include_tasks` instead.

name[missing]: All tasks should be named.
tasks/main.yml:32 Task/Handler: include_tasks file=configure/sys.yml apply={'tags': ['config', 'config_sys'], '__line__': 34, '__file__': PosixPath('tasks/main.yml')}

fqcn[action-core]: Use FQCN for builtin module actions (meta).
tasks/main.yml:39 Use `ansible.builtin.meta` or `ansible.legacy.meta` instead.

fqcn[action-core]: Use FQCN for builtin module actions (include_tasks).
tasks/main.yml:42 Use `ansible.builtin.include_tasks` or `ansible.legacy.include_tasks` instead.

name[missing]: All tasks should be named.
tasks/main.yml:42 Task/Handler: include_tasks service.yml

fqcn[action-core]: Use FQCN for builtin module actions (wait_for).
tasks/main.yml:45 Use `ansible.builtin.wait_for` or `ansible.legacy.wait_for` instead.

fqcn[action-core]: Use FQCN for builtin module actions (include_tasks).
tasks/main.yml:51 Use `ansible.builtin.include_tasks` or `ansible.legacy.include_tasks` instead.

name[missing]: All tasks should be named.
tasks/main.yml:51 Task/Handler: include_tasks file=configure/db.yml apply={'tags': ['config', 'config_db'], '__line__': 53, '__file__': PosixPath('tasks/main.yml')}

fqcn[action-core]: Use FQCN for builtin module actions (include_tasks).
tasks/main.yml:58 Use `ansible.builtin.include_tasks` or `ansible.legacy.include_tasks` instead.

name[missing]: All tasks should be named.
tasks/main.yml:58 Task/Handler: include_tasks file=configure/dict.yml apply={'tags': ['config', 'config_dict'], '__line__': 60, '__file__': PosixPath('tasks/main.yml')}

fqcn[action-core]: Use FQCN for builtin module actions (include_tasks).
tasks/main.yml:65 Use `ansible.builtin.include_tasks` or `ansible.legacy.include_tasks` instead.

name[missing]: All tasks should be named.
tasks/main.yml:65 Task/Handler: include_tasks file=remove.yml apply={'tags': ['remove'], '__line__': 67, '__file__': PosixPath('tasks/main.yml')}

fqcn[action-core]: Use FQCN for builtin module actions (set_fact).
tasks/params.yml:3 Use `ansible.builtin.set_fact` or `ansible.legacy.set_fact` instead.

fqcn[action-core]: Use FQCN for builtin module actions (set_fact).
tasks/params.yml:7 Use `ansible.builtin.set_fact` or `ansible.legacy.set_fact` instead.

fqcn[action-core]: Use FQCN for builtin module actions (command).
tasks/precheck.yml:1 Use `ansible.builtin.command` or `ansible.legacy.command` instead.

fqcn[action-core]: Use FQCN for builtin module actions (fail).
tasks/precheck.yml:5 Use `ansible.builtin.fail` or `ansible.legacy.fail` instead.

fqcn[action-core]: Use FQCN for builtin module actions (file).
tasks/remove.yml:3 Use `ansible.builtin.file` or `ansible.legacy.file` instead.

fqcn[action-core]: Use FQCN for builtin module actions (include_tasks).
tasks/remove.yml:15 Use `ansible.builtin.include_tasks` or `ansible.legacy.include_tasks` instead.

name[missing]: All tasks should be named.
tasks/remove.yml:15 Task/Handler: include_tasks remove/{{ ansible_pkg_mgr }}.yml

fqcn[action-core]: Use FQCN for builtin module actions (apt).
tasks/remove/apt.yml:5 Use `ansible.builtin.apt` or `ansible.legacy.apt` instead.

fqcn[action-core]: Use FQCN for builtin module actions (apt_repository).
tasks/remove/apt.yml:12 Use `ansible.builtin.apt_repository` or `ansible.legacy.apt_repository` instead.

fqcn[action-core]: Use FQCN for builtin module actions (apt_key).
tasks/remove/apt.yml:18 Use `ansible.builtin.apt_key` or `ansible.legacy.apt_key` instead.

fqcn[action-core]: Use FQCN for builtin module actions (dnf).
tasks/remove/dnf.yml:5 Use `ansible.builtin.dnf` or `ansible.legacy.dnf` instead.

fqcn[action-core]: Use FQCN for builtin module actions (yum_repository).
tasks/remove/dnf.yml:12 Use `ansible.builtin.yum_repository` or `ansible.legacy.yum_repository` instead.

fqcn[action-core]: Use FQCN for builtin module actions (rpm_key).
tasks/remove/dnf.yml:19 Use `ansible.builtin.rpm_key` or `ansible.legacy.rpm_key` instead.

fqcn[action-core]: Use FQCN for builtin module actions (yum).
tasks/remove/yum.yml:5 Use `ansible.builtin.yum` or `ansible.legacy.yum` instead.

fqcn[action-core]: Use FQCN for builtin module actions (yum_repository).
tasks/remove/yum.yml:12 Use `ansible.builtin.yum_repository` or `ansible.legacy.yum_repository` instead.

fqcn[action-core]: Use FQCN for builtin module actions (service).
tasks/service.yml:3 Use `ansible.builtin.service` or `ansible.legacy.service` instead.

name[template]: Jinja templates should only be at the end of 'name'
tasks/service.yml:3 Task/Handler: Ensure {{ clickhouse_service }} is enabled: {{ clickhouse_service_enable }} and state: {{ clickhouse_service_ensure }}

jinja[spacing]: Jinja2 spacing could be improved: deb http://repo.yandex.ru/clickhouse/{{ansible_distribution_release}} stable main -> deb http://repo.yandex.ru/clickhouse/{{ ansible_distribution_release }} stable main (warning)
vars/debian.yml:4 Jinja2 template rewrite recommendation: `deb http://repo.yandex.ru/clickhouse/{{ ansible_distribution_release }} stable main`.

Read documentation for instructions on how to ignore specific rule violations.

                       Rule Violation Summary                       
 count tag                    profile    rule associated tags       
     2 jinja[spacing]         basic      formatting (warning)       
     1 schema[inventory]      basic      core                       
     1 schema[meta]           basic      core                       
     9 name[missing]          basic      idiom                      
     1 name[template]         moderate   idiom                      
     1 no-free-form           moderate   syntax, risk               
     1 risky-file-permissions safety     unpredictability           
     2 no-changed-when        shared     command-shell, idempotency 
    61 fqcn[action-core]      production formatting                 

Failed after min profile: 77 failure(s), 2 warning(s) on 56 files.
INFO     Running centos_7 > cleanup
WARNING  Skipping, cleanup playbook not configured.
INFO     Running centos_7 > destroy
INFO     Sanity checks: 'docker'
[WARNING]: Error getting vault password file (datatools): The vault password
file /Users/ro.khabibullin/.vault/datatools_vault was not found
[WARNING]: Error getting vault password file (getstream): The vault password
file /Users/ro.khabibullin/.vault/getstream was not found

PLAY [Destroy] *****************************************************************

TASK [Set async_dir for HOME env] **********************************************
ok: [localhost]

TASK [Destroy molecule instance(s)] ********************************************
changed: [localhost] => (item=centos_7)

TASK [Wait for instance(s) deletion to complete] *******************************
FAILED - RETRYING: [localhost]: Wait for instance(s) deletion to complete (300 retries left).
ok: [localhost] => (item=centos_7)

TASK [Delete docker networks(s)] ***********************************************
skipping: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=3    changed=1    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0

INFO     Running centos_7 > syntax
[WARNING]: Error getting vault password file (datatools): The vault password
file /Users/ro.khabibullin/.vault/datatools_vault was not found
[WARNING]: Error getting vault password file (getstream): The vault password
file /Users/ro.khabibullin/.vault/getstream was not found

playbook: /Users/ro.khabibullin/Projects/netology/mnt-homeworks/08-ansible-05-testing/ansible-clickhouse/molecule/resources/playbooks/converge.yml
INFO     Running centos_7 > create
[WARNING]: Error getting vault password file (datatools): The vault password
file /Users/ro.khabibullin/.vault/datatools_vault was not found
[WARNING]: Error getting vault password file (getstream): The vault password
file /Users/ro.khabibullin/.vault/getstream was not found

PLAY [Create] ******************************************************************

TASK [Set async_dir for HOME env] **********************************************
ok: [localhost]

TASK [Log into a Docker registry] **********************************************
skipping: [localhost] => (item=None) 
skipping: [localhost]

TASK [Check presence of custom Dockerfiles] ************************************
ok: [localhost] => (item={'capabilities': ['SYS_ADMIN'], 'command': '/usr/sbin/init', 'dockerfile': '../resources/Dockerfile.j2', 'env': {'ANSIBLE_USER': 'ansible', 'DEPLOY_GROUP': 'deployer', 'SUDO_GROUP': 'wheel', 'container': 'docker'}, 'image': 'pycontribs/centos:7', 'name': 'centos_7', 'privileged': True, 'tmpfs': ['/run', '/tmp'], 'volumes': ['/sys/fs/cgroup:/sys/fs/cgroup']})

TASK [Create Dockerfiles from image names] *************************************
changed: [localhost] => (item={'capabilities': ['SYS_ADMIN'], 'command': '/usr/sbin/init', 'dockerfile': '../resources/Dockerfile.j2', 'env': {'ANSIBLE_USER': 'ansible', 'DEPLOY_GROUP': 'deployer', 'SUDO_GROUP': 'wheel', 'container': 'docker'}, 'image': 'pycontribs/centos:7', 'name': 'centos_7', 'privileged': True, 'tmpfs': ['/run', '/tmp'], 'volumes': ['/sys/fs/cgroup:/sys/fs/cgroup']})

TASK [Synchronization the context] *********************************************
changed: [localhost] => (item={'capabilities': ['SYS_ADMIN'], 'command': '/usr/sbin/init', 'dockerfile': '../resources/Dockerfile.j2', 'env': {'ANSIBLE_USER': 'ansible', 'DEPLOY_GROUP': 'deployer', 'SUDO_GROUP': 'wheel', 'container': 'docker'}, 'image': 'pycontribs/centos:7', 'name': 'centos_7', 'privileged': True, 'tmpfs': ['/run', '/tmp'], 'volumes': ['/sys/fs/cgroup:/sys/fs/cgroup']})

TASK [Discover local Docker images] ********************************************
ok: [localhost] => (item=None)
ok: [localhost]

TASK [Build an Ansible compatible image (new)] *********************************
ok: [localhost] => (item=molecule_local/pycontribs/centos:7)

TASK [Create docker network(s)] ************************************************
skipping: [localhost]

TASK [Determine the CMD directives] ********************************************
ok: [localhost] => (item=None)
ok: [localhost]

TASK [Create molecule instance(s)] *********************************************
changed: [localhost] => (item=centos_7)

TASK [Wait for instance(s) creation to complete] *******************************
FAILED - RETRYING: [localhost]: Wait for instance(s) creation to complete (300 retries left).
changed: [localhost] => (item=None)
changed: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=9    changed=4    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0

INFO     Running centos_7 > prepare
WARNING  Skipping, prepare playbook not configured.
INFO     Running centos_7 > converge
[WARNING]: Error getting vault password file (datatools): The vault password
file /Users/ro.khabibullin/.vault/datatools_vault was not found
[WARNING]: Error getting vault password file (getstream): The vault password
file /Users/ro.khabibullin/.vault/getstream was not found

PLAY [Converge] ****************************************************************

TASK [Gathering Facts] *********************************************************
ok: [centos_7]

TASK [Apply Clickhouse Role] ***************************************************

TASK [ansible-clickhouse : Include OS Family Specific Variables] ***************
ok: [centos_7]

TASK [ansible-clickhouse : include_tasks] **************************************
included: /Users/ro.khabibullin/Projects/netology/mnt-homeworks/08-ansible-05-testing/ansible-clickhouse/tasks/precheck.yml for centos_7

TASK [ansible-clickhouse : Requirements check | Checking sse4_2 support] *******
ok: [centos_7]

TASK [ansible-clickhouse : Requirements check | Not supported distribution && release] ***
skipping: [centos_7]

TASK [ansible-clickhouse : include_tasks] **************************************
included: /Users/ro.khabibullin/Projects/netology/mnt-homeworks/08-ansible-05-testing/ansible-clickhouse/tasks/params.yml for centos_7

TASK [ansible-clickhouse : Set clickhouse_service_enable] **********************
ok: [centos_7]

TASK [ansible-clickhouse : Set clickhouse_service_ensure] **********************
ok: [centos_7]

TASK [ansible-clickhouse : include_tasks] **************************************
included: /Users/ro.khabibullin/Projects/netology/mnt-homeworks/08-ansible-05-testing/ansible-clickhouse/tasks/install/yum.yml for centos_7

TASK [ansible-clickhouse : Install by YUM | Ensure clickhouse repo installed] ***
--- before: /etc/yum.repos.d/clickhouse.repo
+++ after: /etc/yum.repos.d/clickhouse.repo
@@ -0,0 +1,6 @@
+[clickhouse]
+baseurl = https://packages.clickhouse.com/rpm/stable/
+enabled = 1
+gpgcheck = 0
+name = Clickhouse repo
+

changed: [centos_7]

TASK [ansible-clickhouse : Install by YUM | Ensure clickhouse package installed (latest)] ***
changed: [centos_7]

TASK [ansible-clickhouse : Install by YUM | Ensure clickhouse package installed (version latest)] ***
skipping: [centos_7]

TASK [ansible-clickhouse : include_tasks] **************************************
included: /Users/ro.khabibullin/Projects/netology/mnt-homeworks/08-ansible-05-testing/ansible-clickhouse/tasks/configure/sys.yml for centos_7

TASK [ansible-clickhouse : Check clickhouse config, data and logs] *************
ok: [centos_7] => (item=/var/log/clickhouse-server)
--- before
+++ after
@@ -1,4 +1,4 @@
 {
-    "mode": "0700",
+    "mode": "0770",
     "path": "/etc/clickhouse-server"
 }

changed: [centos_7] => (item=/etc/clickhouse-server)
--- before
+++ after
@@ -1,7 +1,7 @@
 {
-    "group": 0,
-    "mode": "0755",
-    "owner": 0,
+    "group": 995,
+    "mode": "0770",
+    "owner": 999,
     "path": "/var/lib/clickhouse/tmp/",
-    "state": "absent"
+    "state": "directory"
 }

changed: [centos_7] => (item=/var/lib/clickhouse/tmp/)
--- before
+++ after
@@ -1,4 +1,4 @@
 {
-    "mode": "0700",
+    "mode": "0770",
     "path": "/var/lib/clickhouse/"
 }

changed: [centos_7] => (item=/var/lib/clickhouse/)

TASK [ansible-clickhouse : Config | Create config.d folder] ********************
--- before
+++ after
@@ -1,4 +1,4 @@
 {
-    "mode": "0500",
+    "mode": "0770",
     "path": "/etc/clickhouse-server/config.d"
 }

changed: [centos_7]

TASK [ansible-clickhouse : Config | Create users.d folder] *********************
--- before
+++ after
@@ -1,4 +1,4 @@
 {
-    "mode": "0500",
+    "mode": "0770",
     "path": "/etc/clickhouse-server/users.d"
 }

changed: [centos_7]

TASK [ansible-clickhouse : Config | Generate system config] ********************
--- before
+++ after: /Users/ro.khabibullin/.ansible/tmp/ansible-local-59623ksyqc_6n/tmp1bgck_qc/config.j2
@@ -0,0 +1,382 @@
+<?xml version="1.0"?>
+<!--
+ -
+ - Ansible managed: Do NOT edit this file manually!
+ -
+--> 
+<clickhouse>
+    <logger>
+        <!-- Possible levels: https://github.com/pocoproject/poco/blob/develop/Foundation/include/Poco/Logger.h#L105 -->
+        <level>trace</level>
+        <log>/var/log/clickhouse-server/clickhouse-server.log</log>
+        <errorlog>/var/log/clickhouse-server/clickhouse-server.err.log</errorlog>
+        <size>1000M</size>
+        <count>10</count>
+    </logger>
+
+    <http_port>8123</http_port>
+
+    <tcp_port>9000</tcp_port>
+
+    <!-- Used with https_port and tcp_port_secure. Full ssl options list: https://github.com/ClickHouse-Extras/poco/blob/master/NetSSL_OpenSSL/include/Poco/Net/SSLManager.h#L71 -->
+    <openSSL>
+        <server> <!-- Used for https server AND secure tcp port -->
+            <!-- openssl req -subj "/CN=localhost" -new -newkey rsa:2048 -days 365 -nodes -x509 -keyout /etc/clickhouse-server/server.key -out /etc/clickhouse-server/server.crt -->
+            <certificateFile>/etc/clickhouse-server/server.crt</certificateFile>
+            <privateKeyFile>/etc/clickhouse-server/server.key</privateKeyFile>
+            <!-- openssl dhparam -out /etc/clickhouse-server/dhparam.pem 4096 -->
+            <dhParamsFile>/etc/clickhouse-server/dhparam.pem</dhParamsFile>
+            <verificationMode>none</verificationMode>
+            <loadDefaultCAFile>true</loadDefaultCAFile>
+            <cacheSessions>true</cacheSessions>
+            <disableProtocols>sslv2,sslv3</disableProtocols>
+            <preferServerCiphers>true</preferServerCiphers>
+        </server>
+
+        <client> <!-- Used for connecting to https dictionary source -->
+            <loadDefaultCAFile>true</loadDefaultCAFile>
+            <cacheSessions>true</cacheSessions>
+            <disableProtocols>sslv2,sslv3</disableProtocols>
+            <preferServerCiphers>true</preferServerCiphers>
+            <!-- Use for self-signed: <verificationMode>none</verificationMode> -->
+            <invalidCertificateHandler>
+                <!-- Use for self-signed: <name>AcceptCertificateHandler</name> -->
+                <name>RejectCertificateHandler</name>
+            </invalidCertificateHandler>
+        </client>
+    </openSSL>
+
+    <!-- Default root page on http[s] server. For example load UI from https://tabix.io/ when opening http://localhost:8123 -->
+    <!--
+    <http_server_default_response><![CDATA[<html ng-app="SMI2"><head><base href="http://ui.tabix.io/"></head><body><div ui-view="" class="content-ui"></div><script src="http://loader.tabix.io/master.js"></script></body></html>]]></http_server_default_response>
+    -->
+
+    <!-- Port for communication between replicas. Used for data exchange. -->
+    <interserver_http_port>9009</interserver_http_port>
+
+
+
+    <!-- Hostname that is used by other replicas to request this server.
+         If not specified, than it is determined analoguous to 'hostname -f' command.
+         This setting could be used to switch replication to another network interface.
+      -->
+    <!--
+    <interserver_http_host>example.clickhouse.com</interserver_http_host>
+    -->
+
+    <!-- Listen specified host. use :: (wildcard IPv6 address), if you want to accept connections both with IPv4 and IPv6 from everywhere. -->
+    <!-- <listen_host>::</listen_host> -->
+    <!-- Same for hosts with disabled ipv6: -->
+    <!-- <listen_host>0.0.0.0</listen_host> -->
+    <listen_host>127.0.0.1</listen_host>
+
+    <max_connections>2048</max_connections>
+    <keep_alive_timeout>3</keep_alive_timeout>
+
+    <!-- Maximum number of concurrent queries. -->
+    <max_concurrent_queries>100</max_concurrent_queries>
+
+    <!-- Set limit on number of open files (default: maximum). This setting makes sense on Mac OS X because getrlimit() fails to retrieve
+         correct maximum value. -->
+    <!-- <max_open_files>262144</max_open_files> -->
+
+    <!-- Size of cache of uncompressed blocks of data, used in tables of MergeTree family.
+         In bytes. Cache is single for server. Memory is allocated only on demand.
+         Cache is used when 'use_uncompressed_cache' user setting turned on (off by default).
+         Uncompressed cache is advantageous only for very short queries and in rare cases.
+      -->
+    <uncompressed_cache_size>8589934592</uncompressed_cache_size>
+
+    <!-- Approximate size of mark cache, used in tables of MergeTree family.
+         In bytes. Cache is single for server. Memory is allocated only on demand.
+         You should not lower this value.
+      -->
+    <mark_cache_size>5368709120</mark_cache_size>
+
+
+    <!-- Path to data directory, with trailing slash. -->
+    <path>/var/lib/clickhouse/</path>
+
+    <!-- Path to temporary data for processing hard queries. -->
+    <tmp_path>/var/lib/clickhouse/tmp/</tmp_path>
+
+    <!-- Directory with user provided files that are accessible by 'file' table function. -->
+    <user_files_path>/var/lib/clickhouse/user_files/</user_files_path>
+
+    <!-- Path to configuration file with users, access rights, profiles of settings, quotas. -->
+    <users_config>users.xml</users_config>
+
+    <!-- Default profile of settings. -->
+    <default_profile>default</default_profile>
+
+    <!-- System profile of settings. This settings are used by internal processes (Buffer storage, Distibuted DDL worker and so on). -->
+    <!-- <system_profile>default</system_profile> -->
+
+    <!-- Default database. -->
+    <default_database>default</default_database>
+
+    <!-- Server time zone could be set here.
+
+         Time zone is used when converting between String and DateTime types,
+          when printing DateTime in text formats and parsing DateTime from text,
+          it is used in date and time related functions, if specific time zone was not passed as an argument.
+
+         Time zone is specified as identifier from IANA time zone database, like UTC or Africa/Abidjan.
+         If not specified, system time zone at server startup is used.
+
+         Please note, that server could display time zone alias instead of specified name.
+         Example: W-SU is an alias for Europe/Moscow and Zulu is an alias for UTC.
+    -->
+    <!-- <timezone>Europe/Moscow</timezone> -->
+
+    <!-- You can specify umask here (see "man umask"). Server will apply it on startup.
+         Number is always parsed as octal. Default umask is 027 (other users cannot read logs, data files, etc; group can only read).
+    -->
+    <!-- <umask>022</umask> -->
+
+    <!-- Perform mlockall after startup to lower first queries latency
+          and to prevent clickhouse executable from being paged out under high IO load.
+         Enabling this option is recommended but will lead to increased startup time for up to a few seconds.
+    -->
+    <mlock_executable>False</mlock_executable>
+
+    <!-- Configuration of clusters that could be used in Distributed tables.
+         https://clickhouse.com/docs/en/engines/table-engines/special/distributed/
+      -->
+    <remote_servers incl="clickhouse_remote_servers" />
+
+
+    <!-- If element has 'incl' attribute, then for it's value will be used corresponding substitution from another file.
+         By default, path to file with substitutions is /etc/metrika.xml. It could be changed in config in 'include_from' element.
+         Values for substitutions are specified in /clickhouse/name_of_substitution elements in that file.
+      -->
+
+    <!-- ZooKeeper is used to store metadata about replicas, when using Replicated tables.
+         Optional. If you don't use replicated tables, you could omit that.
+
+         See https://clickhouse.com/docs/en/engines/table-engines/mergetree-family/replication/
+      -->
+    <zookeeper incl="zookeeper-servers" optional="true" />
+
+    <!-- Substitutions for parameters of replicated tables.
+          Optional. If you don't use replicated tables, you could omit that.
+         See https://clickhouse.com/docs/en/engines/table-engines/mergetree-family/replication/#creating-replicated-tables
+      -->
+    <macros incl="macros" optional="true" />
+
+
+    <!-- Reloading interval for embedded dictionaries, in seconds. Default: 3600. -->
+    <builtin_dictionaries_reload_interval>3600</builtin_dictionaries_reload_interval>
+
+    <!-- If true, dictionaries are created lazily on first use. Otherwise they are initialised on server startup. Default: true -->
+    <!-- See also: https://clickhouse.com/docs/en/operations/server-configuration-parameters/settings/#server_configuration_parameters-dictionaries_lazy_load -->
+    <dictionaries_lazy_load>True</dictionaries_lazy_load>
+
+    <!-- Maximum session timeout, in seconds. Default: 3600. -->
+    <max_session_timeout>3600</max_session_timeout>
+
+    <!-- Default session timeout, in seconds. Default: 60. -->
+    <default_session_timeout>60</default_session_timeout>
+
+    <!-- Sending data to Graphite for monitoring. Several sections can be defined. -->
+    <!--
+        interval - send every X second
+        root_path - prefix for keys
+        hostname_in_path - append hostname to root_path (default = true)
+        metrics - send data from table system.metrics
+        events - send data from table system.events
+        asynchronous_metrics - send data from table system.asynchronous_metrics
+    -->
+    <!--
+    <graphite>
+        <host>localhost</host>
+        <port>42000</port>
+        <timeout>0.1</timeout>
+        <interval>60</interval>
+        <root_path>one_min</root_path>
+        <hostname_in_path>true</hostname_in_path>
+
+        <metrics>true</metrics>
+        <events>true</events>
+        <asynchronous_metrics>true</asynchronous_metrics>
+    </graphite>
+    <graphite>
+        <host>localhost</host>
+        <port>42000</port>
+        <timeout>0.1</timeout>
+        <interval>1</interval>
+        <root_path>one_sec</root_path>
+
+        <metrics>true</metrics>
+        <events>true</events>
+        <asynchronous_metrics>false</asynchronous_metrics>
+    </graphite>
+    -->
+
+
+    <!-- Query log. Used only for queries with setting log_queries = 1. -->
+    <query_log>
+        <!-- What table to insert data. If table is not exist, it will be created.
+             When query log structure is changed after system update,
+              then old table will be renamed and new table will be created automatically.
+        -->
+        <database>system</database>
+        <table>query_log</table>
+        <!--
+            PARTITION BY expr https://clickhouse.com/docs/en/table_engines/mergetree-family/custom_partitioning_key/
+            Example:
+                event_date
+                toMonday(event_date)
+                toYYYYMM(event_date)
+                toStartOfHour(event_time)
+        -->
+        <partition_by>toYYYYMM(event_date)</partition_by>
+        <!-- Interval of flushing data. -->
+        <flush_interval_milliseconds>7500</flush_interval_milliseconds>
+    </query_log>
+
+    <!-- Query thread log. Has information about all threads participated in query execution.
+         Used only for queries with setting log_query_threads = 1. -->
+    <query_thread_log>
+        <database>system</database>
+        <table>query_thread_log</table>
+        <partition_by>toYYYYMM(event_date)</partition_by>
+        
+        <flush_interval_milliseconds>7500</flush_interval_milliseconds>
+    </query_thread_log>
+
+    <!-- Uncomment if use part log.
+         Part log contains information about all actions with parts in MergeTree tables (creation, deletion, merges, downloads).
+    <part_log>
+        <database>system</database>
+        <table>part_log</table>
+        <flush_interval_milliseconds>7500</flush_interval_milliseconds>
+    </part_log>
+    -->
+
+
+    <!-- Parameters for embedded dictionaries, used in Yandex.Metrica.
+         See https://clickhouse.com/docs/en/dicts/internal_dicts/
+    -->
+
+    <!-- Path to file with region hierarchy. -->
+    <!-- <path_to_regions_hierarchy_file>/opt/geo/regions_hierarchy.txt</path_to_regions_hierarchy_file> -->
+
+    <!-- Path to directory with files containing names of regions -->
+    <!-- <path_to_regions_names_files>/opt/geo/</path_to_regions_names_files> -->
+
+
+    <!-- Configuration of external dictionaries. See:
+         https://clickhouse.com/docs/en/sql-reference/dictionaries/external-dictionaries/external-dicts
+    -->
+    <dictionaries_config>*_dictionary.xml</dictionaries_config>
+
+    <!-- Uncomment if you want data to be compressed 30-100% better.
+         Don't do that if you just started using ClickHouse.
+      -->
+    <compression incl="clickhouse_compression">
+    <!--
+        <!- - Set of variants. Checked in order. Last matching case wins. If nothing matches, lz4 will be used. - ->
+        <case>
+
+            <!- - Conditions. All must be satisfied. Some conditions may be omitted. - ->
+            <min_part_size>10000000000</min_part_size>        <!- - Min part size in bytes. - ->
+            <min_part_size_ratio>0.01</min_part_size_ratio>   <!- - Min size of part relative to whole table size. - ->
+
+            <!- - What compression method to use. - ->
+            <method>zstd</method>
+        </case>
+    -->
+    </compression>
+
+    <!-- Allow to execute distributed DDL queries (CREATE, DROP, ALTER, RENAME) on cluster.
+         Works only if ZooKeeper is enabled. Comment it if such functionality isn't required. -->
+    <distributed_ddl>
+        <!-- Path in ZooKeeper to queue with DDL queries -->
+        <path>/clickhouse/task_queue/ddl</path>
+
+        <!-- Settings from this profile will be used to execute DDL queries -->
+        <!-- <profile>default</profile> -->
+    </distributed_ddl>
+
+    <!-- Settings to fine tune MergeTree tables. See documentation in source code, in MergeTreeSettings.h -->
+        <merge_tree>
+        </merge_tree>
+
+    <!-- Protection from accidental DROP.
+         If size of a MergeTree table is greater than max_table_size_to_drop (in bytes) than table could not be dropped with any DROP query.
+         If you want do delete one table and don't want to restart clickhouse-server, you could create special file <clickhouse-path>/flags/force_drop_table and make DROP once.
+         By default max_table_size_to_drop is 50GB; max_table_size_to_drop=0 allows to DROP any tables.
+         The same for max_partition_size_to_drop.
+         Uncomment to disable protection.
+    -->
+    <!-- <max_table_size_to_drop>0</max_table_size_to_drop> -->
+    <!-- <max_partition_size_to_drop>0</max_partition_size_to_drop> -->
+
+    <!-- Example of parameters for GraphiteMergeTree table engine -->
+    <graphite_rollup_example>
+        <pattern>
+            <regexp>click_cost</regexp>
+            <function>any</function>
+            <retention>
+                <age>0</age>
+                <precision>3600</precision>
+            </retention>
+            <retention>
+                <age>86400</age>
+                <precision>60</precision>
+            </retention>
+        </pattern>
+        <default>
+            <function>max</function>
+            <retention>
+                <age>0</age>
+                <precision>60</precision>
+            </retention>
+            <retention>
+                <age>3600</age>
+                <precision>300</precision>
+            </retention>
+            <retention>
+                <age>86400</age>
+                <precision>3600</precision>
+            </retention>
+        </default>
+    </graphite_rollup_example>
+
+
+    <!-- Exposing metrics data for scraping from Prometheus. -->
+    <!--
+        endpoint – HTTP endpoint for scraping metrics by prometheus server. Start from ‘/’.
+        port – Port for endpoint.
+        metrics – Flag that sets to expose metrics from the system.metrics table.
+        events – Flag that sets to expose metrics from the system.events table.
+        asynchronous_metrics – Flag that sets to expose current metrics values from the system.asynchronous_metrics table.
+    -->
+    <!--
+    <prometheus>
+        <endpoint>/metrics</endpoint>
+        <port>8001</port>
+        <metrics>true</metrics>
+        <events>true</events>
+        <asynchronous_metrics>true</asynchronous_metrics>
+    </prometheus>
+    -->
+
+
+    <!-- Directory in <clickhouse-path> containing schema files for various input formats.
+         The directory will be created if it doesn't exist.
+      -->
+    <format_schema_path>/var/lib/clickhouse//format_schemas/</format_schema_path>
+
+    <!-- Uncomment to disable ClickHouse internal DNS caching. -->
+    <!-- <disable_internal_dns_cache>1</disable_internal_dns_cache> -->
+
+    <kafka>
+    </kafka>
+
+
+
+
+
+</clickhouse>

changed: [centos_7]

TASK [ansible-clickhouse : Config | Generate users config] *********************
--- before
+++ after: /Users/ro.khabibullin/.ansible/tmp/ansible-local-59623ksyqc_6n/tmpvfm9__se/users.j2
@@ -0,0 +1,106 @@
+<?xml version="1.0"?>
+<!--
+ -
+ - Ansible managed: Do NOT edit this file manually!
+ -
+--> 
+<clickhouse>
+   <profiles>
+    <!-- Profiles of settings. -->
+    <!-- Default profiles. -->
+        <default>
+            <max_memory_usage>10000000000</max_memory_usage>
+            <use_uncompressed_cache>0</use_uncompressed_cache>
+            <load_balancing>random</load_balancing>
+            <max_partitions_per_insert_block>100</max_partitions_per_insert_block>
+        </default>
+        <readonly>
+            <readonly>1</readonly>
+        </readonly>
+        <!-- Default profiles end. -->
+    <!-- Custom profiles. -->
+        <!-- Custom profiles end. -->
+    </profiles>
+
+    <!-- Users and ACL. -->
+    <users>
+    <!-- Default users. -->
+            <!-- Default user for login if user not defined -->
+        <default>
+                <password></password>
+                <networks incl="networks" replace="replace">
+                <ip>::1</ip>
+                <ip>127.0.0.1</ip>
+                </networks>
+        <profile>default</profile>
+        <quota>default</quota>
+            </default>
+            <!-- Example of user with readonly access -->
+        <readonly>
+                <password></password>
+                <networks incl="networks" replace="replace">
+                <ip>::1</ip>
+                <ip>127.0.0.1</ip>
+                </networks>
+        <profile>readonly</profile>
+        <quota>default</quota>
+            </readonly>
+        <!-- Custom users. -->
+            <!-- classic user with plain password -->
+        <testuser>
+                <password_sha256_hex>f2ca1bb6c7e907d06dafe4687e579fce76b37e4e93b7605022da52e6ccc26fd2</password_sha256_hex>
+                <networks incl="networks" replace="replace">
+                <ip>::1</ip>
+                <ip>127.0.0.1</ip>
+                </networks>
+        <profile>default</profile>
+        <quota>default</quota>
+                 <allow_databases>
+                    <database>testu1</database>
+                </allow_databases>
+                            </testuser>
+            <!-- classic user with hex password -->
+        <testuser2>
+                <password>testplpassword</password>
+                <networks incl="networks" replace="replace">
+                <ip>::1</ip>
+                <ip>127.0.0.1</ip>
+                </networks>
+        <profile>default</profile>
+        <quota>default</quota>
+                 <allow_databases>
+                    <database>testu2</database>
+                </allow_databases>
+                            </testuser2>
+            <!-- classic user with multi dbs and multi-custom network allow password -->
+        <testuser3>
+                <password>testplpassword</password>
+                <networks incl="networks" replace="replace">
+                <ip>192.168.0.0/24</ip>
+                <ip>10.0.0.0/8</ip>
+                </networks>
+        <profile>default</profile>
+        <quota>default</quota>
+                 <allow_databases>
+                    <database>testu1</database>
+                    <database>testu2</database>
+                    <database>testu3</database>
+                </allow_databases>
+                            </testuser3>
+        </users>
+
+    <!-- Quotas. -->
+    <quotas>
+        <!-- Default quotas. -->
+        <default>
+        <interval>
+        <duration>3600</duration>
+        <queries>0</queries>
+        <errors>0</errors>
+        <result_rows>0</result_rows>
+        <read_rows>0</read_rows>
+        <execution_time>0</execution_time>
+    </interval>
+        </default>
+            </quotas>
+</clickhouse>

changed: [centos_7]

TASK [ansible-clickhouse : Config | Generate remote_servers config] ************
skipping: [centos_7]

TASK [ansible-clickhouse : Config | Generate macros config] ********************
skipping: [centos_7]

TASK [ansible-clickhouse : Config | Generate zookeeper servers config] *********
skipping: [centos_7]

TASK [ansible-clickhouse : Config | Fix interserver_http_port and intersever_https_port collision] ***
skipping: [centos_7]

TASK [ansible-clickhouse : Notify Handlers Now] ********************************

RUNNING HANDLER [ansible-clickhouse : Restart Clickhouse Service] **************
ok: [centos_7]

TASK [ansible-clickhouse : include_tasks] **************************************
included: /Users/ro.khabibullin/Projects/netology/mnt-homeworks/08-ansible-05-testing/ansible-clickhouse/tasks/service.yml for centos_7

TASK [ansible-clickhouse : Ensure clickhouse-server.service is enabled: True and state: restarted] ***
fatal: [centos_7]: FAILED! => {"changed": false, "msg": "Service is in unknown state", "status": {}}

PLAY RECAP *********************************************************************
centos_7                   : ok=18   changed=7    unreachable=0    failed=1    skipped=6    rescued=0    ignored=0

WARNING  Retrying execution failure 2 of: ansible-playbook -D --inventory /Users/ro.khabibullin/.cache/molecule/ansible-clickhouse/centos_7/inventory --skip-tags molecule-notest,notest /Users/ro.khabibullin/Projects/netology/mnt-homeworks/08-ansible-05-testing/ansible-clickhouse/molecule/resources/playbooks/converge.yml
CRITICAL Ansible return code was 2, command was: ['ansible-playbook', '-D', '--inventory', '/Users/ro.khabibullin/.cache/molecule/ansible-clickhouse/centos_7/inventory', '--skip-tags', 'molecule-notest,notest', '/Users/ro.khabibullin/Projects/netology/mnt-homeworks/08-ansible-05-testing/ansible-clickhouse/molecule/resources/playbooks/converge.yml']
WARNING  An error occurred during the test sequence action: 'converge'. Cleaning up.
INFO     Running centos_7 > cleanup
WARNING  Skipping, cleanup playbook not configured.
INFO     Running centos_7 > destroy
[WARNING]: Error getting vault password file (datatools): The vault password
file /Users/ro.khabibullin/.vault/datatools_vault was not found
[WARNING]: Error getting vault password file (getstream): The vault password
file /Users/ro.khabibullin/.vault/getstream was not found

PLAY [Destroy] *****************************************************************

TASK [Set async_dir for HOME env] **********************************************
ok: [localhost]

TASK [Destroy molecule instance(s)] ********************************************
changed: [localhost] => (item=centos_7)

TASK [Wait for instance(s) deletion to complete] *******************************
FAILED - RETRYING: [localhost]: Wait for instance(s) deletion to complete (300 retries left).
changed: [localhost] => (item=centos_7)

TASK [Delete docker networks(s)] ***********************************************
skipping: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=3    changed=2    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0

INFO     Pruning extra files from scenario ephemeral directory
```

</details>

2. Перейдите в каталог с ролью vector-role и создайте сценарий тестирования по умолчанию при помощи `molecule init scenario --driver-name docker`.

<details>
<summary><b>➜  vector-role git:(main) molecule init scenario --driver-name docker</b></summary>

```
INFO     Initializing new scenario default...
INFO     Initialized scenario in /Users/ro.khabibullin/Projects/netology/mnt-homeworks/08-ansible-05-testing/vector-role/molecule/default successfully.
```

</details>

3. Добавьте несколько разных дистрибутивов (centos:8, ubuntu:latest) для инстансов и протестируйте роль, исправьте найденные ошибки, если они есть.
<details>
<summary><b>➜  vector git:(MNT-video) ✗ molecule test -s ubuntu_latest</b></summary>

```commandline
INFO     ubuntu_latest scenario test matrix: dependency, lint, cleanup, destroy, syntax, create, prepare, converge, idempotence, side_effect, verify, cleanup, destroy
INFO     Performing prerun with role_name_check=0...
INFO     Set ANSIBLE_LIBRARY=/Users/ro.khabibullin/.cache/ansible-compat/b0d51c/modules:/Users/ro.khabibullin/.ansible/plugins/modules:/usr/share/ansible/plugins/modules
INFO     Set ANSIBLE_COLLECTIONS_PATH=/Users/ro.khabibullin/.cache/ansible-compat/b0d51c/collections:/Users/ro.khabibullin/.ansible/collections:/usr/share/ansible/collections
INFO     Set ANSIBLE_ROLES_PATH=/Users/ro.khabibullin/.cache/ansible-compat/b0d51c/roles:/Users/ro.khabibullin/.ansible/roles:/usr/share/ansible/roles:/etc/ansible/roles
INFO     Using /Users/ro.khabibullin/.cache/ansible-compat/b0d51c/roles/ramireshab.vector symlink to current repository in order to enable Ansible to find the role using its expected full name.
INFO     Running ubuntu_latest > dependency
WARNING  Skipping, missing the requirements file.
WARNING  Skipping, missing the requirements file.
INFO     Running ubuntu_latest > lint
./tasks/main.yml
  14:1      error    too many blank lines (1 > 0)  (empty-lines)

WARNING  Listing 1 violation(s) that are fatal
syntax-check[specific]: the role 'vector' was not found in /Users/ro.khabibullin/Projects/netology/mnt-homeworks/08-ansible-05-testing/vector/tests/roles:/Users/ro.khabibullin/.cache/ansible-compat/b0d51c/roles:/Users/ro.khabibullin/.ansible/roles:/usr/share/ansible/roles:/etc/ansible/roles:/Users/ro.khabibullin/Projects/netology/mnt-homeworks/08-ansible-05-testing/vector/tests
tests/test.yml:5:7


                  Rule Violation Summary                   
 count tag                    profile rule associated tags 
     1 syntax-check[specific] min     core, unskippable    

Failed after : 1 failure(s), 0 warning(s) on 31 files.
INFO     Running ubuntu_latest > cleanup
WARNING  Skipping, cleanup playbook not configured.
INFO     Running ubuntu_latest > destroy
INFO     Sanity checks: 'docker'
[WARNING]: Error getting vault password file (datatools): The vault password
file /Users/ro.khabibullin/.vault/datatools_vault was not found
[WARNING]: Error getting vault password file (getstream): The vault password
file /Users/ro.khabibullin/.vault/getstream was not found

PLAY [Destroy] *****************************************************************

TASK [Set async_dir for HOME env] **********************************************
ok: [localhost]

TASK [Destroy molecule instance(s)] ********************************************
changed: [localhost] => (item=ubuntu_latest)

TASK [Wait for instance(s) deletion to complete] *******************************
FAILED - RETRYING: [localhost]: Wait for instance(s) deletion to complete (300 retries left).
ok: [localhost] => (item=ubuntu_latest)

TASK [Delete docker networks(s)] ***********************************************
skipping: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=3    changed=1    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0

INFO     Running ubuntu_latest > syntax
[WARNING]: Error getting vault password file (datatools): The vault password
file /Users/ro.khabibullin/.vault/datatools_vault was not found
[WARNING]: Error getting vault password file (getstream): The vault password
file /Users/ro.khabibullin/.vault/getstream was not found
ansible-playbook [core 2.14.2]
  config file = /Users/ro.khabibullin/.cache/molecule/vector/ubuntu_latest/ansible.cfg
  configured module search path = ['/usr/local/lib/python3.11/site-packages/molecule/provisioner/ansible/plugins/modules', '/Users/ro.khabibullin/.cache/molecule/vector/ubuntu_latest/library', '/Users/ro.khabibullin/Projects/netology/mnt-homeworks/08-ansible-05-testing/vector/library', '/Users/ro.khabibullin/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /usr/local/lib/python3.11/site-packages/ansible
  ansible collection location = /Users/ro.khabibullin/.cache/ansible-compat/b0d51c/collections:/Users/ro.khabibullin/.cache/molecule/vector/ubuntu_latest/collections:/Users/ro.khabibullin/.ansible/collections:/usr/share/ansible/collections:/etc/ansible/collections
  executable location = /usr/local/bin/ansible-playbook
  python version = 3.11.1 (main, Dec 23 2022, 09:39:26) [Clang 14.0.0 (clang-1400.0.29.202)] (/usr/local/opt/python@3.11/bin/python3.11)
  jinja version = 3.1.2
  libyaml = False
Using /Users/ro.khabibullin/.cache/molecule/vector/ubuntu_latest/ansible.cfg as config file
1 plays in /Users/ro.khabibullin/Projects/netology/mnt-homeworks/08-ansible-05-testing/vector/molecule/resources/playbooks/converge.yml

playbook: /Users/ro.khabibullin/Projects/netology/mnt-homeworks/08-ansible-05-testing/vector/molecule/resources/playbooks/converge.yml
INFO     Running ubuntu_latest > create
[WARNING]: Error getting vault password file (datatools): The vault password
file /Users/ro.khabibullin/.vault/datatools_vault was not found
[WARNING]: Error getting vault password file (getstream): The vault password
file /Users/ro.khabibullin/.vault/getstream was not found

PLAY [Create] ******************************************************************

TASK [Set async_dir for HOME env] **********************************************
ok: [localhost]

TASK [Log into a Docker registry] **********************************************
skipping: [localhost] => (item=None) 
skipping: [localhost]

TASK [Check presence of custom Dockerfiles] ************************************
ok: [localhost] => (item={'capabilities': ['SYS_ADMIN'], 'command': '/sbin/init', 'dockerfile': '../resources/Dockerfile.j2', 'env': {'ANSIBLE_USER': 'ansible', 'DEPLOY_GROUP': 'deployer', 'SUDO_GROUP': 'sudo', 'container': 'docker'}, 'image': 'ubuntu:latest', 'name': 'ubuntu_latest', 'privileged': True, 'tmpfs': ['/run', '/tmp'], 'volumes': ['/sys/fs/cgroup:/sys/fs/cgroup']})

TASK [Create Dockerfiles from image names] *************************************
changed: [localhost] => (item={'capabilities': ['SYS_ADMIN'], 'command': '/sbin/init', 'dockerfile': '../resources/Dockerfile.j2', 'env': {'ANSIBLE_USER': 'ansible', 'DEPLOY_GROUP': 'deployer', 'SUDO_GROUP': 'sudo', 'container': 'docker'}, 'image': 'ubuntu:latest', 'name': 'ubuntu_latest', 'privileged': True, 'tmpfs': ['/run', '/tmp'], 'volumes': ['/sys/fs/cgroup:/sys/fs/cgroup']})

TASK [Synchronization the context] *********************************************
changed: [localhost] => (item={'capabilities': ['SYS_ADMIN'], 'command': '/sbin/init', 'dockerfile': '../resources/Dockerfile.j2', 'env': {'ANSIBLE_USER': 'ansible', 'DEPLOY_GROUP': 'deployer', 'SUDO_GROUP': 'sudo', 'container': 'docker'}, 'image': 'ubuntu:latest', 'name': 'ubuntu_latest', 'privileged': True, 'tmpfs': ['/run', '/tmp'], 'volumes': ['/sys/fs/cgroup:/sys/fs/cgroup']})

TASK [Discover local Docker images] ********************************************
ok: [localhost] => (item=None)
ok: [localhost]

TASK [Build an Ansible compatible image (new)] *********************************
ok: [localhost] => (item=molecule_local/ubuntu:latest)

TASK [Create docker network(s)] ************************************************
skipping: [localhost]

TASK [Determine the CMD directives] ********************************************
ok: [localhost] => (item=None)
ok: [localhost]

TASK [Create molecule instance(s)] *********************************************
changed: [localhost] => (item=ubuntu_latest)

TASK [Wait for instance(s) creation to complete] *******************************
FAILED - RETRYING: [localhost]: Wait for instance(s) creation to complete (300 retries left).
changed: [localhost] => (item=None)
changed: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=9    changed=4    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0

INFO     Running ubuntu_latest > prepare
WARNING  Skipping, prepare playbook not configured.
INFO     Running ubuntu_latest > converge
[WARNING]: Error getting vault password file (datatools): The vault password
file /Users/ro.khabibullin/.vault/datatools_vault was not found
[WARNING]: Error getting vault password file (getstream): The vault password
file /Users/ro.khabibullin/.vault/getstream was not found
ansible-playbook [core 2.14.2]
  config file = /Users/ro.khabibullin/.cache/molecule/vector/ubuntu_latest/ansible.cfg
  configured module search path = ['/usr/local/lib/python3.11/site-packages/molecule/provisioner/ansible/plugins/modules', '/Users/ro.khabibullin/.cache/molecule/vector/ubuntu_latest/library', '/Users/ro.khabibullin/Projects/netology/mnt-homeworks/08-ansible-05-testing/vector/library', '/Users/ro.khabibullin/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /usr/local/lib/python3.11/site-packages/ansible
  ansible collection location = /Users/ro.khabibullin/.cache/ansible-compat/b0d51c/collections:/Users/ro.khabibullin/.cache/molecule/vector/ubuntu_latest/collections:/Users/ro.khabibullin/.ansible/collections:/usr/share/ansible/collections:/etc/ansible/collections
  executable location = /usr/local/bin/ansible-playbook
  python version = 3.11.1 (main, Dec 23 2022, 09:39:26) [Clang 14.0.0 (clang-1400.0.29.202)] (/usr/local/opt/python@3.11/bin/python3.11)
  jinja version = 3.1.2
  libyaml = False
Using /Users/ro.khabibullin/.cache/molecule/vector/ubuntu_latest/ansible.cfg as config file
Skipping callback 'default', as we already have a stdout callback.
Skipping callback 'minimal', as we already have a stdout callback.
Skipping callback 'oneline', as we already have a stdout callback.

PLAYBOOK: converge.yml *********************************************************
1 plays in /Users/ro.khabibullin/Projects/netology/mnt-homeworks/08-ansible-05-testing/vector/molecule/resources/playbooks/converge.yml

PLAY [Converge] ****************************************************************

TASK [Gathering Facts] *********************************************************
task path: /Users/ro.khabibullin/Projects/netology/mnt-homeworks/08-ansible-05-testing/vector/molecule/resources/playbooks/converge.yml:2
ok: [ubuntu_latest]

TASK [Apply Vector Role] *******************************************************
task path: /Users/ro.khabibullin/Projects/netology/mnt-homeworks/08-ansible-05-testing/vector/molecule/resources/playbooks/converge.yml:5

TASK [vector : Get Vector] *****************************************************
task path: /Users/ro.khabibullin/Projects/netology/mnt-homeworks/08-ansible-05-testing/vector/tasks/main.yml:3
changed: [ubuntu_latest] => {"changed": true, "checksum_dest": null, "checksum_src": "88840c8f043a33d15e15923766b72f06693e1d16", "dest": "/tmp/vector-0.27.0.deb", "elapsed": 1, "gid": 0, "group": "root", "md5sum": "835efdd30eac8feb0801fb03e726119d", "mode": "0644", "msg": "OK (26753298 bytes)", "owner": "root", "size": 26753298, "src": "/root/.ansible/tmp/ansible-tmp-1677077511.5976791-68776-267139472650986/tmpj1gii288", "state": "file", "status_code": 200, "uid": 0, "url": "https://packages.timber.io/vector/0.27.0/vector_0.27.0-1_amd64.deb"}

TASK [vector : Install Vector] *************************************************
task path: /Users/ro.khabibullin/Projects/netology/mnt-homeworks/08-ansible-05-testing/vector/tasks/main.yml:7
NOTIFIED HANDLER vector : Start Vector service for ubuntu_latest
Selecting previously unselected package vector.
(Reading database ... 9550 files and directories currently installed.)
Preparing to unpack /tmp/vector-0.27.0.deb ...
Unpacking vector (0.27.0-1) ...
Setting up vector (0.27.0-1) ...
systemd-journal:x:101:
changed: [ubuntu_latest] => {"changed": true, "stderr": "", "stderr_lines": [], "stdout": "Selecting previously unselected package vector.\n(Reading database ... 9550 files and directories currently installed.)\nPreparing to unpack /tmp/vector-0.27.0.deb ...\nUnpacking vector (0.27.0-1) ...\nSetting up vector (0.27.0-1) ...\nsystemd-journal:x:101:\n", "stdout_lines": ["Selecting previously unselected package vector.", "(Reading database ... 9550 files and directories currently installed.)", "Preparing to unpack /tmp/vector-0.27.0.deb ...", "Unpacking vector (0.27.0-1) ...", "Setting up vector (0.27.0-1) ...", "systemd-journal:x:101:"]}

TASK [vector : Flush handlers] *************************************************
task path: /Users/ro.khabibullin/Projects/netology/mnt-homeworks/08-ansible-05-testing/vector/tasks/main.yml:12
META: triggered running handlers for ubuntu_latest

RUNNING HANDLER [vector : Start Vector service] ********************************
task path: /Users/ro.khabibullin/Projects/netology/mnt-homeworks/08-ansible-05-testing/vector/handlers/main.yml:3
changed: [ubuntu_latest] => {"changed": true, "name": "vector", "state": "started", "status": {"ActiveEnterTimestamp": "n/a", "ActiveEnterTimestampMonotonic": "0", "ActiveExitTimestamp": "n/a", "ActiveExitTimestampMonotonic": "0", "ActiveState": "inactive", "After": "sysinit.target basic.target network-online.target systemd-journald.socket system.slice", "AllowIsolate": "no", "AmbientCapabilities": "cap_net_bind_service", "AssertResult": "no", "AssertTimestamp": "n/a", "AssertTimestampMonotonic": "0", "Before": "shutdown.target", "BlockIOAccounting": "no", "BlockIOWeight": "[not set]", "CPUAccounting": "yes", "CPUAffinityFromNUMA": "no", "CPUQuotaPerSecUSec": "infinity", "CPUQuotaPeriodUSec": "infinity", "CPUSchedulingPolicy": "0", "CPUSchedulingPriority": "0", "CPUSchedulingResetOnFork": "no", "CPUShares": "[not set]", "CPUUsageNSec": "[not set]", "CPUWeight": "[not set]", "CacheDirectoryMode": "0755", "CanFreeze": "yes", "CanIsolate": "no", "CanReload": "yes", "CanStart": "yes", "CanStop": "yes", "CapabilityBoundingSet": "cap_chown cap_dac_override cap_dac_read_search cap_fowner cap_fsetid cap_kill cap_setgid cap_setuid cap_setpcap cap_linux_immutable cap_net_bind_service cap_net_broadcast cap_net_admin cap_net_raw cap_ipc_lock cap_ipc_owner cap_sys_module cap_sys_rawio cap_sys_chroot cap_sys_ptrace cap_sys_pacct cap_sys_admin cap_sys_boot cap_sys_nice cap_sys_resource cap_sys_time cap_sys_tty_config cap_mknod cap_lease cap_audit_write cap_audit_control cap_setfcap cap_mac_override cap_mac_admin cap_syslog cap_wake_alarm cap_block_suspend cap_audit_read cap_perfmon cap_bpf cap_checkpoint_restore", "CleanResult": "success", "CollectMode": "inactive", "ConditionResult": "no", "ConditionTimestamp": "n/a", "ConditionTimestampMonotonic": "0", "ConfigurationDirectoryMode": "0755", "Conflicts": "shutdown.target", "ControlPID": "0", "CoredumpFilter": "0x23", "DefaultDependencies": "yes", "DefaultMemoryLow": "0", "DefaultMemoryMin": "0", "Delegate": "no", "Description": "Vector", "DevicePolicy": "auto", "Documentation": "https://vector.dev", "DynamicUser": "no", "EnvironmentFiles": "/etc/default/vector (ignore_errors=yes)", "ExecMainCode": "0", "ExecMainExitTimestamp": "n/a", "ExecMainExitTimestampMonotonic": "0", "ExecMainPID": "0", "ExecMainStartTimestamp": "n/a", "ExecMainStartTimestampMonotonic": "0", "ExecMainStatus": "0", "ExecReload": "{ path=/bin/kill ; argv[]=/bin/kill -HUP $MAINPID ; ignore_errors=no ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }", "ExecReloadEx": "{ path=/bin/kill ; argv[]=/bin/kill -HUP $MAINPID ; flags= ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }", "ExecStart": "{ path=/usr/bin/vector ; argv[]=/usr/bin/vector ; ignore_errors=no ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }", "ExecStartEx": "{ path=/usr/bin/vector ; argv[]=/usr/bin/vector ; flags= ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }", "ExecStartPre": "{ path=/usr/bin/vector ; argv[]=/usr/bin/vector validate ; ignore_errors=no ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }", "ExecStartPreEx": "{ path=/usr/bin/vector ; argv[]=/usr/bin/vector validate ; flags= ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }", "FailureAction": "none", "FileDescriptorStoreMax": "0", "FinalKillSignal": "9", "FragmentPath": "/lib/systemd/system/vector.service", "FreezerState": "running", "GID": "[not set]", "Group": "vector", "GuessMainPID": "yes", "IOAccounting": "no", "IOReadBytes": "18446744073709551615", "IOReadOperations": "18446744073709551615", "IOSchedulingClass": "2", "IOSchedulingPriority": "4", "IOWeight": "[not set]", "IOWriteBytes": "18446744073709551615", "IOWriteOperations": "18446744073709551615", "IPAccounting": "no", "IPEgressBytes": "[no data]", "IPEgressPackets": "[no data]", "IPIngressBytes": "[no data]", "IPIngressPackets": "[no data]", "Id": "vector.service", "IgnoreOnIsolate": "no", "IgnoreSIGPIPE": "yes", "InactiveEnterTimestamp": "n/a", "InactiveEnterTimestampMonotonic": "0", "InactiveExitTimestamp": "n/a", "InactiveExitTimestampMonotonic": "0", "JobRunningTimeoutUSec": "infinity", "JobTimeoutAction": "none", "JobTimeoutUSec": "infinity", "KeyringMode": "private", "KillMode": "control-group", "KillSignal": "15", "LimitAS": "infinity", "LimitASSoft": "infinity", "LimitCORE": "infinity", "LimitCORESoft": "0", "LimitCPU": "infinity", "LimitCPUSoft": "infinity", "LimitDATA": "infinity", "LimitDATASoft": "infinity", "LimitFSIZE": "infinity", "LimitFSIZESoft": "infinity", "LimitLOCKS": "infinity", "LimitLOCKSSoft": "infinity", "LimitMEMLOCK": "65536", "LimitMEMLOCKSoft": "65536", "LimitMSGQUEUE": "819200", "LimitMSGQUEUESoft": "819200", "LimitNICE": "0", "LimitNICESoft": "0", "LimitNOFILE": "1048576", "LimitNOFILESoft": "1024", "LimitNPROC": "infinity", "LimitNPROCSoft": "infinity", "LimitRSS": "infinity", "LimitRSSSoft": "infinity", "LimitRTPRIO": "0", "LimitRTPRIOSoft": "0", "LimitRTTIME": "infinity", "LimitRTTIMESoft": "infinity", "LimitSIGPENDING": "30963", "LimitSIGPENDINGSoft": "30963", "LimitSTACK": "infinity", "LimitSTACKSoft": "8388608", "LoadState": "loaded", "LockPersonality": "no", "LogLevelMax": "-1", "LogRateLimitBurst": "0", "LogRateLimitIntervalUSec": "0", "LogsDirectoryMode": "0755", "MainPID": "0", "ManagedOOMMemoryPressure": "auto", "ManagedOOMMemoryPressureLimit": "0", "ManagedOOMPreference": "none", "ManagedOOMSwap": "auto", "MemoryAccounting": "yes", "MemoryAvailable": "infinity", "MemoryCurrent": "[not set]", "MemoryDenyWriteExecute": "no", "MemoryHigh": "infinity", "MemoryLimit": "infinity", "MemoryLow": "0", "MemoryMax": "infinity", "MemoryMin": "0", "MemorySwapMax": "infinity", "MountAPIVFS": "no", "NFileDescriptorStore": "0", "NRestarts": "0", "NUMAPolicy": "n/a", "Names": "vector.service", "NeedDaemonReload": "no", "Nice": "0", "NoNewPrivileges": "no", "NonBlocking": "no", "NotifyAccess": "none", "OOMPolicy": "stop", "OOMScoreAdjust": "0", "OnFailureJobMode": "replace", "OnSuccessJobMode": "fail", "Perpetual": "no", "PrivateDevices": "no", "PrivateIPC": "no", "PrivateMounts": "no", "PrivateNetwork": "no", "PrivateTmp": "no", "PrivateUsers": "no", "ProcSubset": "all", "ProtectClock": "no", "ProtectControlGroups": "no", "ProtectHome": "no", "ProtectHostname": "no", "ProtectKernelLogs": "no", "ProtectKernelModules": "no", "ProtectKernelTunables": "no", "ProtectProc": "default", "ProtectSystem": "no", "RefuseManualStart": "no", "RefuseManualStop": "no", "ReloadResult": "success", "RemainAfterExit": "no", "RemoveIPC": "no", "Requires": "system.slice sysinit.target network-online.target", "Restart": "no", "RestartKillSignal": "15", "RestartUSec": "100ms", "RestrictNamespaces": "no", "RestrictRealtime": "no", "RestrictSUIDSGID": "no", "Result": "success", "RootDirectoryStartOnly": "no", "RuntimeDirectoryMode": "0755", "RuntimeDirectoryPreserve": "no", "RuntimeMaxUSec": "infinity", "SameProcessGroup": "no", "SecureBits": "0", "SendSIGHUP": "no", "SendSIGKILL": "yes", "Slice": "system.slice", "StandardError": "inherit", "StandardInput": "null", "StandardOutput": "journal", "StartLimitAction": "none", "StartLimitBurst": "5", "StartLimitIntervalUSec": "10s", "StartupBlockIOWeight": "[not set]", "StartupCPUShares": "[not set]", "StartupCPUWeight": "[not set]", "StartupIOWeight": "[not set]", "StateChangeTimestamp": "n/a", "StateChangeTimestampMonotonic": "0", "StateDirectoryMode": "0755", "StatusErrno": "0", "StopWhenUnneeded": "no", "SubState": "dead", "SuccessAction": "none", "SyslogFacility": "3", "SyslogLevel": "6", "SyslogLevelPrefix": "yes", "SyslogPriority": "30", "SystemCallErrorNumber": "2147483646", "TTYReset": "no", "TTYVHangup": "no", "TTYVTDisallocate": "no", "TasksAccounting": "yes", "TasksCurrent": "[not set]", "TasksMax": "9288", "TimeoutAbortUSec": "1min 30s", "TimeoutCleanUSec": "infinity", "TimeoutStartFailureMode": "terminate", "TimeoutStartUSec": "1min 30s", "TimeoutStopFailureMode": "terminate", "TimeoutStopUSec": "1min 30s", "TimerSlackNSec": "50000", "Transient": "no", "Type": "simple", "UID": "[not set]", "UMask": "0022", "UnitFilePreset": "enabled", "UnitFileState": "disabled", "User": "vector", "UtmpMode": "init", "WatchdogSignal": "6", "WatchdogTimestamp": "n/a", "WatchdogTimestampMonotonic": "0", "WatchdogUSec": "infinity"}}

PLAY RECAP *********************************************************************
ubuntu_latest              : ok=4    changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

INFO     Running ubuntu_latest > idempotence
[WARNING]: Error getting vault password file (datatools): The vault password
file /Users/ro.khabibullin/.vault/datatools_vault was not found
[WARNING]: Error getting vault password file (getstream): The vault password
file /Users/ro.khabibullin/.vault/getstream was not found
ansible-playbook [core 2.14.2]
  config file = /Users/ro.khabibullin/.cache/molecule/vector/ubuntu_latest/ansible.cfg
  configured module search path = ['/usr/local/lib/python3.11/site-packages/molecule/provisioner/ansible/plugins/modules', '/Users/ro.khabibullin/.cache/molecule/vector/ubuntu_latest/library', '/Users/ro.khabibullin/Projects/netology/mnt-homeworks/08-ansible-05-testing/vector/library', '/Users/ro.khabibullin/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /usr/local/lib/python3.11/site-packages/ansible
  ansible collection location = /Users/ro.khabibullin/.cache/ansible-compat/b0d51c/collections:/Users/ro.khabibullin/.cache/molecule/vector/ubuntu_latest/collections:/Users/ro.khabibullin/.ansible/collections:/usr/share/ansible/collections:/etc/ansible/collections
  executable location = /usr/local/bin/ansible-playbook
  python version = 3.11.1 (main, Dec 23 2022, 09:39:26) [Clang 14.0.0 (clang-1400.0.29.202)] (/usr/local/opt/python@3.11/bin/python3.11)
  jinja version = 3.1.2
  libyaml = False
Using /Users/ro.khabibullin/.cache/molecule/vector/ubuntu_latest/ansible.cfg as config file
Skipping callback 'default', as we already have a stdout callback.
Skipping callback 'minimal', as we already have a stdout callback.
Skipping callback 'oneline', as we already have a stdout callback.

PLAYBOOK: converge.yml *********************************************************
1 plays in /Users/ro.khabibullin/Projects/netology/mnt-homeworks/08-ansible-05-testing/vector/molecule/resources/playbooks/converge.yml

PLAY [Converge] ****************************************************************

TASK [Gathering Facts] *********************************************************
task path: /Users/ro.khabibullin/Projects/netology/mnt-homeworks/08-ansible-05-testing/vector/molecule/resources/playbooks/converge.yml:2
ok: [ubuntu_latest]

TASK [Apply Vector Role] *******************************************************
task path: /Users/ro.khabibullin/Projects/netology/mnt-homeworks/08-ansible-05-testing/vector/molecule/resources/playbooks/converge.yml:5

TASK [vector : Get Vector] *****************************************************
task path: /Users/ro.khabibullin/Projects/netology/mnt-homeworks/08-ansible-05-testing/vector/tasks/main.yml:3
ok: [ubuntu_latest] => {"changed": false, "dest": "/tmp/vector-0.27.0.deb", "elapsed": 0, "gid": 0, "group": "root", "mode": "0644", "msg": "HTTP Error 304: Not Modified", "owner": "root", "size": 26753298, "state": "file", "status_code": 304, "uid": 0, "url": "https://packages.timber.io/vector/0.27.0/vector_0.27.0-1_amd64.deb"}

TASK [vector : Install Vector] *************************************************
task path: /Users/ro.khabibullin/Projects/netology/mnt-homeworks/08-ansible-05-testing/vector/tasks/main.yml:7
ok: [ubuntu_latest] => {"changed": false, "stderr": "", "stderr_lines": [], "stdout": "", "stdout_lines": []}

TASK [vector : Flush handlers] *************************************************
task path: /Users/ro.khabibullin/Projects/netology/mnt-homeworks/08-ansible-05-testing/vector/tasks/main.yml:12
META: triggered running handlers for ubuntu_latest

PLAY RECAP *********************************************************************
ubuntu_latest              : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

INFO     Idempotence completed successfully.
INFO     Running ubuntu_latest > side_effect
WARNING  Skipping, side effect playbook not configured.
INFO     Running ubuntu_latest > verify
INFO     Running Ansible Verifier
[WARNING]: Error getting vault password file (datatools): The vault password
file /Users/ro.khabibullin/.vault/datatools_vault was not found
[WARNING]: Error getting vault password file (getstream): The vault password
file /Users/ro.khabibullin/.vault/getstream was not found
ansible-playbook [core 2.14.2]
  config file = /Users/ro.khabibullin/.cache/molecule/vector/ubuntu_latest/ansible.cfg
  configured module search path = ['/usr/local/lib/python3.11/site-packages/molecule/provisioner/ansible/plugins/modules', '/Users/ro.khabibullin/.cache/molecule/vector/ubuntu_latest/library', '/Users/ro.khabibullin/Projects/netology/mnt-homeworks/08-ansible-05-testing/vector/library', '/Users/ro.khabibullin/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /usr/local/lib/python3.11/site-packages/ansible
  ansible collection location = /Users/ro.khabibullin/.cache/ansible-compat/b0d51c/collections:/Users/ro.khabibullin/.cache/molecule/vector/ubuntu_latest/collections:/Users/ro.khabibullin/.ansible/collections:/usr/share/ansible/collections:/etc/ansible/collections
  executable location = /usr/local/bin/ansible-playbook
  python version = 3.11.1 (main, Dec 23 2022, 09:39:26) [Clang 14.0.0 (clang-1400.0.29.202)] (/usr/local/opt/python@3.11/bin/python3.11)
  jinja version = 3.1.2
  libyaml = False
Using /Users/ro.khabibullin/.cache/molecule/vector/ubuntu_latest/ansible.cfg as config file
Skipping callback 'default', as we already have a stdout callback.
Skipping callback 'minimal', as we already have a stdout callback.
Skipping callback 'oneline', as we already have a stdout callback.

PLAYBOOK: verify.yml ***********************************************************
1 plays in /Users/ro.khabibullin/Projects/netology/mnt-homeworks/08-ansible-05-testing/vector/molecule/resources/tests/verify.yml

PLAY [Verify] ******************************************************************

TASK [Gather Installed Packages] ***********************************************
task path: /Users/ro.khabibullin/Projects/netology/mnt-homeworks/08-ansible-05-testing/vector/molecule/resources/tests/verify.yml:7
ok: [ubuntu_latest] => {"ansible_facts": {"discovered_interpreter_python": "/usr/bin/python3", "packages": {"adduser": [{"arch": "all", "category": "admin", "name": "adduser", "origin": "Ubuntu", "source": "apt", "version": "3.118ubuntu5"}], "apt": [{"arch": "amd64", "category": "admin", "name": "apt", "origin": "Ubuntu", "source": "apt", "version": "2.4.8"}], "apt-transport-https": [{"arch": "all", "category": "universe/admin", "name": "apt-transport-https", "origin": "Ubuntu", "source": "apt", "version": "2.4.8"}], "base-files": [{"arch": "amd64", "category": "admin", "name": "base-files", "origin": "Ubuntu", "source": "apt", "version": "12ubuntu4.3"}], "base-passwd": [{"arch": "amd64", "category": "admin", "name": "base-passwd", "origin": "Ubuntu", "source": "apt", "version": "3.5.52build1"}], "bash": [{"arch": "amd64", "category": "shells", "name": "bash", "origin": "Ubuntu", "source": "apt", "version": "5.1-6ubuntu1"}], "bsdextrautils": [{"arch": "amd64", "category": "utils", "name": "bsdextrautils", "origin": "Ubuntu", "source": "apt", "version": "2.37.2-4ubuntu3"}], "bsdutils": [{"arch": "amd64", "category": "utils", "name": "bsdutils", "origin": "Ubuntu", "source": "apt", "version": "1:2.37.2-4ubuntu3"}], "ca-certificates": [{"arch": "all", "category": "misc", "name": "ca-certificates", "origin": "Ubuntu", "source": "apt", "version": "20211016ubuntu0.22.04.1"}], "coreutils": [{"arch": "amd64", "category": "utils", "name": "coreutils", "origin": "Ubuntu", "source": "apt", "version": "8.32-4.1ubuntu1"}], "dash": [{"arch": "amd64", "category": "shells", "name": "dash", "origin": "Ubuntu", "source": "apt", "version": "0.5.11+git20210903+057cd650a4ed-3build1"}], "dbus": [{"arch": "amd64", "category": "devel", "name": "dbus", "origin": "Ubuntu", "source": "apt", "version": "1.12.20-2ubuntu4.1"}], "debconf": [{"arch": "all", "category": "admin", "name": "debconf", "origin": "Ubuntu", "source": "apt", "version": "1.5.79ubuntu1"}], "debianutils": [{"arch": "amd64", "category": "utils", "name": "debianutils", "origin": "Ubuntu", "source": "apt", "version": "5.5-1ubuntu2"}], "diffutils": [{"arch": "amd64", "category": "utils", "name": "diffutils", "origin": "Ubuntu", "source": "apt", "version": "1:3.8-0ubuntu2"}], "dirmngr": [{"arch": "amd64", "category": "utils", "name": "dirmngr", "origin": "Ubuntu", "source": "apt", "version": "2.2.27-3ubuntu2.1"}], "distro-info-data": [{"arch": "all", "category": "devel", "name": "distro-info-data", "origin": "Ubuntu", "source": "apt", "version": "0.52ubuntu0.2"}], "dmsetup": [{"arch": "amd64", "category": "admin", "name": "dmsetup", "origin": "Ubuntu", "source": "apt", "version": "2:1.02.175-2.1ubuntu4"}], "dpkg": [{"arch": "amd64", "category": "admin", "name": "dpkg", "origin": "Ubuntu", "source": "apt", "version": "1.21.1ubuntu2.1"}], "e2fsprogs": [{"arch": "amd64", "category": "admin", "name": "e2fsprogs", "origin": "Ubuntu", "source": "apt", "version": "1.46.5-2ubuntu1.1"}], "findutils": [{"arch": "amd64", "category": "utils", "name": "findutils", "origin": "Ubuntu", "source": "apt", "version": "4.8.0-1ubuntu3"}], "gcc-12-base": [{"arch": "amd64", "category": "libs", "name": "gcc-12-base", "origin": "Ubuntu", "source": "apt", "version": "12.1.0-2ubuntu1~22.04"}], "gir1.2-glib-2.0": [{"arch": "amd64", "category": "introspection", "name": "gir1.2-glib-2.0", "origin": "Ubuntu", "source": "apt", "version": "1.72.0-1"}], "gnupg": [{"arch": "all", "category": "utils", "name": "gnupg", "origin": "Ubuntu", "source": "apt", "version": "2.2.27-3ubuntu2.1"}], "gnupg-l10n": [{"arch": "all", "category": "utils", "name": "gnupg-l10n", "origin": "Ubuntu", "source": "apt", "version": "2.2.27-3ubuntu2.1"}], "gnupg-utils": [{"arch": "amd64", "category": "utils", "name": "gnupg-utils", "origin": "Ubuntu", "source": "apt", "version": "2.2.27-3ubuntu2.1"}], "gnupg2": [{"arch": "all", "category": "universe/utils", "name": "gnupg2", "origin": "Ubuntu", "source": "apt", "version": "2.2.27-3ubuntu2.1"}], "gpg": [{"arch": "amd64", "category": "utils", "name": "gpg", "origin": "Ubuntu", "source": "apt", "version": "2.2.27-3ubuntu2.1"}], "gpg-agent": [{"arch": "amd64", "category": "utils", "name": "gpg-agent", "origin": "Ubuntu", "source": "apt", "version": "2.2.27-3ubuntu2.1"}], "gpg-wks-client": [{"arch": "amd64", "category": "utils", "name": "gpg-wks-client", "origin": "Ubuntu", "source": "apt", "version": "2.2.27-3ubuntu2.1"}], "gpg-wks-server": [{"arch": "amd64", "category": "utils", "name": "gpg-wks-server", "origin": "Ubuntu", "source": "apt", "version": "2.2.27-3ubuntu2.1"}], "gpgconf": [{"arch": "amd64", "category": "utils", "name": "gpgconf", "origin": "Ubuntu", "source": "apt", "version": "2.2.27-3ubuntu2.1"}], "gpgsm": [{"arch": "amd64", "category": "utils", "name": "gpgsm", "origin": "Ubuntu", "source": "apt", "version": "2.2.27-3ubuntu2.1"}], "gpgv": [{"arch": "amd64", "category": "utils", "name": "gpgv", "origin": "Ubuntu", "source": "apt", "version": "2.2.27-3ubuntu2.1"}], "grep": [{"arch": "amd64", "category": "utils", "name": "grep", "origin": "Ubuntu", "source": "apt", "version": "3.7-1build1"}], "groff-base": [{"arch": "amd64", "category": "text", "name": "groff-base", "origin": "Ubuntu", "source": "apt", "version": "1.22.4-8build1"}], "gzip": [{"arch": "amd64", "category": "utils", "name": "gzip", "origin": "Ubuntu", "source": "apt", "version": "1.10-4ubuntu4.1"}], "hostname": [{"arch": "amd64", "category": "admin", "name": "hostname", "origin": "Ubuntu", "source": "apt", "version": "3.23ubuntu2"}], "init-system-helpers": [{"arch": "all", "category": "admin", "name": "init-system-helpers", "origin": "Ubuntu", "source": "apt", "version": "1.62"}], "iproute2": [{"arch": "amd64", "category": "net", "name": "iproute2", "origin": "Ubuntu", "source": "apt", "version": "5.15.0-1ubuntu2"}], "iso-codes": [{"arch": "all", "category": "libs", "name": "iso-codes", "origin": "Ubuntu", "source": "apt", "version": "4.9.0-1"}], "libacl1": [{"arch": "amd64", "category": "libs", "name": "libacl1", "origin": "Ubuntu", "source": "apt", "version": "2.3.1-1"}], "libapparmor1": [{"arch": "amd64", "category": "libs", "name": "libapparmor1", "origin": "Ubuntu", "source": "apt", "version": "3.0.4-2ubuntu2.1"}], "libapt-pkg6.0": [{"arch": "amd64", "category": "libs", "name": "libapt-pkg6.0", "origin": "Ubuntu", "source": "apt", "version": "2.4.8"}], "libargon2-1": [{"arch": "amd64", "category": "libs", "name": "libargon2-1", "origin": "Ubuntu", "source": "apt", "version": "0~20171227-0.3"}], "libassuan0": [{"arch": "amd64", "category": "libs", "name": "libassuan0", "origin": "Ubuntu", "source": "apt", "version": "2.5.5-1build1"}], "libatm1": [{"arch": "amd64", "category": "libs", "name": "libatm1", "origin": "Ubuntu", "source": "apt", "version": "1:2.5.1-4build2"}], "libattr1": [{"arch": "amd64", "category": "libs", "name": "libattr1", "origin": "Ubuntu", "source": "apt", "version": "1:2.5.1-1build1"}], "libaudit-common": [{"arch": "all", "category": "libs", "name": "libaudit-common", "origin": "Ubuntu", "source": "apt", "version": "1:3.0.7-1build1"}], "libaudit1": [{"arch": "amd64", "category": "libs", "name": "libaudit1", "origin": "Ubuntu", "source": "apt", "version": "1:3.0.7-1build1"}], "libblkid1": [{"arch": "amd64", "category": "libs", "name": "libblkid1", "origin": "Ubuntu", "source": "apt", "version": "2.37.2-4ubuntu3"}], "libbpf0": [{"arch": "amd64", "category": "libs", "name": "libbpf0", "origin": "Ubuntu", "source": "apt", "version": "1:0.5.0-1ubuntu22.04.1"}], "libbsd0": [{"arch": "amd64", "category": "libs", "name": "libbsd0", "origin": "Ubuntu", "source": "apt", "version": "0.11.5-1"}], "libbz2-1.0": [{"arch": "amd64", "category": "libs", "name": "libbz2-1.0", "origin": "Ubuntu", "source": "apt", "version": "1.0.8-5build1"}], "libc-bin": [{"arch": "amd64", "category": "libs", "name": "libc-bin", "origin": "Ubuntu", "source": "apt", "version": "2.35-0ubuntu3.1"}], "libc6": [{"arch": "amd64", "category": "libs", "name": "libc6", "origin": "Ubuntu", "source": "apt", "version": "2.35-0ubuntu3.1"}], "libcap-ng0": [{"arch": "amd64", "category": "libs", "name": "libcap-ng0", "origin": "Ubuntu", "source": "apt", "version": "0.7.9-2.2build3"}], "libcap2": [{"arch": "amd64", "category": "libs", "name": "libcap2", "origin": "Ubuntu", "source": "apt", "version": "1:2.44-1build3"}], "libcap2-bin": [{"arch": "amd64", "category": "utils", "name": "libcap2-bin", "origin": "Ubuntu", "source": "apt", "version": "1:2.44-1build3"}], "libcom-err2": [{"arch": "amd64", "category": "libs", "name": "libcom-err2", "origin": "Ubuntu", "source": "apt", "version": "1.46.5-2ubuntu1.1"}], "libcrypt1": [{"arch": "amd64", "category": "libs", "name": "libcrypt1", "origin": "Ubuntu", "source": "apt", "version": "1:4.4.27-1"}], "libcryptsetup12": [{"arch": "amd64", "category": "libs", "name": "libcryptsetup12", "origin": "Ubuntu", "source": "apt", "version": "2:2.4.3-1ubuntu1.1"}], "libdb5.3": [{"arch": "amd64", "category": "libs", "name": "libdb5.3", "origin": "Ubuntu", "source": "apt", "version": "5.3.28+dfsg1-0.8ubuntu3"}], "libdbus-1-3": [{"arch": "amd64", "category": "libs", "name": "libdbus-1-3", "origin": "Ubuntu", "source": "apt", "version": "1.12.20-2ubuntu4.1"}], "libdebconfclient0": [{"arch": "amd64", "category": "libs", "name": "libdebconfclient0", "origin": "Ubuntu", "source": "apt", "version": "0.261ubuntu1"}], "libdevmapper1.02.1": [{"arch": "amd64", "category": "libs", "name": "libdevmapper1.02.1", "origin": "Ubuntu", "source": "apt", "version": "2:1.02.175-2.1ubuntu4"}], "libelf1": [{"arch": "amd64", "category": "libs", "name": "libelf1", "origin": "Ubuntu", "source": "apt", "version": "0.186-1build1"}], "libestr0": [{"arch": "amd64", "category": "libs", "name": "libestr0", "origin": "Ubuntu", "source": "apt", "version": "0.1.10-2.1build3"}], "libexpat1": [{"arch": "amd64", "category": "libs", "name": "libexpat1", "origin": "Ubuntu", "source": "apt", "version": "2.4.7-1ubuntu0.2"}], "libext2fs2": [{"arch": "amd64", "category": "libs", "name": "libext2fs2", "origin": "Ubuntu", "source": "apt", "version": "1.46.5-2ubuntu1.1"}], "libfastjson4": [{"arch": "amd64", "category": "libs", "name": "libfastjson4", "origin": "Ubuntu", "source": "apt", "version": "0.99.9-1build2"}], "libffi8": [{"arch": "amd64", "category": "libs", "name": "libffi8", "origin": "Ubuntu", "source": "apt", "version": "3.4.2-4"}], "libgcc-s1": [{"arch": "amd64", "category": "libs", "name": "libgcc-s1", "origin": "Ubuntu", "source": "apt", "version": "12.1.0-2ubuntu1~22.04"}], "libgcrypt20": [{"arch": "amd64", "category": "libs", "name": "libgcrypt20", "origin": "Ubuntu", "source": "apt", "version": "1.9.4-3ubuntu3"}], "libgdbm6": [{"arch": "amd64", "category": "libs", "name": "libgdbm6", "origin": "Ubuntu", "source": "apt", "version": "1.23-1"}], "libgirepository-1.0-1": [{"arch": "amd64", "category": "libs", "name": "libgirepository-1.0-1", "origin": "Ubuntu", "source": "apt", "version": "1.72.0-1"}], "libglib2.0-0": [{"arch": "amd64", "category": "libs", "name": "libglib2.0-0", "origin": "Ubuntu", "source": "apt", "version": "2.72.4-0ubuntu1"}], "libglib2.0-data": [{"arch": "all", "category": "misc", "name": "libglib2.0-data", "origin": "Ubuntu", "source": "apt", "version": "2.72.4-0ubuntu1"}], "libgmp10": [{"arch": "amd64", "category": "libs", "name": "libgmp10", "origin": "Ubuntu", "source": "apt", "version": "2:6.2.1+dfsg-3ubuntu1"}], "libgnutls30": [{"arch": "amd64", "category": "libs", "name": "libgnutls30", "origin": "Ubuntu", "source": "apt", "version": "3.7.3-4ubuntu1.1"}], "libgpg-error0": [{"arch": "amd64", "category": "libs", "name": "libgpg-error0", "origin": "Ubuntu", "source": "apt", "version": "1.43-3"}], "libgssapi-krb5-2": [{"arch": "amd64", "category": "libs", "name": "libgssapi-krb5-2", "origin": "Ubuntu", "source": "apt", "version": "1.19.2-2ubuntu0.1"}], "libhogweed6": [{"arch": "amd64", "category": "libs", "name": "libhogweed6", "origin": "Ubuntu", "source": "apt", "version": "3.7.3-1build2"}], "libicu70": [{"arch": "amd64", "category": "libs", "name": "libicu70", "origin": "Ubuntu", "source": "apt", "version": "70.1-2"}], "libidn2-0": [{"arch": "amd64", "category": "libs", "name": "libidn2-0", "origin": "Ubuntu", "source": "apt", "version": "2.3.2-2build1"}], "libip4tc2": [{"arch": "amd64", "category": "libs", "name": "libip4tc2", "origin": "Ubuntu", "source": "apt", "version": "1.8.7-1ubuntu5"}], "libjson-c5": [{"arch": "amd64", "category": "libs", "name": "libjson-c5", "origin": "Ubuntu", "source": "apt", "version": "0.15-3~ubuntu1.22.04.1"}], "libk5crypto3": [{"arch": "amd64", "category": "libs", "name": "libk5crypto3", "origin": "Ubuntu", "source": "apt", "version": "1.19.2-2ubuntu0.1"}], "libkeyutils1": [{"arch": "amd64", "category": "misc", "name": "libkeyutils1", "origin": "Ubuntu", "source": "apt", "version": "1.6.1-2ubuntu3"}], "libkmod2": [{"arch": "amd64", "category": "libs", "name": "libkmod2", "origin": "Ubuntu", "source": "apt", "version": "29-1ubuntu1"}], "libkrb5-3": [{"arch": "amd64", "category": "libs", "name": "libkrb5-3", "origin": "Ubuntu", "source": "apt", "version": "1.19.2-2ubuntu0.1"}], "libkrb5support0": [{"arch": "amd64", "category": "libs", "name": "libkrb5support0", "origin": "Ubuntu", "source": "apt", "version": "1.19.2-2ubuntu0.1"}], "libksba8": [{"arch": "amd64", "category": "libs", "name": "libksba8", "origin": "Ubuntu", "source": "apt", "version": "1.6.0-2ubuntu0.2"}], "libldap-2.5-0": [{"arch": "amd64", "category": "libs", "name": "libldap-2.5-0", "origin": "Ubuntu", "source": "apt", "version": "2.5.13+dfsg-0ubuntu0.22.04.1"}], "libldap-common": [{"arch": "all", "category": "libs", "name": "libldap-common", "origin": "Ubuntu", "source": "apt", "version": "2.5.13+dfsg-0ubuntu0.22.04.1"}], "liblz4-1": [{"arch": "amd64", "category": "libs", "name": "liblz4-1", "origin": "Ubuntu", "source": "apt", "version": "1.9.3-2build2"}], "liblzma5": [{"arch": "amd64", "category": "libs", "name": "liblzma5", "origin": "Ubuntu", "source": "apt", "version": "5.2.5-2ubuntu1"}], "libmd0": [{"arch": "amd64", "category": "libs", "name": "libmd0", "origin": "Ubuntu", "source": "apt", "version": "1.0.4-1build1"}], "libmnl0": [{"arch": "amd64", "category": "libs", "name": "libmnl0", "origin": "Ubuntu", "source": "apt", "version": "1.0.4-3build2"}], "libmount1": [{"arch": "amd64", "category": "libs", "name": "libmount1", "origin": "Ubuntu", "source": "apt", "version": "2.37.2-4ubuntu3"}], "libmpdec3": [{"arch": "amd64", "category": "libs", "name": "libmpdec3", "origin": "Ubuntu", "source": "apt", "version": "2.5.1-2build2"}], "libncurses6": [{"arch": "amd64", "category": "libs", "name": "libncurses6", "origin": "Ubuntu", "source": "apt", "version": "6.3-2"}], "libncursesw6": [{"arch": "amd64", "category": "libs", "name": "libncursesw6", "origin": "Ubuntu", "source": "apt", "version": "6.3-2"}], "libnettle8": [{"arch": "amd64", "category": "libs", "name": "libnettle8", "origin": "Ubuntu", "source": "apt", "version": "3.7.3-1build2"}], "libnpth0": [{"arch": "amd64", "category": "libs", "name": "libnpth0", "origin": "Ubuntu", "source": "apt", "version": "1.6-3build2"}], "libnsl2": [{"arch": "amd64", "category": "libs", "name": "libnsl2", "origin": "Ubuntu", "source": "apt", "version": "1.3.0-2build2"}], "libnss-systemd": [{"arch": "amd64", "category": "admin", "name": "libnss-systemd", "origin": "Ubuntu", "source": "apt", "version": "249.11-0ubuntu3.6"}], "libp11-kit0": [{"arch": "amd64", "category": "libs", "name": "libp11-kit0", "origin": "Ubuntu", "source": "apt", "version": "0.24.0-6build1"}], "libpam-cap": [{"arch": "amd64", "category": "libs", "name": "libpam-cap", "origin": "Ubuntu", "source": "apt", "version": "1:2.44-1build3"}], "libpam-modules": [{"arch": "amd64", "category": "admin", "name": "libpam-modules", "origin": "Ubuntu", "source": "apt", "version": "1.4.0-11ubuntu2.3"}], "libpam-modules-bin": [{"arch": "amd64", "category": "admin", "name": "libpam-modules-bin", "origin": "Ubuntu", "source": "apt", "version": "1.4.0-11ubuntu2.3"}], "libpam-runtime": [{"arch": "all", "category": "admin", "name": "libpam-runtime", "origin": "Ubuntu", "source": "apt", "version": "1.4.0-11ubuntu2.3"}], "libpam-systemd": [{"arch": "amd64", "category": "admin", "name": "libpam-systemd", "origin": "Ubuntu", "source": "apt", "version": "249.11-0ubuntu3.6"}], "libpam0g": [{"arch": "amd64", "category": "libs", "name": "libpam0g", "origin": "Ubuntu", "source": "apt", "version": "1.4.0-11ubuntu2.3"}], "libpcre2-8-0": [{"arch": "amd64", "category": "libs", "name": "libpcre2-8-0", "origin": "Ubuntu", "source": "apt", "version": "10.39-3ubuntu0.1"}], "libpcre3": [{"arch": "amd64", "category": "libs", "name": "libpcre3", "origin": "Ubuntu", "source": "apt", "version": "2:8.39-13ubuntu0.22.04.1"}], "libpipeline1": [{"arch": "amd64", "category": "libs", "name": "libpipeline1", "origin": "Ubuntu", "source": "apt", "version": "1.5.5-1"}], "libpopt0": [{"arch": "amd64", "category": "libs", "name": "libpopt0", "origin": "Ubuntu", "source": "apt", "version": "1.18-3build1"}], "libprocps8": [{"arch": "amd64", "category": "libs", "name": "libprocps8", "origin": "Ubuntu", "source": "apt", "version": "2:3.3.17-6ubuntu2"}], "libpython3-stdlib": [{"arch": "amd64", "category": "python", "name": "libpython3-stdlib", "origin": "Ubuntu", "source": "apt", "version": "3.10.6-1~22.04"}], "libpython3.10-minimal": [{"arch": "amd64", "category": "python", "name": "libpython3.10-minimal", "origin": "Ubuntu", "source": "apt", "version": "3.10.6-1~22.04.2"}], "libpython3.10-stdlib": [{"arch": "amd64", "category": "python", "name": "libpython3.10-stdlib", "origin": "Ubuntu", "source": "apt", "version": "3.10.6-1~22.04.2"}], "libreadline8": [{"arch": "amd64", "category": "libs", "name": "libreadline8", "origin": "Ubuntu", "source": "apt", "version": "8.1.2-1"}], "libsasl2-2": [{"arch": "amd64", "category": "libs", "name": "libsasl2-2", "origin": "Ubuntu", "source": "apt", "version": "2.1.27+dfsg2-3ubuntu1.1"}], "libsasl2-modules": [{"arch": "amd64", "category": "devel", "name": "libsasl2-modules", "origin": "Ubuntu", "source": "apt", "version": "2.1.27+dfsg2-3ubuntu1.1"}], "libsasl2-modules-db": [{"arch": "amd64", "category": "libs", "name": "libsasl2-modules-db", "origin": "Ubuntu", "source": "apt", "version": "2.1.27+dfsg2-3ubuntu1.1"}], "libseccomp2": [{"arch": "amd64", "category": "libs", "name": "libseccomp2", "origin": "Ubuntu", "source": "apt", "version": "2.5.3-2ubuntu2"}], "libselinux1": [{"arch": "amd64", "category": "libs", "name": "libselinux1", "origin": "Ubuntu", "source": "apt", "version": "3.3-1build2"}], "libsemanage-common": [{"arch": "all", "category": "libs", "name": "libsemanage-common", "origin": "Ubuntu", "source": "apt", "version": "3.3-1build2"}], "libsemanage2": [{"arch": "amd64", "category": "libs", "name": "libsemanage2", "origin": "Ubuntu", "source": "apt", "version": "3.3-1build2"}], "libsepol2": [{"arch": "amd64", "category": "libs", "name": "libsepol2", "origin": "Ubuntu", "source": "apt", "version": "3.3-1build1"}], "libsmartcols1": [{"arch": "amd64", "category": "libs", "name": "libsmartcols1", "origin": "Ubuntu", "source": "apt", "version": "2.37.2-4ubuntu3"}], "libsqlite3-0": [{"arch": "amd64", "category": "libs", "name": "libsqlite3-0", "origin": "Ubuntu", "source": "apt", "version": "3.37.2-2ubuntu0.1"}], "libss2": [{"arch": "amd64", "category": "libs", "name": "libss2", "origin": "Ubuntu", "source": "apt", "version": "1.46.5-2ubuntu1.1"}], "libssl3": [{"arch": "amd64", "category": "libs", "name": "libssl3", "origin": "Ubuntu", "source": "apt", "version": "3.0.2-0ubuntu1.8"}], "libstdc++6": [{"arch": "amd64", "category": "libs", "name": "libstdc++6", "origin": "Ubuntu", "source": "apt", "version": "12.1.0-2ubuntu1~22.04"}], "libsystemd0": [{"arch": "amd64", "category": "libs", "name": "libsystemd0", "origin": "Ubuntu", "source": "apt", "version": "249.11-0ubuntu3.6"}], "libtasn1-6": [{"arch": "amd64", "category": "libs", "name": "libtasn1-6", "origin": "Ubuntu", "source": "apt", "version": "4.18.0-4build1"}], "libtinfo6": [{"arch": "amd64", "category": "libs", "name": "libtinfo6", "origin": "Ubuntu", "source": "apt", "version": "6.3-2"}], "libtirpc-common": [{"arch": "all", "category": "libs", "name": "libtirpc-common", "origin": "Ubuntu", "source": "apt", "version": "1.3.2-2ubuntu0.1"}], "libtirpc3": [{"arch": "amd64", "category": "libs", "name": "libtirpc3", "origin": "Ubuntu", "source": "apt", "version": "1.3.2-2ubuntu0.1"}], "libuchardet0": [{"arch": "amd64", "category": "libs", "name": "libuchardet0", "origin": "Ubuntu", "source": "apt", "version": "0.0.7-1build2"}], "libudev1": [{"arch": "amd64", "category": "libs", "name": "libudev1", "origin": "Ubuntu", "source": "apt", "version": "249.11-0ubuntu3.6"}], "libunistring2": [{"arch": "amd64", "category": "libs", "name": "libunistring2", "origin": "Ubuntu", "source": "apt", "version": "1.0-1"}], "libuuid1": [{"arch": "amd64", "category": "libs", "name": "libuuid1", "origin": "Ubuntu", "source": "apt", "version": "2.37.2-4ubuntu3"}], "libxml2": [{"arch": "amd64", "category": "libs", "name": "libxml2", "origin": "Ubuntu", "source": "apt", "version": "2.9.13+dfsg-1ubuntu0.2"}], "libxtables12": [{"arch": "amd64", "category": "libs", "name": "libxtables12", "origin": "Ubuntu", "source": "apt", "version": "1.8.7-1ubuntu5"}], "libxxhash0": [{"arch": "amd64", "category": "libs", "name": "libxxhash0", "origin": "Ubuntu", "source": "apt", "version": "0.8.1-1"}], "libzstd1": [{"arch": "amd64", "category": "libs", "name": "libzstd1", "origin": "Ubuntu", "source": "apt", "version": "1.4.8+dfsg-3build1"}], "login": [{"arch": "amd64", "category": "admin", "name": "login", "origin": "Ubuntu", "source": "apt", "version": "1:4.8.1-2ubuntu2.1"}], "logrotate": [{"arch": "amd64", "category": "admin", "name": "logrotate", "origin": "Ubuntu", "source": "apt", "version": "3.19.0-1ubuntu1.1"}], "logsave": [{"arch": "amd64", "category": "admin", "name": "logsave", "origin": "Ubuntu", "source": "apt", "version": "1.46.5-2ubuntu1.1"}], "lsb-base": [{"arch": "all", "category": "misc", "name": "lsb-base", "origin": "Ubuntu", "source": "apt", "version": "11.1.0ubuntu4"}], "lsb-release": [{"arch": "all", "category": "misc", "name": "lsb-release", "origin": "Ubuntu", "source": "apt", "version": "11.1.0ubuntu4"}], "man-db": [{"arch": "amd64", "category": "doc", "name": "man-db", "origin": "Ubuntu", "source": "apt", "version": "2.10.2-1"}], "mawk": [{"arch": "amd64", "category": "utils", "name": "mawk", "origin": "Ubuntu", "source": "apt", "version": "1.3.4.20200120-3"}], "media-types": [{"arch": "all", "category": "net", "name": "media-types", "origin": "Ubuntu", "source": "apt", "version": "7.0.0"}], "mount": [{"arch": "amd64", "category": "admin", "name": "mount", "origin": "Ubuntu", "source": "apt", "version": "2.37.2-4ubuntu3"}], "ncurses-base": [{"arch": "all", "category": "utils", "name": "ncurses-base", "origin": "Ubuntu", "source": "apt", "version": "6.3-2"}], "ncurses-bin": [{"arch": "amd64", "category": "utils", "name": "ncurses-bin", "origin": "Ubuntu", "source": "apt", "version": "6.3-2"}], "networkd-dispatcher": [{"arch": "all", "category": "utils", "name": "networkd-dispatcher", "origin": "Ubuntu", "source": "apt", "version": "2.1-2ubuntu0.22.04.2"}], "openssl": [{"arch": "amd64", "category": "utils", "name": "openssl", "origin": "Ubuntu", "source": "apt", "version": "3.0.2-0ubuntu1.8"}], "passwd": [{"arch": "amd64", "category": "admin", "name": "passwd", "origin": "Ubuntu", "source": "apt", "version": "1:4.8.1-2ubuntu2.1"}], "perl-base": [{"arch": "amd64", "category": "perl", "name": "perl-base", "origin": "Ubuntu", "source": "apt", "version": "5.34.0-3ubuntu1.1"}], "pinentry-curses": [{"arch": "amd64", "category": "utils", "name": "pinentry-curses", "origin": "Ubuntu", "source": "apt", "version": "1.1.1-1build2"}], "procps": [{"arch": "amd64", "category": "admin", "name": "procps", "origin": "Ubuntu", "source": "apt", "version": "2:3.3.17-6ubuntu2"}], "python-apt-common": [{"arch": "all", "category": "python", "name": "python-apt-common", "origin": "Ubuntu", "source": "apt", "version": "2.4.0ubuntu1"}], "python3": [{"arch": "amd64", "category": "python", "name": "python3", "origin": "Ubuntu", "source": "apt", "version": "3.10.6-1~22.04"}], "python3-apt": [{"arch": "amd64", "category": "python", "name": "python3-apt", "origin": "Ubuntu", "source": "apt", "version": "2.4.0ubuntu1"}], "python3-dbus": [{"arch": "amd64", "category": "python", "name": "python3-dbus", "origin": "Ubuntu", "source": "apt", "version": "1.2.18-3build1"}], "python3-gi": [{"arch": "amd64", "category": "python", "name": "python3-gi", "origin": "Ubuntu", "source": "apt", "version": "3.42.1-0ubuntu1"}], "python3-minimal": [{"arch": "amd64", "category": "python", "name": "python3-minimal", "origin": "Ubuntu", "source": "apt", "version": "3.10.6-1~22.04"}], "python3.10": [{"arch": "amd64", "category": "python", "name": "python3.10", "origin": "Ubuntu", "source": "apt", "version": "3.10.6-1~22.04.2"}], "python3.10-minimal": [{"arch": "amd64", "category": "python", "name": "python3.10-minimal", "origin": "Ubuntu", "source": "apt", "version": "3.10.6-1~22.04.2"}], "readline-common": [{"arch": "all", "category": "utils", "name": "readline-common", "origin": "Ubuntu", "source": "apt", "version": "8.1.2-1"}], "rsyslog": [{"arch": "amd64", "category": "admin", "name": "rsyslog", "origin": "Ubuntu", "source": "apt", "version": "8.2112.0-2ubuntu2.2"}], "sed": [{"arch": "amd64", "category": "utils", "name": "sed", "origin": "Ubuntu", "source": "apt", "version": "4.8-1ubuntu2"}], "sensible-utils": [{"arch": "all", "category": "utils", "name": "sensible-utils", "origin": "Ubuntu", "source": "apt", "version": "0.0.17"}], "shared-mime-info": [{"arch": "amd64", "category": "misc", "name": "shared-mime-info", "origin": "Ubuntu", "source": "apt", "version": "2.1-2"}], "sudo": [{"arch": "amd64", "category": "admin", "name": "sudo", "origin": "Ubuntu", "source": "apt", "version": "1.9.9-1ubuntu2.2"}], "systemd": [{"arch": "amd64", "category": "admin", "name": "systemd", "origin": "Ubuntu", "source": "apt", "version": "249.11-0ubuntu3.6"}], "systemd-sysv": [{"arch": "amd64", "category": "admin", "name": "systemd-sysv", "origin": "Ubuntu", "source": "apt", "version": "249.11-0ubuntu3.6"}], "systemd-timesyncd": [{"arch": "amd64", "category": "admin", "name": "systemd-timesyncd", "origin": "Ubuntu", "source": "apt", "version": "249.11-0ubuntu3.6"}], "sysvinit-utils": [{"arch": "amd64", "category": "admin", "name": "sysvinit-utils", "origin": "Ubuntu", "source": "apt", "version": "3.01-1ubuntu1"}], "tar": [{"arch": "amd64", "category": "utils", "name": "tar", "origin": "Ubuntu", "source": "apt", "version": "1.34+dfsg-1build3"}], "ubuntu-keyring": [{"arch": "all", "category": "misc", "name": "ubuntu-keyring", "origin": "Ubuntu", "source": "apt", "version": "2021.03.26"}], "ucf": [{"arch": "all", "category": "utils", "name": "ucf", "origin": "Ubuntu", "source": "apt", "version": "3.0043"}], "usrmerge": [{"arch": "all", "category": "admin", "name": "usrmerge", "origin": "Ubuntu", "source": "apt", "version": "25ubuntu2"}], "util-linux": [{"arch": "amd64", "category": "utils", "name": "util-linux", "origin": "Ubuntu", "source": "apt", "version": "2.37.2-4ubuntu3"}], "vector": [{"arch": "amd64", "category": "admin", "name": "vector", "origin": "", "source": "apt", "version": "0.27.0-1"}], "xdg-user-dirs": [{"arch": "amd64", "category": "utils", "name": "xdg-user-dirs", "origin": "Ubuntu", "source": "apt", "version": "0.17-2ubuntu4"}], "zlib1g": [{"arch": "amd64", "category": "libs", "name": "zlib1g", "origin": "Ubuntu", "source": "apt", "version": "1:1.2.11.dfsg-2ubuntu9.2"}]}}, "changed": false}

TASK [Gather Local Services] ***************************************************
task path: /Users/ro.khabibullin/Projects/netology/mnt-homeworks/08-ansible-05-testing/vector/molecule/resources/tests/verify.yml:12
ok: [ubuntu_latest] => {"ansible_facts": {"services": {"apt-daily-upgrade.service": {"name": "apt-daily-upgrade.service", "source": "systemd", "state": "inactive", "status": "static"}, "apt-daily.service": {"name": "apt-daily.service", "source": "systemd", "state": "inactive", "status": "static"}, "auditd.service": {"name": "auditd.service", "source": "systemd", "state": "stopped", "status": "not-found"}, "autovt@.service": {"name": "autovt@.service", "source": "systemd", "state": "unknown", "status": "alias"}, "console-getty.service": {"name": "console-getty.service", "source": "systemd", "state": "inactive", "status": "enabled-runtime"}, "container-getty@.service": {"name": "container-getty@.service", "source": "systemd", "state": "unknown", "status": "static"}, "cryptdisks-early.service": {"name": "cryptdisks-early.service", "source": "systemd", "state": "inactive", "status": "masked"}, "cryptdisks.service": {"name": "cryptdisks.service", "source": "systemd", "state": "inactive", "status": "masked"}, "dbus": {"name": "dbus", "source": "sysv", "state": "stopped"}, "dbus-org.freedesktop.hostname1.service": {"name": "dbus-org.freedesktop.hostname1.service", "source": "systemd", "state": "inactive", "status": "alias"}, "dbus-org.freedesktop.locale1.service": {"name": "dbus-org.freedesktop.locale1.service", "source": "systemd", "state": "inactive", "status": "alias"}, "dbus-org.freedesktop.login1.service": {"name": "dbus-org.freedesktop.login1.service", "source": "systemd", "state": "inactive", "status": "alias"}, "dbus-org.freedesktop.resolve1.service": {"name": "dbus-org.freedesktop.resolve1.service", "source": "systemd", "state": "inactive", "status": "alias"}, "dbus-org.freedesktop.timedate1.service": {"name": "dbus-org.freedesktop.timedate1.service", "source": "systemd", "state": "inactive", "status": "alias"}, "dbus-org.freedesktop.timesync1.service": {"name": "dbus-org.freedesktop.timesync1.service", "source": "systemd", "state": "inactive", "status": "alias"}, "dbus.service": {"name": "dbus.service", "source": "systemd", "state": "stopped", "status": "static"}, "debug-shell.service": {"name": "debug-shell.service", "source": "systemd", "state": "inactive", "status": "disabled"}, "display-manager.service": {"name": "display-manager.service", "source": "systemd", "state": "stopped", "status": "not-found"}, "dmesg.service": {"name": "dmesg.service", "source": "systemd", "state": "inactive", "status": "disabled"}, "dpkg-db-backup.service": {"name": "dpkg-db-backup.service", "source": "systemd", "state": "inactive", "status": "static"}, "e2scrub@.service": {"name": "e2scrub@.service", "source": "systemd", "state": "unknown", "status": "static"}, "e2scrub_all.service": {"name": "e2scrub_all.service", "source": "systemd", "state": "inactive", "status": "static"}, "e2scrub_fail@.service": {"name": "e2scrub_fail@.service", "source": "systemd", "state": "unknown", "status": "static"}, "e2scrub_reap.service": {"name": "e2scrub_reap.service", "source": "systemd", "state": "inactive", "status": "disabled"}, "emergency.service": {"name": "emergency.service", "source": "systemd", "state": "stopped", "status": "static"}, "fstrim.service": {"name": "fstrim.service", "source": "systemd", "state": "inactive", "status": "static"}, "getty-static.service": {"name": "getty-static.service", "source": "systemd", "state": "inactive", "status": "static"}, "getty@.service": {"name": "getty@.service", "source": "systemd", "state": "unknown", "status": "disabled"}, "hwclock.service": {"name": "hwclock.service", "source": "systemd", "state": "inactive", "status": "masked"}, "hwclock.sh": {"name": "hwclock.sh", "source": "sysv", "state": "stopped"}, "initrd-cleanup.service": {"name": "initrd-cleanup.service", "source": "systemd", "state": "inactive", "status": "static"}, "initrd-parse-etc.service": {"name": "initrd-parse-etc.service", "source": "systemd", "state": "inactive", "status": "static"}, "initrd-switch-root.service": {"name": "initrd-switch-root.service", "source": "systemd", "state": "inactive", "status": "static"}, "initrd-udevadm-cleanup-db.service": {"name": "initrd-udevadm-cleanup-db.service", "source": "systemd", "state": "inactive", "status": "static"}, "kmod-static-nodes.service": {"name": "kmod-static-nodes.service", "source": "systemd", "state": "inactive", "status": "static"}, "kmod.service": {"name": "kmod.service", "source": "systemd", "state": "inactive", "status": "alias"}, "logrotate.service": {"name": "logrotate.service", "source": "systemd", "state": "inactive", "status": "static"}, "man-db.service": {"name": "man-db.service", "source": "systemd", "state": "inactive", "status": "static"}, "modprobe@.service": {"name": "modprobe@.service", "source": "systemd", "state": "unknown", "status": "static"}, "motd-news.service": {"name": "motd-news.service", "source": "systemd", "state": "inactive", "status": "static"}, "networkd-dispatcher.service": {"name": "networkd-dispatcher.service", "source": "systemd", "state": "inactive", "status": "disabled"}, "plymouth-start.service": {"name": "plymouth-start.service", "source": "systemd", "state": "stopped", "status": "not-found"}, "procps": {"name": "procps", "source": "sysv", "state": "stopped"}, "procps.service": {"name": "procps.service", "source": "systemd", "state": "inactive", "status": "alias"}, "quotaon.service": {"name": "quotaon.service", "source": "systemd", "state": "inactive", "status": "static"}, "rc-local.service": {"name": "rc-local.service", "source": "systemd", "state": "inactive", "status": "static"}, "rc.service": {"name": "rc.service", "source": "systemd", "state": "inactive", "status": "masked"}, "rcS.service": {"name": "rcS.service", "source": "systemd", "state": "inactive", "status": "masked"}, "rescue.service": {"name": "rescue.service", "source": "systemd", "state": "stopped", "status": "static"}, "rsyslog.service": {"name": "rsyslog.service", "source": "systemd", "state": "stopped", "status": "enabled"}, "serial-getty@.service": {"name": "serial-getty@.service", "source": "systemd", "state": "unknown", "status": "disabled"}, "sudo.service": {"name": "sudo.service", "source": "systemd", "state": "inactive", "status": "masked"}, "syslog.service": {"name": "syslog.service", "source": "systemd", "state": "inactive", "status": "alias"}, "system-update-cleanup.service": {"name": "system-update-cleanup.service", "source": "systemd", "state": "inactive", "status": "static"}, "systemd-ask-password-console.service": {"name": "systemd-ask-password-console.service", "source": "systemd", "state": "inactive", "status": "static"}, "systemd-ask-password-wall.service": {"name": "systemd-ask-password-wall.service", "source": "systemd", "state": "inactive", "status": "static"}, "systemd-backlight@.service": {"name": "systemd-backlight@.service", "source": "systemd", "state": "unknown", "status": "static"}, "systemd-binfmt.service": {"name": "systemd-binfmt.service", "source": "systemd", "state": "inactive", "status": "static"}, "systemd-bless-boot.service": {"name": "systemd-bless-boot.service", "source": "systemd", "state": "inactive", "status": "static"}, "systemd-boot-check-no-failures.service": {"name": "systemd-boot-check-no-failures.service", "source": "systemd", "state": "inactive", "status": "disabled"}, "systemd-boot-system-token.service": {"name": "systemd-boot-system-token.service", "source": "systemd", "state": "inactive", "status": "static"}, "systemd-exit.service": {"name": "systemd-exit.service", "source": "systemd", "state": "inactive", "status": "static"}, "systemd-fsck-root.service": {"name": "systemd-fsck-root.service", "source": "systemd", "state": "stopped", "status": "static"}, "systemd-fsck@.service": {"name": "systemd-fsck@.service", "source": "systemd", "state": "unknown", "status": "static"}, "systemd-fsckd.service": {"name": "systemd-fsckd.service", "source": "systemd", "state": "stopped", "status": "static"}, "systemd-halt.service": {"name": "systemd-halt.service", "source": "systemd", "state": "inactive", "status": "static"}, "systemd-hibernate-resume@.service": {"name": "systemd-hibernate-resume@.service", "source": "systemd", "state": "unknown", "status": "static"}, "systemd-hibernate.service": {"name": "systemd-hibernate.service", "source": "systemd", "state": "inactive", "status": "static"}, "systemd-hostnamed.service": {"name": "systemd-hostnamed.service", "source": "systemd", "state": "inactive", "status": "static"}, "systemd-hybrid-sleep.service": {"name": "systemd-hybrid-sleep.service", "source": "systemd", "state": "inactive", "status": "static"}, "systemd-initctl.service": {"name": "systemd-initctl.service", "source": "systemd", "state": "inactive", "status": "static"}, "systemd-journal-flush.service": {"name": "systemd-journal-flush.service", "source": "systemd", "state": "inactive", "status": "static"}, "systemd-journald.service": {"name": "systemd-journald.service", "source": "systemd", "state": "running", "status": "static"}, "systemd-journald@.service": {"name": "systemd-journald@.service", "source": "systemd", "state": "unknown", "status": "static"}, "systemd-kexec.service": {"name": "systemd-kexec.service", "source": "systemd", "state": "inactive", "status": "static"}, "systemd-localed.service": {"name": "systemd-localed.service", "source": "systemd", "state": "inactive", "status": "static"}, "systemd-logind.service": {"name": "systemd-logind.service", "source": "systemd", "state": "inactive", "status": "static"}, "systemd-machine-id-commit.service": {"name": "systemd-machine-id-commit.service", "source": "systemd", "state": "inactive", "status": "static"}, "systemd-modules-load.service": {"name": "systemd-modules-load.service", "source": "systemd", "state": "inactive", "status": "static"}, "systemd-network-generator.service": {"name": "systemd-network-generator.service", "source": "systemd", "state": "inactive", "status": "disabled"}, "systemd-networkd-wait-online.service": {"name": "systemd-networkd-wait-online.service", "source": "systemd", "state": "inactive", "status": "disabled"}, "systemd-networkd.service": {"name": "systemd-networkd.service", "source": "systemd", "state": "inactive", "status": "disabled"}, "systemd-poweroff.service": {"name": "systemd-poweroff.service", "source": "systemd", "state": "inactive", "status": "static"}, "systemd-pstore.service": {"name": "systemd-pstore.service", "source": "systemd", "state": "inactive", "status": "disabled"}, "systemd-quotacheck.service": {"name": "systemd-quotacheck.service", "source": "systemd", "state": "inactive", "status": "static"}, "systemd-random-seed.service": {"name": "systemd-random-seed.service", "source": "systemd", "state": "inactive", "status": "static"}, "systemd-reboot.service": {"name": "systemd-reboot.service", "source": "systemd", "state": "inactive", "status": "static"}, "systemd-remount-fs.service": {"name": "systemd-remount-fs.service", "source": "systemd", "state": "stopped", "status": "enabled-runtime"}, "systemd-resolved.service": {"name": "systemd-resolved.service", "source": "systemd", "state": "inactive", "status": "enabled"}, "systemd-rfkill.service": {"name": "systemd-rfkill.service", "source": "systemd", "state": "inactive", "status": "static"}, "systemd-suspend-then-hibernate.service": {"name": "systemd-suspend-then-hibernate.service", "source": "systemd", "state": "inactive", "status": "static"}, "systemd-suspend.service": {"name": "systemd-suspend.service", "source": "systemd", "state": "inactive", "status": "static"}, "systemd-sysctl.service": {"name": "systemd-sysctl.service", "source": "systemd", "state": "inactive", "status": "static"}, "systemd-sysext.service": {"name": "systemd-sysext.service", "source": "systemd", "state": "inactive", "status": "disabled"}, "systemd-sysusers.service": {"name": "systemd-sysusers.service", "source": "systemd", "state": "stopped", "status": "static"}, "systemd-time-wait-sync.service": {"name": "systemd-time-wait-sync.service", "source": "systemd", "state": "inactive", "status": "disabled"}, "systemd-timedated.service": {"name": "systemd-timedated.service", "source": "systemd", "state": "inactive", "status": "static"}, "systemd-timesyncd.service": {"name": "systemd-timesyncd.service", "source": "systemd", "state": "inactive", "status": "enabled"}, "systemd-tmpfiles-clean.service": {"name": "systemd-tmpfiles-clean.service", "source": "systemd", "state": "stopped", "status": "static"}, "systemd-tmpfiles-setup-dev.service": {"name": "systemd-tmpfiles-setup-dev.service", "source": "systemd", "state": "inactive", "status": "static"}, "systemd-tmpfiles-setup.service": {"name": "systemd-tmpfiles-setup.service", "source": "systemd", "state": "stopped", "status": "static"}, "systemd-update-done.service": {"name": "systemd-update-done.service", "source": "systemd", "state": "stopped", "status": "not-found"}, "systemd-update-utmp-runlevel.service": {"name": "systemd-update-utmp-runlevel.service", "source": "systemd", "state": "stopped", "status": "static"}, "systemd-update-utmp.service": {"name": "systemd-update-utmp.service", "source": "systemd", "state": "stopped", "status": "static"}, "systemd-user-sessions.service": {"name": "systemd-user-sessions.service", "source": "systemd", "state": "inactive", "status": "static"}, "systemd-volatile-root.service": {"name": "systemd-volatile-root.service", "source": "systemd", "state": "inactive", "status": "static"}, "user-runtime-dir@.service": {"name": "user-runtime-dir@.service", "source": "systemd", "state": "unknown", "status": "static"}, "user@.service": {"name": "user@.service", "source": "systemd", "state": "unknown", "status": "static"}, "vector.service": {"name": "vector.service", "source": "systemd", "state": "running", "status": "disabled"}, "x11-common.service": {"name": "x11-common.service", "source": "systemd", "state": "inactive", "status": "masked"}}}, "changed": false}

PLAY RECAP *********************************************************************
ubuntu_latest              : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

INFO     Verifier completed successfully.
INFO     Running ubuntu_latest > cleanup
WARNING  Skipping, cleanup playbook not configured.
INFO     Running ubuntu_latest > destroy
[WARNING]: Error getting vault password file (datatools): The vault password
file /Users/ro.khabibullin/.vault/datatools_vault was not found
[WARNING]: Error getting vault password file (getstream): The vault password
file /Users/ro.khabibullin/.vault/getstream was not found

PLAY [Destroy] *****************************************************************

TASK [Set async_dir for HOME env] **********************************************
ok: [localhost]

TASK [Destroy molecule instance(s)] ********************************************
changed: [localhost] => (item=ubuntu_latest)

TASK [Wait for instance(s) deletion to complete] *******************************
FAILED - RETRYING: [localhost]: Wait for instance(s) deletion to complete (300 retries left).
changed: [localhost] => (item=ubuntu_latest)

TASK [Delete docker networks(s)] ***********************************************
skipping: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=3    changed=2    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0

INFO     Pruning extra files from scenario ephemeral directory

```

</details>

<details>
<summary><b>➜ vector git:(MNT-video) ✗ molecule test -s centos_8</b></summary>

```commandline 
INFO     centos_8 scenario test matrix: dependency, lint, cleanup, destroy, syntax, create, prepare, converge, idempotence, side_effect, verify, cleanup, destroy
INFO     Performing prerun with role_name_check=0...
INFO     Set ANSIBLE_LIBRARY=/Users/ro.khabibullin/.cache/ansible-compat/b0d51c/modules:/Users/ro.khabibullin/.ansible/plugins/modules:/usr/share/ansible/plugins/modules
INFO     Set ANSIBLE_COLLECTIONS_PATH=/Users/ro.khabibullin/.cache/ansible-compat/b0d51c/collections:/Users/ro.khabibullin/.ansible/collections:/usr/share/ansible/collections
INFO     Set ANSIBLE_ROLES_PATH=/Users/ro.khabibullin/.cache/ansible-compat/b0d51c/roles:/Users/ro.khabibullin/.ansible/roles:/usr/share/ansible/roles:/etc/ansible/roles
INFO     Using /Users/ro.khabibullin/.cache/ansible-compat/b0d51c/roles/ramireshab.vector symlink to current repository in order to enable Ansible to find the role using its expected full name.
INFO     Running centos_8 > dependency
WARNING  Skipping, missing the requirements file.
WARNING  Skipping, missing the requirements file.
INFO     Running centos_8 > lint
./tasks/main.yml
  14:1      error    too many blank lines (1 > 0)  (empty-lines)

WARNING  Listing 1 violation(s) that are fatal
syntax-check[specific]: the role 'vector' was not found in /Users/ro.khabibullin/Projects/netology/mnt-homeworks/08-ansible-05-testing/vector/tests/roles:/Users/ro.khabibullin/.cache/ansible-compat/b0d51c/roles:/Users/ro.khabibullin/.ansible/roles:/usr/share/ansible/roles:/etc/ansible/roles:/Users/ro.khabibullin/Projects/netology/mnt-homeworks/08-ansible-05-testing/vector/tests
tests/test.yml:5:7


                  Rule Violation Summary                   
 count tag                    profile rule associated tags 
     1 syntax-check[specific] min     core, unskippable    

Failed after : 1 failure(s), 0 warning(s) on 31 files.
INFO     Running centos_8 > cleanup
WARNING  Skipping, cleanup playbook not configured.
INFO     Running centos_8 > destroy
INFO     Sanity checks: 'docker'
[WARNING]: Error getting vault password file (datatools): The vault password
file /Users/ro.khabibullin/.vault/datatools_vault was not found
[WARNING]: Error getting vault password file (getstream): The vault password
file /Users/ro.khabibullin/.vault/getstream was not found

PLAY [Destroy] *****************************************************************

TASK [Set async_dir for HOME env] **********************************************
ok: [localhost]

TASK [Destroy molecule instance(s)] ********************************************
changed: [localhost] => (item=centos_8)

TASK [Wait for instance(s) deletion to complete] *******************************
FAILED - RETRYING: [localhost]: Wait for instance(s) deletion to complete (300 retries left).
ok: [localhost] => (item=centos_8)

TASK [Delete docker networks(s)] ***********************************************
skipping: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=3    changed=1    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0

INFO     Running centos_8 > syntax
[WARNING]: Error getting vault password file (datatools): The vault password
file /Users/ro.khabibullin/.vault/datatools_vault was not found
[WARNING]: Error getting vault password file (getstream): The vault password
file /Users/ro.khabibullin/.vault/getstream was not found

playbook: /Users/ro.khabibullin/Projects/netology/mnt-homeworks/08-ansible-05-testing/vector/molecule/resources/playbooks/converge.yml
INFO     Running centos_8 > create
[WARNING]: Error getting vault password file (datatools): The vault password
file /Users/ro.khabibullin/.vault/datatools_vault was not found
[WARNING]: Error getting vault password file (getstream): The vault password
file /Users/ro.khabibullin/.vault/getstream was not found

PLAY [Create] ******************************************************************

TASK [Set async_dir for HOME env] **********************************************
ok: [localhost]

TASK [Log into a Docker registry] **********************************************
skipping: [localhost] => (item=None) 
skipping: [localhost]

TASK [Check presence of custom Dockerfiles] ************************************
ok: [localhost] => (item={'capabilities': ['SYS_ADMIN'], 'command': '/usr/sbin/init', 'dockerfile': '../resources/Dockerfile.j2', 'env': {'ANSIBLE_USER': 'ansible', 'DEPLOY_GROUP': 'deployer', 'SUDO_GROUP': 'wheel', 'container': 'docker'}, 'image': 'pycontribs/centos:8', 'name': 'centos_8', 'privileged': True, 'tmpfs': ['/run', '/tmp'], 'volumes': ['/sys/fs/cgroup:/sys/fs/cgroup']})

TASK [Create Dockerfiles from image names] *************************************
changed: [localhost] => (item={'capabilities': ['SYS_ADMIN'], 'command': '/usr/sbin/init', 'dockerfile': '../resources/Dockerfile.j2', 'env': {'ANSIBLE_USER': 'ansible', 'DEPLOY_GROUP': 'deployer', 'SUDO_GROUP': 'wheel', 'container': 'docker'}, 'image': 'pycontribs/centos:8', 'name': 'centos_8', 'privileged': True, 'tmpfs': ['/run', '/tmp'], 'volumes': ['/sys/fs/cgroup:/sys/fs/cgroup']})

TASK [Synchronization the context] *********************************************
changed: [localhost] => (item={'capabilities': ['SYS_ADMIN'], 'command': '/usr/sbin/init', 'dockerfile': '../resources/Dockerfile.j2', 'env': {'ANSIBLE_USER': 'ansible', 'DEPLOY_GROUP': 'deployer', 'SUDO_GROUP': 'wheel', 'container': 'docker'}, 'image': 'pycontribs/centos:8', 'name': 'centos_8', 'privileged': True, 'tmpfs': ['/run', '/tmp'], 'volumes': ['/sys/fs/cgroup:/sys/fs/cgroup']})

TASK [Discover local Docker images] ********************************************
ok: [localhost] => (item=None)
ok: [localhost]

TASK [Build an Ansible compatible image (new)] *********************************
failed: [localhost] (item=molecule_local/pycontribs/centos:8) => {"ansible_loop_var": "item", "attempts": 3, "changed": false, "item": {"ansible_index_var": "i", "ansible_loop_var": "item", "changed": true, "checksum": "06b3cb5226c5fc519334b8a352a41e18a216bbee", "dest": "/Users/ro.khabibullin/.cache/molecule/vector/centos_8/Dockerfile_pycontribs_centos_8", "diff": [], "failed": false, "gid": 20, "group": "staff", "i": 0, "invocation": {"module_args": {"_original_basename": "Dockerfile.j2", "attributes": null, "backup": false, "checksum": "06b3cb5226c5fc519334b8a352a41e18a216bbee", "content": null, "dest": "/Users/ro.khabibullin/.cache/molecule/vector/centos_8/Dockerfile_pycontribs_centos_8", "directory_mode": null, "follow": false, "force": true, "group": null, "local_follow": null, "mode": "0600", "owner": null, "remote_src": null, "selevel": null, "serole": null, "setype": null, "seuser": null, "src": "/Users/ro.khabibullin/.ansible/tmp/ansible-tmp-1677077862.291989-69605-18792516646712/source", "unsafe_writes": false, "validate": null}}, "item": {"capabilities": ["SYS_ADMIN"], "command": "/usr/sbin/init", "dockerfile": "../resources/Dockerfile.j2", "env": {"ANSIBLE_USER": "ansible", "DEPLOY_GROUP": "deployer", "SUDO_GROUP": "wheel", "container": "docker"}, "image": "pycontribs/centos:8", "name": "centos_8", "privileged": true, "tmpfs": ["/run", "/tmp"], "volumes": ["/sys/fs/cgroup:/sys/fs/cgroup"]}, "md5sum": "5728441d73bcfecd33b68e56cd3932eb", "mode": "0600", "owner": "ro.khabibullin", "size": 2210, "src": "/Users/ro.khabibullin/.ansible/tmp/ansible-tmp-1677077862.291989-69605-18792516646712/source", "state": "file", "uid": 503}, "msg": "Error building molecule_local/pycontribs/centos - code: 1, message: The command '/bin/sh -c if [ $(command -v apt-get) ]; then apt-get update && apt-get upgrade -y && apt-get install -y apt-transport-https gnupg2 python3-minimal python3-apt man systemd systemd-sysv rsyslog sudo bash ca-certificates iproute2 && apt-get clean;     elif [ $(command -v dnf) ]; then dnf makecache && dnf --assumeyes upgrade && dnf --assumeyes install python3 sudo python3-devel python*-dnf bash iproute && dnf clean all;     elif [ $(command -v yum) ]; then sed -i 's/^\\(tsflags=*\\)/# \\1/g' /etc/yum.conf && yum makecache fast && yum upgrade -y && yum makecache fast && yum install -y sudo python3 systemd rsyslog man yum-plugin-ovl bash iproute && sed -i 's/plugins=0/plugins=1/g' /etc/yum.conf && yum clean all;     elif [ $(command -v zypper) ]; then zypper refresh && zypper install -y python sudo bash python-xml iproute2 && zypper clean -a;     elif [ $(command -v apk) ]; then apk update && apk add --no-cache python sudo bash ca-certificates;     elif [ $(command -v xbps-install) ]; then xbps-install -Syu && xbps-install -y python sudo bash ca-certificates iproute2 && xbps-remove -O; fi' returned a non-zero code: 1, logs: ['Step 1/10 : FROM pycontribs/centos:8', '', 'Pulling from pycontribs/centos', 'Digest: sha256:6a43bcc66a0bce18c49863fc299ace63bbafd624d6e0ce8b86a7e9a86d9f348f', 'Status: Image is up to date for pycontribs/centos:8', ' ---> fec8cb567d93', 'Step 2/10 : ENV ANSIBLE_USER ansible', '', ' ---> Using cache', ' ---> bac4ba930778', 'Step 3/10 : ENV DEPLOY_GROUP deployer', '', ' ---> Using cache', ' ---> 8e639b61986c', 'Step 4/10 : ENV SUDO_GROUP wheel', '', ' ---> Using cache', ' ---> 1919fc3e6781', 'Step 5/10 : ENV container docker', '', ' ---> Using cache', ' ---> dc6e7ce57fab', \"Step 6/10 : RUN if [ $(command -v apt-get) ]; then apt-get update && apt-get upgrade -y && apt-get install -y apt-transport-https gnupg2 python3-minimal python3-apt man systemd systemd-sysv rsyslog sudo bash ca-certificates iproute2 && apt-get clean;     elif [ $(command -v dnf) ]; then dnf makecache && dnf --assumeyes upgrade && dnf --assumeyes install python3 sudo python3-devel python*-dnf bash iproute && dnf clean all;     elif [ $(command -v yum) ]; then sed -i 's/^\\\\(tsflags=*\\\\)/# \\\\1/g' /etc/yum.conf && yum makecache fast && yum upgrade -y && yum makecache fast && yum install -y sudo python3 systemd rsyslog man yum-plugin-ovl bash iproute && sed -i 's/plugins=0/plugins=1/g' /etc/yum.conf && yum clean all;     elif [ $(command -v zypper) ]; then zypper refresh && zypper install -y python sudo bash python-xml iproute2 && zypper clean -a;     elif [ $(command -v apk) ]; then apk update && apk add --no-cache python sudo bash ca-certificates;     elif [ $(command -v xbps-install) ]; then xbps-install -Syu && xbps-install -y python sudo bash ca-certificates iproute2 && xbps-remove -O; fi\", '', ' ---> Running in ca985faaf94f', 'CentOS Linux 8 - AppStream                      102  B/s |  38  B     00:00    ', \"\\x1b[91mError: Failed to download metadata for repo 'appstream': Cannot prepare internal mirrorlist: No URLs in mirrorlist\", '\\x1b[0m', 'Removing intermediate container ca985faaf94f']"}
FAILED - RETRYING: [localhost]: Build an Ansible compatible image (new) (3 retries left).
FAILED - RETRYING: [localhost]: Build an Ansible compatible image (new) (2 retries left).
FAILED - RETRYING: [localhost]: Build an Ansible compatible image (new) (1 retries left).

PLAY RECAP *********************************************************************
localhost                  : ok=5    changed=2    unreachable=0    failed=1    skipped=1    rescued=0    ignored=0

WARNING  Retrying execution failure 2 of: ansible-playbook --inventory /Users/ro.khabibullin/.cache/molecule/vector/centos_8/inventory --skip-tags molecule-notest,notest /usr/local/lib/python3.11/site-packages/molecule_docker/playbooks/create.yml
CRITICAL Ansible return code was 2, command was: ['ansible-playbook', '--inventory', '/Users/ro.khabibullin/.cache/molecule/vector/centos_8/inventory', '--skip-tags', 'molecule-notest,notest', '/usr/local/lib/python3.11/site-packages/molecule_docker/playbooks/create.yml']
WARNING  An error occurred during the test sequence action: 'create'. Cleaning up.
INFO     Running centos_8 > cleanup
WARNING  Skipping, cleanup playbook not configured.
INFO     Running centos_8 > destroy
[WARNING]: Error getting vault password file (datatools): The vault password
file /Users/ro.khabibullin/.vault/datatools_vault was not found
[WARNING]: Error getting vault password file (getstream): The vault password
file /Users/ro.khabibullin/.vault/getstream was not found

PLAY [Destroy] *****************************************************************

TASK [Set async_dir for HOME env] **********************************************
ok: [localhost]

TASK [Destroy molecule instance(s)] ********************************************
changed: [localhost] => (item=centos_8)

TASK [Wait for instance(s) deletion to complete] *******************************
FAILED - RETRYING: [localhost]: Wait for instance(s) deletion to complete (300 retries left).
ok: [localhost] => (item=centos_8)

TASK [Delete docker networks(s)] ***********************************************
skipping: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=3    changed=1    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0

INFO     Pruning extra files from scenario ephemeral directory

```

</details>

4. Добавьте несколько assert'ов в verify.yml файл для  проверки работоспособности vector-role (проверка, что конфиг валидный, проверка успешности запуска, etc). Запустите тестирование роли повторно и проверьте, что оно прошло успешно.

<details>
<summary><b>INFO     Running ubuntu_latest > verify</b></summary>

```commandline
INFO     Running ubuntu_latest > verify
INFO     Running Ansible Verifier
[WARNING]: Error getting vault password file (datatools): The vault password
file /Users/ro.khabibullin/.vault/datatools_vault was not found
[WARNING]: Error getting vault password file (getstream): The vault password
file /Users/ro.khabibullin/.vault/getstream was not found
ansible-playbook [core 2.14.2]
  config file = /Users/ro.khabibullin/.cache/molecule/vector/ubuntu_latest/ansible.cfg
  configured module search path = ['/usr/local/lib/python3.11/site-packages/molecule/provisioner/ansible/plugins/modules', '/Users/ro.khabibullin/.cache/molecule/vector/ubuntu_latest/library', '/Users/ro.khabibullin/Projects/netology/mnt-homeworks/08-ansible-05-testing/vector/library', '/Users/ro.khabibullin/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /usr/local/lib/python3.11/site-packages/ansible
  ansible collection location = /Users/ro.khabibullin/.cache/ansible-compat/b0d51c/collections:/Users/ro.khabibullin/.cache/molecule/vector/ubuntu_latest/collections:/Users/ro.khabibullin/.ansible/collections:/usr/share/ansible/collections:/etc/ansible/collections
  executable location = /usr/local/bin/ansible-playbook
  python version = 3.11.1 (main, Dec 23 2022, 09:39:26) [Clang 14.0.0 (clang-1400.0.29.202)] (/usr/local/opt/python@3.11/bin/python3.11)
  jinja version = 3.1.2
  libyaml = False
Using /Users/ro.khabibullin/.cache/molecule/vector/ubuntu_latest/ansible.cfg as config file
Skipping callback 'default', as we already have a stdout callback.
Skipping callback 'minimal', as we already have a stdout callback.
Skipping callback 'oneline', as we already have a stdout callback.

PLAYBOOK: verify.yml ***********************************************************
1 plays in /Users/ro.khabibullin/Projects/netology/mnt-homeworks/08-ansible-05-testing/vector/molecule/resources/tests/verify.yml

PLAY [Verify] ******************************************************************

TASK [Gather Installed Packages] ***********************************************
task path: /Users/ro.khabibullin/Projects/netology/mnt-homeworks/08-ansible-05-testing/vector/molecule/resources/tests/verify.yml:7
ok: [ubuntu_latest] => {"ansible_facts": {"discovered_interpreter_python": "/usr/bin/python3", "packages": {"adduser": [{"arch": "all", "category": "admin", "name": "adduser", "origin": "Ubuntu", "source": "apt", "version": "3.118ubuntu5"}], "apt": [{"arch": "amd64", "category": "admin", "name": "apt", "origin": "Ubuntu", "source": "apt", "version": "2.4.8"}], "apt-transport-https": [{"arch": "all", "category": "universe/admin", "name": "apt-transport-https", "origin": "Ubuntu", "source": "apt", "version": "2.4.8"}], "base-files": [{"arch": "amd64", "category": "admin", "name": "base-files", "origin": "Ubuntu", "source": "apt", "version": "12ubuntu4.3"}], "base-passwd": [{"arch": "amd64", "category": "admin", "name": "base-passwd", "origin": "Ubuntu", "source": "apt", "version": "3.5.52build1"}], "bash": [{"arch": "amd64", "category": "shells", "name": "bash", "origin": "Ubuntu", "source": "apt", "version": "5.1-6ubuntu1"}], "bsdextrautils": [{"arch": "amd64", "category": "utils", "name": "bsdextrautils", "origin": "Ubuntu", "source": "apt", "version": "2.37.2-4ubuntu3"}], "bsdutils": [{"arch": "amd64", "category": "utils", "name": "bsdutils", "origin": "Ubuntu", "source": "apt", "version": "1:2.37.2-4ubuntu3"}], "ca-certificates": [{"arch": "all", "category": "misc", "name": "ca-certificates", "origin": "Ubuntu", "source": "apt", "version": "20211016ubuntu0.22.04.1"}], "coreutils": [{"arch": "amd64", "category": "utils", "name": "coreutils", "origin": "Ubuntu", "source": "apt", "version": "8.32-4.1ubuntu1"}], "dash": [{"arch": "amd64", "category": "shells", "name": "dash", "origin": "Ubuntu", "source": "apt", "version": "0.5.11+git20210903+057cd650a4ed-3build1"}], "dbus": [{"arch": "amd64", "category": "devel", "name": "dbus", "origin": "Ubuntu", "source": "apt", "version": "1.12.20-2ubuntu4.1"}], "debconf": [{"arch": "all", "category": "admin", "name": "debconf", "origin": "Ubuntu", "source": "apt", "version": "1.5.79ubuntu1"}], "debianutils": [{"arch": "amd64", "category": "utils", "name": "debianutils", "origin": "Ubuntu", "source": "apt", "version": "5.5-1ubuntu2"}], "diffutils": [{"arch": "amd64", "category": "utils", "name": "diffutils", "origin": "Ubuntu", "source": "apt", "version": "1:3.8-0ubuntu2"}], "dirmngr": [{"arch": "amd64", "category": "utils", "name": "dirmngr", "origin": "Ubuntu", "source": "apt", "version": "2.2.27-3ubuntu2.1"}], "distro-info-data": [{"arch": "all", "category": "devel", "name": "distro-info-data", "origin": "Ubuntu", "source": "apt", "version": "0.52ubuntu0.2"}], "dmsetup": [{"arch": "amd64", "category": "admin", "name": "dmsetup", "origin": "Ubuntu", "source": "apt", "version": "2:1.02.175-2.1ubuntu4"}], "dpkg": [{"arch": "amd64", "category": "admin", "name": "dpkg", "origin": "Ubuntu", "source": "apt", "version": "1.21.1ubuntu2.1"}], "e2fsprogs": [{"arch": "amd64", "category": "admin", "name": "e2fsprogs", "origin": "Ubuntu", "source": "apt", "version": "1.46.5-2ubuntu1.1"}], "findutils": [{"arch": "amd64", "category": "utils", "name": "findutils", "origin": "Ubuntu", "source": "apt", "version": "4.8.0-1ubuntu3"}], "gcc-12-base": [{"arch": "amd64", "category": "libs", "name": "gcc-12-base", "origin": "Ubuntu", "source": "apt", "version": "12.1.0-2ubuntu1~22.04"}], "gir1.2-glib-2.0": [{"arch": "amd64", "category": "introspection", "name": "gir1.2-glib-2.0", "origin": "Ubuntu", "source": "apt", "version": "1.72.0-1"}], "gnupg": [{"arch": "all", "category": "utils", "name": "gnupg", "origin": "Ubuntu", "source": "apt", "version": "2.2.27-3ubuntu2.1"}], "gnupg-l10n": [{"arch": "all", "category": "utils", "name": "gnupg-l10n", "origin": "Ubuntu", "source": "apt", "version": "2.2.27-3ubuntu2.1"}], "gnupg-utils": [{"arch": "amd64", "category": "utils", "name": "gnupg-utils", "origin": "Ubuntu", "source": "apt", "version": "2.2.27-3ubuntu2.1"}], "gnupg2": [{"arch": "all", "category": "universe/utils", "name": "gnupg2", "origin": "Ubuntu", "source": "apt", "version": "2.2.27-3ubuntu2.1"}], "gpg": [{"arch": "amd64", "category": "utils", "name": "gpg", "origin": "Ubuntu", "source": "apt", "version": "2.2.27-3ubuntu2.1"}], "gpg-agent": [{"arch": "amd64", "category": "utils", "name": "gpg-agent", "origin": "Ubuntu", "source": "apt", "version": "2.2.27-3ubuntu2.1"}], "gpg-wks-client": [{"arch": "amd64", "category": "utils", "name": "gpg-wks-client", "origin": "Ubuntu", "source": "apt", "version": "2.2.27-3ubuntu2.1"}], "gpg-wks-server": [{"arch": "amd64", "category": "utils", "name": "gpg-wks-server", "origin": "Ubuntu", "source": "apt", "version": "2.2.27-3ubuntu2.1"}], "gpgconf": [{"arch": "amd64", "category": "utils", "name": "gpgconf", "origin": "Ubuntu", "source": "apt", "version": "2.2.27-3ubuntu2.1"}], "gpgsm": [{"arch": "amd64", "category": "utils", "name": "gpgsm", "origin": "Ubuntu", "source": "apt", "version": "2.2.27-3ubuntu2.1"}], "gpgv": [{"arch": "amd64", "category": "utils", "name": "gpgv", "origin": "Ubuntu", "source": "apt", "version": "2.2.27-3ubuntu2.1"}], "grep": [{"arch": "amd64", "category": "utils", "name": "grep", "origin": "Ubuntu", "source": "apt", "version": "3.7-1build1"}], "groff-base": [{"arch": "amd64", "category": "text", "name": "groff-base", "origin": "Ubuntu", "source": "apt", "version": "1.22.4-8build1"}], "gzip": [{"arch": "amd64", "category": "utils", "name": "gzip", "origin": "Ubuntu", "source": "apt", "version": "1.10-4ubuntu4.1"}], "hostname": [{"arch": "amd64", "category": "admin", "name": "hostname", "origin": "Ubuntu", "source": "apt", "version": "3.23ubuntu2"}], "init-system-helpers": [{"arch": "all", "category": "admin", "name": "init-system-helpers", "origin": "Ubuntu", "source": "apt", "version": "1.62"}], "iproute2": [{"arch": "amd64", "category": "net", "name": "iproute2", "origin": "Ubuntu", "source": "apt", "version": "5.15.0-1ubuntu2"}], "iso-codes": [{"arch": "all", "category": "libs", "name": "iso-codes", "origin": "Ubuntu", "source": "apt", "version": "4.9.0-1"}], "libacl1": [{"arch": "amd64", "category": "libs", "name": "libacl1", "origin": "Ubuntu", "source": "apt", "version": "2.3.1-1"}], "libapparmor1": [{"arch": "amd64", "category": "libs", "name": "libapparmor1", "origin": "Ubuntu", "source": "apt", "version": "3.0.4-2ubuntu2.1"}], "libapt-pkg6.0": [{"arch": "amd64", "category": "libs", "name": "libapt-pkg6.0", "origin": "Ubuntu", "source": "apt", "version": "2.4.8"}], "libargon2-1": [{"arch": "amd64", "category": "libs", "name": "libargon2-1", "origin": "Ubuntu", "source": "apt", "version": "0~20171227-0.3"}], "libassuan0": [{"arch": "amd64", "category": "libs", "name": "libassuan0", "origin": "Ubuntu", "source": "apt", "version": "2.5.5-1build1"}], "libatm1": [{"arch": "amd64", "category": "libs", "name": "libatm1", "origin": "Ubuntu", "source": "apt", "version": "1:2.5.1-4build2"}], "libattr1": [{"arch": "amd64", "category": "libs", "name": "libattr1", "origin": "Ubuntu", "source": "apt", "version": "1:2.5.1-1build1"}], "libaudit-common": [{"arch": "all", "category": "libs", "name": "libaudit-common", "origin": "Ubuntu", "source": "apt", "version": "1:3.0.7-1build1"}], "libaudit1": [{"arch": "amd64", "category": "libs", "name": "libaudit1", "origin": "Ubuntu", "source": "apt", "version": "1:3.0.7-1build1"}], "libblkid1": [{"arch": "amd64", "category": "libs", "name": "libblkid1", "origin": "Ubuntu", "source": "apt", "version": "2.37.2-4ubuntu3"}], "libbpf0": [{"arch": "amd64", "category": "libs", "name": "libbpf0", "origin": "Ubuntu", "source": "apt", "version": "1:0.5.0-1ubuntu22.04.1"}], "libbsd0": [{"arch": "amd64", "category": "libs", "name": "libbsd0", "origin": "Ubuntu", "source": "apt", "version": "0.11.5-1"}], "libbz2-1.0": [{"arch": "amd64", "category": "libs", "name": "libbz2-1.0", "origin": "Ubuntu", "source": "apt", "version": "1.0.8-5build1"}], "libc-bin": [{"arch": "amd64", "category": "libs", "name": "libc-bin", "origin": "Ubuntu", "source": "apt", "version": "2.35-0ubuntu3.1"}], "libc6": [{"arch": "amd64", "category": "libs", "name": "libc6", "origin": "Ubuntu", "source": "apt", "version": "2.35-0ubuntu3.1"}], "libcap-ng0": [{"arch": "amd64", "category": "libs", "name": "libcap-ng0", "origin": "Ubuntu", "source": "apt", "version": "0.7.9-2.2build3"}], "libcap2": [{"arch": "amd64", "category": "libs", "name": "libcap2", "origin": "Ubuntu", "source": "apt", "version": "1:2.44-1build3"}], "libcap2-bin": [{"arch": "amd64", "category": "utils", "name": "libcap2-bin", "origin": "Ubuntu", "source": "apt", "version": "1:2.44-1build3"}], "libcom-err2": [{"arch": "amd64", "category": "libs", "name": "libcom-err2", "origin": "Ubuntu", "source": "apt", "version": "1.46.5-2ubuntu1.1"}], "libcrypt1": [{"arch": "amd64", "category": "libs", "name": "libcrypt1", "origin": "Ubuntu", "source": "apt", "version": "1:4.4.27-1"}], "libcryptsetup12": [{"arch": "amd64", "category": "libs", "name": "libcryptsetup12", "origin": "Ubuntu", "source": "apt", "version": "2:2.4.3-1ubuntu1.1"}], "libdb5.3": [{"arch": "amd64", "category": "libs", "name": "libdb5.3", "origin": "Ubuntu", "source": "apt", "version": "5.3.28+dfsg1-0.8ubuntu3"}], "libdbus-1-3": [{"arch": "amd64", "category": "libs", "name": "libdbus-1-3", "origin": "Ubuntu", "source": "apt", "version": "1.12.20-2ubuntu4.1"}], "libdebconfclient0": [{"arch": "amd64", "category": "libs", "name": "libdebconfclient0", "origin": "Ubuntu", "source": "apt", "version": "0.261ubuntu1"}], "libdevmapper1.02.1": [{"arch": "amd64", "category": "libs", "name": "libdevmapper1.02.1", "origin": "Ubuntu", "source": "apt", "version": "2:1.02.175-2.1ubuntu4"}], "libelf1": [{"arch": "amd64", "category": "libs", "name": "libelf1", "origin": "Ubuntu", "source": "apt", "version": "0.186-1build1"}], "libestr0": [{"arch": "amd64", "category": "libs", "name": "libestr0", "origin": "Ubuntu", "source": "apt", "version": "0.1.10-2.1build3"}], "libexpat1": [{"arch": "amd64", "category": "libs", "name": "libexpat1", "origin": "Ubuntu", "source": "apt", "version": "2.4.7-1ubuntu0.2"}], "libext2fs2": [{"arch": "amd64", "category": "libs", "name": "libext2fs2", "origin": "Ubuntu", "source": "apt", "version": "1.46.5-2ubuntu1.1"}], "libfastjson4": [{"arch": "amd64", "category": "libs", "name": "libfastjson4", "origin": "Ubuntu", "source": "apt", "version": "0.99.9-1build2"}], "libffi8": [{"arch": "amd64", "category": "libs", "name": "libffi8", "origin": "Ubuntu", "source": "apt", "version": "3.4.2-4"}], "libgcc-s1": [{"arch": "amd64", "category": "libs", "name": "libgcc-s1", "origin": "Ubuntu", "source": "apt", "version": "12.1.0-2ubuntu1~22.04"}], "libgcrypt20": [{"arch": "amd64", "category": "libs", "name": "libgcrypt20", "origin": "Ubuntu", "source": "apt", "version": "1.9.4-3ubuntu3"}], "libgdbm6": [{"arch": "amd64", "category": "libs", "name": "libgdbm6", "origin": "Ubuntu", "source": "apt", "version": "1.23-1"}], "libgirepository-1.0-1": [{"arch": "amd64", "category": "libs", "name": "libgirepository-1.0-1", "origin": "Ubuntu", "source": "apt", "version": "1.72.0-1"}], "libglib2.0-0": [{"arch": "amd64", "category": "libs", "name": "libglib2.0-0", "origin": "Ubuntu", "source": "apt", "version": "2.72.4-0ubuntu1"}], "libglib2.0-data": [{"arch": "all", "category": "misc", "name": "libglib2.0-data", "origin": "Ubuntu", "source": "apt", "version": "2.72.4-0ubuntu1"}], "libgmp10": [{"arch": "amd64", "category": "libs", "name": "libgmp10", "origin": "Ubuntu", "source": "apt", "version": "2:6.2.1+dfsg-3ubuntu1"}], "libgnutls30": [{"arch": "amd64", "category": "libs", "name": "libgnutls30", "origin": "Ubuntu", "source": "apt", "version": "3.7.3-4ubuntu1.1"}], "libgpg-error0": [{"arch": "amd64", "category": "libs", "name": "libgpg-error0", "origin": "Ubuntu", "source": "apt", "version": "1.43-3"}], "libgssapi-krb5-2": [{"arch": "amd64", "category": "libs", "name": "libgssapi-krb5-2", "origin": "Ubuntu", "source": "apt", "version": "1.19.2-2ubuntu0.1"}], "libhogweed6": [{"arch": "amd64", "category": "libs", "name": "libhogweed6", "origin": "Ubuntu", "source": "apt", "version": "3.7.3-1build2"}], "libicu70": [{"arch": "amd64", "category": "libs", "name": "libicu70", "origin": "Ubuntu", "source": "apt", "version": "70.1-2"}], "libidn2-0": [{"arch": "amd64", "category": "libs", "name": "libidn2-0", "origin": "Ubuntu", "source": "apt", "version": "2.3.2-2build1"}], "libip4tc2": [{"arch": "amd64", "category": "libs", "name": "libip4tc2", "origin": "Ubuntu", "source": "apt", "version": "1.8.7-1ubuntu5"}], "libjson-c5": [{"arch": "amd64", "category": "libs", "name": "libjson-c5", "origin": "Ubuntu", "source": "apt", "version": "0.15-3~ubuntu1.22.04.1"}], "libk5crypto3": [{"arch": "amd64", "category": "libs", "name": "libk5crypto3", "origin": "Ubuntu", "source": "apt", "version": "1.19.2-2ubuntu0.1"}], "libkeyutils1": [{"arch": "amd64", "category": "misc", "name": "libkeyutils1", "origin": "Ubuntu", "source": "apt", "version": "1.6.1-2ubuntu3"}], "libkmod2": [{"arch": "amd64", "category": "libs", "name": "libkmod2", "origin": "Ubuntu", "source": "apt", "version": "29-1ubuntu1"}], "libkrb5-3": [{"arch": "amd64", "category": "libs", "name": "libkrb5-3", "origin": "Ubuntu", "source": "apt", "version": "1.19.2-2ubuntu0.1"}], "libkrb5support0": [{"arch": "amd64", "category": "libs", "name": "libkrb5support0", "origin": "Ubuntu", "source": "apt", "version": "1.19.2-2ubuntu0.1"}], "libksba8": [{"arch": "amd64", "category": "libs", "name": "libksba8", "origin": "Ubuntu", "source": "apt", "version": "1.6.0-2ubuntu0.2"}], "libldap-2.5-0": [{"arch": "amd64", "category": "libs", "name": "libldap-2.5-0", "origin": "Ubuntu", "source": "apt", "version": "2.5.13+dfsg-0ubuntu0.22.04.1"}], "libldap-common": [{"arch": "all", "category": "libs", "name": "libldap-common", "origin": "Ubuntu", "source": "apt", "version": "2.5.13+dfsg-0ubuntu0.22.04.1"}], "liblz4-1": [{"arch": "amd64", "category": "libs", "name": "liblz4-1", "origin": "Ubuntu", "source": "apt", "version": "1.9.3-2build2"}], "liblzma5": [{"arch": "amd64", "category": "libs", "name": "liblzma5", "origin": "Ubuntu", "source": "apt", "version": "5.2.5-2ubuntu1"}], "libmd0": [{"arch": "amd64", "category": "libs", "name": "libmd0", "origin": "Ubuntu", "source": "apt", "version": "1.0.4-1build1"}], "libmnl0": [{"arch": "amd64", "category": "libs", "name": "libmnl0", "origin": "Ubuntu", "source": "apt", "version": "1.0.4-3build2"}], "libmount1": [{"arch": "amd64", "category": "libs", "name": "libmount1", "origin": "Ubuntu", "source": "apt", "version": "2.37.2-4ubuntu3"}], "libmpdec3": [{"arch": "amd64", "category": "libs", "name": "libmpdec3", "origin": "Ubuntu", "source": "apt", "version": "2.5.1-2build2"}], "libncurses6": [{"arch": "amd64", "category": "libs", "name": "libncurses6", "origin": "Ubuntu", "source": "apt", "version": "6.3-2"}], "libncursesw6": [{"arch": "amd64", "category": "libs", "name": "libncursesw6", "origin": "Ubuntu", "source": "apt", "version": "6.3-2"}], "libnettle8": [{"arch": "amd64", "category": "libs", "name": "libnettle8", "origin": "Ubuntu", "source": "apt", "version": "3.7.3-1build2"}], "libnpth0": [{"arch": "amd64", "category": "libs", "name": "libnpth0", "origin": "Ubuntu", "source": "apt", "version": "1.6-3build2"}], "libnsl2": [{"arch": "amd64", "category": "libs", "name": "libnsl2", "origin": "Ubuntu", "source": "apt", "version": "1.3.0-2build2"}], "libnss-systemd": [{"arch": "amd64", "category": "admin", "name": "libnss-systemd", "origin": "Ubuntu", "source": "apt", "version": "249.11-0ubuntu3.6"}], "libp11-kit0": [{"arch": "amd64", "category": "libs", "name": "libp11-kit0", "origin": "Ubuntu", "source": "apt", "version": "0.24.0-6build1"}], "libpam-cap": [{"arch": "amd64", "category": "libs", "name": "libpam-cap", "origin": "Ubuntu", "source": "apt", "version": "1:2.44-1build3"}], "libpam-modules": [{"arch": "amd64", "category": "admin", "name": "libpam-modules", "origin": "Ubuntu", "source": "apt", "version": "1.4.0-11ubuntu2.3"}], "libpam-modules-bin": [{"arch": "amd64", "category": "admin", "name": "libpam-modules-bin", "origin": "Ubuntu", "source": "apt", "version": "1.4.0-11ubuntu2.3"}], "libpam-runtime": [{"arch": "all", "category": "admin", "name": "libpam-runtime", "origin": "Ubuntu", "source": "apt", "version": "1.4.0-11ubuntu2.3"}], "libpam-systemd": [{"arch": "amd64", "category": "admin", "name": "libpam-systemd", "origin": "Ubuntu", "source": "apt", "version": "249.11-0ubuntu3.6"}], "libpam0g": [{"arch": "amd64", "category": "libs", "name": "libpam0g", "origin": "Ubuntu", "source": "apt", "version": "1.4.0-11ubuntu2.3"}], "libpcre2-8-0": [{"arch": "amd64", "category": "libs", "name": "libpcre2-8-0", "origin": "Ubuntu", "source": "apt", "version": "10.39-3ubuntu0.1"}], "libpcre3": [{"arch": "amd64", "category": "libs", "name": "libpcre3", "origin": "Ubuntu", "source": "apt", "version": "2:8.39-13ubuntu0.22.04.1"}], "libpipeline1": [{"arch": "amd64", "category": "libs", "name": "libpipeline1", "origin": "Ubuntu", "source": "apt", "version": "1.5.5-1"}], "libpopt0": [{"arch": "amd64", "category": "libs", "name": "libpopt0", "origin": "Ubuntu", "source": "apt", "version": "1.18-3build1"}], "libprocps8": [{"arch": "amd64", "category": "libs", "name": "libprocps8", "origin": "Ubuntu", "source": "apt", "version": "2:3.3.17-6ubuntu2"}], "libpython3-stdlib": [{"arch": "amd64", "category": "python", "name": "libpython3-stdlib", "origin": "Ubuntu", "source": "apt", "version": "3.10.6-1~22.04"}], "libpython3.10-minimal": [{"arch": "amd64", "category": "python", "name": "libpython3.10-minimal", "origin": "Ubuntu", "source": "apt", "version": "3.10.6-1~22.04.2"}], "libpython3.10-stdlib": [{"arch": "amd64", "category": "python", "name": "libpython3.10-stdlib", "origin": "Ubuntu", "source": "apt", "version": "3.10.6-1~22.04.2"}], "libreadline8": [{"arch": "amd64", "category": "libs", "name": "libreadline8", "origin": "Ubuntu", "source": "apt", "version": "8.1.2-1"}], "libsasl2-2": [{"arch": "amd64", "category": "libs", "name": "libsasl2-2", "origin": "Ubuntu", "source": "apt", "version": "2.1.27+dfsg2-3ubuntu1.1"}], "libsasl2-modules": [{"arch": "amd64", "category": "devel", "name": "libsasl2-modules", "origin": "Ubuntu", "source": "apt", "version": "2.1.27+dfsg2-3ubuntu1.1"}], "libsasl2-modules-db": [{"arch": "amd64", "category": "libs", "name": "libsasl2-modules-db", "origin": "Ubuntu", "source": "apt", "version": "2.1.27+dfsg2-3ubuntu1.1"}], "libseccomp2": [{"arch": "amd64", "category": "libs", "name": "libseccomp2", "origin": "Ubuntu", "source": "apt", "version": "2.5.3-2ubuntu2"}], "libselinux1": [{"arch": "amd64", "category": "libs", "name": "libselinux1", "origin": "Ubuntu", "source": "apt", "version": "3.3-1build2"}], "libsemanage-common": [{"arch": "all", "category": "libs", "name": "libsemanage-common", "origin": "Ubuntu", "source": "apt", "version": "3.3-1build2"}], "libsemanage2": [{"arch": "amd64", "category": "libs", "name": "libsemanage2", "origin": "Ubuntu", "source": "apt", "version": "3.3-1build2"}], "libsepol2": [{"arch": "amd64", "category": "libs", "name": "libsepol2", "origin": "Ubuntu", "source": "apt", "version": "3.3-1build1"}], "libsmartcols1": [{"arch": "amd64", "category": "libs", "name": "libsmartcols1", "origin": "Ubuntu", "source": "apt", "version": "2.37.2-4ubuntu3"}], "libsqlite3-0": [{"arch": "amd64", "category": "libs", "name": "libsqlite3-0", "origin": "Ubuntu", "source": "apt", "version": "3.37.2-2ubuntu0.1"}], "libss2": [{"arch": "amd64", "category": "libs", "name": "libss2", "origin": "Ubuntu", "source": "apt", "version": "1.46.5-2ubuntu1.1"}], "libssl3": [{"arch": "amd64", "category": "libs", "name": "libssl3", "origin": "Ubuntu", "source": "apt", "version": "3.0.2-0ubuntu1.8"}], "libstdc++6": [{"arch": "amd64", "category": "libs", "name": "libstdc++6", "origin": "Ubuntu", "source": "apt", "version": "12.1.0-2ubuntu1~22.04"}], "libsystemd0": [{"arch": "amd64", "category": "libs", "name": "libsystemd0", "origin": "Ubuntu", "source": "apt", "version": "249.11-0ubuntu3.6"}], "libtasn1-6": [{"arch": "amd64", "category": "libs", "name": "libtasn1-6", "origin": "Ubuntu", "source": "apt", "version": "4.18.0-4build1"}], "libtinfo6": [{"arch": "amd64", "category": "libs", "name": "libtinfo6", "origin": "Ubuntu", "source": "apt", "version": "6.3-2"}], "libtirpc-common": [{"arch": "all", "category": "libs", "name": "libtirpc-common", "origin": "Ubuntu", "source": "apt", "version": "1.3.2-2ubuntu0.1"}], "libtirpc3": [{"arch": "amd64", "category": "libs", "name": "libtirpc3", "origin": "Ubuntu", "source": "apt", "version": "1.3.2-2ubuntu0.1"}], "libuchardet0": [{"arch": "amd64", "category": "libs", "name": "libuchardet0", "origin": "Ubuntu", "source": "apt", "version": "0.0.7-1build2"}], "libudev1": [{"arch": "amd64", "category": "libs", "name": "libudev1", "origin": "Ubuntu", "source": "apt", "version": "249.11-0ubuntu3.6"}], "libunistring2": [{"arch": "amd64", "category": "libs", "name": "libunistring2", "origin": "Ubuntu", "source": "apt", "version": "1.0-1"}], "libuuid1": [{"arch": "amd64", "category": "libs", "name": "libuuid1", "origin": "Ubuntu", "source": "apt", "version": "2.37.2-4ubuntu3"}], "libxml2": [{"arch": "amd64", "category": "libs", "name": "libxml2", "origin": "Ubuntu", "source": "apt", "version": "2.9.13+dfsg-1ubuntu0.2"}], "libxtables12": [{"arch": "amd64", "category": "libs", "name": "libxtables12", "origin": "Ubuntu", "source": "apt", "version": "1.8.7-1ubuntu5"}], "libxxhash0": [{"arch": "amd64", "category": "libs", "name": "libxxhash0", "origin": "Ubuntu", "source": "apt", "version": "0.8.1-1"}], "libzstd1": [{"arch": "amd64", "category": "libs", "name": "libzstd1", "origin": "Ubuntu", "source": "apt", "version": "1.4.8+dfsg-3build1"}], "login": [{"arch": "amd64", "category": "admin", "name": "login", "origin": "Ubuntu", "source": "apt", "version": "1:4.8.1-2ubuntu2.1"}], "logrotate": [{"arch": "amd64", "category": "admin", "name": "logrotate", "origin": "Ubuntu", "source": "apt", "version": "3.19.0-1ubuntu1.1"}], "logsave": [{"arch": "amd64", "category": "admin", "name": "logsave", "origin": "Ubuntu", "source": "apt", "version": "1.46.5-2ubuntu1.1"}], "lsb-base": [{"arch": "all", "category": "misc", "name": "lsb-base", "origin": "Ubuntu", "source": "apt", "version": "11.1.0ubuntu4"}], "lsb-release": [{"arch": "all", "category": "misc", "name": "lsb-release", "origin": "Ubuntu", "source": "apt", "version": "11.1.0ubuntu4"}], "man-db": [{"arch": "amd64", "category": "doc", "name": "man-db", "origin": "Ubuntu", "source": "apt", "version": "2.10.2-1"}], "mawk": [{"arch": "amd64", "category": "utils", "name": "mawk", "origin": "Ubuntu", "source": "apt", "version": "1.3.4.20200120-3"}], "media-types": [{"arch": "all", "category": "net", "name": "media-types", "origin": "Ubuntu", "source": "apt", "version": "7.0.0"}], "mount": [{"arch": "amd64", "category": "admin", "name": "mount", "origin": "Ubuntu", "source": "apt", "version": "2.37.2-4ubuntu3"}], "ncurses-base": [{"arch": "all", "category": "utils", "name": "ncurses-base", "origin": "Ubuntu", "source": "apt", "version": "6.3-2"}], "ncurses-bin": [{"arch": "amd64", "category": "utils", "name": "ncurses-bin", "origin": "Ubuntu", "source": "apt", "version": "6.3-2"}], "networkd-dispatcher": [{"arch": "all", "category": "utils", "name": "networkd-dispatcher", "origin": "Ubuntu", "source": "apt", "version": "2.1-2ubuntu0.22.04.2"}], "openssl": [{"arch": "amd64", "category": "utils", "name": "openssl", "origin": "Ubuntu", "source": "apt", "version": "3.0.2-0ubuntu1.8"}], "passwd": [{"arch": "amd64", "category": "admin", "name": "passwd", "origin": "Ubuntu", "source": "apt", "version": "1:4.8.1-2ubuntu2.1"}], "perl-base": [{"arch": "amd64", "category": "perl", "name": "perl-base", "origin": "Ubuntu", "source": "apt", "version": "5.34.0-3ubuntu1.1"}], "pinentry-curses": [{"arch": "amd64", "category": "utils", "name": "pinentry-curses", "origin": "Ubuntu", "source": "apt", "version": "1.1.1-1build2"}], "procps": [{"arch": "amd64", "category": "admin", "name": "procps", "origin": "Ubuntu", "source": "apt", "version": "2:3.3.17-6ubuntu2"}], "python-apt-common": [{"arch": "all", "category": "python", "name": "python-apt-common", "origin": "Ubuntu", "source": "apt", "version": "2.4.0ubuntu1"}], "python3": [{"arch": "amd64", "category": "python", "name": "python3", "origin": "Ubuntu", "source": "apt", "version": "3.10.6-1~22.04"}], "python3-apt": [{"arch": "amd64", "category": "python", "name": "python3-apt", "origin": "Ubuntu", "source": "apt", "version": "2.4.0ubuntu1"}], "python3-dbus": [{"arch": "amd64", "category": "python", "name": "python3-dbus", "origin": "Ubuntu", "source": "apt", "version": "1.2.18-3build1"}], "python3-gi": [{"arch": "amd64", "category": "python", "name": "python3-gi", "origin": "Ubuntu", "source": "apt", "version": "3.42.1-0ubuntu1"}], "python3-minimal": [{"arch": "amd64", "category": "python", "name": "python3-minimal", "origin": "Ubuntu", "source": "apt", "version": "3.10.6-1~22.04"}], "python3.10": [{"arch": "amd64", "category": "python", "name": "python3.10", "origin": "Ubuntu", "source": "apt", "version": "3.10.6-1~22.04.2"}], "python3.10-minimal": [{"arch": "amd64", "category": "python", "name": "python3.10-minimal", "origin": "Ubuntu", "source": "apt", "version": "3.10.6-1~22.04.2"}], "readline-common": [{"arch": "all", "category": "utils", "name": "readline-common", "origin": "Ubuntu", "source": "apt", "version": "8.1.2-1"}], "rsyslog": [{"arch": "amd64", "category": "admin", "name": "rsyslog", "origin": "Ubuntu", "source": "apt", "version": "8.2112.0-2ubuntu2.2"}], "sed": [{"arch": "amd64", "category": "utils", "name": "sed", "origin": "Ubuntu", "source": "apt", "version": "4.8-1ubuntu2"}], "sensible-utils": [{"arch": "all", "category": "utils", "name": "sensible-utils", "origin": "Ubuntu", "source": "apt", "version": "0.0.17"}], "shared-mime-info": [{"arch": "amd64", "category": "misc", "name": "shared-mime-info", "origin": "Ubuntu", "source": "apt", "version": "2.1-2"}], "sudo": [{"arch": "amd64", "category": "admin", "name": "sudo", "origin": "Ubuntu", "source": "apt", "version": "1.9.9-1ubuntu2.2"}], "systemd": [{"arch": "amd64", "category": "admin", "name": "systemd", "origin": "Ubuntu", "source": "apt", "version": "249.11-0ubuntu3.6"}], "systemd-sysv": [{"arch": "amd64", "category": "admin", "name": "systemd-sysv", "origin": "Ubuntu", "source": "apt", "version": "249.11-0ubuntu3.6"}], "systemd-timesyncd": [{"arch": "amd64", "category": "admin", "name": "systemd-timesyncd", "origin": "Ubuntu", "source": "apt", "version": "249.11-0ubuntu3.6"}], "sysvinit-utils": [{"arch": "amd64", "category": "admin", "name": "sysvinit-utils", "origin": "Ubuntu", "source": "apt", "version": "3.01-1ubuntu1"}], "tar": [{"arch": "amd64", "category": "utils", "name": "tar", "origin": "Ubuntu", "source": "apt", "version": "1.34+dfsg-1build3"}], "ubuntu-keyring": [{"arch": "all", "category": "misc", "name": "ubuntu-keyring", "origin": "Ubuntu", "source": "apt", "version": "2021.03.26"}], "ucf": [{"arch": "all", "category": "utils", "name": "ucf", "origin": "Ubuntu", "source": "apt", "version": "3.0043"}], "usrmerge": [{"arch": "all", "category": "admin", "name": "usrmerge", "origin": "Ubuntu", "source": "apt", "version": "25ubuntu2"}], "util-linux": [{"arch": "amd64", "category": "utils", "name": "util-linux", "origin": "Ubuntu", "source": "apt", "version": "2.37.2-4ubuntu3"}], "vector": [{"arch": "amd64", "category": "admin", "name": "vector", "origin": "", "source": "apt", "version": "0.27.0-1"}], "xdg-user-dirs": [{"arch": "amd64", "category": "utils", "name": "xdg-user-dirs", "origin": "Ubuntu", "source": "apt", "version": "0.17-2ubuntu4"}], "zlib1g": [{"arch": "amd64", "category": "libs", "name": "zlib1g", "origin": "Ubuntu", "source": "apt", "version": "1:1.2.11.dfsg-2ubuntu9.2"}]}}, "changed": false}

TASK [Gather Local Services] ***************************************************
task path: /Users/ro.khabibullin/Projects/netology/mnt-homeworks/08-ansible-05-testing/vector/molecule/resources/tests/verify.yml:12
ok: [ubuntu_latest] => {"ansible_facts": {"services": {"apt-daily-upgrade.service": {"name": "apt-daily-upgrade.service", "source": "systemd", "state": "inactive", "status": "static"}, "apt-daily.service": {"name": "apt-daily.service", "source": "systemd", "state": "inactive", "status": "static"}, "auditd.service": {"name": "auditd.service", "source": "systemd", "state": "stopped", "status": "not-found"}, "autovt@.service": {"name": "autovt@.service", "source": "systemd", "state": "unknown", "status": "alias"}, "console-getty.service": {"name": "console-getty.service", "source": "systemd", "state": "inactive", "status": "enabled-runtime"}, "container-getty@.service": {"name": "container-getty@.service", "source": "systemd", "state": "unknown", "status": "static"}, "cryptdisks-early.service": {"name": "cryptdisks-early.service", "source": "systemd", "state": "inactive", "status": "masked"}, "cryptdisks.service": {"name": "cryptdisks.service", "source": "systemd", "state": "inactive", "status": "masked"}, "dbus": {"name": "dbus", "source": "sysv", "state": "stopped"}, "dbus-org.freedesktop.hostname1.service": {"name": "dbus-org.freedesktop.hostname1.service", "source": "systemd", "state": "inactive", "status": "alias"}, "dbus-org.freedesktop.locale1.service": {"name": "dbus-org.freedesktop.locale1.service", "source": "systemd", "state": "inactive", "status": "alias"}, "dbus-org.freedesktop.login1.service": {"name": "dbus-org.freedesktop.login1.service", "source": "systemd", "state": "inactive", "status": "alias"}, "dbus-org.freedesktop.resolve1.service": {"name": "dbus-org.freedesktop.resolve1.service", "source": "systemd", "state": "inactive", "status": "alias"}, "dbus-org.freedesktop.timedate1.service": {"name": "dbus-org.freedesktop.timedate1.service", "source": "systemd", "state": "inactive", "status": "alias"}, "dbus-org.freedesktop.timesync1.service": {"name": "dbus-org.freedesktop.timesync1.service", "source": "systemd", "state": "inactive", "status": "alias"}, "dbus.service": {"name": "dbus.service", "source": "systemd", "state": "stopped", "status": "static"}, "debug-shell.service": {"name": "debug-shell.service", "source": "systemd", "state": "inactive", "status": "disabled"}, "display-manager.service": {"name": "display-manager.service", "source": "systemd", "state": "stopped", "status": "not-found"}, "dmesg.service": {"name": "dmesg.service", "source": "systemd", "state": "inactive", "status": "disabled"}, "dpkg-db-backup.service": {"name": "dpkg-db-backup.service", "source": "systemd", "state": "inactive", "status": "static"}, "e2scrub@.service": {"name": "e2scrub@.service", "source": "systemd", "state": "unknown", "status": "static"}, "e2scrub_all.service": {"name": "e2scrub_all.service", "source": "systemd", "state": "inactive", "status": "static"}, "e2scrub_fail@.service": {"name": "e2scrub_fail@.service", "source": "systemd", "state": "unknown", "status": "static"}, "e2scrub_reap.service": {"name": "e2scrub_reap.service", "source": "systemd", "state": "inactive", "status": "disabled"}, "emergency.service": {"name": "emergency.service", "source": "systemd", "state": "stopped", "status": "static"}, "fstrim.service": {"name": "fstrim.service", "source": "systemd", "state": "inactive", "status": "static"}, "getty-static.service": {"name": "getty-static.service", "source": "systemd", "state": "inactive", "status": "static"}, "getty@.service": {"name": "getty@.service", "source": "systemd", "state": "unknown", "status": "disabled"}, "hwclock.service": {"name": "hwclock.service", "source": "systemd", "state": "inactive", "status": "masked"}, "hwclock.sh": {"name": "hwclock.sh", "source": "sysv", "state": "stopped"}, "initrd-cleanup.service": {"name": "initrd-cleanup.service", "source": "systemd", "state": "inactive", "status": "static"}, "initrd-parse-etc.service": {"name": "initrd-parse-etc.service", "source": "systemd", "state": "inactive", "status": "static"}, "initrd-switch-root.service": {"name": "initrd-switch-root.service", "source": "systemd", "state": "inactive", "status": "static"}, "initrd-udevadm-cleanup-db.service": {"name": "initrd-udevadm-cleanup-db.service", "source": "systemd", "state": "inactive", "status": "static"}, "kmod-static-nodes.service": {"name": "kmod-static-nodes.service", "source": "systemd", "state": "inactive", "status": "static"}, "kmod.service": {"name": "kmod.service", "source": "systemd", "state": "inactive", "status": "alias"}, "logrotate.service": {"name": "logrotate.service", "source": "systemd", "state": "inactive", "status": "static"}, "man-db.service": {"name": "man-db.service", "source": "systemd", "state": "inactive", "status": "static"}, "modprobe@.service": {"name": "modprobe@.service", "source": "systemd", "state": "unknown", "status": "static"}, "motd-news.service": {"name": "motd-news.service", "source": "systemd", "state": "inactive", "status": "static"}, "networkd-dispatcher.service": {"name": "networkd-dispatcher.service", "source": "systemd", "state": "inactive", "status": "disabled"}, "plymouth-start.service": {"name": "plymouth-start.service", "source": "systemd", "state": "stopped", "status": "not-found"}, "procps": {"name": "procps", "source": "sysv", "state": "stopped"}, "procps.service": {"name": "procps.service", "source": "systemd", "state": "inactive", "status": "alias"}, "quotaon.service": {"name": "quotaon.service", "source": "systemd", "state": "inactive", "status": "static"}, "rc-local.service": {"name": "rc-local.service", "source": "systemd", "state": "inactive", "status": "static"}, "rc.service": {"name": "rc.service", "source": "systemd", "state": "inactive", "status": "masked"}, "rcS.service": {"name": "rcS.service", "source": "systemd", "state": "inactive", "status": "masked"}, "rescue.service": {"name": "rescue.service", "source": "systemd", "state": "stopped", "status": "static"}, "rsyslog.service": {"name": "rsyslog.service", "source": "systemd", "state": "stopped", "status": "enabled"}, "serial-getty@.service": {"name": "serial-getty@.service", "source": "systemd", "state": "unknown", "status": "disabled"}, "sudo.service": {"name": "sudo.service", "source": "systemd", "state": "inactive", "status": "masked"}, "syslog.service": {"name": "syslog.service", "source": "systemd", "state": "inactive", "status": "alias"}, "system-update-cleanup.service": {"name": "system-update-cleanup.service", "source": "systemd", "state": "inactive", "status": "static"}, "systemd-ask-password-console.service": {"name": "systemd-ask-password-console.service", "source": "systemd", "state": "inactive", "status": "static"}, "systemd-ask-password-wall.service": {"name": "systemd-ask-password-wall.service", "source": "systemd", "state": "inactive", "status": "static"}, "systemd-backlight@.service": {"name": "systemd-backlight@.service", "source": "systemd", "state": "unknown", "status": "static"}, "systemd-binfmt.service": {"name": "systemd-binfmt.service", "source": "systemd", "state": "inactive", "status": "static"}, "systemd-bless-boot.service": {"name": "systemd-bless-boot.service", "source": "systemd", "state": "inactive", "status": "static"}, "systemd-boot-check-no-failures.service": {"name": "systemd-boot-check-no-failures.service", "source": "systemd", "state": "inactive", "status": "disabled"}, "systemd-boot-system-token.service": {"name": "systemd-boot-system-token.service", "source": "systemd", "state": "inactive", "status": "static"}, "systemd-exit.service": {"name": "systemd-exit.service", "source": "systemd", "state": "inactive", "status": "static"}, "systemd-fsck-root.service": {"name": "systemd-fsck-root.service", "source": "systemd", "state": "stopped", "status": "static"}, "systemd-fsck@.service": {"name": "systemd-fsck@.service", "source": "systemd", "state": "unknown", "status": "static"}, "systemd-fsckd.service": {"name": "systemd-fsckd.service", "source": "systemd", "state": "stopped", "status": "static"}, "systemd-halt.service": {"name": "systemd-halt.service", "source": "systemd", "state": "inactive", "status": "static"}, "systemd-hibernate-resume@.service": {"name": "systemd-hibernate-resume@.service", "source": "systemd", "state": "unknown", "status": "static"}, "systemd-hibernate.service": {"name": "systemd-hibernate.service", "source": "systemd", "state": "inactive", "status": "static"}, "systemd-hostnamed.service": {"name": "systemd-hostnamed.service", "source": "systemd", "state": "inactive", "status": "static"}, "systemd-hybrid-sleep.service": {"name": "systemd-hybrid-sleep.service", "source": "systemd", "state": "inactive", "status": "static"}, "systemd-initctl.service": {"name": "systemd-initctl.service", "source": "systemd", "state": "inactive", "status": "static"}, "systemd-journal-flush.service": {"name": "systemd-journal-flush.service", "source": "systemd", "state": "inactive", "status": "static"}, "systemd-journald.service": {"name": "systemd-journald.service", "source": "systemd", "state": "running", "status": "static"}, "systemd-journald@.service": {"name": "systemd-journald@.service", "source": "systemd", "state": "unknown", "status": "static"}, "systemd-kexec.service": {"name": "systemd-kexec.service", "source": "systemd", "state": "inactive", "status": "static"}, "systemd-localed.service": {"name": "systemd-localed.service", "source": "systemd", "state": "inactive", "status": "static"}, "systemd-logind.service": {"name": "systemd-logind.service", "source": "systemd", "state": "inactive", "status": "static"}, "systemd-machine-id-commit.service": {"name": "systemd-machine-id-commit.service", "source": "systemd", "state": "inactive", "status": "static"}, "systemd-modules-load.service": {"name": "systemd-modules-load.service", "source": "systemd", "state": "inactive", "status": "static"}, "systemd-network-generator.service": {"name": "systemd-network-generator.service", "source": "systemd", "state": "inactive", "status": "disabled"}, "systemd-networkd-wait-online.service": {"name": "systemd-networkd-wait-online.service", "source": "systemd", "state": "inactive", "status": "disabled"}, "systemd-networkd.service": {"name": "systemd-networkd.service", "source": "systemd", "state": "inactive", "status": "disabled"}, "systemd-poweroff.service": {"name": "systemd-poweroff.service", "source": "systemd", "state": "inactive", "status": "static"}, "systemd-pstore.service": {"name": "systemd-pstore.service", "source": "systemd", "state": "inactive", "status": "disabled"}, "systemd-quotacheck.service": {"name": "systemd-quotacheck.service", "source": "systemd", "state": "inactive", "status": "static"}, "systemd-random-seed.service": {"name": "systemd-random-seed.service", "source": "systemd", "state": "inactive", "status": "static"}, "systemd-reboot.service": {"name": "systemd-reboot.service", "source": "systemd", "state": "inactive", "status": "static"}, "systemd-remount-fs.service": {"name": "systemd-remount-fs.service", "source": "systemd", "state": "stopped", "status": "enabled-runtime"}, "systemd-resolved.service": {"name": "systemd-resolved.service", "source": "systemd", "state": "inactive", "status": "enabled"}, "systemd-rfkill.service": {"name": "systemd-rfkill.service", "source": "systemd", "state": "inactive", "status": "static"}, "systemd-suspend-then-hibernate.service": {"name": "systemd-suspend-then-hibernate.service", "source": "systemd", "state": "inactive", "status": "static"}, "systemd-suspend.service": {"name": "systemd-suspend.service", "source": "systemd", "state": "inactive", "status": "static"}, "systemd-sysctl.service": {"name": "systemd-sysctl.service", "source": "systemd", "state": "inactive", "status": "static"}, "systemd-sysext.service": {"name": "systemd-sysext.service", "source": "systemd", "state": "inactive", "status": "disabled"}, "systemd-sysusers.service": {"name": "systemd-sysusers.service", "source": "systemd", "state": "stopped", "status": "static"}, "systemd-time-wait-sync.service": {"name": "systemd-time-wait-sync.service", "source": "systemd", "state": "inactive", "status": "disabled"}, "systemd-timedated.service": {"name": "systemd-timedated.service", "source": "systemd", "state": "inactive", "status": "static"}, "systemd-timesyncd.service": {"name": "systemd-timesyncd.service", "source": "systemd", "state": "inactive", "status": "enabled"}, "systemd-tmpfiles-clean.service": {"name": "systemd-tmpfiles-clean.service", "source": "systemd", "state": "stopped", "status": "static"}, "systemd-tmpfiles-setup-dev.service": {"name": "systemd-tmpfiles-setup-dev.service", "source": "systemd", "state": "inactive", "status": "static"}, "systemd-tmpfiles-setup.service": {"name": "systemd-tmpfiles-setup.service", "source": "systemd", "state": "stopped", "status": "static"}, "systemd-update-done.service": {"name": "systemd-update-done.service", "source": "systemd", "state": "stopped", "status": "not-found"}, "systemd-update-utmp-runlevel.service": {"name": "systemd-update-utmp-runlevel.service", "source": "systemd", "state": "stopped", "status": "static"}, "systemd-update-utmp.service": {"name": "systemd-update-utmp.service", "source": "systemd", "state": "stopped", "status": "static"}, "systemd-user-sessions.service": {"name": "systemd-user-sessions.service", "source": "systemd", "state": "inactive", "status": "static"}, "systemd-volatile-root.service": {"name": "systemd-volatile-root.service", "source": "systemd", "state": "inactive", "status": "static"}, "user-runtime-dir@.service": {"name": "user-runtime-dir@.service", "source": "systemd", "state": "unknown", "status": "static"}, "user@.service": {"name": "user@.service", "source": "systemd", "state": "unknown", "status": "static"}, "vector.service": {"name": "vector.service", "source": "systemd", "state": "running", "status": "disabled"}, "x11-common.service": {"name": "x11-common.service", "source": "systemd", "state": "inactive", "status": "masked"}}}, "changed": false}

PLAY RECAP *********************************************************************
ubuntu_latest              : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

INFO     Verifier completed successfully.
```

</details>

5. Добавьте новый тег на коммит с рабочим сценарием в соответствии с семантическим версионированием.

### Tox

1. Добавьте в директорию с vector-role файлы из [директории](./example)
2. Запустите `docker run --privileged=True -v <path_to_repo>:/opt/vector-role -w /opt/vector-role -it aragast/netology:latest /bin/bash`, где path_to_repo - путь до корня репозитория с vector-role на вашей файловой системе.

```commandline
➜  08-ansible-05-testing git:(MNT-video) ✗ docker run --privileged=True -v /Users/ro.khabibullin/Projects/netology/mnt-homeworks/08-ansible-05-testing/vector:/opt/vector-role -w /opt/vector-role -it aragast/netology:latest /bin/bash
[root@23cfdf6c05aa vector-role]# 
```

3. Внутри контейнера выполните команду `tox`, посмотрите на вывод.

```commandline
py37-ansible30 create: /opt/vector-role/.tox/py37-ansible30
py37-ansible30 installdeps: -rtox-requirements.txt, ansible<3.1
py37-ansible30 installed: ansible==3.0.0,ansible-base==2.10.17,ansible-compat==1.0.0,ansible-lint==5.1.3,arrow==1.2.3,bcrypt==4.0.1,binaryornot==0.4.4,bracex==2.3.post1,cached-property==1.5.2,Cerberus==1.3.2,certifi==2022.12.7,cffi==1.15.1,chardet==5.1.0,charset-normalizer==3.0.1,click==8.1.3,click-help-colors==0.9.1,cookiecutter==2.1.1,cryptography==39.0.1,distro==1.8.0,enrich==1.2.7,idna==3.4,importlib-metadata==6.0.0,Jinja2==3.1.2,jinja2-time==0.2.0,jmespath==1.0.1,lxml==4.9.2,markdown-it-py==2.2.0,MarkupSafe==2.1.2,mdurl==0.1.2,molecule==3.4.0,molecule-podman==1.0.1,packaging==23.0,paramiko==2.12.0,pathspec==0.11.0,pluggy==0.13.1,pycparser==2.21,Pygments==2.14.0,PyNaCl==1.5.0,python-dateutil==2.8.2,python-slugify==8.0.0,PyYAML==5.4.1,requests==2.28.2,rich==13.3.1,ruamel.yaml==0.17.21,ruamel.yaml.clib==0.2.7,selinux==0.2.1,six==1.16.0,subprocess-tee==0.3.5,tenacity==8.2.1,text-unidecode==1.3,typing_extensions==4.5.0,urllib3==1.26.14,wcmatch==8.4.1,yamllint==1.26.3,zipp==3.14.0
py37-ansible30 run-test-pre: PYTHONHASHSEED='1516432522'
py37-ansible30 run-test: commands[0] | molecule test -s compatibility --destroy always
CRITICAL 'molecule/compatibility/molecule.yml' glob failed.  Exiting.
ERROR: InvocationError for command /opt/vector-role/.tox/py37-ansible30/bin/molecule test -s compatibility --destroy always (exited with code 1)
```

5. Создайте облегчённый сценарий для `molecule` с драйвером `molecule_podman`. Проверьте его на исполнимость.
<details>
<summary><b>➜  vector git:(MNT-video) ✗ molecule test -s molecule_podman</b></summary>

```commandline
INFO     molecule_podman scenario test matrix: dependency, lint, cleanup, destroy, syntax, create, prepare, converge, idempotence, side_effect, verify, cleanup, destroy
INFO     Performing prerun with role_name_check=0...
INFO     Set ANSIBLE_LIBRARY=/Users/ro.khabibullin/.cache/ansible-compat/b0d51c/modules:/Users/ro.khabibullin/.ansible/plugins/modules:/usr/share/ansible/plugins/modules
INFO     Set ANSIBLE_COLLECTIONS_PATH=/Users/ro.khabibullin/.cache/ansible-compat/b0d51c/collections:/Users/ro.khabibullin/.ansible/collections:/usr/share/ansible/collections
INFO     Set ANSIBLE_ROLES_PATH=/Users/ro.khabibullin/.cache/ansible-compat/b0d51c/roles:/Users/ro.khabibullin/.ansible/roles:/usr/share/ansible/roles:/etc/ansible/roles
INFO     Using /Users/ro.khabibullin/.cache/ansible-compat/b0d51c/roles/ramireshab.vector symlink to current repository in order to enable Ansible to find the role using its expected full name.
INFO     Running molecule_podman > dependency
WARNING  Skipping, missing the requirements file.
WARNING  Skipping, missing the requirements file.
INFO     Running molecule_podman > lint
./tasks/main.yml
  14:1      error    too many blank lines (1 > 0)  (empty-lines)

./.tox/py37-ansible30/lib/python3.7/site-packages/ansible_collections/infinidat/infinibox/.gitlab-ci.yml
  34:10     error    too many spaces after hyphen  (hyphens)
  35:10     error    too many spaces after hyphen  (hyphens)
  36:10     error    too many spaces after hyphen  (hyphens)
  37:10     error    too many spaces after hyphen  (hyphens)
  38:10     error    too many spaces after hyphen  (hyphens)
  39:10     error    too many spaces after hyphen  (hyphens)

./.tox/py37-ansible30/lib/python3.7/site-packages/ansible_collections/infinidat/infinibox/playbooks/test_remove_resources.yml
  206:1     error    too many blank lines (2 > 0)  (empty-lines)

./.tox/py37-ansible30/lib/python3.7/site-packages/ansible_collections/community/sops/tests/integration/targets/lookup_sops/files/hidden-json.yaml
  2:1       error    syntax error: found character '\t' that cannot start any token (syntax)

./.tox/py37-ansible30/lib/python3.7/site-packages/ansible_collections/community/sops/tests/integration/targets/lookup_sops/files/hidden-binary.yaml
  2:1       error    syntax error: found character '\t' that cannot start any token (syntax)

./.tox/py37-ansible210/lib/python3.7/site-packages/ansible_collections/infinidat/infinibox/.gitlab-ci.yml
  34:10     error    too many spaces after hyphen  (hyphens)
  35:10     error    too many spaces after hyphen  (hyphens)
  36:10     error    too many spaces after hyphen  (hyphens)
  37:10     error    too many spaces after hyphen  (hyphens)
  38:10     error    too many spaces after hyphen  (hyphens)
  39:10     error    too many spaces after hyphen  (hyphens)

./.tox/py37-ansible210/lib/python3.7/site-packages/ansible_collections/infinidat/infinibox/playbooks/test_remove_resources.yml
  206:1     error    too many blank lines (2 > 0)  (empty-lines)

./.tox/py37-ansible210/lib/python3.7/site-packages/molecule/cookiecutter/scenario/driver/delegated/{{cookiecutter.molecule_directory}}/{{cookiecutter.scenario_name}}/create.yml
  2:2       error    syntax error: found character '%' that cannot start any token (syntax)

./.tox/py37-ansible210/lib/python3.7/site-packages/molecule/cookiecutter/scenario/driver/delegated/{{cookiecutter.molecule_directory}}/{{cookiecutter.scenario_name}}/destroy.yml
  2:2       error    syntax error: found character '%' that cannot start any token (syntax)

./.tox/py37-ansible210/lib/python3.7/site-packages/molecule/cookiecutter/scenario/verifier/ansible/{{cookiecutter.molecule_directory}}/{{cookiecutter.scenario_name}}/verify.yml
  4:2       error    syntax error: found character '%' that cannot start any token (syntax)

./.tox/py37-ansible210/lib/python3.7/site-packages/molecule/cookiecutter/molecule/{{cookiecutter.role_name}}/{{cookiecutter.molecule_directory}}/{{cookiecutter.scenario_name}}/molecule.yml
  8:2       error    syntax error: found character '%' that cannot start any token (syntax)

WARNING  Listing 1 violation(s) that are fatal
syntax-check[specific]: the role 'vector' was not found in /Users/ro.khabibullin/Projects/netology/mnt-homeworks/08-ansible-05-testing/vector/tests/roles:/Users/ro.khabibullin/.cache/ansible-compat/b0d51c/roles:/Users/ro.khabibullin/.ansible/roles:/usr/share/ansible/roles:/etc/ansible/roles:/Users/ro.khabibullin/Projects/netology/mnt-homeworks/08-ansible-05-testing/vector/tests
tests/test.yml:5:7


                  Rule Violation Summary                   
 count tag                    profile rule associated tags 
     1 syntax-check[specific] min     core, unskippable    

Failed after : 1 failure(s), 0 warning(s) on 34 files.
INFO     Running molecule_podman > cleanup
WARNING  Skipping, cleanup playbook not configured.
INFO     Running molecule_podman > destroy
INFO     Sanity checks: 'podman'
[WARNING]: Error getting vault password file (datatools): The vault password
file /Users/ro.khabibullin/.vault/datatools_vault was not found
[WARNING]: Error getting vault password file (getstream): The vault password
file /Users/ro.khabibullin/.vault/getstream was not found

PLAY [Destroy] *****************************************************************

TASK [Set async_dir for HOME env] **********************************************
ok: [localhost]

TASK [Destroy molecule instance(s)] ********************************************
changed: [localhost] => (item={'capabilities': ['SYS_ADMIN'], 'command': '/sbin/init', 'dockerfile': '../resources/Dockerfile.j2', 'env': {'ANSIBLE_USER': 'ansible', 'DEPLOY_GROUP': 'deployer', 'SUDO_GROUP': 'sudo', 'container': 'docker'}, 'image': 'ubuntu:latest', 'name': 'ubuntu_latest', 'privileged': True, 'tmpfs': ['/run', '/tmp'], 'volumes': ['/sys/fs/cgroup:/sys/fs/cgroup']})

TASK [Wait for instance(s) deletion to complete] *******************************
FAILED - RETRYING: [localhost]: Wait for instance(s) deletion to complete (300 retries left).
changed: [localhost] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': '760241757029.77436', 'results_file': '/Users/ro.khabibullin/.ansible_async/760241757029.77436', 'changed': True, 'item': {'capabilities': ['SYS_ADMIN'], 'command': '/sbin/init', 'dockerfile': '../resources/Dockerfile.j2', 'env': {'ANSIBLE_USER': 'ansible', 'DEPLOY_GROUP': 'deployer', 'SUDO_GROUP': 'sudo', 'container': 'docker'}, 'image': 'ubuntu:latest', 'name': 'ubuntu_latest', 'privileged': True, 'tmpfs': ['/run', '/tmp'], 'volumes': ['/sys/fs/cgroup:/sys/fs/cgroup']}, 'ansible_loop_var': 'item'})

PLAY RECAP *********************************************************************
localhost                  : ok=3    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

INFO     Running molecule_podman > syntax
[WARNING]: Error getting vault password file (datatools): The vault password
file /Users/ro.khabibullin/.vault/datatools_vault was not found
[WARNING]: Error getting vault password file (getstream): The vault password
file /Users/ro.khabibullin/.vault/getstream was not found
ansible-playbook [core 2.14.2]
  config file = /Users/ro.khabibullin/.cache/molecule/vector/molecule_podman/ansible.cfg
  configured module search path = ['/usr/local/lib/python3.11/site-packages/molecule/provisioner/ansible/plugins/modules', '/Users/ro.khabibullin/.cache/molecule/vector/molecule_podman/library', '/Users/ro.khabibullin/Projects/netology/mnt-homeworks/08-ansible-05-testing/vector/library', '/Users/ro.khabibullin/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /usr/local/lib/python3.11/site-packages/ansible
  ansible collection location = /Users/ro.khabibullin/.cache/ansible-compat/b0d51c/collections:/Users/ro.khabibullin/.cache/molecule/vector/molecule_podman/collections:/Users/ro.khabibullin/.ansible/collections:/usr/share/ansible/collections:/etc/ansible/collections
  executable location = /usr/local/bin/ansible-playbook
  python version = 3.11.1 (main, Dec 23 2022, 09:39:26) [Clang 14.0.0 (clang-1400.0.29.202)] (/usr/local/opt/python@3.11/bin/python3.11)
  jinja version = 3.1.2
  libyaml = False
Using /Users/ro.khabibullin/.cache/molecule/vector/molecule_podman/ansible.cfg as config file
1 plays in /Users/ro.khabibullin/Projects/netology/mnt-homeworks/08-ansible-05-testing/vector/molecule/resources/playbooks/converge.yml

playbook: /Users/ro.khabibullin/Projects/netology/mnt-homeworks/08-ansible-05-testing/vector/molecule/resources/playbooks/converge.yml
INFO     Running molecule_podman > create
[WARNING]: Error getting vault password file (datatools): The vault password
file /Users/ro.khabibullin/.vault/datatools_vault was not found
[WARNING]: Error getting vault password file (getstream): The vault password
file /Users/ro.khabibullin/.vault/getstream was not found

PLAY [Create] ******************************************************************

TASK [get podman executable path] **********************************************
ok: [localhost]

TASK [save path to executable as fact] *****************************************
ok: [localhost]

TASK [Set async_dir for HOME env] **********************************************
ok: [localhost]

TASK [Log into a container registry] *******************************************
skipping: [localhost] => (item="ubuntu_latest registry username: None specified") 
skipping: [localhost]

TASK [Check presence of custom Dockerfiles] ************************************
ok: [localhost] => (item=Dockerfile: ../resources/Dockerfile.j2)

TASK [Create Dockerfiles from image names] *************************************
changed: [localhost] => (item="Dockerfile: ../resources/Dockerfile.j2; Image: ubuntu:latest")

TASK [Discover local Podman images] ********************************************
failed: [localhost] (item=ubuntu_latest) => {"ansible_loop_var": "item", "changed": false, "item": {"ansible_index_var": "i", "ansible_loop_var": "item", "changed": true, "checksum": "f2a55a6b663585869c406d23ec64a6edf4c5a7aa", "dest": "/Users/ro.khabibullin/.cache/molecule/vector/molecule_podman/Dockerfile_ubuntu_latest", "diff": [], "failed": false, "gid": 20, "group": "staff", "i": 0, "invocation": {"module_args": {"_original_basename": "Dockerfile.j2", "attributes": null, "backup": false, "checksum": "f2a55a6b663585869c406d23ec64a6edf4c5a7aa", "content": null, "dest": "/Users/ro.khabibullin/.cache/molecule/vector/molecule_podman/Dockerfile_ubuntu_latest", "directory_mode": null, "follow": false, "force": true, "group": null, "local_follow": null, "mode": "0600", "owner": null, "remote_src": null, "selevel": null, "serole": null, "setype": null, "seuser": null, "src": "/Users/ro.khabibullin/.ansible/tmp/ansible-tmp-1677080037.157192-77547-245141596562148/source", "unsafe_writes": false, "validate": null}}, "item": {"capabilities": ["SYS_ADMIN"], "command": "/sbin/init", "dockerfile": "../resources/Dockerfile.j2", "env": {"ANSIBLE_USER": "ansible", "DEPLOY_GROUP": "deployer", "SUDO_GROUP": "sudo", "container": "docker"}, "image": "ubuntu:latest", "name": "ubuntu_latest", "privileged": true, "tmpfs": ["/run", "/tmp"], "volumes": ["/sys/fs/cgroup:/sys/fs/cgroup"]}, "md5sum": "494f081df668e1c263575fc6845e4a2e", "mode": "0600", "owner": "ro.khabibullin", "size": 2199, "src": "/Users/ro.khabibullin/.ansible/tmp/ansible-tmp-1677080037.157192-77547-245141596562148/source", "state": "file", "uid": 503}, "msg": "Unable to gather info for 'molecule_local/ubuntu_latest': Cannot connect to Podman. Please verify your connection to the Linux system using `podman system connection list`, or try `podman machine init` and `podman machine start` to manage a new Linux VM\nError: unable to connect to Podman socket: Get \"http://d/v4.4.1/libpod/_ping\": dial unix ///var/folders/dm/n13q44px2rqcl8mr7bwfjx2h0000gq/T/podman-run--1/podman/podman.sock: connect: no such file or directory\n"}

PLAY RECAP *********************************************************************
localhost                  : ok=5    changed=1    unreachable=0    failed=1    skipped=1    rescued=0    ignored=0

WARNING  Retrying execution failure 2 of: ansible-playbook --inventory /Users/ro.khabibullin/.cache/molecule/vector/molecule_podman/inventory --skip-tags molecule-notest,notest /usr/local/lib/python3.11/site-packages/molecule_podman/playbooks/create.yml
CRITICAL Ansible return code was 2, command was: ['ansible-playbook', '--inventory', '/Users/ro.khabibullin/.cache/molecule/vector/molecule_podman/inventory', '--skip-tags', 'molecule-notest,notest', '/usr/local/lib/python3.11/site-packages/molecule_podman/playbooks/create.yml']
WARNING  An error occurred during the test sequence action: 'create'. Cleaning up.
INFO     Running molecule_podman > cleanup
WARNING  Skipping, cleanup playbook not configured.
INFO     Running molecule_podman > destroy
[WARNING]: Error getting vault password file (datatools): The vault password
file /Users/ro.khabibullin/.vault/datatools_vault was not found
[WARNING]: Error getting vault password file (getstream): The vault password
file /Users/ro.khabibullin/.vault/getstream was not found

PLAY [Destroy] *****************************************************************

TASK [Set async_dir for HOME env] **********************************************
ok: [localhost]

TASK [Destroy molecule instance(s)] ********************************************
changed: [localhost] => (item={'capabilities': ['SYS_ADMIN'], 'command': '/sbin/init', 'dockerfile': '../resources/Dockerfile.j2', 'env': {'ANSIBLE_USER': 'ansible', 'DEPLOY_GROUP': 'deployer', 'SUDO_GROUP': 'sudo', 'container': 'docker'}, 'image': 'ubuntu:latest', 'name': 'ubuntu_latest', 'privileged': True, 'tmpfs': ['/run', '/tmp'], 'volumes': ['/sys/fs/cgroup:/sys/fs/cgroup']})

TASK [Wait for instance(s) deletion to complete] *******************************
FAILED - RETRYING: [localhost]: Wait for instance(s) deletion to complete (300 retries left).
changed: [localhost] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': '308838266667.77621', 'results_file': '/Users/ro.khabibullin/.ansible_async/308838266667.77621', 'changed': True, 'item': {'capabilities': ['SYS_ADMIN'], 'command': '/sbin/init', 'dockerfile': '../resources/Dockerfile.j2', 'env': {'ANSIBLE_USER': 'ansible', 'DEPLOY_GROUP': 'deployer', 'SUDO_GROUP': 'sudo', 'container': 'docker'}, 'image': 'ubuntu:latest', 'name': 'ubuntu_latest', 'privileged': True, 'tmpfs': ['/run', '/tmp'], 'volumes': ['/sys/fs/cgroup:/sys/fs/cgroup']}, 'ansible_loop_var': 'item'})

PLAY RECAP *********************************************************************
localhost                  : ok=3    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

INFO     Pruning extra files from scenario ephemeral directory
```
</details>

6. Пропишите правильную команду в `tox.ini` для того чтобы запускался облегчённый сценарий.

```yaml
commands =
    {posargs:molecule test -s molecule_podman --destroy always}
```

8. Запустите команду `tox`. Убедитесь, что всё отработало успешно.
<details>
<summary><b>[root@963007cdabc6 vector-role]# tox</b></summary>

```commandline
py37-ansible210 installed: ansible==2.10.7,ansible-base==2.10.17,ansible-compat==1.0.0,ansible-lint==5.1.3,arrow==1.2.3,bcrypt==4.0.1,binaryornot==0.4.4,bracex==2.3.post1,cached-property==1.5.2,Cerberus==1.3.2,certifi==2022.12.7,cffi==1.15.1,chardet==5.1.0,charset-normalizer==3.0.1,click==8.1.3,click-help-colors==0.9.1,cookiecutter==2.1.1,cryptography==39.0.1,distro==1.8.0,enrich==1.2.7,idna==3.4,importlib-metadata==6.0.0,Jinja2==3.1.2,jinja2-time==0.2.0,jmespath==1.0.1,lxml==4.9.2,markdown-it-py==2.2.0,MarkupSafe==2.1.2,mdurl==0.1.2,molecule==3.4.0,molecule-podman==1.0.1,packaging==23.0,paramiko==2.12.0,pathspec==0.11.0,pluggy==0.13.1,pycparser==2.21,Pygments==2.14.0,PyNaCl==1.5.0,python-dateutil==2.8.2,python-slugify==8.0.0,PyYAML==5.4.1,requests==2.28.2,rich==13.3.1,ruamel.yaml==0.17.21,ruamel.yaml.clib==0.2.7,selinux==0.2.1,six==1.16.0,subprocess-tee==0.3.5,tenacity==8.2.1,text-unidecode==1.3,typing_extensions==4.5.0,urllib3==1.26.14,wcmatch==8.4.1,yamllint==1.26.3,zipp==3.14.0
py37-ansible210 run-test-pre: PYTHONHASHSEED='2329635104'
py37-ansible210 run-test: commands[0] | molecule test -s molecule_podman --destroy always
INFO     molecule_podman scenario test matrix: dependency, lint, cleanup, destroy, syntax, create, prepare, converge, idempotence, side_effect, verify, cleanup, destroy
INFO     Performing prerun...
WARNING  Failed to locate command: [Errno 2] No such file or directory: 'git': 'git'
INFO     Guessed /opt/vector-role as project root directory
INFO     Using /root/.cache/ansible-lint/b984a4/roles/ramireshab.vector symlink to current repository in order to enable Ansible to find the role using its expected full name.
INFO     Added ANSIBLE_ROLES_PATH=~/.ansible/roles:/usr/share/ansible/roles:/etc/ansible/roles:/root/.cache/ansible-lint/b984a4/roles
INFO     Inventory /opt/vector-role/molecule/molecule_podman/../resources/inventory/hosts.yml linked to /root/.cache/molecule/vector-role/molecule_podman/inventory/hosts
INFO     Inventory /opt/vector-role/molecule/molecule_podman/../resources/inventory/group_vars/ linked to /root/.cache/molecule/vector-role/molecule_podman/inventory/group_vars
INFO     Inventory /opt/vector-role/molecule/molecule_podman/../resources/inventory/host_vars/ linked to /root/.cache/molecule/vector-role/molecule_podman/inventory/host_vars
INFO     Running molecule_podman > dependency
INFO     Running ansible-galaxy collection install --force -v containers.podman:>=1.7.0
INFO     Running ansible-galaxy collection install --force -v ansible.posix:>=1.3.0
WARNING  Skipping, missing the requirements file.
WARNING  Skipping, missing the requirements file.
INFO     Inventory /opt/vector-role/molecule/molecule_podman/../resources/inventory/hosts.yml linked to /root/.cache/molecule/vector-role/molecule_podman/inventory/hosts
INFO     Inventory /opt/vector-role/molecule/molecule_podman/../resources/inventory/group_vars/ linked to /root/.cache/molecule/vector-role/molecule_podman/inventory/group_vars
INFO     Inventory /opt/vector-role/molecule/molecule_podman/../resources/inventory/host_vars/ linked to /root/.cache/molecule/vector-role/molecule_podman/inventory/host_vars
INFO     Running molecule_podman > lint
COMMAND: yamllint .
ansible-lint
flake8

./.tox/py37-ansible210/lib/python3.7/site-packages/ansible_collections/infinidat/infinibox/.gitlab-ci.yml
  34:10     error    too many spaces after hyphen  (hyphens)
  35:10     error    too many spaces after hyphen  (hyphens)
  36:10     error    too many spaces after hyphen  (hyphens)
  37:10     error    too many spaces after hyphen  (hyphens)
  38:10     error    too many spaces after hyphen  (hyphens)
  39:10     error    too many spaces after hyphen  (hyphens)

./.tox/py37-ansible210/lib/python3.7/site-packages/ansible_collections/infinidat/infinibox/playbooks/test_remove_resources.yml
  206:1     error    too many blank lines (2 > 0)  (empty-lines)

./.tox/py37-ansible210/lib/python3.7/site-packages/molecule/cookiecutter/molecule/{{cookiecutter.role_name}}/{{cookiecutter.molecule_directory}}/{{cookiecutter.scenario_name}}/molecule.yml
  8:2       error    syntax error: found character '%' that cannot start any token (syntax)

./.tox/py37-ansible210/lib/python3.7/site-packages/molecule/cookiecutter/scenario/driver/delegated/{{cookiecutter.molecule_directory}}/{{cookiecutter.scenario_name}}/create.yml
  2:2       error    syntax error: found character '%' that cannot start any token (syntax)

./.tox/py37-ansible210/lib/python3.7/site-packages/molecule/cookiecutter/scenario/driver/delegated/{{cookiecutter.molecule_directory}}/{{cookiecutter.scenario_name}}/destroy.yml
  2:2       error    syntax error: found character '%' that cannot start any token (syntax)

./.tox/py37-ansible210/lib/python3.7/site-packages/molecule/cookiecutter/scenario/verifier/ansible/{{cookiecutter.molecule_directory}}/{{cookiecutter.scenario_name}}/verify.yml
  4:2       error    syntax error: found character '%' that cannot start any token (syntax)

./.tox/py37-ansible30/lib/python3.7/site-packages/ansible_collections/community/sops/tests/integration/targets/lookup_sops/files/hidden-binary.yaml
  2:1       error    syntax error: found character '\t' that cannot start any token (syntax)

./.tox/py37-ansible30/lib/python3.7/site-packages/ansible_collections/community/sops/tests/integration/targets/lookup_sops/files/hidden-json.yaml
  2:1       error    syntax error: found character '\t' that cannot start any token (syntax)

./.tox/py37-ansible30/lib/python3.7/site-packages/ansible_collections/infinidat/infinibox/.gitlab-ci.yml
  34:10     error    too many spaces after hyphen  (hyphens)
  35:10     error    too many spaces after hyphen  (hyphens)
  36:10     error    too many spaces after hyphen  (hyphens)
  37:10     error    too many spaces after hyphen  (hyphens)
  38:10     error    too many spaces after hyphen  (hyphens)
  39:10     error    too many spaces after hyphen  (hyphens)

./.tox/py37-ansible30/lib/python3.7/site-packages/ansible_collections/infinidat/infinibox/playbooks/test_remove_resources.yml
  206:1     error    too many blank lines (2 > 0)  (empty-lines)

./.tox/py37-ansible30/lib/python3.7/site-packages/molecule/cookiecutter/molecule/{{cookiecutter.role_name}}/{{cookiecutter.molecule_directory}}/{{cookiecutter.scenario_name}}/molecule.yml
  8:2       error    syntax error: found character '%' that cannot start any token (syntax)

./.tox/py37-ansible30/lib/python3.7/site-packages/molecule/cookiecutter/scenario/driver/delegated/{{cookiecutter.molecule_directory}}/{{cookiecutter.scenario_name}}/create.yml
  2:2       error    syntax error: found character '%' that cannot start any token (syntax)

./.tox/py37-ansible30/lib/python3.7/site-packages/molecule/cookiecutter/scenario/driver/delegated/{{cookiecutter.molecule_directory}}/{{cookiecutter.scenario_name}}/destroy.yml
  2:2       error    syntax error: found character '%' that cannot start any token (syntax)

./.tox/py37-ansible30/lib/python3.7/site-packages/molecule/cookiecutter/scenario/verifier/ansible/{{cookiecutter.molecule_directory}}/{{cookiecutter.scenario_name}}/verify.yml
  4:2       error    syntax error: found character '%' that cannot start any token (syntax)

./.tox/py39-ansible210/lib/python3.9/site-packages/ansible_collections/infinidat/infinibox/.gitlab-ci.yml
  34:10     error    too many spaces after hyphen  (hyphens)
  35:10     error    too many spaces after hyphen  (hyphens)
  36:10     error    too many spaces after hyphen  (hyphens)
  37:10     error    too many spaces after hyphen  (hyphens)
  38:10     error    too many spaces after hyphen  (hyphens)
  39:10     error    too many spaces after hyphen  (hyphens)

./.tox/py39-ansible210/lib/python3.9/site-packages/ansible_collections/infinidat/infinibox/playbooks/test_remove_resources.yml
  206:1     error    too many blank lines (2 > 0)  (empty-lines)

./tasks/main.yml
  14:1      error    too many blank lines (1 > 0)  (empty-lines)

Failed to locate command: [Errno 2] No such file or directory: 'git': 'git'
Traceback (most recent call last):
  File "/opt/vector-role/.tox/py37-ansible210/bin/ansible-lint", line 8, in <module>
    sys.exit(_run_cli_entrypoint())
  File "/opt/vector-role/.tox/py37-ansible210/lib/python3.7/site-packages/ansiblelint/__main__.py", line 299, in _run_cli_entrypoint
    sys.exit(main(sys.argv))
  File "/opt/vector-role/.tox/py37-ansible210/lib/python3.7/site-packages/ansiblelint/__main__.py", line 211, in main
    from ansiblelint.generate_docs import rules_as_rich, rules_as_rst, rules_as_str
  File "/opt/vector-role/.tox/py37-ansible210/lib/python3.7/site-packages/ansiblelint/generate_docs.py", line 6, in <module>
    from rich.console import render_group
ImportError: cannot import name 'render_group' from 'rich.console' (/opt/vector-role/.tox/py37-ansible210/lib/python3.7/site-packages/rich/console.py)
/bin/sh: line 2: flake8: command not found
CRITICAL Lint failed with error code 127
WARNING  An error occurred during the test sequence action: 'lint'. Cleaning up.
INFO     Inventory /opt/vector-role/molecule/molecule_podman/../resources/inventory/hosts.yml linked to /root/.cache/molecule/vector-role/molecule_podman/inventory/hosts
INFO     Inventory /opt/vector-role/molecule/molecule_podman/../resources/inventory/group_vars/ linked to /root/.cache/molecule/vector-role/molecule_podman/inventory/group_vars
INFO     Inventory /opt/vector-role/molecule/molecule_podman/../resources/inventory/host_vars/ linked to /root/.cache/molecule/vector-role/molecule_podman/inventory/host_vars
INFO     Running molecule_podman > cleanup
WARNING  Skipping, cleanup playbook not configured.
INFO     Inventory /opt/vector-role/molecule/molecule_podman/../resources/inventory/hosts.yml linked to /root/.cache/molecule/vector-role/molecule_podman/inventory/hosts
INFO     Inventory /opt/vector-role/molecule/molecule_podman/../resources/inventory/group_vars/ linked to /root/.cache/molecule/vector-role/molecule_podman/inventory/group_vars
INFO     Inventory /opt/vector-role/molecule/molecule_podman/../resources/inventory/host_vars/ linked to /root/.cache/molecule/vector-role/molecule_podman/inventory/host_vars
INFO     Running molecule_podman > destroy
INFO     Sanity checks: 'podman'

PLAY [Destroy] *****************************************************************

TASK [Destroy molecule instance(s)] ********************************************
changed: [localhost] => (item={'capabilities': ['SYS_ADMIN'], 'command': '/sbin/init', 'dockerfile': '../resources/Dockerfile.j2', 'env': {'ANSIBLE_USER': 'ansible', 'DEPLOY_GROUP': 'deployer', 'SUDO_GROUP': 'sudo', 'container': 'docker'}, 'image': 'ubuntu:latest', 'name': 'ubuntu_latest', 'privileged': True, 'tmpfs': ['/run', '/tmp'], 'volumes': ['/sys/fs/cgroup:/sys/fs/cgroup']})

TASK [Wait for instance(s) deletion to complete] *******************************
changed: [localhost] => (item={'started': 1, 'finished': 0, 'ansible_job_id': '364851636941.111', 'results_file': '/root/.ansible_async/364851636941.111', 'changed': True, 'failed': False, 'item': {'capabilities': ['SYS_ADMIN'], 'command': '/sbin/init', 'dockerfile': '../resources/Dockerfile.j2', 'env': {'ANSIBLE_USER': 'ansible', 'DEPLOY_GROUP': 'deployer', 'SUDO_GROUP': 'sudo', 'container': 'docker'}, 'image': 'ubuntu:latest', 'name': 'ubuntu_latest', 'privileged': True, 'tmpfs': ['/run', '/tmp'], 'volumes': ['/sys/fs/cgroup:/sys/fs/cgroup']}, 'ansible_loop_var': 'item'})

PLAY RECAP *********************************************************************
localhost                  : ok=2    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

INFO     Pruning extra files from scenario ephemeral directory
ERROR: InvocationError for command /opt/vector-role/.tox/py37-ansible210/bin/molecule test -s molecule_podman --destroy always (exited with code 1)
py37-ansible30 installed: ansible==3.0.0,ansible-base==2.10.17,ansible-compat==1.0.0,ansible-lint==5.1.3,arrow==1.2.3,bcrypt==4.0.1,binaryornot==0.4.4,bracex==2.3.post1,cached-property==1.5.2,Cerberus==1.3.2,certifi==2022.12.7,cffi==1.15.1,chardet==5.1.0,charset-normalizer==3.0.1,click==8.1.3,click-help-colors==0.9.1,cookiecutter==2.1.1,cryptography==39.0.1,distro==1.8.0,enrich==1.2.7,idna==3.4,importlib-metadata==6.0.0,Jinja2==3.1.2,jinja2-time==0.2.0,jmespath==1.0.1,lxml==4.9.2,markdown-it-py==2.2.0,MarkupSafe==2.1.2,mdurl==0.1.2,molecule==3.4.0,molecule-podman==1.0.1,packaging==23.0,paramiko==2.12.0,pathspec==0.11.0,pluggy==0.13.1,pycparser==2.21,Pygments==2.14.0,PyNaCl==1.5.0,python-dateutil==2.8.2,python-slugify==8.0.0,PyYAML==5.4.1,requests==2.28.2,rich==13.3.1,ruamel.yaml==0.17.21,ruamel.yaml.clib==0.2.7,selinux==0.2.1,six==1.16.0,subprocess-tee==0.3.5,tenacity==8.2.1,text-unidecode==1.3,typing_extensions==4.5.0,urllib3==1.26.14,wcmatch==8.4.1,yamllint==1.26.3,zipp==3.14.0
py37-ansible30 run-test-pre: PYTHONHASHSEED='2329635104'
py37-ansible30 run-test: commands[0] | molecule test -s molecule_podman --destroy always
INFO     molecule_podman scenario test matrix: dependency, lint, cleanup, destroy, syntax, create, prepare, converge, idempotence, side_effect, verify, cleanup, destroy
INFO     Performing prerun...
WARNING  Failed to locate command: [Errno 2] No such file or directory: 'git': 'git'
INFO     Guessed /opt/vector-role as project root directory
INFO     Using /root/.cache/ansible-lint/b984a4/roles/ramireshab.vector symlink to current repository in order to enable Ansible to find the role using its expected full name.
INFO     Added ANSIBLE_ROLES_PATH=~/.ansible/roles:/usr/share/ansible/roles:/etc/ansible/roles:/root/.cache/ansible-lint/b984a4/roles
INFO     Inventory /opt/vector-role/molecule/molecule_podman/../resources/inventory/hosts.yml linked to /root/.cache/molecule/vector-role/molecule_podman/inventory/hosts
INFO     Inventory /opt/vector-role/molecule/molecule_podman/../resources/inventory/group_vars/ linked to /root/.cache/molecule/vector-role/molecule_podman/inventory/group_vars
INFO     Inventory /opt/vector-role/molecule/molecule_podman/../resources/inventory/host_vars/ linked to /root/.cache/molecule/vector-role/molecule_podman/inventory/host_vars
INFO     Running molecule_podman > dependency
WARNING  Skipping, missing the requirements file.
WARNING  Skipping, missing the requirements file.
INFO     Inventory /opt/vector-role/molecule/molecule_podman/../resources/inventory/hosts.yml linked to /root/.cache/molecule/vector-role/molecule_podman/inventory/hosts
INFO     Inventory /opt/vector-role/molecule/molecule_podman/../resources/inventory/group_vars/ linked to /root/.cache/molecule/vector-role/molecule_podman/inventory/group_vars
INFO     Inventory /opt/vector-role/molecule/molecule_podman/../resources/inventory/host_vars/ linked to /root/.cache/molecule/vector-role/molecule_podman/inventory/host_vars
INFO     Running molecule_podman > lint
COMMAND: yamllint .
ansible-lint
flake8

./.tox/py37-ansible210/lib/python3.7/site-packages/ansible_collections/infinidat/infinibox/.gitlab-ci.yml
  34:10     error    too many spaces after hyphen  (hyphens)
  35:10     error    too many spaces after hyphen  (hyphens)
  36:10     error    too many spaces after hyphen  (hyphens)
  37:10     error    too many spaces after hyphen  (hyphens)
  38:10     error    too many spaces after hyphen  (hyphens)
  39:10     error    too many spaces after hyphen  (hyphens)

./.tox/py37-ansible210/lib/python3.7/site-packages/ansible_collections/infinidat/infinibox/playbooks/test_remove_resources.yml
  206:1     error    too many blank lines (2 > 0)  (empty-lines)

./.tox/py37-ansible210/lib/python3.7/site-packages/molecule/cookiecutter/molecule/{{cookiecutter.role_name}}/{{cookiecutter.molecule_directory}}/{{cookiecutter.scenario_name}}/molecule.yml
  8:2       error    syntax error: found character '%' that cannot start any token (syntax)

./.tox/py37-ansible210/lib/python3.7/site-packages/molecule/cookiecutter/scenario/driver/delegated/{{cookiecutter.molecule_directory}}/{{cookiecutter.scenario_name}}/create.yml
  2:2       error    syntax error: found character '%' that cannot start any token (syntax)

./.tox/py37-ansible210/lib/python3.7/site-packages/molecule/cookiecutter/scenario/driver/delegated/{{cookiecutter.molecule_directory}}/{{cookiecutter.scenario_name}}/destroy.yml
  2:2       error    syntax error: found character '%' that cannot start any token (syntax)

./.tox/py37-ansible210/lib/python3.7/site-packages/molecule/cookiecutter/scenario/verifier/ansible/{{cookiecutter.molecule_directory}}/{{cookiecutter.scenario_name}}/verify.yml
  4:2       error    syntax error: found character '%' that cannot start any token (syntax)

./.tox/py37-ansible30/lib/python3.7/site-packages/ansible_collections/community/sops/tests/integration/targets/lookup_sops/files/hidden-binary.yaml
  2:1       error    syntax error: found character '\t' that cannot start any token (syntax)

./.tox/py37-ansible30/lib/python3.7/site-packages/ansible_collections/community/sops/tests/integration/targets/lookup_sops/files/hidden-json.yaml
  2:1       error    syntax error: found character '\t' that cannot start any token (syntax)

./.tox/py37-ansible30/lib/python3.7/site-packages/ansible_collections/infinidat/infinibox/.gitlab-ci.yml
  34:10     error    too many spaces after hyphen  (hyphens)
  35:10     error    too many spaces after hyphen  (hyphens)
  36:10     error    too many spaces after hyphen  (hyphens)
  37:10     error    too many spaces after hyphen  (hyphens)
  38:10     error    too many spaces after hyphen  (hyphens)
  39:10     error    too many spaces after hyphen  (hyphens)

./.tox/py37-ansible30/lib/python3.7/site-packages/ansible_collections/infinidat/infinibox/playbooks/test_remove_resources.yml
  206:1     error    too many blank lines (2 > 0)  (empty-lines)

./.tox/py37-ansible30/lib/python3.7/site-packages/molecule/cookiecutter/molecule/{{cookiecutter.role_name}}/{{cookiecutter.molecule_directory}}/{{cookiecutter.scenario_name}}/molecule.yml
  8:2       error    syntax error: found character '%' that cannot start any token (syntax)

./.tox/py37-ansible30/lib/python3.7/site-packages/molecule/cookiecutter/scenario/driver/delegated/{{cookiecutter.molecule_directory}}/{{cookiecutter.scenario_name}}/create.yml
  2:2       error    syntax error: found character '%' that cannot start any token (syntax)

./.tox/py37-ansible30/lib/python3.7/site-packages/molecule/cookiecutter/scenario/driver/delegated/{{cookiecutter.molecule_directory}}/{{cookiecutter.scenario_name}}/destroy.yml
  2:2       error    syntax error: found character '%' that cannot start any token (syntax)

./.tox/py37-ansible30/lib/python3.7/site-packages/molecule/cookiecutter/scenario/verifier/ansible/{{cookiecutter.molecule_directory}}/{{cookiecutter.scenario_name}}/verify.yml
  4:2       error    syntax error: found character '%' that cannot start any token (syntax)

./.tox/py39-ansible210/lib/python3.9/site-packages/ansible_collections/infinidat/infinibox/.gitlab-ci.yml
  34:10     error    too many spaces after hyphen  (hyphens)
  35:10     error    too many spaces after hyphen  (hyphens)
  36:10     error    too many spaces after hyphen  (hyphens)
  37:10     error    too many spaces after hyphen  (hyphens)
  38:10     error    too many spaces after hyphen  (hyphens)
  39:10     error    too many spaces after hyphen  (hyphens)

./.tox/py39-ansible210/lib/python3.9/site-packages/ansible_collections/infinidat/infinibox/playbooks/test_remove_resources.yml
  206:1     error    too many blank lines (2 > 0)  (empty-lines)

./tasks/main.yml
  14:1      error    too many blank lines (1 > 0)  (empty-lines)

Failed to locate command: [Errno 2] No such file or directory: 'git': 'git'
Traceback (most recent call last):
  File "/opt/vector-role/.tox/py37-ansible30/bin/ansible-lint", line 8, in <module>
    sys.exit(_run_cli_entrypoint())
  File "/opt/vector-role/.tox/py37-ansible30/lib/python3.7/site-packages/ansiblelint/__main__.py", line 299, in _run_cli_entrypoint
    sys.exit(main(sys.argv))
  File "/opt/vector-role/.tox/py37-ansible30/lib/python3.7/site-packages/ansiblelint/__main__.py", line 211, in main
    from ansiblelint.generate_docs import rules_as_rich, rules_as_rst, rules_as_str
  File "/opt/vector-role/.tox/py37-ansible30/lib/python3.7/site-packages/ansiblelint/generate_docs.py", line 6, in <module>
    from rich.console import render_group
ImportError: cannot import name 'render_group' from 'rich.console' (/opt/vector-role/.tox/py37-ansible30/lib/python3.7/site-packages/rich/console.py)
/bin/sh: line 2: flake8: command not found
CRITICAL Lint failed with error code 127
WARNING  An error occurred during the test sequence action: 'lint'. Cleaning up.
INFO     Inventory /opt/vector-role/molecule/molecule_podman/../resources/inventory/hosts.yml linked to /root/.cache/molecule/vector-role/molecule_podman/inventory/hosts
INFO     Inventory /opt/vector-role/molecule/molecule_podman/../resources/inventory/group_vars/ linked to /root/.cache/molecule/vector-role/molecule_podman/inventory/group_vars
INFO     Inventory /opt/vector-role/molecule/molecule_podman/../resources/inventory/host_vars/ linked to /root/.cache/molecule/vector-role/molecule_podman/inventory/host_vars
INFO     Running molecule_podman > cleanup
WARNING  Skipping, cleanup playbook not configured.
INFO     Inventory /opt/vector-role/molecule/molecule_podman/../resources/inventory/hosts.yml linked to /root/.cache/molecule/vector-role/molecule_podman/inventory/hosts
INFO     Inventory /opt/vector-role/molecule/molecule_podman/../resources/inventory/group_vars/ linked to /root/.cache/molecule/vector-role/molecule_podman/inventory/group_vars
INFO     Inventory /opt/vector-role/molecule/molecule_podman/../resources/inventory/host_vars/ linked to /root/.cache/molecule/vector-role/molecule_podman/inventory/host_vars
INFO     Running molecule_podman > destroy
INFO     Sanity checks: 'podman'

PLAY [Destroy] *****************************************************************

TASK [Destroy molecule instance(s)] ********************************************
changed: [localhost] => (item={'capabilities': ['SYS_ADMIN'], 'command': '/sbin/init', 'dockerfile': '../resources/Dockerfile.j2', 'env': {'ANSIBLE_USER': 'ansible', 'DEPLOY_GROUP': 'deployer', 'SUDO_GROUP': 'sudo', 'container': 'docker'}, 'image': 'ubuntu:latest', 'name': 'ubuntu_latest', 'privileged': True, 'tmpfs': ['/run', '/tmp'], 'volumes': ['/sys/fs/cgroup:/sys/fs/cgroup']})

TASK [Wait for instance(s) deletion to complete] *******************************
changed: [localhost] => (item={'started': 1, 'finished': 0, 'ansible_job_id': '568653061359.223', 'results_file': '/root/.ansible_async/568653061359.223', 'changed': True, 'failed': False, 'item': {'capabilities': ['SYS_ADMIN'], 'command': '/sbin/init', 'dockerfile': '../resources/Dockerfile.j2', 'env': {'ANSIBLE_USER': 'ansible', 'DEPLOY_GROUP': 'deployer', 'SUDO_GROUP': 'sudo', 'container': 'docker'}, 'image': 'ubuntu:latest', 'name': 'ubuntu_latest', 'privileged': True, 'tmpfs': ['/run', '/tmp'], 'volumes': ['/sys/fs/cgroup:/sys/fs/cgroup']}, 'ansible_loop_var': 'item'})

PLAY RECAP *********************************************************************
localhost                  : ok=2    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

INFO     Pruning extra files from scenario ephemeral directory
ERROR: InvocationError for command /opt/vector-role/.tox/py37-ansible30/bin/molecule test -s molecule_podman --destroy always (exited with code 1)


```

</details>

9. Добавьте новый тег на коммит с рабочим сценарием в соответствии с семантическим версионированием.

После выполнения у вас должно получится два сценария molecule и один tox.ini файл в репозитории. Не забудьте указать в ответе теги решений Tox и Molecule заданий. В качестве решения пришлите ссылку на  ваш репозиторий и скриншоты этапов выполнения задания. 

## Необязательная часть

1. Проделайте схожие манипуляции для создания роли lighthouse.
2. Создайте сценарий внутри любой из своих ролей, который умеет поднимать весь стек при помощи всех ролей.
3. Убедитесь в работоспособности своего стека. Создайте отдельный verify.yml, который будет проверять работоспособность интеграции всех инструментов между ними.
4. Выложите свои roles в репозитории.

В качестве решения пришлите ссылки и скриншоты этапов выполнения задания.

---

### Как оформить ДЗ?

Выполненное домашнее задание пришлите ссылкой на .md-файл в вашем репозитории.
