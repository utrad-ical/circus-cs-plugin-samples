FROM node:12

# Add plugin manifest file.
COPY plugin.json /

# Add main script for this CAD.
COPY src/* /plugin/

# Install dependencies via NPM inside the container.
WORKDIR /plugin
RUN npm install

# This is the main entry point when this container is invoked.
CMD ["node", "/plugin/index.js"]
