FROM alpine:3.13
RUN apk update && apk add python3
WORKDIR /home/
RUN mkdir output
WORKDIR /home/data/
ADD ./app /home/data/
RUN python3 /home/data/script.py
CMD ["cat","/home/output/results.txt"]