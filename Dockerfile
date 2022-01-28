FROM python

WORKDIR /app
COPY . .
RUN chmod +x ./entrypoint.sh
RUN python -m pip install --upgrade pip
RUN pip install -e .[prod]
ENV FLASK_APP=employees
ENV FLASK_ENV=development

ENTRYPOINT [ "./entrypoint.sh" ]