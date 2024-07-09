#!/bin/bash -e

export FLASK_APP=segmenter
export FLASK_ENV=production

N_WORKERS=3

echo "Serving with $N_WORKERS workers"

gunicorn -b 0.0.0.0:5000 \
    --workers $N_WORKERS \
    --log-level=warning \
    --access-logformat '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"' \
    $@ "segmenter:create_app()"
