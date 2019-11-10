#!/bin/bash

InstallDir="/sgoinfre/goinfre/Perso/$USER"

if [ "$1" == "install-python" ]; then
	curl -s "https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh" -o Miniconda_Install.sh
	if which python > /dev/null 2>&1;
	then
    	while true; do
        	read -p "Python is already installed, do you want to reinstall it ?`echo $'\n[yes|no]> '`" yn
        	case $yn in
            	[Yy]es )
					rm -rf "$InstallDir/Miniconda";
					rm -rf "$InstallDir/.condrac" "$InstallDir/.continuum";
					echo "Python has been removed.";
					bash Miniconda_Install.sh -b -f -p "$InstallDir/Miniconda" > /dev/null 2>&1;
					sed -i.'' 's/export PATH=\/Users/export PATH=\/sgoinfre\/goinfre\/Perso\/agelloz\/Miniconda\/bin:\/Users/g' ~/.zshrc;
					echo "Python has been installed.";
					echo "You now need to source your '~/.zshrc' file manually to apply changes to PATH.";
					rm Miniconda_Install.sh;
					break;;
            	[Nn]o )
					echo "exit.";
					exit;;
            	* ) echo "[yes|no]>";;
        	esac
    	done
	else
    	bash Miniconda_Install.sh -b -f -p $InstallDir/Miniconda;
    	echo "Python has been installed.";
		rm Miniconda_Install.sh;
	fi
fi
