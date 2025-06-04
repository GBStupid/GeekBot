FROM python:3.12 AS base


FROM base AS install
WORKDIR /tmp
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

FROM base AS run
WORKDIR /app
COPY --from=install /install /usr/local
COPY . .

RUN groupadd --gid 1000 geekbot && \
  useradd --uid 1000 --gid geekbot --shell /bin/bash --create-home geekbot

RUN chown -R geekbot:geekbot /app

USER geekbot
CMD [ "python", "src/main.py" ] 
