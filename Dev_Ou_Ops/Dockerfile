FROM debian:buster
RUN apt -y update 
RUN apt -y install git python3 python3-pip
RUN python3 -m pip install bottle
RUN git clone https://github.com/nono128/tp2.git

CMD ["python3","test.py"]

