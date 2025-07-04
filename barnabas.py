import psutil
import pyttsx3
import socket
import speech_recognition as sr
import sys

#init for constant variables/funtions
engine = pyttsx3.init()
def get_ip_address():
    interfaces = psutil.net_if_addrs()
    stats = psutil.net_if_stats()

    for iface_name, iface_addrs in interfaces.items():
        if stats[iface_name].isup:  # Check if the interface is up
            for addr in iface_addrs:
                if addr.family == socket.AF_INET and not addr.address.startswith("127."):
                    print(f"{iface_name}: {addr.address}")
                    bsay(f"{iface_name} is up with an ip adress of {addr.address}")
def bsay(t):
    engine.say(t)
    engine.runAndWait()
def get_cpu_usage():
    cpustats = psutil.cpu_percent(interval=1)
    engine.say(f"Cpu usage is at {cpustats}%")
    print(f"Cpu usage: {cpustats}%")
    engine.runAndWait()
def get_memory_usage():
    memory_info = psutil.virtual_memory()
    engine.say(f"memory usage is at {memory_info.percent}%")
    print(f"Memory usage: {memory_info.percent}%")
    engine.runAndWait()
    

#main 
engine.setProperty('rate', 175)
print("would you like to load into assistant mode?")
user_input = input().strip().lower()
if user_input == "yes" or user_input == "y":
    bsay("voice test check check")
    print(r"""
        ##                                                                                         ##
   ##                 ##                                                     ##                 ##
  ##                 ##                                                       ##                 ##
  ##                ###                                                       ###                ##
#  #               ###                                                         ###               # #
## ##              ###                                                         ###              ## ##
 ## ##            ###                                                           ###            ## ##
  ## ##          ###                                                             ###          ## ##
   #####         ###                                                             ###         #####
    ######      ###                #                             #                ###     #######
      #######   ###               ##                             ##               ###  ########
        #######  ###              ##                             ##              ###  #######
           #########              ##                             ##              #########
              ########           ##                               ##           ########
               ###########      ###                               ###      ###########
                  ############ ####                               #### ############
                    ################                             ################
                           ##########                           ##########
                              ########                         ########
                               #########chg               rpp#########
                                ######rog=${             CHGRPP######
                                ####ROG-chgrp}ch     modprog=${CH####
                                #MODPROG-chmod}cho@wnprog=${CHOWNPRO#
                                G-chown}cmpprog=${@CMPPROG-cmp}cpprog
                                 =${CPPROG-cp}mkdi@rprog=${MKDIRPROG
                               @@@@@-mkdir}mvprog@=${MVPROG-mv}rm@@@@@
                              @'''''@prog=${RMPROG@-rm}stripprog@'''''@
                              @''''''@=${STRIPPROG@-strip}posix@''''''@
                             @'''''''@_mkdir=mode=@!755mkdir_um@'''''''@
                             @'''''''@ask=22backup@suffix=chgrp@'''''''@
                             @''''''@cmd=chmodcmd@@@@$chmodprogc@''''''@
                              @@'''@howncmd=mvcm@d@$m@@vprogrmcmd@'''@@
                               =@@@"$rmprog-f"@@sr@ipcm@@d=src=ds@@@t
                                =dir_arg=dst@@_arg=@opy_@@on_change=f
                                alseis_targ@@et_a_@irecto@@ry=possibl
                                 yusage="\@@Usage@$0[OPTION]...[-T]S
                                 RCFILEDSTFILwhile@test$#-ne0;docase
                                 $1incoy_on_chang@e=true;;dir_arg=tr
                                  ue;;chgrpcmd="$c@hgrpprog $2"shif
                                  t;;--help)echo"@$usage"; exit $?;
                                   ;-mmode=$2case$@deinecho"$0:inv
                                   alidmode:##$mode@">&##2dst_arg=
                                    $2esacs##hift#@#do_e##xit='(e
                                    it$ret##echo#####"$0:##$dist_
                                     arg:####fi#######te####st-z
                                      "$di#################r_ar
                                      g";t#################hend
                                       o_ex###############it='
                                        (ex###   it$   ###ret
                                        );ex#   it$re   #t'tr
                                         ap"r   et+12   9;$d
                                          o_e   xit"1   tra
                                          p"r   et=13   0;$
                                           do_  exit"  2tr
                                            ap" ret=1 41;
                                              $do   exi
    """)
    bsay("welcome please enter a command")
else:
    if user_input == "no" or user_input == "n":
        sys.exit()
        print("goodbye")
while True :
    user_input = ""
    user_input = input("ENTER COMMAND:").strip().lower()
    if user_input == "exit":
        bsay("goodbye")
        sys.exit()
    if user_input == "getip":
        get_ip_address()
    if user_input == "getcpu":
        get_cpu_usage()
    if user_input == "getmem":
        get_memory_usage()
    if user_input == "help":
        engine.say("please look to the display for a list of commands")
        print("help: displays a list of commands\nexit: exits BARNABAS \ngetip: fetches the ip adress for the device \ngetcpu: fetches current cpu usage \ngetmem: fetches current RAM usage")
        engine.runAndWait()
