import os
os.system('docker ps -a')


ansible-playbook -i hosts playbook.yml --extra-vars '{"count":"4","container_name":"docker","container_image":"ubuntu_ssh"}'
