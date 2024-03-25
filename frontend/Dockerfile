FROM node:20.10.0-alpine

WORKDIR /app/frontend/

COPY package*.json /app/frontend/
RUN npm install

RUN npm install @reduxjs/toolkit react-router-dom tailwindcss @headlessui/react && \
    npm install && \
    npm i react-router-dom && \
    npm install tailwindcss && \
    npm install --cpu=x64 --os=linux sharp && \
    npm install --cpu=x64 --os=linux --libc=musl sharp

COPY . /app/frontend/

RUN npm run build

EXPOSE 8080
CMD [ "npm", "run", "dev" ]
