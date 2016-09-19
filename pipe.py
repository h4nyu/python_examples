
import subprocess
import time

if __name__ == "__main__":
    start_time = time.time()
    proc = subprocess.Popen(comand, 
                    shell = True,
                    stdin = subprocess.PIPE,
                    stdout=subprocess.PIPE,
                    stderr = subprocess.PIPE)

    for proc in procs:
        proc.wait()

    end_time = time.time()

    print(round(end_time - start_time, 2))
