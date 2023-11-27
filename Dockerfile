FROM python:3.10-bullseye as base 

# Install Google Chrome
RUN curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list && \
    apt-get -yqq update && \
    apt-get -yqq install google-chrome-stable jq && \
    rm -rf /var/lib/apt/lists/*

# Install latest chromedriver
RUN CHROMEDRIVER_URL=$(curl -s https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions-with-downloads.json | jq -r '.channels.Stable.downloads.chromedriver[] | select(.platform == "linux64") | .url') \
    && curl -sSLf --retry 3 --output /tmp/chromedriver-linux64.zip "$CHROMEDRIVER_URL" \
    && unzip -o /tmp/chromedriver-linux64.zip -d /tmp \
    && rm -rf /tmp/chromedriver-linux64.zip \
    && mv -f /tmp/chromedriver-linux64/chromedriver "/usr/local/bin/chromedriver" \
    && chmod +x "/usr/local/bin/chromedriver"

WORKDIR /app

FROM base as requirements
ADD requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

FROM requirements as runtime
ADD . /app
EXPOSE 8000
ENV DISPLAY=:99
RUN useradd -ms /bin/bash dockeruser
USER dockeruser
CMD ["gunicorn", "--chdir", "src/skydivewx", "-b", "0.0.0.0:8000", "app:server"]