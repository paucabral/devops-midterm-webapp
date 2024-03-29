FROM python

COPY ./requirements.txt /home/myapp/requirements.txt
RUN pip install -r /home/myapp/requirements.txt
COPY ./static /home/myapp/static/
COPY ./templates /home/myapp/templates/
COPY app.py /home/myapp/
COPY api.py /home/myapp/
EXPOSE 5050
CMD python3 /home/myapp/app.py