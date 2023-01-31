<html>
  <head>
    <title>Custom VPC Creation in AWS using Boto3</title>
  </head>
  <body>
    <h1>Custom VPC Creation in AWS using Boto3</h1>
    <h2>Introduction</h2>
    <p>This tutorial will guide you through the process of creating a custom Virtual Private Cloud (VPC) in Amazon Web Services (AWS) using the Boto3 Python library.</p>
    <h2>Prerequisites</h2>
    <ul>
      <li>An AWS account</li>
      <li>Boto3 library installed in your system</li>
    </ul>
    <h2>Step 1: Import the Boto3 Library</h2>
    <p>To start, you'll need to import the Boto3 library in your Python script:</p>
    <pre>
import boto3
    </pre>
    <h2>Step 2: Create a Boto3 Client for EC2</h2>
    <p>Next, create a Boto3 client for EC2:</p>
    <pre>
ec2 = boto3.client('ec2')
    </pre>
    <h2>Step 3: Define the CIDR Block for the VPC</h2>
    <p>Define the CIDR block for the VPC:</p>
    <pre>
vpc_cidr = '10.0.0.0/16'
    </pre>
    <h2>Step 4: Create the VPC</h2>
    <p>Create the VPC using the following code:</p>
    <pre>
response = ec2.create_vpc(
    CidrBlock=vpc_cidr
)
    </pre>
    <h2>Step 5: Get the VPC ID</h2>
    <p>Get the VPC ID:</p>
    <pre>
vpc_id = response['Vpc']['VpcId']
    </pre>
    <h2>Step 6: Create a Subnet within the VPC</h2>
    <p>Create a subnet within the VPC:</p>
    <pre>
response = ec2.create_subnet(
    VpcId=vpc_id,
    CidrBlock='10.0.0.0/24',
    AvailabilityZone='us-west-2a'
)
    </pre>
    <h2>Step 7: Get the Subnet ID</h2>
    <p>Get the Subnet ID:</p>
    <pre>
subnet_id = response['Subnet']['SubnetId']
    </pre>
    <h2>Step 8: Create an Internet Gateway</h2>
    <p>Create an Internet Gateway:</p>
    <pre>
response = ec2.create_internet_gateway()
    </pre>
    <h2>Step 9: Get the Internet Gateway ID</h2>
    <p>Get the Internet Gateway ID:</p>
    <pre>
internet_gateway_id = response['InternetGateway']['InternetGatewayId']
</pre>
<h2>Step 10: Attach the Internet Gateway to the VPC</h2>
<p>Attach the Internet Gateway to the VPC:</p>
<pre>
response = ec2.attach_internet_gateway(
InternetGatewayId=internet_gateway_id,
VpcId=vpc_id
)
</pre>
<h2>Step 11: Create a Route Table</h2>
<p>Create a Route Table:</p>
<pre>
response = ec2.create_route_table(
VpcId=vpc_id
)
</pre>
<h2>Step 12: Get the Route Table ID</h2>
<p>Get the Route Table ID:</p>
<pre>
route_table_id = response['RouteTable']['RouteTableId']
</pre>
<h2>Step 13: Create a Route for the Internet Gateway</h2>
<p>Create a Route for the Internet Gateway:</p>
<pre>
response = ec2.create_route(
DestinationCidrBlock='0.0.0.0/0',
GatewayId=internet_gateway_id,
RouteTableId=route_table_id
)
</pre>
<h2>Step 14: Associate the Subnet with the Route Table</h2>
<p>Associate the Subnet with the Route Table:</p>
<pre>
response = ec2.associate_route_table(
SubnetId=subnet_id,
RouteTableId=route_table_id
)
</pre>
<h2>Step 15: Launch an EC2 Instance within the VPC</h2>
<p>Finally, launch an EC2 instance within the VPC:</p>
<pre>
response = ec2.run_instances(
ImageId='ami-0c55b159cbfafe1f0',
InstanceType='t2.micro',
MinCount=1,
MaxCount=1,
SubnetId=subnet_id
)
</pre>
<h2>Conclusion</h2>
<p>This tutorial has demonstrated how to create a custom VPC in AWS using Boto3. This VPC can be used to host your applications and services in a secure and isolated environment.</p>

  </body>
</html>
