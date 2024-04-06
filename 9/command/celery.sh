#!/bin/bash

celery -A src.tasks:celery worker
