#Modification par Kiko pour rajouter le COPY / WORKDIR (et ne plus utiliser git clone) 

FROM debian:buster

WORKDIR /data
# --> va créer le dossier /data et travailler dedans (car sinon tu es à la racine, et ça peut casser le systeme du conteneur)

RUN apt -y update 
RUN apt -y install git python3 python3-pip
RUN python3 -m pip install bottle psutil
#RUN ls -lah

COPY main.py /data/main.py
#  --> va copier "main.py" de ton systeme, et le mettre dans le fichier "main.py" dans ton conteneur 

#RUN git clone https://github.com/nono128/tp2.git

CMD ["python3","main.py"]

