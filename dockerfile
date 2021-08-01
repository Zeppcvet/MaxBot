FROM python:3-alpine
ARG TEMP_TOKEN_VAR
ENV STATIC_TOKEN_VAR=$TEMP_TOKEN_VAR
run pip install pipenv telegram && pipenv install python-telegram-bot bs4
COPY . /MaxBot
EXPOSE 443 80 88 8443
# run export $BOT_TOKEN = STATIC_TOKEN_VAR
run echo $STATIC_TOKEN_VAR $$ echo $TEMP_TOKEN_VAR
CMD ["pipenv", "run", "/MaxBot/main.py"]
# CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]
