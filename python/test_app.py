from os import environ
# from opentelemetry import trace
from flask import Flask, request
import logging
import requests

# from azure.monitor.opentelemetry import configure_azure_monitor

# configure_azure_monitor()

app = Flask(__name__)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

@app.route("/")
def server_request():
    print(request.args.get("param"))
    logger.info("request page")
    return "Flask App"

@app.route("/dependencies")
def dependencies_request():
    print(request.args.get("param"))
    requests.get('https://learn.microsoft.com/en-us/azure/azure-monitor/app/opentelemetry-enable?tabs=python')
    return "dependencies"

@app.route("/exceptions")
def exception_request():
    print(request.args.get("param"))
    try:
        raise Exception('Test Error')
    except Exception as e:
        logger.error(e)
    try:
        raise Exception('Test Exception')
    except Exception as e:
        logger.exception(e)
    # Use these manual events until events exporter is added.
    # produce_trace_and_exception_events()
    requests.get('https://httpstat.us/400')
    return "exceptions", 500

# def test_import_attach_dependencies():
#     import asgiref
#     import certifi
#     import charset_normalizer
#     import deprecated
#     import fixedint
#     import idna
#     import importlib_metadata
#     import isodate
#     import msrest
#     import oauthlib
#     import packaging
#     import pkg_resources
#     import psutil
#     import requests
#     import setuptools
#     import six
#     import typing_extensions
#     import urllib3
#     import wrapt
#     import zipp

# def produce_trace_and_exception_events():
#     tracer = trace.get_tracer(__name__)

#     # Trace message events
#     with tracer.start_as_current_span("hello") as span:
#         span.add_event("Custom event", {"test": "attributes"})
    
#     # Exception events
#     try:
#         with tracer.start_as_current_span("hello") as span:
#             raise Exception("Custom exception message.")
#     except Exception:
#         print("Exception raised")

if __name__ == "__main__":
    # Test imports of attach dependencies to detect breaking conflicts.
    # test_import_attach_dependencies()
    # port = environ["PYTHON_TEST_APP_PORT"]
    port = "8082"
    print("Server running at port: %s" % port)
    app.run(port=port, host='0.0.0.0')

