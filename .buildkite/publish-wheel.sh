#!/bin/bash
set -eu
pip install devpi-client
devpi use https://devpi.kx.gd/koordinates/trixie
devpi login "$DEVPI_USER" --password="$DEVPI_PASSWORD"
devpi upload dist/*.whl
