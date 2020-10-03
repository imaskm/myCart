FROM python:3.8.6-alpine3.12
COPY . ./MyCart
WORKDIR ./MyCart
RUN pip3 install -r requirements.txt
ENV PYTHONPATH="$PYTHONPATH:/MyCart"
ENV DB_PATH=/MyCart/mycart.db
RUN python3 ./mycart/scripts/init.py
ENTRYPOINT python3  mycart/main.py
