# Change after 3.12 is fixed: https://github.com/open-telemetry/opentelemetry-python/issues/3370
FROM mcr.microsoft.com/cbl-mariner/base/python:3.9-cm2.0

# Create app directory
WORKDIR /usr/src/pythonapp

# Flask
COPY test_app.py ./
COPY requirements.txt ./
# TODO: Copy json for AAD and statsbeat
# copy applicationinsights.json if it exists. This is used for AAD authentication and statsbeat
# COPY applicationinsights.json* ./

# TODO: Find way to pull this from PYTHON_TEST_APP_PORT
EXPOSE 8082

RUN python3 -m ensurepip && \
    # Change after Flask 3.0.0 is supported: https://github.com/open-telemetry/opentelemetry-python-contrib/issues/1975
    python3 -m pip install -r requirements.txt

ENV APPLICATIONINSIGHTS_CONNECTION_STRING="InstrumentationKey=ec500fd4-d1b0-48e4-8bea-85d15385b671;IngestionEndpoint=https://centralus-2.in.applicationinsights.azure.com/;LiveEndpoint=https://centralus.livediagnostics.monitor.azure.com/;ApplicationId=4592960f-3e47-45b7-bae3-7c9e9d788943"

CMD [ "python3", "test_app.py" ]