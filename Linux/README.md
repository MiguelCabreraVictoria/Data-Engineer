# Linux 


### Commands
			Know OS = cat /etc/os-release
			Copy directory = cp -r <path> <path>
			Change Hostname  = hostname <new_name>
			
### Important Directories

- Home Directories : /root, /home/username
- User Executable : /bin, /usr/bin, /usr/local/bin
- System Executables : /sbin, /usr/sbin, /usr/local/sbin
- Other Mountpoints : /media, /mnt
- Configuration : /etc
- Temporary Files : /tmp
- Kernels and Bootloader: /boot
- Server Data: /var, /srv
- System Information: /proc, /sys
- Shares Libraries: /lib, /usr/lib, /usr/local/lib

### Files Types

- Regular file (-) : Normal files such as text, data, or executable files
- Directory (d) : Files that are lists of other files
- Link (l) : A shotcut that points to the location of the actual file
			
			ln -s <path> <link_name>
			unlink <link_name>		

- Special file (c) : Mechanism used for input and output, such as files in /dev
- Socket (s) : A special file that provides inter-process networking protected by the fiel system´access control
- Pipe (p) : A special file that allows processes to communicate with each other without saving network socket semantics

### Filter & IO redirection command

- Grep : grep command is used to find texts from any text input

			grep <word> <file_path>
			grep -i <word> <file_path>
			grep -iR <word> <directory>
			grep -vi <word> <file_path>

- less: Reader 
			less <file_path>

- more: Reader
			more <file_path>

- cut: 
			cut -d: -f1 <fiel_path>

- awk : 
			awk -F':' '{print $1}' <file_path>

- find: 
			find <path> -name <word>


### Users & Groups

- Users
	- Users and groups are used to control access to files and resources
	- Users login to the system by supplying their username and password
	- Every file on the system is owned by a user and associated with a group
	- Every process has an owner and group affilation and can only access the resources its owner and group can access
	- Every user of the system is assigned a unique user ID number
	- Users name and UID are stored in /etc/passwd
	- Users password is stored in /etc/shadow in encrypted form
	- Users are assigned a home directory and a program that is run when they login
	- Users cannot read, write or execute each other files without permission

- Types of users
	- 
	- 


- Commands

			head -1 /etc/passwd
			id <user>

			useradd <name>
			passwd <name>
			su - <name>
			
			userdel <user>
			userdel -r <user>

			groupadd <name>
			usermod -aG <group_name> <user_name>

			groupdel <group_name>

			lsof -u <user_name>


### File Permissions

- r : permission to read a file or list a directory´s contents
- w/a : permission to write to a file or create and remove files from a directory : 
- x : permissiion to execute a program or change into a directory and do a long listing of the directory
- - : no permission (in place of the r,w or x)

			Give permission to other users
			
			chown <user_name>:<group_name> <path>
			chown -R  <user_name>:<group_name> <path>

			chmod o-x /opt/devopsdir
			chmod o-r /opt/devopsdir

			chmod g+w /opt/devopsdir

			 ls -ld /opt/devopsdir

### Changing Permissions

- To change access mode: chmod[-option]... mode[,mode] file|directory

- mode includes:
	- u,g,o for user, group and other
	- +, - for grant, deny or set
	- r, w, s for read. write and execute

- options:
	- -R Recurive
	- -v Verbose
	- --reference Reference another file for its mode
