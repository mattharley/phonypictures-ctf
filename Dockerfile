FROM ubuntu:14.04
MAINTAINER Matt Harley <matt@mattharley.com>

RUN apt-get -y --force-yes update

# install ssh
RUN apt-get -y --force-yes install openssh-server 
RUN cp /etc/ssh/sshd_config /etc/ssh/sshd_config.factory-defaults
RUN chmod a-w /etc/ssh/sshd_config.factory-defaults

RUN echo "AllowUsers root" >> /etc/ssh/sshd_config

# install pip/python
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
RUN apt-get -y --force-yes install ncurses-dev python2.7-dev

ONBUILD COPY . /usr/src/app
ONBUILD RUN pip install --no-cache-dir -r requirements.txt

# ftp server
RUN apt-get -y --force-yes install vsftpd
RUN usermod -d /usr/src/app ftp 
RUN restart vsftpd

EXPOSE 80/tcp
EXPOSE 21/tcp