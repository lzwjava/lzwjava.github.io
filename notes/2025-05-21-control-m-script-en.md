---
title: Control-M Script
lang: en
layout: post
audio: false
translated: false
generated: true
---

I'll provide a comprehensive Control-M script example that demonstrates common job definitions, scheduling, and dependencies. Control-M scripts are typically written in XML or JSON format for job definitions. Below is an example of a Control-M job flow in XML format, showcasing a variety of features like job types, scheduling, dependencies, and notifications.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<DEFTABLE>
  <!-- Defining a folder for organizing jobs -->
  <FOLDER DATACENTER="PRIMARY_DC" NAME="Finance_Processing">
    <VARIABLES>
      <VARIABLE NAME="%%ENVIRONMENT" VALUE="PROD"/>
      <VARIABLE NAME="%%BASE_PATH" VALUE="/app/finance"/>
    </VARIABLES>

    <!-- Job 1: File Transfer Job -->
    <JOB NAME="Transfer_Daily_Transactions" APPLICATION="Finance" SUB_APPLICATION="Daily">
      <DESCRIPTION>Transfers daily transaction files from source to processing directory</DESCRIPTION>
      <TASKTYPE>FileTransfer</TASKTYPE>
      <HOST>ftpserver01</HOST>
      <RUN_AS>finance_user</RUN_AS>
      <COMMAND>
        sftp get /source/transactions/daily_%%DATE%%.csv %%BASE_PATH%%/input/
      </COMMAND>
      <SCHEDULING>
        <DAYS>ALL</DAYS>
        <TIMEFROM>0100</TIMEFROM>
        <TIMETO>0200</TIMETO>
      </SCHEDULING>
      <NOTIFY>
        <ON_STATUS STATUS="ENDED OK">
          <ACTION TYPE="EMAIL">
            <TO>finance_team@company.com</TO>
            <SUBJECT>Daily Transactions Transferred</SUBJECT>
            <MESSAGE>File transfer completed successfully for %%DATE%%</MESSAGE>
          </ACTION>
        </ON_STATUS>
        <ON_STATUS STATUS="ENDED NOTOK">
          <ACTION TYPE="EMAIL">
            <TO>admin@company.com</TO>
            <SUBJECT>ALERT: File Transfer Failed</SUBJECT>
            <MESSAGE>File transfer failed for %%DATE%%. Please investigate.</MESSAGE>
          </ACTION>
        </ON_STATUS>
      </NOTIFY>
    </JOB>

    <!-- Job 2: Data Processing Job -->
    <JOB NAME="Process_Transactions" APPLICATION="Finance" SUB_APPLICATION="Daily">
      <DESCRIPTION>Processes daily transaction files</DESCRIPTION>
      <TASKTYPE>Command</TASKTYPE>
      <HOST>appserver01</HOST>
      <RUN_AS>finance_user</RUN_AS>
      <COMMAND>
        python %%BASE_PATH%%/scripts/process_transactions.py --input %%BASE_PATH%%/input/daily_%%DATE%%.csv --output %%BASE_PATH%%/output/
      </COMMAND>
      <INCOND NAME="Transfer_Daily_Transactions_OK" ODATE="%%DATE%%" AND_OR="AND"/>
      <SCHEDULING>
        <DAYS>ALL</DAYS>
        <TIMEFROM>0230</TIMEFROM>
        <TIMETO>0400</TIMETO>
      </SCHEDULING>
      <VARIABLES>
        <VARIABLE NAME="%%INPUT_FILE" VALUE="daily_%%DATE%%.csv"/>
      </VARIABLES>
      <ON>
        <DO>
          <DOACTION TYPE="SetVariable" NAME="%%PROCESS_STATUS" VALUE="COMPLETED"/>
        </DO>
        <DO_STATUS STATUS="ENDED NOTOK">
          <DOACTION TYPE="Rerun"/>
          <DOACTION TYPE="EMAIL">
            <TO>admin@company.com</TO>
            <SUBJECT>ALERT: Transaction Processing Failed</SUBJECT>
            <MESSAGE>Processing failed for %%INPUT_FILE%%</MESSAGE>
          </DOACTION>
        </DO_STATUS>
      </ON>
    </JOB>

    <!-- Job 3: Database Update Job -->
    <JOB NAME="Update_Database" APPLICATION="Finance" SUB_APPLICATION="Daily">
      <DESCRIPTION>Updates database with processed transactions</DESCRIPTION>
      <TASKTYPE>Database</TASKTYPE>
      <HOST>dbserver01</HOST>
      <RUN_AS>db_user</RUN_AS>
      <CONNECTION_PROFILE>ORACLE_FINANCE</CONNECTION_PROFILE>
      <STATEMENT>
        <![CDATA[
          INSERT INTO transactions
          SELECT * FROM processed_transactions
          WHERE process_date = '%%DATE%%'
        ]]>
      </STATEMENT>
      <INCOND NAME="Process_Transactions_OK" ODATE="%%DATE%%" AND_OR="AND"/>
      <SCHEDULING>
        <DAYS>ALL</DAYS>
        <TIMEFROM>0430</TIMEFROM>
        <TIMETO>0600</TIMETO>
      </SCHEDULING>
      <QUANTITATIVE_RESOURCE NAME="DB_CONNECTIONS" QUANTITY="2"/>
      <ON>
        <DO_STATUS STATUS="ENDED OK">
          <DOACTION TYPE="SetVariable" NAME="%%DB_UPDATE_STATUS" VALUE="SUCCESS"/>
        </DO_STATUS>
        <DO_STATUS STATUS="ENDED NOTOK">
          <DOACTION TYPE="StopCyclic"/>
          <DOACTION TYPE="EMAIL">
            <TO>db_admin@company.com</TO>
            <SUBJECT>ALERT: Database Update Failed</SUBJECT>
            <MESSAGE>Database update failed for %%DATE%%</MESSAGE>
          </DOACTION>
        </DO_STATUS>
      </ON>
    </JOB>

    <!-- Control-M Flow Control -->
    <FLOW NAME="Daily_Finance_Flow">
      <INCOND NAME="Transfer_Daily_Transactions_OK" ODATE="%%DATE%%"/>
      <OUTCOND NAME="Daily_Finance_Complete" ODATE="%%DATE%%"/>
      <STEP JOB_NAME="Transfer_Daily_Transactions"/>
      <STEP JOB_NAME="Process_Transactions"/>
      <STEP JOB_NAME="Update_Database"/>
    </FLOW>

    <!-- Cyclic Job Example -->
    <JOB NAME="Monitor_Disk_Space" APPLICATION="Finance" SUB_APPLICATION="Monitoring">
      <DESCRIPTION>Monitors disk space every hour</DESCRIPTION>
      <TASKTYPE>Command</TASKTYPE>
      <HOST>appserver01</HOST>
      <RUN_AS>sysadmin</RUN_AS>
      <COMMAND>
        df -h %%BASE_PATH%% | grep -v Filesystem | awk '{print $5}' | mail -s "Disk Space Report" admin@company.com
      </COMMAND>
      <CYCLIC>
        <INTERVAL TYPE="MINUTES" VALUE="60"/>
      </CYCLIC>
      <SCHEDULING>
        <DAYS>ALL</DAYS>
        <TIMEFROM>0000</TIMEFROM>
        <TIMETO>2359</TIMETO>
      </SCHEDULING>
    </JOB>
  </FOLDER>
</DEFTABLE>
```

### Explanation of the Control-M Script
This script defines a folder named `Finance_Processing` with several jobs that form a daily financial processing workflow:
1. **Transfer_Daily_Transactions**: A file transfer job that retrieves daily transaction files via SFTP.
2. **Process_Transactions**: A command job that processes the transferred files using a Python script, dependent on the successful completion of the file transfer.
3. **Update_Database**: A database job that updates an Oracle database with processed data, dependent on the processing job.
4. **Monitor_Disk_Space**: A cyclic job that runs every hour to monitor disk space.

### Key Features
- **Dependencies**: Uses `INCOND` to ensure jobs run in sequence (e.g., processing waits for file transfer completion).
- **Scheduling**: Jobs are scheduled daily with specific time windows.
- **Notifications**: Email alerts for success and failure scenarios.
- **Variables**: Environment and file path variables for reusability.
- **Flow Control**: A `FLOW` element to define the sequence of job execution.
- **Cyclic Job**: A monitoring job that runs hourly.
- **Resource Management**: Limits database connections using `QUANTITATIVE_RESOURCE`.

This script is designed to be imported into a Control-M environment and can be customized further based on specific requirements, such as additional job types or conditions. If you need modifications or have a specific use case, let me know!