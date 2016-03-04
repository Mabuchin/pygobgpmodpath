# About
It constructs an evaluation environment in GoBGP.

# Ansible-Gobgp
And the following operations to all nodes.
 - Config to clone from the git.
 - Kill the process of gobgp.
 - To start the zebra
 - To start the process of gobgp.
## HowToUse
Run following command on the BB-dev-server.(only root user)

```
[root@dev ansible]# cd /root/gobgpmodpath/ansible
[root@dev ansible]# ansible-playbook -i playbook/hosts_gobgp playbook/run_gobgpd.yaml --private-key=~/.ssh/id_rsa
```

If you fail the check the status of the ssh-agent.
```
[root@dev ansible]# ssh-add -l
2048 30:d7:c2:33:4a:70:90:47:90:90:a5:91:87:07:7b:3a /root/.ssh/id_rsa (RSA)
```

If there is no id_rsa registered with the ` ssh-add ` command.
```
[root@dev ansible]# eval `ssh-agent` 
[root@dev ansible]# ssh-add
Enter passphrase for /root/.ssh/id_rsa:
```

# Gobgpmodpath

To generate a route to the specified node.
route_test.py is the test case.
## HowToUse

Describing the route.
It runs as follows.

```
(venv)[root@dev gobgpmodpath]# python route_test.py
```


# Template_Render

Generate a Router Script from Jinja2 template.