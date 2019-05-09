FROM node:12

COPY plugin.json /plugin.json
COPY src /plugin

# Install dependencies
WORKDIR /plugin
RUN npm install

CMD ["node /plugin/index.js"]
