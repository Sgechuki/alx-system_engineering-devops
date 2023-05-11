This repository contains a collection of shell scripts for various tasks related to system engineering and DevOps. Below is a brief description of each script:

## 0-iam_betty
This script switches the current user to the user "betty" in the system.

## 1-who_am_i
This script prints the effective username of the current user.

## 2-groups
This script prints all the groups the current user is a part of.

## 3-new_owner
This script changes the owner of the file "hello" to the user "betty".

## 4-empty
This script creates an empty file called "hello".

## 5-execute
This script adds execute permission to the owner of the file "hello".

## 6-multiple_permissions
This script adds execute permission to the owner and group owner, and read permission to other users, to the file "hello".

## 7-everybody
This script adds execution permission to the owner, group owner, and other users, to the file "hello".

## 8-James_Bond
This script sets the permissions of the file "hello" as follows: owner - no permission, group - no permission, other users - all permissions.

## 9-John_Doe
This script sets the mode of the file "hello" to "-rwxr-x-wx" (i.e., read, write, execute for owner; read, execute for group owner; write, execute for other users).

## 10-mirror_permissions
This script sets the mode of the file "hello" the same as the mode of the file "olleh".

## 11-directories_permissions
This script adds execute permission to all subdirectories of the current directory for the owner, group owner, and all other users.

## 12-directory_permissions
This script creates a directory called "my_dir" with permissions "751" in the working directory.

## 13-change_group
This script changes the group owner of the file "hello" to "school".

## 100-change_owner_and_group
This advanced script changes the owner to "vincent" and the group owner to "staff" for all files and directories in the working directory.
