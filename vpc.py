import boto3

# Create a boto3 client to EC2
ec2 = boto3.client('ec2')

# Define the CIDR block for the VPC
vpc_cidr = '10.0.0.0/16'

# Create the VPC
response = ec2.create_vpc(
    CidrBlock=vpc_cidr
)

# Get the VPC ID
vpc_id = response['Vpc']['VpcId']

# Create a subnet within the VPC
response = ec2.create_subnet(
    VpcId=vpc_id,
    CidrBlock='10.0.0.0/24',
    AvailabilityZone='us-west-2a'
)

# Get the Subnet ID
subnet_id = response['Subnet']['SubnetId']

# Create an Internet Gateway
response = ec2.create_internet_gateway()

# Get the Internet Gateway ID
internet_gateway_id = response['InternetGateway']['InternetGatewayId']

# Attach the Internet Gateway to the VPC
ec2.attach_internet_gateway(
    InternetGatewayId=internet_gateway_id,
    VpcId=vpc_id
)

# Create a route table
response = ec2.create_route_table(
    VpcId=vpc_id
)

# Get the Route Table ID
route_table_id = response['RouteTable']['RouteTableId']

# Add a default route to the route table
ec2.create_route(
    RouteTableId=route_
