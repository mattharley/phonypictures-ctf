FROM ubuntu:14.04
MAINTAINER Matt Harley <matt@mattharley.com>

RUN apt-get -y --force-yes update
RUN apt-get -y --force-yes install openssh-server ncurses-dev python2.7-dev python-pip

# install ssh
RUN cp /etc/ssh/sshd_config /etc/ssh/sshd_config.factory-defaults
RUN chmod a-w /etc/ssh/sshd_config.factory-defaults
RUN echo 'root:b!gb0ss' | chpasswd

# install pip/python
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . /usr/src/app
RUN pip install -r requirements.txt

# Game of Clones!
RUN cp /usr/src/app/GameOfClones.gif /root

# start ssh
RUN cp /usr/src/app/sshd_config /etc/ssh/sshd_config
RUN /etc/init.d/ssh start

EXPOSE 22/tcp
EXPOSE 5000/tcp
EXPOSE 5001/tcp
