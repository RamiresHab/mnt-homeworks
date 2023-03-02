FROM centos:centos7.9.2009
RUN yum update -q -y \
  && yum install -q -y wget make git gcc openssl-devel bzip2-devel libffi-devel \
  && cd /usr/src \
  && wget https://www.python.org/ftp/python/3.7.4/Python-3.7.4.tgz \
  && tar xzf Python-3.7.4.tgz \
  && cd Python-3.7.4 \
  && ./configure --enable-optimizations \
  && make altinstall \
  && rm -rf /usr/src/Python-3.7.4.tgz \
  && yum clean all \
  # set python3.7 as default
  && alternatives --install /usr/bin/python python /usr/bin/python2 50 \
  && alternatives --install /usr/bin/python python /usr/local/bin/python3.7 70 \
  && alternatives --set python /usr/local/bin/python3.7 \
  # symlink pip
  && ln -s /usr/local/bin/pip3.7 /usr/bin/pip \
  && pip install --no-cache-dir --upgrade pip pipenv setuptools wheel \
  && pip install --no-cache-dir flask flask-jsonpify flask-restful \
  && ln -s /usr/local/bin/pipenv /usr/bin/pipenv \
  && mkdir /python_api
COPY python-api.py /python_api
ENTRYPOINT ["python3", "/python_api/python-api.py"]
