# Ansible Collection - my_own_namespace.yandex_cloud_elk

## Documentation for the collection.
This is homework to netology. We have a role test_role and a module my_own_module in this collection.

## Playbook
Test playbook starts with command ```ansible-playbook site.yml```

### Roles
test_role has variables in role/test/role/vars/mail.yml

| Name           | Default Value | Description                     |
| -------------- | ------------- |---------------------------------|
| `path_file` | "/tmp/text" | Path to file for recording text |
| `content_file` | "Hello" | Text recording to file          |

## Modules
my_own_module is in plugins/modules/my_own_module.py
It has description in plugins/modules/README.md

## Version 1.0.0
