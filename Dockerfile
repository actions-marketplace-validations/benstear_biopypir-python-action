FROM python:3-slim AS builder
ADD . /app
WORKDIR /app

# We are installing a dependency here directly into our app source dir
RUN pip install --target=/app requests
RUN pip install --target=/app --upgrade pip setuptools wheel
RUN pip install --target=/app os
RUN pip install --target=/app time
RUN pip install --target=/app json
RUN pip install --target=/app pandas 
RUN pip install --target=/app tabulate 
RUN pip install --target=/app glob
RUN pip install --target=/app numpy 

# A distroless container image with Python and some basics like SSL certificates
# https://github.com/GoogleContainerTools/distroless
FROM gcr.io/distroless/python3-debian10
COPY --from=builder /app /app
WORKDIR /app
ENV PYTHONPATH /app
CMD ["/cmd/main.py"]
