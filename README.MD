# 24 Sevens
## Backend
Go to `backend` folder, create a virtual environment and install the requirements.

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Frontend
Go to `frontend` folder, install the requirements and run the server.

```bash
cd frontend
npm install
npm start
```

## Nginx

Go to `nginx` folder, correct ports and servernames

```bash
cd nginx
nano backend.conf
nano frontend.conf
```

## Docker

Edit the `docker-compose.yml`, correct ports and configs

```bash
nano docker-compose.yml
```

## Deployment

```bash
docker-compose up
```
