FROM alpine:3.7

WORKDIR /usr/src/app

COPY requirements.txt .

# Upgrade, install dependencies and remove unecessary files
RUN apk upgrade --no-cache \
	&& apk add --no-cache python3 python3-dev bash postgresql-dev musl-dev gcc \
	&& pip3 install --no-cache-dir --upgrade pip \
	&& pip3 install --no-cache-dir -r requirements.txt \
	&& rm -rf /var/cache/* \
	&& rm -rf /root/.cache/*

# Run database migrations
RUN alembic -c ./migrations/alembic.ini upgrade head

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]