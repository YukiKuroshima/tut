# base image
FROM node:9.2

# set working directory
RUN mkdir /usr/src/app
WORKDIR /usr/src/app

# add `/usr/src/app/node_modules/.bin` to $PATH
ENV PATH /usr/src/app/node_modules/.bin:$PATH

# install and cache app dependencies
ADD ./package.json /usr/src/app/package.json
RUN npm install --silent
RUN npm install react-scripts@1.0.17 -g --silent

# start app
CMD ["npm", "start"]
