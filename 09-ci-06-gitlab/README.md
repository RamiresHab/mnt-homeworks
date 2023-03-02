# Домашнее задание к занятию 12 «GitLab»

## Подготовка к выполнению

1. Подготовьте к работе GitLab [по инструкции](https://cloud.yandex.ru/docs/tutorials/infrastructure-management/gitlab-containers).
2. Создайте свой новый проект.
3. Создайте новый репозиторий в GitLab, наполните его [файлами](./repository).
4. Проект должен быть публичным, остальные настройки по желанию.

## Основная часть

### DevOps

В репозитории содержится код проекта на Python. Проект — RESTful API сервис. Ваша задача — автоматизировать сборку образа с выполнением python-скрипта:

1. Образ собирается на основе [centos:7](https://hub.docker.com/_/centos?tab=tags&page=1&ordering=last_updated).
2. Python версии не ниже 3.7.
3. Установлены зависимости: `flask` `flask-jsonpify` `flask-restful`.
4. Создана директория `/python_api`.
5. Скрипт из репозитория размещён в /python_api.
6. Точка вызова: запуск скрипта.
7. Если сборка происходит на ветке `master`: должен подняться pod kubernetes на основе образа `python-api`, иначе этот шаг нужно пропустить.

## Итог

В качестве ответа пришлите подробные скриншоты по каждому пункту задания:

- файл gitlab-ci.yml;

1. https://github.com/RamiresHab/mnt-homeworks/blob/MNT-video/09-ci-06-gitlab/gitlab-ci.png
2. https://github.com/RamiresHab/mnt-homeworks/blob/MNT-video/09-ci-06-gitlab/repository/gitlab-ci.yml

- Dockerfile; 

1. https://github.com/RamiresHab/mnt-homeworks/blob/MNT-video/09-ci-06-gitlab/Dockerfile.png
2. https://github.com/RamiresHab/mnt-homeworks/blob/MNT-video/09-ci-06-gitlab/repository/Dockerfile

- лог успешного выполнения пайплайна;

1. https://github.com/RamiresHab/mnt-homeworks/blob/MNT-video/09-ci-06-gitlab/pipeline.png
2. https://github.com/RamiresHab/mnt-homeworks/blob/MNT-video/09-ci-06-gitlab/build.log
3. https://github.com/RamiresHab/mnt-homeworks/blob/MNT-video/09-ci-06-gitlab/deploy.log

- решённый Issue.

Про Issue в задании для DevOps ничего не было

### Важно 
После выполнения задания выключите и удалите все задействованные ресурсы в Yandex Cloud.

## Необязательная часть

Автомазируйте работу тестировщика — пусть у вас будет отдельный конвейер, который автоматически поднимает контейнер и выполняет проверку, например, при помощи curl. На основе вывода будет приниматься решение об успешности прохождения тестирования.

---