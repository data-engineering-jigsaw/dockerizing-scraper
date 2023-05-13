FROM mcr.microsoft.com/playwright/python:v1.32.0-jammy

WORKDIR /home/pwuser

COPY ./scraper/requirements.txt .
RUN pip3 install -r requirements.txt

COPY ./scraper/ ./scraper

WORKDIR /home/pwuser/scraper

CMD ["python3", "manage.py", "save_as_json"]
