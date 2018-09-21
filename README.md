# Website-Blocker
This is a Website Blocker which will prevent you from accessing unnecessary websites during your working hours.

To run on Windows:
  Method I:
    1. Open Task Scheduler
    2. Create a new task
    3. Name the task and click on Run with highest priviliges
    4. Click on Triggers -> New -> Begin The Task -> On startup
    5. Click on Actions -> New -> Add the path to the script
    6. Click on Conditionds and uncheck Start the task only if the computer is on AC power
    7. Click on Ok
    8. Restart the computer
    
  Method II:
    1. Open Command Prompt as an Administrator
    2. Run the script from the command line
    
Method I will run the script as a process while Method II will not.
