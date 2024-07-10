#!/bin/bash

BASE_DIR="/opt/segmenter-svc"
SEGMENTER="$BASE_DIR/segmenter"

REQUIREMENTS="$BASE_DIR/requirements.txt"
WORKING_DIR="$BASE_DIR/aws_lambda/dist/build"
ARCHIVE_NAME="segmenter_lambda.zip"

mkdir -p $WORKING_DIR

cp aws_lambda/segmentation_handler.py $WORKING_DIR
cp -r $SEGMENTER $WORKING_DIR

# install dependencies
pip install --target $WORKING_DIR -r $REQUIREMENTS

# slim down package
find $WORKING_DIR -name "*.pyc" -exec rm -rf {} +
find $WORKING_DIR -name ".so" -exec strip --strip-unneeded {} +

# compress into zip
7za a $WORKING_DIR/../$ARCHIVE_NAME $WORKING_DIR/*
