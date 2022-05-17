# STAGE 1 --------------------------------------------
FROM node:14-alpine as base

WORKDIR /svelte

COPY ./svelte/rollup.config.js /svelte
COPY ./svelte/package*.json /svelte/

RUN npm install

COPY ./svelte/src /svelte/src
COPY ./svelte/public /svelte/public

RUN npm run build

# STAGE 2 --------------------------------------------
FROM nginx:latest

#Copy NGINX configuration
COPY nginx.conf /etc/nginx/nginx.conf

# Copy static files
COPY --from=base /svelte/public /usr/share/nginx/html
