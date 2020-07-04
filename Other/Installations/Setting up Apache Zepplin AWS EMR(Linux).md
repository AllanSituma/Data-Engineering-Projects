#Setting up Apache Zepplin AWS (Linux)

#Prequisites

1. Set up a free tier AWS account
2. Download Key pair for ssh
3. Login to AWS manager console
4. Go to services -> EMR -> Create Cluster
5. Follow instructions to set up
6. After set up, click Enable Services in Web (Cluster)
7. Go to security and access -> Security groups for Master
8. Click on security group ID for ElasticMapReduce-master
9. Edit inbound rules
10. Add rule, Type->SSH, Source-> MyIP, Save Rules
11. Download foxyproxy -> https://chrome.google.com/webstore/detail/foxyproxy-standard/gcknhkkoolaabfmlnjonogaaifnjlfnp
12. Install and restart chrome
13. Follow next steps in AWS!