FROM python:alpine3.16 as base
# set poetry for installations
ENV POETRY_VERSION=1.0.5
ENV POETRY_VENV=/opt/poetry-venv
ENV POETRY_HOME=/opt/poetry
# Tell Poetry where to place its cache and virtual environment
ENV POETRY_CACHE_DIR=/opt/.cache
# Install and setup poetry
# Install poetry separated from system interpreter
RUN python3 -m venv $POETRY_VENV \
    && $POETRY_VENV/bin/pip install -U pip setuptools \
    && $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION}
# Add `poetry` to PATH
ENV PATH="${PATH}:${POETRY_VENV}/bin"
WORKDIR /app
# Copy Dependencies
COPY . /app/
# [OPTIONAL] Validate the project is properly configured
RUN poetry check
# Install Dependencies
RUN poetry install --no-interaction --no-ansi

FROM base as production
# Run application
EXPOSE 5000
CMD ["poetry", "run", "gunicorn", "-b", "0.0.0.0:5000", "todo_app.app:app" ]

FROM base as development
# Run application
EXPOSE 5000
CMD ["poetry" , "run", "flask", "run", "--host=0.0.0.0"]