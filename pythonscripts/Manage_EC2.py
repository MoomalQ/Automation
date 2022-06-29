"""
Task: Manage EC2 instance using python
"""
import boto3


def create_ec2_instance():
    """
    Create an EC2 instanc
    """
    print("Creating EC2 instance ")
    try:

        ec2_client = boto3.client("ec2", region_name="eu-west-3")
        instances = ec2_client.run_instances(
            ImageId="ami-00f13602fa9acface",
            MinCount=1,
            MaxCount=1,
            InstanceType="t4g.nano",
            KeyName="KeyPair1"
        )

        print(instances["Instances"][0]["InstanceId"])
    except Exception as exception:
        print(exception)


def describe_ec2_instance():
    """
    Describe EC2 instance
    """
    try:
        print("Describing EC2 instance")
        ec2_client = boto3.client("ec2")
        # Terminates the 3rd instance in the list Reservation
        print(ec2_client.describe_instances()[
              "Reservations"][3]["Instances"][0]["InstanceId"])
        return str(ec2_client.describe_instances()["Reservations"][3]["Instances"][0]["InstanceId"])
    except Exception as exception:
        print(exception)


def reboot_ec2_instance():
    """
    Reboot EC2 instance
    """
    try:
        print("Reboot EC2 instance")
        instance_id = describe_ec2_instance()
        ec2_client = boto3.client("ec2")
        print(ec2_client.reboot_instances(InstanceIds=[instance_id]))
    except Exception as exception:
        print(exception)


def stop_ec2_instance():
    """
    Stop EC2 instance
    """
    try:
        print("Stop EC2 instance")
        instance_id = describe_ec2_instance()
        ec2_client = boto3.client("ec2")
        print(ec2_client.stop_instances(InstanceIds=[instance_id]))
    except Exception as exception:
        print(exception)


def start_ec2_instance():
    """
    Start EC2 instance
    """
    try:
        print("Start EC2 instance")
        instance_id = describe_ec2_instance()
        ec2_client = boto3.client("ec2")
        print(ec2_client.start_instances(InstanceIds=[instance_id]))
    except Exception as exception:
        print(exception)


def terminate_ec2_instance():
    """
    Terminate EC2 instance
    """
    try:
        print("Terminate EC2 instance")
        instance_id = describe_ec2_instance()
        ec2_client = boto3.client("ec2")
        print(ec2_client.terminate_instances(InstanceIds=[instance_id]))
    except Exception as exception:
        print(exception)


# create_ec2_instance()
# describe_ec2_instance()
# reboot_ec2_instance()
# stop_ec2_instance()
# start_ec2_instance()
terminate_ec2_instance()
