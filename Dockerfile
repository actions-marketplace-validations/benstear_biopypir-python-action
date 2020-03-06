FROM python:3-slim AS builder
ADD . /app
WORKDIR /app

# We are installing a dependency here directly into our app source dir
RUN pip install --target=/app numpy

# A distroless container image with Python and some basics like SSL certificates
# https://github.com/GoogleContainerTools/distroless
FROM gcr.io/distroless/python3-debian10
COPY --from=builder /app /app
COPY step_3.sh /step_3.sh
WORKDIR /app
ENV PYTHONPATH /app
#CMD ["/app/main.py"]
#CMD ["ls -a"]
#CMD ["pwd"]
CMD ["chmod +x step_3.sh"]
RUN ./step_3.sh
