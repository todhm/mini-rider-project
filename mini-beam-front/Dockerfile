FROM node:15.10-alpine
WORKDIR /usr/src/app

ENV PATH /usr/src/app/node_modules/.bin:$PATH
COPY package.json /usr/src/app/package.json

RUN npm install


COPY . /usr/src/app

#########
# FINAL #
#########
EXPOSE 3000
CMD ["npm", "run", "dev"]