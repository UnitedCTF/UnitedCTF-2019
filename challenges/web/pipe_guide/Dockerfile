FROM erikap/ruby-sinatra

WORKDIR /usr/src/app

COPY /app .
COPY /flag /ex3cute_m3_to_g3t_th3_fl4g
RUN chown root /ex3cute_m3_to_g3t_th3_fl4g
RUN chmod 111 /ex3cute_m3_to_g3t_th3_fl4g
RUN chmod u+s /ex3cute_m3_to_g3t_th3_fl4g

USER www-data

