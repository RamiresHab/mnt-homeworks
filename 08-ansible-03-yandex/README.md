## Плейбук
Этот плейбук устанавливает СУБД Clickhouse, сервис Vector и lighthouse для просмотра собранных логов.
Для запуска плейбука используется команда:

```
ansible-playbook -i inventory/prod.yml site.yml
```

## Требования
Для запуска плейбука нужен ansible версии не ниже 2.10. Для установки пакетов нужны сервера под управлением Ubuntu 22.04 и выше.

## Инвентори
В inventory/prod.yml нужно внести адреса серверов, на которые будет устанавливаться софт и пользователей, под которыми ansible будет ходить на эти сервера. 

| Name           | Default Value | Description                        |
| -------------- | ------------- | -----------------------------------|
| `clickhouse_version` | 22.3.3.44 | Версия clickhouse |
| `clickhouse_packages.name` | clickhouse-common-static, clickhouse-client, clickhouse-server | Названия пакетов для установки clickhouse  |
| `vector_version` | 0.27.0 | Версия vector |
| `vector_package` | vector | название пакета для установкиvector |

  
## Темплейты
В template/lighthouse.j2 содержится конфиг nginx для lighthouse.

## Тэги
В плейбуке прописаны следующие тэги:
 * для установки clickhouse можно использовать --tag clickhouse;
 * для установки vector-role можно использовать --tag vector;
 * для установки lighthouse-role можно использовать --tag lighthouse

-------

# Домашнее задание к занятию "3. Использование Yandex Cloud"

## Подготовка к выполнению

1. Подготовьте в Yandex Cloud три хоста: для `clickhouse`, для `vector` и для `lighthouse`.

Ссылка на репозиторий LightHouse: https://github.com/VKCOM/lighthouse

## Основная часть

1. Допишите playbook: нужно сделать ещё один play, который устанавливает и настраивает lighthouse.

```
- name: Install lighthouse
  hosts: lighthouse
  handlers:
    - name: Start nginx service
      become: true
      ansible.builtin.service:
        name: nginx
        state: restarted
  tasks:
    - name: Install nginx
      become: true
      ansible.builtin.apt:
        name: nginx
    - name: Download lighthouse
      become: true
      ansible.builtin.git:
        repo: https://github.com/VKCOM/lighthouse.git
        dest: /var/www/lighthouse
    - name: Fix owner and mode
      become: true
      ansible.builtin.file:
        path: /var/www/lighthouse
        state: directory
        mode: '0755'
        owner: www-data
    - name: nginx config
      become: true
      ansible.builtin.template:
        src: template/lighthouse.j2
        dest: /etc/nginx/sites-available/lighthouse
        owner: www-data
    - name: Symlink to sites-enabled
      become: true
      ansible.builtin.file:
        src: /etc/nginx/sites-available/lighthouse
        dest: /etc/nginx/sites-enabled/lighthouse
        state: link
      notify: Start nginx service
```

2. При создании tasks рекомендую использовать модули: `get_url`, `template`, `yum`, `apt`.
3. Tasks должны: скачать статику lighthouse, установить nginx или любой другой webserver, настроить его конфиг для открытия lighthouse, запустить webserver.
4. Приготовьте свой собственный inventory файл `prod.yml`.

```
---
clickhouse:
  hosts:
    clickhouse-01:
      ansible_host: 158.160.62.99
      ansible_user: roman

vector:
  hosts:
    vector-01:
      ansible_host: 158.160.47.177
      ansible_user: roman
      
lighthouse:
  hosts:
    lighthouse-01:
      ansible_host: 158.160.59.204
      ansible_user: roman
```

5. Запустите `ansible-lint site.yml` и исправьте ошибки, если они есть.
6. Попробуйте запустить playbook на этом окружении с флагом `--check`.
7. Запустите playbook на `prod.yml` окружении с флагом `--diff`. Убедитесь, что изменения на системе произведены.
8. Повторно запустите playbook с флагом `--diff` и убедитесь, что playbook идемпотентен.

```
➜  playbook git:(MNT-video) ✗ ansible-playbook -i inventory/prod.yml site.yml --diff
[WARNING]: Error getting vault password file (datatools): The vault password file /Users/ro.khabibullin/.vault/datatools_vault was not found
[WARNING]: Error getting vault password file (getstream): The vault password file /Users/ro.khabibullin/.vault/getstream was not found

PLAY [Install Clickhouse] **********************************************************************************************************************************************************************************************************************************************************************************************

TASK [Gathering Facts] *************************************************************************************************************************************************************************************************************************************************************************************************
ok: [clickhouse-01]

TASK [Get clickhouse distrib] ******************************************************************************************************************************************************************************************************************************************************************************************
ok: [clickhouse-01] => (item={'name': 'clickhouse-common-static', 'arch': 'amd64'})
ok: [clickhouse-01] => (item={'name': 'clickhouse-client', 'arch': 'all'})
ok: [clickhouse-01] => (item={'name': 'clickhouse-server', 'arch': 'all'})

TASK [Install clickhouse packages] *************************************************************************************************************************************************************************************************************************************************************************************
ok: [clickhouse-01] => (item={'name': 'clickhouse-common-static', 'arch': 'amd64'})
ok: [clickhouse-01] => (item={'name': 'clickhouse-client', 'arch': 'all'})
ok: [clickhouse-01] => (item={'name': 'clickhouse-server', 'arch': 'all'})

TASK [Flush handlers] **************************************************************************************************************************************************************************************************************************************************************************************************

TASK [Create database] *************************************************************************************************************************************************************************************************************************************************************************************************
ok: [clickhouse-01]

PLAY [Install Vector] **************************************************************************************************************************************************************************************************************************************************************************************************

TASK [Gathering Facts] *************************************************************************************************************************************************************************************************************************************************************************************************
ok: [vector-01]

TASK [Get Vector] ******************************************************************************************************************************************************************************************************************************************************************************************************
ok: [vector-01]

TASK [Install Vector] **************************************************************************************************************************************************************************************************************************************************************************************************
ok: [vector-01]

TASK [Flush handlers] **************************************************************************************************************************************************************************************************************************************************************************************************

PLAY [Install lighthouse] **********************************************************************************************************************************************************************************************************************************************************************************************

TASK [Gathering Facts] *************************************************************************************************************************************************************************************************************************************************************************************************
ok: [lighthouse-01]

TASK [Install nginx] ***************************************************************************************************************************************************************************************************************************************************************************************************
ok: [lighthouse-01]

TASK [Download lighthouse] *********************************************************************************************************************************************************************************************************************************************************************************************
ok: [lighthouse-01]

TASK [Fix owner and mode] **********************************************************************************************************************************************************************************************************************************************************************************************
ok: [lighthouse-01]

TASK [nginx config] ****************************************************************************************************************************************************************************************************************************************************************************************************
ok: [lighthouse-01]

TASK [Symlink to sites-enabled] ****************************************************************************************************************************************************************************************************************************************************************************************
ok: [lighthouse-01]

PLAY RECAP *************************************************************************************************************************************************************************************************************************************************************************************************************
clickhouse-01              : ok=4    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
lighthouse-01              : ok=6    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
vector-01                  : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

9. Подготовьте README.md файл по своему playbook. В нём должно быть описано: что делает playbook, какие у него есть параметры и теги.

10. Готовый playbook выложите в свой репозиторий, поставьте тег `08-ansible-03-yandex` на фиксирующий коммит, в ответ предоставьте ссылку на него.

---

### Как оформить ДЗ?

Выполненное домашнее задание пришлите ссылкой на .md-файл в вашем репозитории.

---
