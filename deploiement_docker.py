import os, argparse
import time


"""
Deploiement labs docker
Author :    Matthieu DEBRAY
Dependancies :
    - os, argparse
    - docker and ansible in OS
Release :   V0.1  10/2020
"""



def deploy(args):

    dict={}
    dict["count"] = args.count
    dict["container_name"] = args.name
    dict["container_image"] = args.docker
    ans = """
        ansible-playbook -i ./ansible/hosts ./ansible/playbook.yml --extra-vars '{}'
    """.format(dict)
    os.system(ans)
    time.sleep(2)


    for i in range(1,int(args.count)+1,1):

        var1 = "docker inspect -f '=> {{.Name}} - {{.NetworkSettings.IPAddress }}' "
        var2 = (args.name)+str(i)
        var3 = "docker inspect -f '{{.NetworkSettings.IPAddress }}' "
        # Clean hots ip in ssh
        # var4 = os.popen(var3+var2).read()
        # os.system('ssh-keygen -R {}'.format(var4))
        os.system(var1+var2)



## Main call
if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Deploiement docker')
    parser.add_argument('-c', '--count', help='Docker', type=str, required=True)
    parser.add_argument('-n', '--name', help='Docker', type=str, required=True)
    parser.add_argument('-d', '--docker', help='Image docker', type=str, required=True)
    args = parser.parse_args()

    deploy(args)
