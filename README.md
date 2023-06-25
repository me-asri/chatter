# Chatter
__Chatter__ is a simple chatroom webapp written using VueJS for frontend and FastAPI for backend. 

## Requirements
 * Docker
 * Docker Compose

## Installation
__Chatter__ makes use of Docker Compose to setup and bring up both the backend and frontend servers.
### Generating Secret
__Chatter__ requires a 32 byte secret in hex format to be defined in the `CHATTER_SECRET` environment variable.
The `.env` file is used for storing the secret.
```
echo "CHATTER_SECRET=$(openssl rand -hex 32)" > .env
```

### Starting Chatter
```
docker compose up
```

### Stopping Chatter
```
docker compose down
```

## Disclaimer
__Here be dragons!__

This is an experimental software I've written to learn a thing or two about VueJS, FastAPI and Docker.

I'm not responsible if Megumin causes an explosion in your house.

## External Libraries
 * [Vue.js](https://vuejs.org/) - [MIT](https://raw.githubusercontent.com/vuejs/core/main/LICENSE)
 * [Vuetify](https://vuetifyjs.com/) - [MIT](https://raw.githubusercontent.com/vuetifyjs/vuetify/master/LICENSE.md)
 * [FastAPI](https://fastapi.tiangolo.com/) - [MIT](https://raw.githubusercontent.com/tiangolo/fastapi/master/LICENSE)