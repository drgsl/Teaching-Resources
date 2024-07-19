import subprocess




def RunProcess(command:str,
               arguments:str = ""):

    process = subprocess.Popen(command, shell=True, text=True, 
    stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    print("out:" + process.stdout.read())

    print("err:" + process.stderr.read())

    return process.stdout.read()
 


    



RunProcess("python -m pyroGamer.Runner.GUI.Hub.Tester --Test")
    
