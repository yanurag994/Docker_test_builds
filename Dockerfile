FROM alpine:3.13
RUN apk update && apk add python3
WORKDIR /home/
RUN mkdir output
RUN mkdir data
ADD ./app /home/
CMD python3 script.py && cat /home/output/results.txt