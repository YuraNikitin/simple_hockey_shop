# ---- Dev build ----
FROM node:12.14.1 as base

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    nginx

RUN npm install -g @vue/cli

COPY ./portal/package.json /frontend/portal/package.json
COPY ./portal/.eslintrc.js /frontend/portal/.eslintrc.js
COPY ./portal/index.html /frontend/portal/index.html

WORKDIR /frontend/portal

RUN npm install
