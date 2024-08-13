FROM python:3.12-alpine AS deps

COPY requirements.txt /

RUN pip install --upgrade pip && \
    pip wheel --no-cache-dir --no-deps --wheel-dir=/wheel -r /requirements.txt

FROM python:3.12-alpine AS app

LABEL org.opencontainers.image.source=https://github.com/meysam81/reddit-scheduled-submit
LABEL org.opencontainers.image.description="A simple script to schedule posts on Reddit."

RUN addgroup -S app && adduser -S app -G app

WORKDIR /app

COPY --from=deps /wheel /wheel
RUN pip install --no-cache /wheel/* && rm -rf /wheel

USER app:app

COPY main.py .

ENTRYPOINT ["/app/main.py"]
CMD ["--help"]
