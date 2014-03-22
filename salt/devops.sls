postgresql-server:
  pkg:
    - installed

postgresql-devel:
  pkg:
    - installed

python-devel:
  pkg:
    - installed

gcc:
  pkg:
    - installed

nginx:
  pkg:
    - installed

erlang:
  pkg:
    - installed

rabbitmq-server:
  pkg:
    - installed
    - require:
      - pkg: erlang

python-pip:
  pkg:
    - installed

uwsgi:
  pip.installed:
    - require:
      - pkg: python-pip

Django:
  pip.installed:
    - name: Django == 1.6.2
    - require:
      - pkg: python-pip

celery:
  pip.installed:
    - name: celery == 3.1.9
    - require:
      - pkg: python-pip

django-celery:
  pip.installed:
    - name: django-celery == 3.1.9
    - require:
      - pkg: python-pip

psycopg2:
  pip.installed:
    - name: psycopg2 == 2.5.2
    - require:
      - pkg: python-pip
      - pkg: postgresql-devel
      - pkg: gcc
      - pkg: python-devel

supervisor:
  pip.installed:
    - require:
      - pkg: python-pip

virtualenv:
  pip.installed:
    - require:
      - pkg: python-pip

south:
  pip.installed:
    - require:
      - pkg: python-pip

/etc/nginx/conf.d/devops-challenge.conf:
  file.managed:
    - source: salt://devops-challenge.conf
    - require:
      - pkg: nginx

/etc/supvervisord.conf:
  file.managed:
    - source: salt://supervisord.conf
    - require:
      - pip: supervisor

/etc/init.d/supvervisord:
  file.managed:
    - source: salt://supervisord
    - require:
      - pip: supervisor

nginx_service:
  service:
    - name: nginx
    - running
    - enable: True

supervisord_service:
  service:
    - name: supervisord
    - running
    - enable: True

rabbitmq-server_service:
  service:
    - name: rabbitmq-server
    - running
    - enable: True

postgresql_service:
  service:
    - name: postgresql
    - running
    - enable: True

