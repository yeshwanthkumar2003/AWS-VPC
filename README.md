<html>
  <head>
    <title>Custom VPC in AWS</title>
  </head>
  <body>
    <h1>Custom VPC in AWS</h1>
    <p>This tutorial will guide you through the process of creating a custom Virtual Private Cloud (VPC) in Amazon Web Services (AWS).</p>
    <h2>Step 1: Log into AWS Console</h2>
    <p>To start, log into the AWS Console using your AWS account credentials.</p>
    <img src="https://aws.amazon.com/images/aws-console.png" alt="AWS Console Login">
    <h2>Step 2: Navigate to the VPC Dashboard</h2>
    <p>Once logged in, navigate to the VPC Dashboard by clicking on the VPC link under the Networking & Content Delivery section of the AWS Management Console.</p>
    <img src="https://aws.amazon.com/images/vpc-dashboard.png" alt="VPC Dashboard">
    <h2>Step 3: Create a New VPC</h2>
    <p>Click on the Create VPC button to create a new VPC. Enter a name for the VPC and select the IPv4 CIDR block for the VPC. In this example, we are using 10.0.0.0/16 as the CIDR block.</p>
    <img src="https://aws.amazon.com/images/create-vpc.png" alt="Create VPC">
    <h2>Step 4: Create Subnets</h2>
    <p>Create subnets within the VPC by clicking on the Subnets link in the navigation panel and then clicking on the Create Subnet button. Enter a name for the subnet and select the VPC you just created from the VPC dropdown menu. Select the Availability Zone for the subnet and enter the IPv4 CIDR block for the subnet.</p>
    <img src="https://aws.amazon.com/images/create-subnet.png" alt="Create Subnet">
    <h2>Step 5: Create a Route Table</h2>
    <p>Create a route table for the VPC by clicking on the Route Tables link in the navigation panel and then clicking on the Create Route Table button. Enter a name for the route table and select the VPC you just created from the VPC dropdown menu.</p>
    <img src="https://aws.amazon.com/images/create-route-table.png" alt="Create Route Table">
    <h2>Step 6: Add a Default Route</h2>
    <p>Add a default route to the route table by clicking on the Routes tab, clicking on the Edit button, and then clicking on the Add another route button. Enter 0.0.0.0/0 as the destination and select the Internet Gateway that you created earlier as the target.</p>
    <img src="https://aws.amazon.com/images/add-default-route.png" alt="Add Default Route">
    <h2>Step 7: Associate the Subnets with the Route Table</h2>
    <p>Associate the subnets with the route table by selecting the subnets from the Subnet Associations tab and clicking on the Edit button. Select the route table you just created from the Route Table dropdown menu and click on the Savebutton to complete the association.</p>
<img src="https://aws.amazon.com/images/associate-subnets-route-table.png" alt="Associate Subnets with Route Table">
<h2>Step 8: Create an Internet Gateway</h2>
<p>Create an Internet Gateway by clicking on the Internet Gateways link in the navigation panel and then clicking on the Create Internet Gateway button. Enter a name for the Internet Gateway and click on the Yes, Create button to complete the process.</p>
<img src="https://aws.amazon.com/images/create-internet-gateway.png" alt="Create Internet Gateway">
<h2>Step 9: Attach the Internet Gateway to the VPC</h2>
<p>Attach the Internet Gateway to the VPC by selecting the Internet Gateway from the list and clicking on the Attach to VPC button. Select the VPC you created earlier from the VPC dropdown menu and click on the Yes, Attach button to complete the process.</p>
<img src="https://aws.amazon.com/images/attach-internet-gateway-to-vpc.png" alt="Attach Internet Gateway to VPC">
<h2>Conclusion</h2>
<p>You have successfully created a custom VPC in AWS. You can now launch instances into your VPC and configure them to use your custom network settings.</p>

  </body>
</html>


