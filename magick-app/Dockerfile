FROM node:6.1.0-wheezy

RUN mkdir /usr/src/magick
COPY . /usr/src/magick
WORKDIR /usr/src/magick

RUN npm install 
RUN echo deb http://archive.debian.org/debian wheezy main > /etc/apt/sources.list
RUN echo deb http://archive.debian.org/debian-archive/debian-security/ wheezy updates/main >> /etc/apt/sources.list
RUN apt-get update
RUN apt-get install ghostscript -y --force-yes
RUN apt-get install vim -y --force-yes
# RUN apt-get install curl
# RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | bash
# RUN npm install -g npm
# RUN nvm install node
EXPOSE 3000
EXPOSE 31337
CMD ["npm", "start"]