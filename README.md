# snapshotalyzer-30000
Demo project to manage AWS EC2 instance snapshots

## About

This project is a demo, and uses [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html?id=docs_gateway)
to manage AWS EC2 instance snapshots.

## Configuring

shotty uses the configuration file created by the AWS cli, e.g. 

`aws configure --profile shotty`

## Running
This project requires Python 3 and the `boto3` package.

First, install [pipenv](https://github.com/pypa/pipenv). Then:

```
pipenv install
pipenv run shotty/shotty.py
```
