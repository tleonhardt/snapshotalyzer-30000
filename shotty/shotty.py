#!/usr/bin/env python3
"""Demo project to manage AWS EC2 instance snapshots using boto3."""
import boto3

session = boto3.Session(profile_name='shotty')
ec2 = session.resource('ec2')


def list_instances() -> None:
    """List running EC2 instances."""
    for i in ec2.instances.all():
        print(i)


if __name__ == '__main__':
    list_instances()
