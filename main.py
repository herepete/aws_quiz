#!/usr/bin/python3
import time
import os
os.system('clear')

terminology=[
["What is EBS?","High avaliable ,low latency, attach to servers.Like attacheding a device to your computer at home"],
["What is EFS?","Network storage like a NAS ,can be accessed by multiple machines"],
["What is Dynamo DB?","Amazon no sql database"],
["What is Neptune?","Graph database \n\ngood for things like Fraud detection"],
["What is Cloud formation?","Infrastructure as code, a common language to describe and provision all the infrastructure resources in your environment in a safe, repeatable way.\n\nWorks alongside Aws Service Catalog"],
["What is Aws Config?","Record and evaluate configurations of your AWS resources"],
["What is Aurora?"," a fully managed MySQL- and PostgreSQL-compatible relational database built for the cloud that combines the performance and availability of traditional enterprise databases with the simplicity and cost-effectiveness of open source databases."],
["What is Direct Connect? ","a dedicated network connection to AWS"],
["What is Lambda?","AWS Lambda lets you run code without provisioning or managing servers. You pay only for the compute time you consume—there is no charge when your code is not running"],
["What is Elastic Beanstalk?","an easy-to-use service for deploying and scaling web applications and services\n\n developed with Java, NET, PHP, Node. js, Python, Ruby, Go, and Docker on familiar servers such as Apache, Nginx, Passenger, and IIS."],
["What is OpsWorks? ","OpsWorks lets you use Chef and Puppet to automate how servers are configured, deployed, and managed across your Amazon EC2 instances or on-premises compute environments"],
["What is Redshift?","Amazon Redshift uses SQL to analyze structured and semi-structured data across data warehouses, operational databases, and data lakes, using AWS-designed hardware and machine learning to deliver the best price performance at any scale."],
["What is Amazon Athena?","Amazon Athena is an interactive query service that makes it easy to analyze data in Amazon S3 using standard SQL. Athena is serverless, so there is no infrastructure to manage, and you pay only for the queries that you run."],
["What are Step Functions?","AWS Step Functions is a visual workflow service that helps developers use AWS services to build distributed applications, automate processes, orchestrate microservices, and create data and machine learning (ML) pipelines."],
["What is Kinesis Data Stream?","Amazon Kinesis makes it easy to collect, process, and analyze real-time, streaming data so you can get timely insights and react quickly to new information. "],
["What is SNS?","Amazon Simple Notification Service (Amazon SNS)\n\nis a flexible, fully managed  pub-sub messaging service. What that  means is that you can create a topic,  and users can subscribe to that topic, and  when you publish a message to that topic,  the users that have subscribed to that topic  will receive that message, it can also be used  for push notifications to mobile devices."],
["What is SQS?","Amazon Simple Queue Service (Amazon SQS)\n\nis a fully managed message queuing service and  that makes it easy to decouple your applications  from demand.\n\nWhat that means is that it  allows messages to build up in a queue until the processing server that processes  those messages can catch up with demand."],
["What is SWF?","Amazon simple workflow is a web service that makes it easy to coordinate work across distributed application components,\n\nFor new applications, it is recommended to  use Step Functions"],
["What is SES?","Amazon Simple Email Service (SES) lets you reach customers confidently without an on-premises Simple Mail Transfer Protocol (SMTP) system"],
["What is Lightsail?","Build applications and websites fast with low-cost, pre-configured cloud resources"],
["What is CloudFront?","A CDN, Amazon CloudFront automatically maps network conditions and intelligently routes your user’s traffic to the most performant AWS edge location to serve up cached or dynamic content."],
["What is Amazon Connect?","With Amazon Connect, you can set up a contact center in minutes that can scale to support millions of customers."],
["What is CodeCommit?","Securely host highly scalable private Git repositories and collaborate on code"],
["What is Global Accelerator?","a networking service that helps you improve the availability, performance, and security of your public applications.\n\nIt is commonly used for non-HTTP use cases as oppoase to Cloudfront which typically deals with dynamic content from http"],
["What is Amazon pinpoint ","Connect with customers through scalable, targeted multichannel communications"],
["What is Athena?","Analyze petabyte-scale data where it lives with ease and flexibility.\n\n allows you to analyze data stored  in an Amazon S3 bucket using your standard SQL  statements "],
["What is Quicksight?","is a business  intelligence reporting tool. Similar to tableau,"],
["What is Cloudformation?","provides a common language to describe and provision all the infrastructure resources in your environment in a safe, repeatable way"],
["What is Cloud Watch?","is  a monitoring service for AWS cloud resources and  applications that are deployed on the AWS cloud."],
["What is Aws Service Catalog ?","Create, share, organize, and govern your curated  IaC templates\n\n works alongside cloudformation"],
["What is Aws System Manager?","provides a unified user interface that allows you  to view operational data from multiple AWS  services and to automate tasks across those  AWS resources. "],
["What is CloudTrail?","Track user activity and API usage, good for security"],
["What is Aws Config?","Record and evaluate configurations of your AWS resources \n\nThis greatly simplifies compliance auditing  security analysis, change management and control, "],
["What is Ops Works?","Automate Operations with Chef and Puppet"],
["What is Trusted Adviser?","- provides recommendations that help you follow AWS best practices. Saving cost, better performance and security "],
["What is Step Functions ?","Visual workflows for distributed applications"],
["What is Pinpoint?","allows you to send Email, SMS, and mobile  push messages for targeted marketing campaigns  as well as direct messages to your individual  customers. "],
["What is Finspace?","is a petabyte  scale data management, and analytics service  purpose-built for the financial services industry.  "],
["What is Kinesis?","allows you to collect, process, and analyze  real real-time streaming data."],
["What is Quicksight ?","is a business  intelligence reporting tool. Similar to tableau,"],
["What is Cloud search?","a fully managed search engine service that  supports up to 34 languages. "],
["What is Amazon Open search?"," is a distributed, community-driven, Apache 2.0-licensed, 100% open-source search and analytics suite used for a broad set of use cases like real-time application monitoring, log analytics, and website search."],
["What is DeepLens?","is a deep learning-enabled  video camera. "],
["What is SageMaker?","It allows you to build and train your own  machine learning models and then deploy them to  the AWS cloud and use them as a back end for your applications."],
["What is Amazon Rekogintion?","provides deep  learning-based analysis of video and images.  "],
["What is Amazon Lex?","allows you to build conversational  chatbots. These can be used in many applications,such as first-line support for customers."],
["What is Amazon Polly?","provides natural-sounding text to speech in dozens of Lanaguages."],
["What is Comprehend?","can use deep learning to  analyze text for insights and relationships.\n\nThis can be used for customer analysis or  for advanced searching of documents."],
["What is Translate?","Translate can use machine learning to accurately  translate text to a number of different languages.  "],
["What is Transcribe?","is an automatic speech  recognition service that can analyze audio files  that are stored in Amazon S3 and  then return the transcribed text."],
["What is AWS  Artifact?","is an online portal that provides access  to AWS security and compliance documentation, and that documentation can be readily available  when needed for auditing and compliance purposes"],
["What is AWS Certificate Manager?","Provision and manage SSL/TLS certificates with AWS services and connected resources"],
["What is Amazon Cloud Directory ?","is a  cloud-based directory service that can have  hierarchies of data in multiple dimensions.\n\nUnlike conventional LDAP-based directory  services that can only have a single hierarchy." ],
["What is AWS Directory Service ?","is a fully managed Microsoft  active directory service in the AWS cloud.  "],
["What is AWS CloudHSM ?","is a dedicated hardware security  module in the AWS cloud. "],
["What is Amazon Cognito ?","Implement secure, frictionless customer identity and access management that scales"],
["What is AWS Identity and Access Management (IAM )?","allows you to manage user access to your  AWS services and resources in your account."],
["What is Amazon Inspector?","is an automated  security assessment service"],
["What is AWS Key Management Service (KMS)?","Create and control keys used to encrypt or digitally sign your data"],
["What is AWS Shield  ?","provides protection against distributed denial  of service or DDoS,standard version of is implemented automatically on all AWS accounts "],
["What is Web Application Firewall WAF)?","is a web application firewall that sits infront of your website to provide additional  protection against common attacks such as SQL injection and cross-side scripting."],
["What is AWS Cloud9?","A cloud IDE for writing, running, and debugging code"],
["What is AWS Codestar?","Quickly develop, build, and deploy applications on AWS \n\nmakes  it easy to develop and deploy applications  to AWS. \n\nIt can manage the entire CI/CD pipeline  for you. It has a project management dashboard,  including an integrated issue tracking  capability powered by Atlassian Jira software?"],
["What is X-Ray?","Analyze and debug production and distributed applications \n\nmakes it easy to analyze and debug  applications. \n\nThis provides you with a better  insight to the performance of your application  and the underlying services that it relies upon.  "],
["What is CodeCommit?","Is a git repository just like  GitHub, and it's running in the AWS cloud.  "],
["What is Codebuild?","Build and test code with automatic scaling"],
["What is Codepipeline?","CI/CD"],
["What is CodeDeploy?","Automate code deployment to maintain application uptime"],
["What is Elemental Media Convert?","Process video files to prepare on-demand content for distribution or archiving"],
["What is Elemental MediaLive?"," Encode live video for broadcast and streaming to any device"],
["What is Elemental MediaPackage?","prepares  and protect video content for delivery over the internet.  "],
["What is Elemental MediaStore?","Store and deliver video assets for live streaming media workflows"],
["What is Elemental Media Tailor?","inserts individually targeted advertising into  video streams. "],
["What is Kineses Video Stream?","streams video from connected devices  through to the AWS cloud for analytics machine  learning and other processing applications."],
["What is Aws Mobile Hub?","allows you to easily configure  your AWS services for mobile applications in one  place."],
["What is Aws Device Farm?","is an app testing  service for Android, iOS and web applications.  "],
["What is Aws AppSync?","is a  GraphQL backend for mobile and web applications.  "],
["What is Aws Application Discovery Service?","gathers  information about an enterprise's on-premises  data centers to help plan migration  over to AWS. "],
["What is Aws DataBase Migration Service (DMS)?","orchestrates the  migration of databases over to the AWS cloud. "],
["What is Aws Server Migration Service?","can automate the  migration of thousands of on-premise workloads  over to the AWS cloud. "],
["What is Aws Snowball?","is a portable petabyte-scale data  storage device that can be used to migrate data  from on-premise environments over to the  AWS cloud. "],
["What is Amazon WorkDocs?","is a secure, fully managed file  collaboration and management service in the  AWS cloud."],
["What is Amazon workmail?","is a secure  managed business email and calendar service"],
["What is Amazon Chime?","is an online meeting service in  the AWS cloud. "],
["What is Amazon Workspaces?","is a fully managed secure desktop as a service. "],
["What is Amazon AppStream 2.0 ?","is a  fully managed secure application streaming service  that allows you to stream desktop applications  from AWS to an HTML5 compatible web browser. "],
["What is AWS IOT?","is a managed cloud platform that lets  embedded devices such as Microcontrollers and Raspberry Pi to securely interact with  cloud applications and other devices.  "],
["What is Amazon FreeRTOS?","is an operating system  for microcontrollers such as the microchip  PIC32 that allows small, low-cost, low-power  devices to connect to AWS Internet of Things."],
["What is AWS Greengrass?","Build intelligent IoT devices faster"],
["What is Aws Gamelift?","Dedicated server management for session-based multiplayer games"],
["What is Aws LumberYard?","It's a  game development environment"],
#["What is ?",""],
#["What is ?",""],
#["What is ?",""],

#["",""],
#["",""],
#["",""]
]
questions=[
["What is EBS?","High avaliable ,low latency, attach to servers.Like attacheding a device to your computer at home","Storage"],
["What is EFS?","Network storage like a NAS ,can be accessed by multiple machines","Storage"],
["Which Storage solution offers network like Storage?","EFS (Elastic file system)","Storage"],
["What is the default file system?","EFS","Storage"],
["What is Dynamo DB?","Amazon no sql database","Database"],
["What is Neptune?","Graph database \n\ngood for things like Fraud detection","Database"],
["What is the Amazon no sql database solution?","DynamoDB","Database"],
["What is Cloud formation?","common language to describe and provision all the infrastructure resources in your environment in a safe, repeatable way.","Other"],
["What is CloudWatch?","Observe and monitor resources and applications on AWS, on premises, and on other clouds","Other"],
["What is Aws Config?","Record and evaluate configurations of your AWS resources","Other"],
["What is the difference between SNS and SQS?","\nSNS sends notifications two ways, A2A and A2P.\n    - A2A provides high-throughput, push-based, many-to-many messaging between distributed systems, microservices, and event-driven serverless applications. These applications include Amazon Simple Queue Service (SQS), Amazon Kinesis Data Firehose, AWS Lambda, and other HTTPS endpoints.\n    - A2P functionality lets you send messages to your customers with SMS texts, push notifications, and email. \n\nSQS lets you send, store, and receive messages between software components at any volume, without losing messages or requiring other services to be available.","Other"],
["If you have a bottleneck where a processing server is struggling with a queue what could help?","Simple Queue Service (SQS) \n\nFully managed message queuing for microservices, distributed systems, and serverless applications","Other"],
["What is Aurora?"," a fully managed MySQL- and PostgreSQL-compatible relational database built for the cloud that combines the performance and availability of traditional enterprise databases with the simplicity and cost-effectiveness of open source databases.","Database"],
["What is a relational database?","Amazon Relational Database Service (RDS)\n\nA relational database is a collection of data items with pre-defined relationships between them. These items are organized as a set of tables with columns and rows.","Database"],
["Where would you use a EC2 database over a RDS Database?","if you want full control, you need extra features i.e Oracle feature","Database"],
["Where would you use a RDS database over a EC2 Database?","its highly optimized, \nno dba needed,\nrds deals with backupsi\nrds deals with patching , \nnyou deal with optimization and tuning rather than database admin","Database"],
[""," ","Database"],
["What is difference between Aurora and RDS?","\nAmazon Aurora is a fully managed MySQL- and PostgreSQL-compatible relational database built for the cloud , \nAmazon RDS (Relational Database Service) is a managed SQL database service a relational database in cloud. It supports Aurora, MySQL, PostgreSQL, MariaDB, Microsoft SQL Server, and Oracle database engines.","Database"],
["Which storage should you use if you need a high-performance storage service for a single instance?","EBS Elastic Block Storage\n\nEBS used to be accessible to a single EC2 instance only, making it most like your physical hard drive. That’s still generally how it’s used (as per-instance storage) \nbut in special cases, Amazon EBS Multi-Attach can turn EBS into multi-instance storage, like EFS.\n\nEBS Instances can be either General Purpose SSD (for general use) or Provisioned IOPS SSD, for mission-critical workloads.","Storage"],
["Which storage should you use if you need a shared file storage option for multiple EC2 instances with automatic, high-performance scaling?","EFS \n\ncan be mounted by multiple EC2 instances, meaning many virtual machines may store files within an EFS instance.\n\nIts main feature is its scalability. EFS can grow or shrink according to demand, with more and more files being added without disturbing your application or having to provision new infrastructure. ","Storage"],
["Which Storage should you use for storing long-term data?","S3\n\nS3 is also useful for storing data on which complex queries may be run. This makes it useful for data related to customer purchases, behaviour or profiles, because that data can be easily queried and fed into analytics tools.\n\nThis  capacity for interfacing with other tools also makes S3 great for back-up and restoration, as it can be paired with Amazon Glacier for even more secure backing up.\n\nS3 also supports static websites, so if you need to host a static HTML page, S3 is a good choice.","Storage"],
["What greatly simplifies compliance auditing  security analysis, change management and control,  and also operational troubleshooting?","Aws Config \n\n-Record and evaluate configurations of your AWS resources","Security"],
["If you had a large fleet What could help to shorten the time  to detect and resolve any operational problems?","Aws System Manager \n\n- Gain operational insights into AWS and on-premises resources","Security"],
["How could you Mange infrastructure with Devops?","AWS CloudFormation\n\nSpeed up cloud provisioning with infrastructure as code","Other"],
["What helps with Streamline operational troubleshooting and change management,Deploy a compliance-as-code framework,Continually audit security monitoring and analysis?","AWS Config \n\n Assess, audit, and evaluate configurations of your resources","Other"],
["What helps with Audit activity,Identify security incidents ,Troubleshoot operational issues?","AWS CloudTrail\n\nTrack user activity and api usage","Security"],
["What is the shared responabllity model?","Desciption of the security and compilance model followed\n\nresponabliites vary per service\n\nCustomer responsibility “Security in the Cloud”\nAWS responsibility “Security of the Cloud”","Security"],
["What could monitor application performance or aid in root  cause analysis?","Cloudwatch","Security"],
["What can aid with Centralize operational data , Automatically resolve application issues , Implement best practices , Remediate security events","AWS Systems Manager\n\nGain operational insights into AWS and on-premises resources","Security"],
["What enables you to assess, audit, and  evaluate the configurations of your AWS resources?","Aws Config  \n\n- Record and evaluate configurations of your AWS resources","Security"],
["Which service  can a company use to discover and protect sensitive data that is stored in Amazon S3 buckets","Macie","Security"],
["What can Trusted Adviser do for you?","analyzes your AWS environment and provides best practice recommendations in five categories: \n\nCost optimization, \nfault tolerance, \nperformance, \nservice limits, \nsecurity.","Security"],
["What tool could warn you about security issues i.e open ports or MFA not turned on?","Trusted Adviser","Security"],
["What tool could tell you about potential monthley savings?","Trusted Adviser","Security"],
["What could help appy access control and accelerate proviosing of CI/CD pipelines?","Aws Service Catalog \n\nCreate, share, organize, and govern your curated IaC templates","Other"],
["What provides a unified user interface that allows you  to view operational data from multiple AWS  services and to automate tasks across those  AWS resources?","Aws System Manager","Other"],
["What tool monitors services  & can be used for triggering scaling operation?","Cloud Watch -\n\n Observe and monitor resources and applications on AWS, on premises, and on other clouds, is a monitoring service","Other"],
["What helps  Governance and Compilance by defining what can be deployed in AWS?","Aws Service Catalog \n\nCreate, share, organize, and govern your curated IaC templates","Other"],
["What is the difference between Amazon connect and direct connect","Connect -  service that operates as a Cloud based call centre \\Direct Connect -  you can maintain a dedicated connection between AWS and your on-premise.","Other"],
["What provides managed instances of chef and puppet?","Ops Works\n\nAutomate Operations with Chef and Puppet","Other"],
["What are the 6 advatanges of cloud computing?","\n1)Trade fixed expense for variable expense\n2)Benefit from massive economies of scale\n3)Stop guessing capacity \n4)Increase speed and agility\n5)Stop spending money running and maintaining data centers \n6)Go Global in minutes)","Other"],
["How can you monitor log and API Calls?","CloudTrail\n\nTrack user activity and API usage","Security"],
["What analyze your AWS account  and the resources inside it,  and then it can advise you  on how to best achieve high security and  best performance from those resources?","Trusted Adviser - provides recommendations that help you follow AWS best practices.","Security"],
["What is a git repository just like  GitHub, and it's running in the AWS cloud?","CodeCommit \n\n-Securely host highly scalable private Git repositories and collaborate on code","Development tools"],
["What compiles your source code runs  tests and then produces software packages  that are ready to deploy on AWS?","CodeBuild - Build and test code with automatic scaling","Development tools"],
["What can manage the entire CI/CD pipeline  for you. It has a project management dashboard,  including an integrated issue tracking  capability powered by Atlassian Jira software?","AWS Codestar \n\nQuickly develop, build, and deploy applications on AWS","Development tools"],
["What is a service that automates  software deployments to a variety of compute  services?","Code Deploy \n\n Automate code deployment to maintain application uptime","Development tools"],
["What allows you to deploy servers directly to AWS from an integrated development  environment.","AWS Cloud9 \n\n A cloud IDE for writing, running, and debugging code","Development tools"],
["What provides you with a better  insight to the performance of your application  and the underlying services that it relies upon. Including analyze and debug?","X-Ray -Analyze and debug production and distributed applications","Development tools"],
["What is  an integrated development environment running in  the AWS cloud?","AWS Cloud9 \n\n A cloud IDE for writing, running, and debugging code","Development tools"],
["What can build, test, and then deploy  your code every time a code change occurs?","CodePipeline \n\n Automate continuous delivery pipelines for fast and reliable updates","Development tools"],
["What is Cloud9?","A cloud IDE for writing, running, and debugging code","Development tools - Terminology"],
["What is CodeStar?","Quickly develop, build, and deploy applications on AWS","Development tools - Terminology"],
["What is X-Ray?","Analyze and debug production and distributed applications","Development tools - Terminology"],
["What is Codecommit?","a git repository just like  GitHub, and it's running in the AWS cloud.","Development tools - Terminology"],
["What is CodeBuild?","Build and test code with automatic scaling","Development tools - Terminology"],
["What is CodePipeline?","A CI/CD","Development tools - Terminology"],
["What is Code Deploy?","Automate code deployment to maintain application uptime","Development tools - Terminology"],
["What is Deeplens?","The world’s first deep learning enabled video camera for developers","Machine Learning"],
["What is SageMaker?","It allows you to build and train your own  machine learning models and then deploy them to  the AWS cloud and use them as a back end for your applications.","Machine Learning"],
["What is Amazon Rekogintion?","provides deep  learning-based analysis of video and images.  ","Machine Learning"],
["What is Amazon Lex?","Build chatbots with conversational AI","Machine Learning"],
["What is Amazon Polly?","provides natural-sounding text to speech in dozens of Lanaguages.","Machine Learning"],
["What is Comprehend?","Derive and understand valuable insights from text within documents","Machine Learning"],
["What is Translate?","Fluent and accurate machine translation","Machine Learning"],
["What is Transcribe?","Automatically convert speech to text","Machine Learning"],
["What is the command to get help on S3 CLI?","aws s3 help or aws s3api help","CLI"],
["Which IS is the CLI installed on my default?","Linux AMI not unbuntu ","CLI"],
["Which service provide information on ongoing and upcoming sceduleded events that can effect an aws account?","Aws personal health dashboard","Buisness Case"],
["Which 4 main areas in which AWS customer are realizing value by moving to cloud computing?","Cost Saving\nStaff Productivity\nOperational Resilience\nBuisness Agility","Buisness Case"],
["Order these from cheapest to most expensive. Enterprise,Developer,Business","Developer > Business >Enterprise","Buisness Case"],
["Which sla should you choose if you are expermenting or testing in aws?","Developer","Buisness Case"],
["Which sla should you choose if you have production worloads in aws?","Buisness","Buisness Case"],
["Which sla should you choose if you are business or mission Critical workloads ?","Enterprise","Buisness Case"],
["What does the Concierge support team do ?","help with billing and account inquries & acosiated best practices","Buisness Case"],
["What is a central repo for compilance related information?","Aws Artifact","Arch and Compilance"],
["What is best for Regular audits and setup evaliation for example non compilant account and notificate when a resource changes?","Aws Config","Arch and Compilance"],
["What is AWS config?","AWS Config provides a detailed view of the resources associated with your AWS account, including how they are configured, how they are related to one another, and how the configurations and their relationships have changed over time.","Arch and Compilance"],
["What are the Design principles?","Perform operations as code\nMake frequent, small, reversible changes\nRefine operations procedures frequently\nAnticipate failure\nLearn from all operational failures","Arch and Compilance"],
["Which service can track resource change and establish compilance?","Aws config","Arch and Compilance"],
["What is Loosley coupled Application?","A loosely coupled workload entails the processing of a large number of smaller jobs. Generally, the smaller job runs on one node, either consuming one process or multiple processes with shared memory parallelization (SMP) for parallelization within that node.\n\nLoosely coupled applications are found in many areas, including Monte Carlo simulations, image processing, genomics analysis, and Electronic Design Automation (EDA).","Arch and Compilance"],
["What is Tightly coupled Application?","Tightly coupled applications consist of parallel processes that are dependent on each other to carry out the calculation. Unlike a loosely coupled computation, all processes of a tightly coupled simulation iterate together and require communication with one another.\n\nExamples of tightly coupled HPC workloads include: computational fluid dynamics, weather prediction, and reservoir simulation. ","Arch and Compilance"],
["How much data can i store in s3?","The total volume of data and number of objects you can store in Amazon S3 are unlimited.\n\nIndividual Amazon S3 objects can range in size from a minimum of 0 bytes to a maximum of 5 TB. \nThe largest object that can be uploaded in a single PUT is 5 GB. For objects larger than 100 MB, customers should consider using the multipart upload capability.","S3"],
["What pricing option is best for applications with short-term spiky or unpredicatable workloads","On demand instances","EC2"],
["What pricing option is best for a new customer piloting a customer facing application for one month","On demand instances","EC2"],
["What pricing option is the default?","On-demand","EC2"],
["What pricing option is Good for burst capacity type work and like Ebay for EC2?","Spot instances","EC2"],
["What pricing option is good for a long term 1 or 3 year contract?","Reserved instances","EC2"],
["What pricing option is good for a regular one off event (i.e payroll)?","Scheduled instances","EC2"],
["What pricing option gives you no cost benefit but you have the capacity reserved for you?","On Demand Capacity reservations","EC2"],
["What pricing option gives you a server to yourself?","Dedicated hosts","EC2"],
["What pricing option gives you a single tenant instance which you pay for by the hour?","Dedicated Instances","EC2"],
["What tool could you use to help look at saving you costs","Cost explorer","EC2"],
["What is an EC2 fleet?","An EC2 Fleet contains the configuration information to launch a fleet—or group—of instances.","EC2"],
["What are the 5 Ec2 instance states?","Start\nStop (Ebs backend only)\nStop-Hibernate (EBS Backed only)\nReboot\nTerminate\n\nS.S.S T.(O).R","EC2"],
["Can you stop a non EBS backed instance?","No","EC2"],
["What is the easiest and safest method to connect to an EC2 instance?","EC2 instance connect as everything is being done in the AWS console","EC2"],
["Which service automatically handles application health montioring, load balancing,auto scaling,deployment and proviosing?","Elastic beanstalk","EC2"],
["What attached to an ec2 instance allows a user to use IAM?","role","EC2"],
["What service does A AWS snowball nativley support?","EC2","EC2"],
["What is a fully managed service designed to launch or terminate aws instances automatically?","AWS Auto Scaling","EC2"],
["When would you choose Reserved instances over On Demand?","up to a 75% discount","EC2"],
["What enables you to quickly discover all of the scalable resources underlying your application and set up application scaling in minutes using built-in scaling recommendations.?","AWS Auto scaling","EC2"],
["Why would you use an EC2 auto scaliing group with a website?","a cost-effective approach for ensuring the website is highly available","EC2"],
["What 4 core types of autoscaling exist?","1)Sceulded scaling policy - according to predictable load changes\n2)Predictive scaling - uses daily and weekly trends to determine when to scale.\n3target tracking scaling policy )\n4) step scaling policy - will launch resources in response to demand, this will not ensure the resource are ready at the right time as there will be a delay.","EC2"],
["What do Ops works and Elastic beanstalk have in common?","can be used to deploy applications on aws","Deployment"],
["Which service can be used to privatley store and manage versions of source code?","Codecommit","Deployment"],
["What is CloudEndure?","CloudEndure Disaster Recovery enables organizations to quickly and easily shift their disaster recovery strategy to AWS from existing physical or virtual data centers, private clouds, or other public clouds, in addition to supporting cross-region / cross-AZ disaster recovery in AWS.","Deployment"],
["What is aws outposts?","AWS Outposts is a fully managed service that extends AWS infrastructure, services, APIs, and tools to customer premises. By providing local access to AWS managed infrastructure","Deployment"],
["What service enables userts to monitor for specific phrases, value or patterns and set up alarms based on metrics? ","Amazon Cloudwatch logs","Cloudwatch"],
["How can you monitor the operational health of an entire system of AWS cloud resources to optimize cost and resource usage? ","Amazon Cloudwatch","Cloudwatch"],
["What allows access to an S3 bucket from an ec2 instance without accessing the internt","VPC endpoint\n\n A VPC endpoint enables customers to privately connect to supported AWS services and VPC endpoint services powered by AWS PrivateLink. \nAmazon VPC instances do not require public IP addresses to communicate with resources of the service.\n Traffic between an Amazon VPC and a service does not leave the Amazon network. ","VPC"],
["What must be attached to a VPC to enable inbound internet traffic?","Internet gateway","VPC"],
["What 2 compontents are needed to build a site to site vpn?","Customer Gateway & Virtual Private Gateway","VPC"],
["What 3 items combine to offer the best DDOS protection?","1)Aws Shield \n2)Cloudfront \n3)Route 53","VPC"],
["What 2 items can be used to extend an on premises VPN to the AWS network?","1)AWS Direct Connect \n2)AWS VPN","VPC"],
["What is a use case for VPC peering?","a company with a single aws region with thousands of VPC in various account to interconnect and simpfily managment and cost\n\nA VPC peering connection is a networking connection between two VPCs that enables you to route traffic between them privately. Instances in either VPC can communicate with each other as if they are within the same network. You can create a VPC peering connection between your own VPCs, with a VPC in another AWS account, or with a VPC in a different AWS Region.","Deployment"],
["What are some differences between a VPC VPN & Direct connect?","VPC VPN - uses IPSec to establish an encrypted network between you intranet and amazon vpc over the internet\nDirect connection does not involve the internet instead it uses dedicated private network connections between your intranet and a Amazon VPC","Deployment"],
["Which 2 services can be used to block network traffic to an instance","1)Security Groups-Act as a Firewall for associated EC2 instaces controlling both inbound and outbound traffic at the instance level\n2)Network ACL-control inbound and outbound traffic at the subnet level\nboth act in effect as firewalls","Deployment"],
["Which level does the Network ACL operate at?","Subnet level (As oppose to Security groups which are insatnce level)","Deployment"],
["Which level does the Security Group operate at?","instance level (as oppose to Network ACL which is the subnet level)","Deployment"],
["Which Service can run a managed PostgreSQL database?","RDS","Databases"],
["What are 2 benefits over using RDS over EC2 for relational datbases?","1)Automated backups\n2Software Patching)","Databases"],
["If you wanted to move a EC2 database to a higher avaliability solution. What should you consider?","Migrate to RDS and enable Multi-AZ","Databases"],
["What is the customer responsability for RDS?","Security","Databases"],
["When using RDS according to the shared responsabliity model who is respoisble for Scheduling and performing backups?","Sceduling -customer, performing -AWS","Databases"],
["Which service an ability to host a nosql database?","DynamoDB","Databases"],
["What could you use to consolidate data into one data Warehouse?","Redshift","Databases"],
["What could you use to consolidate data into one data Warehouse?","Redshift","Databases"],
["What could you use to process a large amount of data by making graphical queries with High throughput?","Neptune","Databases"],
["Which acts as a data extra , transform and load (ETL) tool to make it easy to prepare data for analtics?","AWS Glue","Databases"],
["What could you use for dashboards and reporting services?","Amazon quicksight","Databases"],
["What allows S3 backups to another region?","S3 Cross-Region Replication ","S3"],
["What allows Auto cost savings by moving objects between tiers based on access pattern changes?","S3 Intelligient-Tiering","S3"],
["How should as EC2 instance be given access to an S3 bucket?","Create an IAM profile that grants access to S3","S3"],
["What service provides a cost effective solution to storing data for up to 5 years and have it accessable within 48 hours?","S3 Glacier","S3"],
["An archiving system needs to be built to store terabytes of data what the best priced option?","S3 Glacier","S3"],
["What allows you to run one time queries on data in S3?","Amazone Athena","S3"],
["What can help encrypt data stored on S3?","AWS KMS (Key managment service)","S3"],
]

services=[
["Amazon Athena","Analyze petabyte-scale data where it lives with ease and flexibility"],
["Amazon Kinesis","Easily collect, process, and analyze video and data streams in real time\n\nFor Example a Social Media Stream which alongside Lambda could take out the hastags put in a  DB and make them avaliable for users to browse"],
["Amazon QuickSight","a business  intelligence reporting tool. Similar to tableau,"],
["Amazon Simple Notification Service (Amazon SNS)","Amazon Simple Notification Service (Amazon SNS)\n\nis a flexible, fully managed  publish/subscribe messaging service. What that  means is that you can create a topic,  and users can subscribe to that topic, and  when you publish a message to that topic,  the users that have subscribed to that topic  will receive that message, it can also be used  for push notifications to mobile devices"],
["Amazon Simple Queue Service (Amazon SQS)","Amazon Simple Queue Service (Amazon SQS)\n\nis a fully managed message queuing service and  that makes it easy to decouple your applications  from demand.\n\nWhat that means is that it  allows messages to build up in a queue until the processing server that processes  those messages can catch up with demand."],
["AWS Batch","Batch processing, ML model training, and analysis at any scale, \n\nAWS Batch lets developers, scientists, and engineers efficiently run hundreds of thousands of batch and ML computing jobs while optimizing compute resources, so you can focus on analyzing results and solving problems. Use Cases Finanical service analysis,drug testing,train ML models"],
["Amazon EC2",""],
["AWS Elastic Beanstalk","an easy-to-use service for deploying and scaling web applications and services\n\n developed with Java, NET, PHP, Node. js, Python, Ruby, Go, and Docker on familiar servers such as Apache, Nginx, Passenger, and IIS.\n\nSimilar to Lightsail which is a more simple application rather that Beanstalks powerful flexablity on configuration i.e Autoscaling "],
["AWS Lambda","AWS Lambda lets you run code without provisioning or managing servers. You pay only for the compute time you consume—there is no charge when your code is not running\n\nUse case include:\n1)When a photo is uploaded to s3 trigger a lambda function to resize the photo"],
["Amazon Lightsail","Build applications and websites fast with low-cost, pre-configured cloud resources\n\nSimilar to Elastic Beanstalk which offers more flexability i.e Autoscaling on configuration. \nLightsail is a more simple application"],
["Amazon WorkSpaces","is a fully managed secure desktop as a service."],
["Amazon Elastic Container Service (Amazon ECS)","Run highly secure, reliable, and scalable containers"],
["Amazon Elastic Kubernetes Service (Amazon EKS)","The most trusted way to start, run, and scale Kubernetes"],
["AWS Fargate","Serverless compute for containers\n\nIt differs from EC2 in that - Amazon EC2 manages or deploys your own EC2 instances to effectively run applications. \nFargate AWS allows you to run containers without the need for EC2 instances. "],
["Amazon Aurora","a fully managed MySQL- and PostgreSQL-compatible relational database built for the cloud that combines the performance and availability of traditional enterprise databases with the simplicity and cost-effectiveness of open source databases."],
["Amazon DynamoDB","Amazon no sql database"],
["Amazon ElastiCache","Unlock microsecond latency and scale with in-memory caching"],
["Amazon RDS","Amazon Relational Database Service (RDS)\n\nA relational database is a collection of data items with pre-defined relationships between them. These items are organized as a set of tables with columns and rows.\n\nIf you want full control, you need extra features i.e Oracle feature deploy on ec2\n\nAdvantanges include: \n\n1)its highly optimized, \n2)no dba needed,\n3)rds deals with backups\n4)rds deals with patching , \n5)you deal with optimization and tuning rather than database admin\n\n\nYou have 3 options for a database\n1)EC2 -ultimate control\n2)RDS -to reduce the management overhead of running a database in EC2. You click a few buttons, and you get a database ready to store data. Amazon handles all the fiddly bits—provisioning instances, replication and backups, maintenance and updates. \n3)Aurora a cloud-first database. Amazon still handles all the fiddly work of managing the database—but under the hood, it’s quite different.it scales faster,scales further , is more durable,is more resilient.It also works Serverless i.e run Aurora without having to guess how many compute nodes you need. It automatically starts and stops nodes to match the needs of your application. It scales up to meet a spike in demand and scales down when things are quiet.\n\nThe limitations on Aurora it support only 2 database engines where RDS has 5 (including MariaDB,Oracle or Microsfot Sql server)"],
["Amazon Redshift","Amazon Redshift uses SQL to analyze structured and semi-structured data across data warehouses, operational databases, and data lakes, using AWS-designed hardware and machine learning to deliver the best price performance at any scale"],
["AWS CodeBuild","Build and test code with automatic scaling"],
["AWS CodeCommit","Is a git repository just like  GitHub, and it's running in the AWS cloud"],
["AWS CodeDeploy","Automate code deployment to maintain application uptime"],
["AWS CodePipeline","A CI/CD"],
["AWS CodeStar","Quickly develop, build, and deploy applications on AWS. \nIt makes  it easy to develop and deploy applications  to AWS.\n\nIt can manage the entire CI/CD pipeline  for you. It has a project management dashboard,  including an integrated issue tracking  capability powered by Atlassian Jira software."],
["Amazon Connect","With Amazon Connect, you can set up a contact center in minutes that can scale to support millions of customers."],
["AWS Auto Scaling","Application scaling to optimize performance and costs\n\nAWS Auto Scaling monitors your applications and automatically adjusts capacity to maintain steady, predictable performance at the lowest possible cost. \n\nAdvantages \n1)it’s easy to setup application scaling for multiple resources across multiple services in minutes\n2)Make smart scaling decisions\n3)Automatically maintan performance\n4)pay only for what you need "],
["AWS Budgets","AWS Budgets lets you set custom cost and usage budgets that alert you when your budget thresholds are exceeded (or forecasted to exceed)."],
["AWS CloudFormation","provides a common language to describe and provision all the infrastructure resources in your environment in a safe, repeatable way"],
["AWS CloudTrail","Track user activity and API usage, good for security"],
["Amazon CloudWatch","Observe and monitor resources and applications on AWS, on premises, and on other clouds"],
["AWS Config","Record and evaluate configurations of your AWS resources \nThis greatly simplifies compliance auditing  security analysis, change management and control,and also operational troubleshooting.\n\nUse cases:\n1)Discovery -AWS Config will discover resources that exist in your account, record their current configuration and capture any changes to these configurations.\n2)Continous audit and compilance"],
["AWS Cost and Usage Report","contains the most comprehensive set of cost and usage data available. \nYou can use Cost and Usage Reports to publish your AWS billing reports to an Amazon Simple Storage Service (Amazon S3) bucket that you own. \nYou can receive reports that break down your costs by the hour, day, or month, by product or product resource, or by tags that you define yourself."],
["Amazon EventBridge (Amazon CloudWatch Events)","Amazon S3 can send events to Amazon EventBridge whenever certain events happen in your bucket. \n\nEventBridge makes it easier to connect applications. You can ingest, filter, transform and deliver events without writing custom code.\n\na good example is a website with an order service using Eventbridge you can decouple application and services to speed up the process,improve monitoring and make it easy to develop. \n\nhttps://www.youtube.com/watch?v=TXh5oU_yo9M "],
["AWS License Manager","Manage your software licenses and fine-tune licensing costs"],
["AWS Managed Services","in short - AMS is an enterprise service that provides ongoing management of your AWS infrastructure.\n\nAWS Managed Services (AMS) helps you adopt AWS at scale and operate more efficiently and securely. \nAMS extends your team with operational capabilities including monitoring, incident detection and management, security, patch, backup, and cost optimization.\n\n Benefits:\n1)Security - 150+ managed guardrails and security checks\n2)Incident managment - 80% of indidents proactivley detected and notfied\n3)Automation -\n4)Cost Savings\n5)Aws expertise - 24*7 global coverage"],
["AWS Organizations","Centrally manage your environment as you scale your AWS resources"],
["AWS Secrets Manager","Centrally manage the lifecycle of secrets\nAWS Secrets Manager helps you manage, retrieve, and rotate database credentials, API keys, and other secrets throughout their lifecycles."],
["AWS Systems Manager","Really a dashboard to view and manage your resources. \n\nGain operational insights into resources on AWS, on premises, and on other clouds\n\nUse cases:\nCentralize operational data\nAutomatically resolve application issues"],
["AWS Systems Manager Parameter Store","provides secure, hierarchical storage for configuration data management and secrets management. \nYou can store data such as passwords, database strings, Amazon Machine Image (AMI) IDs, and license codes as parameter values. You can store values as plain text or encrypted data. \nYou can reference Systems Manager parameters in your scripts, commands, SSM documents, and configuration and automation workflows by using the unique name that you specified when you created the parameter"],
["AWS Trusted Advisor","Reduce costs, improve performance, improve security"],
["Amazon API Gateway","Create, maintain, and secure APIs at any scale"],
["Amazon CloudFront","Amazon CloudFront is a content delivery network (CDN) service that helps you distribute your static and dynamic content quickly and reliably with high speed"],
["AWS Direct Connect","AWS Direct Connect is a cloud service that links your network directly to AWS to deliver consistent, low-latency performance."],
["Amazon Route 53","dns"],
["Amazon VPC","Amazon Virtual Private Cloud (Amazon VPC) enables you to launch AWS resources into a virtual network that you've defined."],
["AWS Artifact","Access AWS and ISV security and compliance reports"],
["AWS Certificate Manager (ACM)","Provision and manage SSL/TLS certificates with AWS services and connected resources\n\nACM removes the time-consuming manual process of purchasing, uploading, and renewing SSL/TLS certificates."],
["AWS CloudHSM","Provision and manage SSL/TLS certificates with AWS services and connected resources"],
["Amazon Cognito","Amazon Cognito provides authentication, authorization, and user management for your web and mobile apps. \n\nYour users can sign in directly with a user name and password, or through a third party such as Facebook, Amazon, Google or Apple."],
["Amazon Detective","Analyze and visualize security data to investigate potential security issues"],
["Amazon GuardDuty","Protect your AWS accounts with intelligent threat detection"],
["AWS Identity and Access Management (IAM)","Securely manage identities and access to AWS services and resources"],
["Amazon Inspector","Automated and continual vulnerability management at scale that continually scans AWS workloads for software vulnerabilities and unintended network exposure."],
["AWS License Manager","Manage your software licenses and fine-tune licensing costs"],
["Amazon Macie","Discover and protect your sensitive data at scale.\n\nAmazon Macie is a data security service that uses machine learning (ML) and pattern matching to discover and help protect your sensitive data."],
["AWS Shield","Maximize application availability and responsiveness with managed DDoS protection"],
["AWS WAF","Protect your web applications from common exploits"],
["AWS Backup","AWS Backup is a fully-managed service that makes it easy to centralize and automate data protection across AWS services, in the cloud, and on premises.\n\nUsing this service, you can configure backup policies and monitor activity for your AWS resources in one place."],
["Amazon Elastic Block Store (Amazon EBS)","Easy to use, high performance block storage at any scale\n\nDefault Filesytem\n\nIts Cousin EFS offers network like storage"],
["Amazon Elastic File System (Amazon EFS)","Serverless, fully elastic file storage\n\nautomatically grows and shrinks as you add and remove files with no need for management or provisioning.\n\nOffers Network like Storage"],
["Amazon S3","Amazon Simple Storage Service (Amazon S3) is an object storage service offering industry-leading scalability, data availability, security, and performance."],
["Amazon S3 Glacier","Long-term, secure, durable storage classes for data archiving at the lowest cost and milliseconds access"],
["AWS Snowball Edge","AWS Snowball Edge is a type of Snowball device with on-board storage and compute power for select AWS capabilities. Snowball Edge can do local processing and edge-computing workloads in addition to transferring data between your local environment and the AWS Cloud."],
["AWS Storage Gateway","AWS Storage Gateway is a set of hybrid cloud storage services that provide on-premises access to virtually unlimited cloud storage."],
#["What service enables userts to monitor for specific phrases, value or patterns and set up alarms based on metrics? ","Amazon Cloudwatch logs","Cloudwatch"]
#["How can you monitor the operational health of an entire system of AWS cloud resources to optimize cost and resource usage? ","Amazon Cloudwatch","Cloudwatch"]
#["AWS Storage Gateway","""],
#["AWS Storage Gateway","AWS Storage Gateway is a set of hybrid cloud storage services that provide on-premises access to virtually unlimited cloud storage."],
#["AWS Storage Gateway","AWS Storage Gateway is a set of hybrid cloud storage services that provide on-premises access to virtually unlimited cloud storage."],
#["AWS Storage Gateway","AWS Storage Gateway is a set of hybrid cloud storage services that provide on-premises access to virtually unlimited cloud storage."],
#["AWS Storage Gateway","AWS Storage Gateway is a set of hybrid cloud storage services that provide on-premises access to virtually unlimited cloud storage."],

]




import random
random.shuffle(questions)
random.shuffle(terminology)
random.shuffle(services)
#sleep_time=1
number_of_questions=len(questions)
number_of_terminology=len(terminology)
number_of_services=len(services)
count=1

print (f"Do you want a test on services(s) , Questions={number_of_services}")
print (f"a more focused set of questions (f) ")

user_input=input("")
sleep_time=int(input("please enter the number of seconds you want to sleep for between question and answer?"))

if user_input=="s":

    try_again=[]
    for i in services:
        os.system('clear')
        print ("Quesion - ",count,"/",number_of_services)
        count+=1
        print("=========")
        print ("# Question - ", i[0])
        time.sleep(sleep_time)
        print ("# Answer - ", i[1])
        print()
        print()
        print()
        user_result=input("Did you get that right(y/n) (default=n)")
        if user_result!="y":
            temp_list=[i[0],i[1]]
            try_again.append(temp_list)
        input("....press enter to continue.......")
        print()
    print("Here is a second go at those questions you struggled with")
    input("Press any button to continue")
    number_of_try_again=len(try_again)
    you_need_to_work_on=[]
    count_try_again=1
    for j in try_again:
        os.system('clear')
        print ("Quesion - ",count_try_again,"/",number_of_try_again)
        count_try_again+=1
        print("=========")
        print ("# Question - ", j[0])
        time.sleep(sleep_time)
        print ("# Answer - ", j[1])
        print()
        print()
        print()
        user_result2=input("Did you get that right(y/n) (default=n) ")
        if user_result2!="y":
            temp_list=[j[0],j[1]]
            you_need_to_work_on.append(temp_list)
    print()
    print("Summary")
    print("=======")
    print ("This is the end of the test")
    first_round=number_of_services-number_of_try_again
    print (f"There were  {number_of_services} questions")
    print(f"First round you got {first_round} correct")
    second_round=number_of_try_again-len(you_need_to_work_on)
    print (f"Second round you got {second_round} correct")
    to_work_on=len(you_need_to_work_on)
    print ()
    if to_work_on >0:
        print (f"These are the focus areas as you got these {to_work_on} wrong twice")
        print()
        for k in you_need_to_work_on:
            print ("=========")
            print (k[0])
            print (k[1][:150])
    else:
        print ("Congrats you did well, no extra revision needed :)")


elif user_input=="f":
    section_already_worked_on=[]
    while True:
        list_of_sections=[]
        for i in questions:
            try:
                list_of_sections.append(i[2])
            except:
                pass
        unique_sections=set(list_of_sections)
        count=0
        for j in unique_sections:
            count_instances=0
            for k in list_of_sections:
                if k == j:
                    count_instances+=1
            if j in section_already_worked_on:
                print (count,end=" ")
                #this makes the output green
                print("\033[1;32;40m",j,end=" ")
                print ("Questions=",count_instances," -Done",end="")
                #this makes the output black again
                print("\033[0;37;40m")
            else:
                print (count,end=" ")
                #this makes the output "normal"
                print("\033[0;37;40m",j,end=" ")
                print ("Questions=",count_instances)
            count+=1

        #this print clears down any oustanding colour formatting before continuning
        print("\033[0;37;40m",end=" ")
        user_input_section_choice_num=int(input("enter a number to check..."))
        user_input_section_choice_word_list=list(unique_sections)
        user_input_section_choice_word=user_input_section_choice_word_list[user_input_section_choice_num]
        section_already_worked_on.append(user_input_section_choice_word)
        for all in questions:
            try:
                #breakpoint()
                if all[2] == user_input_section_choice_word:
                    os.system('clear')
                    print ("Section -",all[2])
                    print("=========")
                    print ("# Question - ", all[0])
                    time.sleep(sleep_time)
                    print ("# Answer - ", all[1])
                    print()
                    print()
                    print()
                    input("....press enter to continue.......")
                    print()
            except:
                pass

    
else: 
    print ("Invalid input")

