# Exercise 3 - Linux Permissions

## Objective

Practice Linux users, groups and permissions.

## Users Created

- analyst1
- engineer1
- intern1

## Group Created

- dataops

## Tasks Completed

- Created users
- Created dataops group
- Added users to group
- Created shared folder
- Configured permissions
- Tested access restrictions

## Commands Used
sudo useradd analyst1

sudo groupadd dataops

sudo usermod -aG dataops analyst1

sudo group add dataops

sudo usermod -aG dataops analyst1

sudo usermod -aG dataops engineer1

sudo mkdir /shared_data

sudo chown root:dataops /shared_data

sudo chmod 770 /shared_data
