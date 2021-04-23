FROM nginx:1.17.8
COPY ./nginx.conf.template /nginx.conf.template
CMD ["/bin/sh" , "-c" , "envsubst '${FRONTEND_SERVER_API},${BACKEND_SERVER_API},${DEFAULT_HOST_NAME}' < /nginx.conf.template > /etc/nginx/nginx.conf && exec nginx -g 'daemon off;'"]
