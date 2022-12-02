FROM nginx:1.23

# RUN apt-get update
# RUN apt-get install nginx-extras

RUN rm /etc/nginx/conf.d/default.conf
RUN rm /etc/nginx/nginx.conf

COPY nginx.conf /etc/nginx/nginx.conf
COPY conf.d/. /etc/nginx/conf.d