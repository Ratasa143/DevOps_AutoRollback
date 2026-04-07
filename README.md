Overview

This project demonstrates a simplified DevOps pipeline using Python. It automates deployment, continuously monitors application health, detects failures, and performs automatic rollback to a stable version.

The system simulates real-world DevOps practices used to maintain application reliability during faulty deployments.

 Objectives

-Automate application deployment
-Monitor application health in real-time
-Detect failures (HTTP errors or crashes)
-Trigger automatic rollback to stable version
-Maintain logs for all operations

Technologies Used
Python
Flask
Requests library
Logging module
File handling (shutil, os)


Project Structure
devops-auto-rollback/

│
├── app/
│   └── app.py
│
├── versions/
│   ├── v1/
│   └── v2/
│
├── deploy.py
├── monitor.py
├── rollback.py
├── requirements.txt
└── README.md


How It Works
A version (v1 or v2) is deployed using deploy.py
The Flask application starts running
monitor.py continuously checks the app health
If a failure is detected (status ≠ 200), rollback is triggered
rollback.py restores the stable version (v1)
Setup and Execution

Step 1: Install dependencies

pip install -r requirements.txt

Step 2: Deploy a version

python deploy.py

Enter:

v1 → Stable version
v2 → Buggy version

Step 3: Run the application

python app/app.py

Step 4: Start monitoring (open new terminal)

python monitor.py
Auto Rollback Flow
Monitor checks app every 5 seconds
If app returns error (500) or crashes
Rollback is automatically triggered
Stable version is restored
Failure Simulation
v1: Stable version (returns 200 OK)
v2: Buggy version (returns 500 error or crashes)
Output
deploy.log (deployment logs)
monitor.log (monitoring logs)
rollback.log (rollback logs)
Console messages showing failure and rollback


Learning Outcomes
Understanding CI/CD pipeline basics
Implementing monitoring systems
Handling failures in production
Automating rollback mechanisms
Conclusion

This project demonstrates core DevOps concepts like automation, monitoring, and fault recovery using a simple Python-based system.