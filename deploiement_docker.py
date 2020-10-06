import os, argparse

"""
Deploiement labs docker
Author :    Matthieu DEBRAY
Dependancies :
    - os, argparse
    - docker in OS
Release :   V0.1  10/2020
"""



def deploy(args):

    dict={}
    dict["count"] = args.count
    dict["container_name"] = args.name
    dict["container_image"] = args.docker
    var = """
        ansible-playbook -i ./ansible/hosts ./ansible/playbook.yml --extra-vars '{}'
    """.format(dict)
    os.system(var)


## Main call
if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Deploiement docker')
    parser.add_argument('-c', '--count', help='Docker', type=str, required=True)
    parser.add_argument('-n', '--name', help='Docker', type=str, required=True)
    parser.add_argument('-d', '--docker', help='Image docker', type=str, required=True)
    args = parser.parse_args()

    deploy(args)
