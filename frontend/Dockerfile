FROM node:16-alpine

RUN mkdir -p /usr/src/frontend
WORKDIR /usr/src/frontend

COPY . /usr/src/frontend/
RUN npm i
RUN npm run build
RUN npm install -g serve
CMD ["serve", "-s", "build", "-l", "3000"]
