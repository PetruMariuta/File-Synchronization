import os
import time
from apscheduler.schedulers.background import BlockingScheduler
import argparse



parser = argparse.ArgumentParser()
parser.add_argument('--source', type=str, help='path to source folder')
parser.add_argument('--replica', type=str, help='path to replica folder')
parser.add_argument('--interval', type=int, help='synchronization interval in seconds')
parser.add_argument('--log', type=str, help='path to log file')
args = parser.parse_args()

source = args.source
replica_folder_path = args.replica
interval2 = args.interval
log_file = args.log

#source = r"C:\FACULTATE\python\projects\filesync\source"
#replica_folder_path = r"C:\FACULTATE\python\projects\filesync\replica"


#delete everything from the replica file before copying
def clean_replica(replica_folder_path):
    for i in os.listdir(replica_folder_path):
        replica_path = os.path.join(replica_folder_path, i)
        #print(replica_path)
        
        try:
            if os.path.isfile(replica_path):
                os.unlink(replica_path)
            elif os.path.isdir(replica_path):
                os.rmdir(replica_path)
        except Exception as error:
            print(f"Failed to delete {replica_path} due to {error}")

    print(f"\nReplica folder cleaning performed at {local_time}")

    #write to logs
    
    with open(log_file , "a") as f:
            f.write(f"\nReplica folder cleaning performed at {local_time}")



def file_syncro():
    
    global source, replica_folder_path, local_time
    local_time = time.strftime("%H:%M:%S")

    clean_replica(replica_folder_path)

    
    #print(os.getcwd())
    
    os.system(f'xcopy {source} {replica_folder_path} /E /I /Y')
    # /E flag specifies to copy all subdirectories (including empty ones) 
    # /I flag specifies that the destination should be treated as a dir
    # /Y flag specifies to suppress the "confirm" to overwrite an existing file

    print(f"File synchronization performed at {local_time}")
    
    #write to logs
    with open(log_file , "a") as f:
        f.write(f"\nFile synchronization performed at {local_time}")
     


  
scheduler = BlockingScheduler()
scheduler.add_job(file_syncro, 'interval', seconds=interval2)
scheduler.start()

#Command copy-paste:
#python synchronization.py --source C:\FACULTATE\python\projects\filesync\source --replica C:\FACULTATE\python\projects\filesync\replica --interval 5 --log C:\FACULTATE\python\projects\filesync\logs.txt