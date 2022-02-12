#!/bin/bash
# resize terminal window
resize -s 40 70 > /dev/null
#Colors
cyan='\e[0;36m'
lightcyan='\e[96m'
green='\e[0;32m'
lightgreen='\e[1;32m'
white='\e[1;37m'
red='\e[1;31m'
yellow='\e[1;33m'
blue='\e[1;34m'
Escape="\033";
white="${Escape}[0m";
RedF="${Escape}[31m";
GreenF="${Escape}[32m";
LighGreenF="${Escape}[92m"
YellowF="${Escape}[33m";
BlueF="${Escape}[34m";
CyanF="${Escape}[36m";
Reset="${Escape}[0m";
# Check root
[[ `id -u` -eq 0 ]] > /dev/null 2>&1 || { echo  $red "You must be root to run the script"; echo ; exit 1; }
clear
# check internet 
function checkinternet() 
{
  ping -c 1 google.com > /dev/null 2>&1
  if [[ "$?" != 0 ]]
  then
    echo -e $yellow " Checking For Internet: ${RedF}FAILED"
    echo
    echo -e $red "This Script Needs An Active Internet Connection"
    echo
    echo -e $yellow " LeoFi Exit"
    echo && sleep 2
    exit
  else
    echo -e $yellow " Checking For Internet: ${LighGreenF}CONNECTED"
  fi
}
checkinternet
sleep 2

echo -e $blue
sudo cat /etc/issue.net
#check dependencies existence
echo -e $blue "" 
echo "® Checking dependencies configuration ®" 
echo "                                       " 
# check if john is installed
which john > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e $green "[ ✔ ] John the ripper..............${LighGreenF}[ found ]"
which john > /dev/null 2>&1
sleep 2
else
echo -e $red "[ X ] John the Ripper -> ${RedF}not found "
echo -e $yellow "[ ! ] Installing Metasploit-Framework "
sudo apt-get install john -y
echo -e $blue "[ ✔ ] Done installing ...."
which john > /dev/null 2>&1
sleep 2
fi
#check if xterm is installed
which aircrack-ng > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e $green "[ ✔ ] Aircrack-ng.............................${LighGreenF}[ found ]"
which aircrack-ng > /dev/null 2>&1
sleep 2
else
echo ""
echo -e $red "[ X ] Aircrack-ng -> ${RedF}not found! "
fi
