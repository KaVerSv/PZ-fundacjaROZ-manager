FROM node:20.10.0-alpine

WORKDIR /app/frontend/

COPY package*.json /app/frontend/
RUN npm install

RUN npm install @reduxjs/toolkit react-router-dom tailwindcss @headlessui/react

COPY . /app/frontend/

EXPOSE 8080
CMD [ "npm", "run", "dev" ]
