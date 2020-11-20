import os, argparse


"""
Manage labs docker
Author :    ZeR0HoPe
Dependancies :
    - os, argparse
    - docker in OS
Release :   V0.1  10/2020
"""

def manage(args):




    if args.info:
        var1 = "docker inspect -f '=> {{.Name}} - {{.NetworkSettings.IPAddress }}' "
        var2 = '$(docker ps -qa)'
        os.system(var1+var2)

    if args.delete:
        var3 = "docker inspect -f '{{.Name}}' "
        var4 = '$(docker ps -qa)'
        os.system(var3+var4)


## Main call
if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Manage docker')
    parser.add_argument('-i', '--info', help='Information', action="store_true")
    parser.add_argument('-d', '--delete', help='Delete', action="store_true")
    args = parser.parse_args()

    manage(args)
