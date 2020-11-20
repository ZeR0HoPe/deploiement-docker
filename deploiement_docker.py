import os, argparse


"""
Deploiement labs docker
Author :    ZeR0HoPe
Dependancies :
    - os, argparse
    - docker in OS
Release :   V0.1  10/2020
"""

def deploy(args):

        for i in range(int(args.count)):

            if args.docker in ['centos_ssh', 'fedora_ssh']:

                var1 = 'docker run -d -v /sys/fs/cgroup:/sys/fs/cgroup:ro --mount type=tmpfs,destination=/run --name {0} {1}'.format(args.name + str(i), args.docker)

            else:
                var1 = 'docker run -d -P --name {0} {1}'.format(args.name + str(i),  args.docker)

            os.system(var1)

        for i in range(int(args.count)):
            var2 = "docker inspect -f '=> {{.Name}} - {{.NetworkSettings.IPAddress }}' "
            var3 = (args.name)+str(i)
            os.system(var2+var3)


## Main call
if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Deploiement docker')
    parser.add_argument('-c', '--count', help='number', type=str, required=True)
    parser.add_argument('-n', '--name', help='name', type=str, required=True)
    parser.add_argument('-d', '--docker', help='Image docker', type=str, required=True)
    parser.add_argument('-i', '--info', help='Information', action="store_true")
    args = parser.parse_args()

    deploy(args)
