#!/usr/bin/python3
import time
import os
os.system('clear')

terminology=[
["What is EBS?","High avaliable ,low latency, attach to servers.Like attacheding a device to your computer at home"],
["What is EFS?","Network storage like a NAS ,can be accessed by multiple machines"],
["What is Dynamo DB?","Amazon no sql database"],
["What is Neptune?","Graph database \n\ngood for things like Fraud detection"],
["What is Cloud formation?","common language to describe and provision all the infrastructure resources in your environment in a safe, repeatable way."],
["What is Aws Config?","Record and evaluate configurations of your AWS resources"],
["What is Aurora?"," a fully managed MySQL- and PostgreSQL-compatible relational database built for the cloud that combines the performance and availability of traditional enterprise databases with the simplicity and cost-effectiveness of open source databases."],
["What is Direct Connect? ","a dedicated network connection to AWS"],
["What is Lambda?","AWS Lambda lets you run code without provisioning or managing servers. You pay only for the compute time you consume—there is no charge when your code is not running"],
["What is Elastic Beanstalk?","AWS Elastic Beanstalk is an easy-to-use service for deploying and scaling web applications and services developed with Java, NET, PHP, Node. js, Python, Ruby, Go, and Docker on familiar servers such as Apache, Nginx, Passenger, and IIS."],
["What is OpsWorks? ","OpsWorks is an application-management service that makes it easy for both developers and operations personnel to deploy and operate applications of all shapes and sizes"],
["What is Redshift?","Amazon Redshift uses SQL to analyze structured and semi-structured data across data warehouses, operational databases, and data lakes, using AWS-designed hardware and machine learning to deliver the best price performance at any scale."],
["What is Amazon Athena?","Amazon Athena is an interactive query service that makes it easy to analyze data in Amazon S3 using standard SQL. Athena is serverless, so there is no infrastructure to manage, and you pay only for the queries that you run."],
["What are Step Functions?","AWS Step Functions is a visual workflow service that helps developers use AWS services to build distributed applications, automate processes, orchestrate microservices, and create data and machine learning (ML) pipelines."],
["What is Kinesis Data Stream?","Amazon Kinesis makes it easy to collect, process, and analyze real-time, streaming data so you can get timely insights and react quickly to new information. "],
["What is SNS?","Amazon Simple Notification Service (Amazon SNS)"],
["What is SQS?","Amazon Simple Queue Service (Amazon SQS)"],
["What is SES?","Amazon Simple Email Service (SES) lets you reach customers confidently without an on-premises Simple Mail Transfer Protocol (SMTP) system"],
["What is Lightsail?","Build applications and websites fast with low-cost, pre-configured cloud resources"],
["What is CloudFront?","Amazon CloudFront automatically maps network conditions and intelligently routes your user’s traffic to the most performant AWS edge location to serve up cached or dynamic content."],
["What is Amazon Connect?","With Amazon Connect, you can set up a contact center in minutes that can scale to support millions of customers."],
["What is CodeCommit?","Securely host highly scalable private Git repositories and collaborate on code"],
["What is Global Accelerator?",""],
#["What is ",""],
#["What is ",""],
#["What is ",""],
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
["What is difference between Aurora and RDS?","\nAmazon Aurora is a fully managed MySQL- and PostgreSQL-compatible relational database built for the cloud , \nAmazon RDS (Relational Database Service) is a managed SQL database service a relational database in cloud. It supports Aurora, MySQL, PostgreSQL, MariaDB, Microsoft SQL Server, and Oracle database engines.","Database"],
["Which storage should you use if you need a high-performance storage service for a single instance?","EBS Elastic Block Storage\n\nEBS used to be accessible to a single EC2 instance only, making it most like your physical hard drive. That’s still generally how it’s used (as per-instance storage) \nbut in special cases, Amazon EBS Multi-Attach can turn EBS into multi-instance storage, like EFS.\n\nEBS Instances can be either General Purpose SSD (for general use) or Provisioned IOPS SSD, for mission-critical workloads.","Storage"],
["Which storage should you use if you need a shared file storage option for multiple EC2 instances with automatic, high-performance scaling?","EFS \n\ncan be mounted by multiple EC2 instances, meaning many virtual machines may store files within an EFS instance.\n\nIts main feature is its scalability. EFS can grow or shrink according to demand, with more and more files being added without disturbing your application or having to provision new infrastructure. ","Storage"],
["Which Storage should you use for storing long-term data?","S3\n\nS3 is also useful for storing data on which complex queries may be run. This makes it useful for data related to customer purchases, behaviour or profiles, because that data can be easily queried and fed into analytics tools.\n\nThis  capacity for interfacing with other tools also makes S3 great for back-up and restoration, as it can be paired with Amazon Glacier for even more secure backing up.\n\nS3 also supports static websites, so if you need to host a static HTML page, S3 is a good choice.","Storage"],
["What greatly simplifies compliance auditing  security analysis, change management and control,  and also operational troubleshooting?","Aws Config \n\n-Record and evaluate configurations of your AWS resources","Security"],
["If you had a large fleet What could help to shorten the time  to detect and resolve any operational problems?","Aws System Manager \n\n- Gain operational insights into AWS and on-premises resources","Security"],
["How could you Mange infrastructure with Devops?","AWS CloudFormation\n\nSpeed up cloud provisioning with infrastructure as code","Other"],
["What helps with Streamline operational troubleshooting and change management,Deploy a compliance-as-code framework,Continually audit security monitoring and analysis?","AWS Config \n\n Assess, audit, and evaluate configurations of your resources","Other"],
["What helps with Audit activity,Identify security incidents ,Troubleshoot operational issues?","AWS CloudTrail\n\nTrack user activity and api usage","Security"],
["What could monitor application performance or aid in root  cause analysis?","Cloudwatch","Security"],
["What can aid with Centralize operational data , Automatically resolve application issues , Implement best practices , Remediate security events","AWS Systems Manager\n\nGain operational insights into AWS and on-premises resources","Security"],
["What enables you to assess, audit, and  evaluate the configurations of your AWS resources?","Aws Config  \n\n- Record and evaluate configurations of your AWS resources","Security"],
["What could help appy access control and accelerate proviosing of CI/CD pipelines?","Aws Service Catalog \n\nCreate, share, organize, and govern your curated IaC templates","Other"],
["What provides a unified user interface that allows you  to view operational data from multiple AWS  services and to automate tasks across those  AWS resources?","Aws System Manager","Other"],
["What tool monitors services  & can be used for triggering scaling operation?","Cloud Watch -\n\n Observe and monitor resources and applications on AWS, on premises, and on other clouds, is a monitoring service","Other"],
["What helps  Governance and Compilance by defining what can be deployed in AWS?","Aws Service Catalog \n\nCreate, share, organize, and govern your curated IaC templates","Other"],
["What provides managed instances of chef and puppet?","Ops Works\n\nAutomate Operations with Chef and Puppet","Other"],
["How can you monitor log and API Calls?","CloudTrail\n\nTrack user activity and API usage","Security"],
["What analyze your AWS account  and the resources inside it,  and then it can advise you  on how to best achieve high security and  best performance from those resources?","Trusted Adviser - provides recommendations that help you follow AWS best practices.","Security"],
#["",""],
#["",""],
#["",""],
#["",""],
]



import random
random.shuffle(questions)
random.shuffle(terminology)
sleep_time=5
number_of_questions=len(questions)
number_of_terminology=len(terminology)
count=1

user_input=input("Do you want terminology(t) , all Questions(non Terminology) (a) or a subset(s)")

if user_input=="t":

    for i in terminology:
        os.system('clear')
        print ("Quesion - ",count,"/",number_of_terminology)
        count+=1
        print("=========")
        print ("# Question - ", i[0])
        time.sleep(sleep_time)
        print ("# Answer - ", i[1])
        print()
        print()
        print()
        input("....press enter to continue.......")
        print()


elif user_input=="a":

    #breakpoint()
    for i in questions:
        os.system('clear')
        print ("Quesion - ",count,"/",number_of_questions)
        count+=1
        print("=========")
        print ("# Question - ", i[0])
        time.sleep(sleep_time)
        print ("# Answer - ", i[1])
        print()
        print()
        print()
        input("....press enter to continue.......")
        print()
elif user_input=="s":
    print ("S pressed")
    list_of_sections=[]
    for i in questions:
        try:
           list_of_sections.append(i[2])
        except:
            pass
    unique_sections=set(list_of_sections)
    count=0
    for j in unique_sections:
        print (count," ",j)
        count+=1

    user_input_section_choice_num=int(input("enter a number to check..."))
    user_input_section_choice_word_list=list(unique_sections)
    user_input_section_choice_word=user_input_section_choice_word_list[user_input_section_choice_num]
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

