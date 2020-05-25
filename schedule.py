import datetime

import win32com.client


def schedule():
    scheduler = win32com.client.Dispatch('Schedule.Service')
    scheduler.Connect()
    root = scheduler.GetFolder('\\')
    task = scheduler.NewTask(0)

    # Create trigger
    trigger = task.Triggers.Create(1)
    trigger.StartBoundary = (datetime.datetime.now() + datetime.timedelta(seconds=30)).isoformat()

    # Create action
    TASK_ACTION_EXEC = 0
    action = task.Actions.Create(TASK_ACTION_EXEC)
    action.ID = 'Run demo'
    action.Path = 'cmd.exe'
    action.Arguments = '/c "D:\Personal\Aleksandr_Gonopolskiy\win-task-scheduler\demo.bat"'

    # Set parameters
    task.RegistrationInfo.Description = 'Demo Task'
    task.Settings.Enabled = True
    task.Settings.StopIfGoingOnBatteries = False

    # Register task
    root.RegisterTaskDefinition(
        'DEMO Task',  # Task name
        task,
        6,  # If task already exists, it will be updated
        '',  # No user
        '',  # No password
        0  # Task only if current user is logged in, possible to run when not logged in but requires sys admins to enable log on as batch job for user
    )


if __name__ == "__main__":
    schedule()
