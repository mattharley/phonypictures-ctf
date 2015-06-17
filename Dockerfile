FROM ubuntu:14.04
MAINTAINER Matt Harley <matt@mattharley.com>

RUN apt-get -y --force-yes update

# install ssh
RUN apt-get -y --force-yes install openssh-server 
RUN cp /etc/ssh/sshd_config /etc/ssh/sshd_config.factory-defaults
RUN chmod a-w /etc/ssh/sshd_config.factory-defaults

RUN echo 'root:b!gb0ss' | chpasswd
RUN echo "AllowUsers root" >> /etc/ssh/sshd_config
RUN echo "PermitRootLogin yes" >> /etc/ssh/sshd_config

RUN /etc/init.d/ssh start

# install pip/python
RUN mkdir -p /usr/src/app
RUN apt-get -y --force-yes install ncurses-dev python2.7-dev python-pip

WORKDIR /usr/src/app
COPY . /usr/src/app
RUN pip install -r requirements.txt

EXPOSE 22/tcp
EXPOSE 5000/tcp
EXPOSE 5001/tcp