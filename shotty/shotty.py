#!/usr/bin/env python3
"""Demo project to manage AWS EC2 instance snapshots using boto3."""
import boto3
import click

session = boto3.Session(profile_name='shotty')
ec2 = session.resource('ec2')


def filter_instances(project):
    """Filter EC2 instances based on Project tag"""
    if project:
        filters = [{'Name': 'tag:Project', 'Values': [project]}]
        ec2_instances = ec2.instances.filter(Filters=filters)
    else:
        ec2_instances = ec2.instances.all()
    return ec2_instances


@click.group()
def instances():
    """Commands for instances"""


@instances.command('list')
@click.option('--project', default=None, help="Only instances for project (tag Project:<name>)")
def list_instances(project) -> None:
    """List EC2 instances"""
    ec2_instances = filter_instances(project)

    for i in ec2_instances:
        tags = { tag['Key']: tag['Value'] for tag in i.tags or [] }
        print(', '.join((i.id,
                         i.instance_type,
                         i.placement['AvailabilityZone'],
                         i.state['Name'],
                         i.public_dns_name,
                         tags.get('Project', '<no project>'))))
    return


@instances.command('stop')
@click.option('--project', default=None, help="Only instances for project (tag Project:<name>)")
def stop_instances(project) -> None:
    """Stop EC2 instances"""
    ec2_instances = filter_instances(project)

    for i in ec2_instances:
        print("Stopping {}...".format(i.id))
        i.stop()


@instances.command('start')
@click.option('--project', default=None, help="Only instances for project (tag Project:<name>)")
def start_instances(project) -> None:
    """Start EC2 instances"""
    ec2_instances = filter_instances(project)

    for i in ec2_instances:
        print("Starting {}...".format(i.id))
        i.start()


if __name__ == '__main__':
    instances()
