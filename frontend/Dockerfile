FROM node:18-alpine

WORKDIR /app/frontend/

COPY package*.json /app/frontend/
RUN npm install

COPY . /app/frontend/

RUN npm run build

EXPOSE 8080

CMD [ "npm", "run", "preview" ]