FROM nginx

RUN rm /etc/nginx/conf.d/default.conf
RUN rm /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/
COPY app.conf /etc/nginx/conf.d/