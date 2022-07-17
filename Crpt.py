#!/usr/bin/python
#-*-coding:utf-8-*-

import re
import smtplib
import getpass
import sys
import os
import random
import string
import time

try:
	import twilio
except ImportError:
	os.system("pip install twilio")
	pass

try:
	input = raw_input
except NameError:
	pass
###################################
#        Les Bannières            #
###################################
def verif_os():
    if os.name == "nt":
        systeme_d_exploitation = "windows"
    if os.name == "posix":
        systeme_d_exploitation = "posix"
    return systeme_d_exploitation

class bcolors:
	PURPLE = '\033[95m'
	CYAN = '\033[96m'
	DARKCYAN = '\033[36m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	BOLD = '\033[1m'
	UNDERL = '\033[4m'
	ENDC = '\033[0m'
	WHITE = '\033[97m'
	backBlack = '\033[40m'
	backRed = '\033[41m'
	backGreen = '\033[42m'
	backYellow = '\033[43m'
	backBlue = '\033[44m'
	backMagenta = '\033[45m'
	backCyan = '\033[46m'
	backWhite = '\033[47m'

        
	def disable(self):
		self.PURPLE = ''
		self.CYAN = ''
		self.BLUE = ''
		self.GREEN = ''
		self.YELLOW = ''
		self.RED = ''
		self.ENDC = ''
		self.WHITE = ''
		self.BOLD = ''
		self.UNDERL = ''
		self.backBlack = ''
		self.backRed = ''
		self.backGreen = ''
		self.backYellow = ''
		self.backBlue = ''
		self.backMagenta = ''
		self.backCyan = ''
		self.backWhite = ''
		self.DARKCYAN = ''

def banner():
	if verif_os() == "posix":
		os.system("clear")
	if verif_os() == "windows":
		os.system("cls")
	graphique()

def graphique():
    menu = random.randrange(1, 14)
    if menu == 1:
		print(bcolors.RED + """
		                                        ,--,          ,----,                                                                     
             .--,-``-.                    ,--,---.'|        ,/   .`|                                                                     
    ,---,   /   /     '.     ,---,.     ,--.'|   | :      ,`   .'  :          .--.--.                                                    
  .'  .' `\/ ../        ;  ,'  .' |  ,--,  | :   : |    ;    ;     /         /  /    '.                                          ,--,    
,---.'     \ ``\  .`-    ,---.'   ,---.'|  : |   ' :  .'___,/    ,'         |  :  /`. /               ,---,                    ,--.'|    
|   |  .`\  \___\/   \   |   |   .;   : |  | ;   ; '  |    :     |          ;  |  |--`            ,-+-. /  | .--.--.           |  |,     
:   : |  '  |    \   :   :   :  : |   | : _' '   | |__;    |.';  ;          |  :  ;_      ,---.  ,--.'|'   |/  /    '    ,---. `--'_     
|   ' '  ;  :    /  /   /:   |  |-:   : |.'  |   | :.'`----'  |  |           \  \    `.  /     \|   |  ,"' |  :  /`./   /     \,' ,'|    
'   | ;  .  |    \  \   \|   :  ;/|   ' '  ; '   :    ;   '   :  ;            `----.   \/    /  |   | /  | |  :  ;_    /    /  '  | |    
|   | :  |  '___ /   :   |   |   .\   \  .'. |   |  ./    |   |  '            __ \  \  .    ' / |   | |  | |\  \    `..    ' / |  | :    
'   : | /  ;/   /\   /   '   :  '  `---`:  | ;   : ;      '   :  |           /  /`--'  '   ;   /|   | |  |/  `----.   '   ;   /'  : |__  
|   | '` ,// ,,/  ',-    |   |  |       '  ; |   ,/       ;   |.'           '--'.     /'   |  / |   | |--'  /  /`--'  '   |  / |  | '.'| 
;   :  .'  \ ''\        ;|   :  \       |  : '---'        '---'               `--'---' |   :    |   |/     '--'.     /|   :    ;  :    ; 
|   ,.'     \   \     .' |   | ,'       '  ,/                                           \   \  /'---'        `--'---'  \   \  /|  ,   /  
'---'        `--`-,,-'   `----'         '--'                                             `----'                         `----'  ---`-' """)
    if menu == 2:
        print(bcolors.YELLOW + r"""
          ____                                                     ____              
        ,'  , `. .--.--.    ,----..             .--.--.          ,'  , `. .--.--.    
     ,-+-,.' _ |/  /    '. /   /   \           /  /    '.     ,-+-,.' _ |/  /    '.  
  ,-+-. ;   , ||  :  /`. /|   :     :         |  :  /`. /  ,-+-. ;   , ||  :  /`. /  
 ,--.'|'   |  ;;  |  |--` .   |  ;. /         ;  |  |--`  ,--.'|'   |  ;;  |  |--`   
|   |  ,', |  '|  :  ;_   .   ; /--`          |  :  ;_   |   |  ,', |  '|  :  ;_     
|   | /  | |  ||\  \    `.;   | ;  __          \  \    `.|   | /  | |  ||\  \    `.  
'   | :  | :  |, `----.   |   : |.' .'          `----.   '   | :  | :  |, `----.   \ 
;   . |  ; |--'  __ \  \  .   | '_.' :          __ \  \  ;   . |  ; |--'  __ \  \  | 
|   : |  | ,    /  /`--'  '   ; : \  |         /  /`--'  |   : |  | ,    /  /`--'  / 
|   : '  |/    '--'.     /'   | '/  .'        '--'.     /|   : '  |/    '--'.     /  
;   | |`-'       `--'---' |   :    /            `--'---' ;   | |`-'       `--'---'   
|   ;/                     \   \ .'                      |   ;/                      
'---'                       `---`                        '---'                        """ + bcolors.ENDC)
        return

    if menu == 3:
        print(bcolors.GREEN + r"""
 ______  ______  _______  ___   _   _________   
(  __  \/ ___  \(  ____ \/   ) ( \  \__   __/
| (  \  \/   \  | (    \/ /) | | (     ) (
| |   ) |  ___) | (__  / (_) (_| |     | |
| |   | | (___ (|  __)(____   _| |     | |
| |   ) |     ) | (        ) ( | |     | |
| (__/  /\___/  | )        | | | (____/| |
(______/\______/|/         (_) (_______)_(""" + bcolors.ENDC)
        return

    if menu == 4:
        print(bcolors.backBlack + r"""
|      *******                                                  |
|     *       ***                                          *    | 
|    *         **                                         ***   | 
|    **        *                                           *    | 
|     ***                                 ****                  | 
|    ** ***           ***  ***  ****     * **** *   ***  ***    | 
|     *** ***        * ***  **** **** * **  ****   * ***  ***   | 
|       *** ***     *   ***  **   **** ****       *   ***  **   | 
|         *** ***  **    *** **    **    ***     **    *** **   | 
|           ** *** ********  **    **      ***   ********  **   | 
|            ** ** *******   **    **        *** *******   **   | 
|             * *  **        **    **   ****  ** **        **   | 
|   ***        *   ****    * **    **  * **** *  ****    * **   | 
|  *  *********     *******  ***   ***    ****    *******  *** *| 
| *     *****        *****    ***   ***            *****    *** | 
| *                                                             | 
|  **                                                           |""" + bcolors.ENDC)

    if menu == 5:
        print(bcolors.RED + r"""
        ___    ,-,--.      _,---.            ,-,--.        ___    ,-,--.  
  .-._ .'=.'\ ,-.'-  _\ _.='.'-,  \         ,-.'-  _\.-._ .'=.'\ ,-.'-  _\ 
 /==/ \|==|  /==/_ ,_.'/==.'-     /        /==/_ ,_./==/ \|==|  /==/_ ,_.' 
 |==|,|  / - \==\  \  /==/ -   .-'         \==\  \  |==|,|  / - \==\  \    
 |==|  \/  , |\==\ -\ |==|_   /_,-.         \==\ -\ |==|  \/  , |\==\ -\   
 |==|- ,   _ |_\==\ ,\|==|  , \_.' )        _\==\ ,\|==|- ,   _ |_\==\ ,\  
 |==| _ /\   /==/\/ _ \==\-  ,    (        /==/\/ _ |==| _ /\   /==/\/ _ | 
 /==/  / / , \==\ - , //==/ _  ,  /        \==\ - , /==/  / / , \==\ - , / 
 `--`./  `--` `--`---' `--`------'          `--`---'`--`./  `--` `--`---'""" + bcolors.ENDC)
        return

    if menu == 6:
        print(bcolors.backWhite + r'''
 ███▄ ▄███▓ ██████  ▄████      ██████ ███▄ ▄███▓ ██████ 
▓██▒▀█▀ ██▒██    ▒ ██▒ ▀█▒   ▒██    ▒▓██▒▀█▀ ██▒██    ▒ 
▓██    ▓██░ ▓██▄  ▒██░▄▄▄░   ░ ▓██▄  ▓██    ▓██░ ▓██▄   
▒██    ▒██  ▒   ██░▓█  ██▓     ▒   ██▒██    ▒██  ▒   ██▒
▒██▒   ░██▒██████▒░▒▓███▀▒   ▒██████▒▒██▒   ░██▒██████▒▒
░ ▒░   ░  ▒ ▒▓▒ ▒ ░░▒   ▒    ▒ ▒▓▒ ▒ ░ ▒░   ░  ▒ ▒▓▒ ▒ ░
░  ░      ░ ░▒  ░ ░ ░   ░    ░ ░▒  ░ ░  ░      ░ ░▒  ░ ░
░      ░  ░  ░  ░ ░ ░   ░    ░  ░  ░ ░      ░  ░  ░  ░  
       ░        ░       ░          ░        ░        ░  ''' + bcolors.ENDC)
        return

    if menu == 7:
        print(bcolors.YELLOW + r"""
MMMMMMMM               MMMMMMMM  SSSSSSSSSSSSSSS        GGGGGGGGGGGGG        SSSSSSSSSSSSSSSMMMMMMMM               MMMMMMMM  SSSSSSSSSSSSSSS 
M:::::::M             M:::::::MSS:::::::::::::::S    GGG::::::::::::G      SS:::::::::::::::M:::::::M             M:::::::MSS:::::::::::::::S
M::::::::M           M::::::::S:::::SSSSSS::::::S  GG:::::::::::::::G     S:::::SSSSSS::::::M::::::::M           M::::::::S:::::SSSSSS::::::S
M:::::::::M         M:::::::::S:::::S     SSSSSSS G:::::GGGGGGGG::::G     S:::::S     SSSSSSM:::::::::M         M:::::::::S:::::S     SSSSSSS
M::::::::::M       M::::::::::S:::::S            G:::::G       GGGGGG     S:::::S           M::::::::::M       M::::::::::S:::::S            
M:::::::::::M     M:::::::::::S:::::S           G:::::G                   S:::::S           M:::::::::::M     M:::::::::::S:::::S            
M:::::::M::::M   M::::M:::::::MS::::SSSS        G:::::G                    S::::SSSS        M:::::::M::::M   M::::M:::::::MS::::SSSS         
M::::::M M::::M M::::M M::::::M SS::::::SSSSS   G:::::G    GGGGGGGGGG       SS::::::SSSSS   M::::::M M::::M M::::M M::::::M SS::::::SSSSS    
M::::::M  M::::M::::M  M::::::M   SSS::::::::SS G:::::G    G::::::::G         SSS::::::::SS M::::::M  M::::M::::M  M::::::M   SSS::::::::SS  
M::::::M   M:::::::M   M::::::M      SSSSSS::::SG:::::G    GGGGG::::G            SSSSSS::::SM::::::M   M:::::::M   M::::::M      SSSSSS::::S 
M::::::M    M:::::M    M::::::M           S:::::G:::::G        G::::G                 S:::::M::::::M    M:::::M    M::::::M           S:::::S
M::::::M     MMMMM     M::::::M           S:::::SG:::::G       G::::G                 S:::::M::::::M     MMMMM     M::::::M           S:::::S
M::::::M               M::::::SSSSSSS     S:::::S G:::::GGGGGGGG::::G     SSSSSSS     S:::::M::::::M               M::::::SSSSSSS     S:::::S
M::::::M               M::::::S::::::SSSSSS:::::S  GG:::::::::::::::G     S::::::SSSSSS:::::M::::::M               M::::::S::::::SSSSSS:::::S
M::::::M               M::::::S:::::::::::::::SS     GGG::::::GGG:::G     S:::::::::::::::SSM::::::M               M::::::S:::::::::::::::SS 
MMMMMMMM               MMMMMMMMSSSSSSSSSSSSSSS          GGGGGG   GGGG      SSSSSSSSSSSSSSS  MMMMMMMM               MMMMMMMMSSSSSSSSSSSSSSS""" + bcolors.ENDC)
        return

    if menu == 8:
        print(bcolors.RED + r'''
          !\_________________________/!\
          !!Dan:Hi.                  !! \
          !!Ted:I want crypt my sms. !!  \
          !!Dan:I know how.          !!  !
          !!Ted:Please tell more.    !!  !
          !!Dan:It's a program make  !!  !
          !!    by Sensei & D3F4LT   !!  !
          !!                         !!  !
          !!                         !!  /
          !!_________________________!! /
          !/_________________________\!/
             __\_________________/__/!_
            !_______________________!/
          ________________________
         /oooo  oooo  oooo  oooo /!
        /ooooooooooooooooooooooo/ /
       /ooooooooooooooooooooooo/ /
      /C=_____________________/_/''' + bcolors.ENDC)

    if menu == 9:
        print(bcolors.YELLOW + """
         01011001011011110111010100100000011100
         10011001010110000101101100011011000111
         10010010000001101000011000010111011001
         10010100100000011101000110111100100000
         01101101011101010110001101101000001000
         00011101000110100101101101011001010010
         00000110111101101110001000000111100101
         10111101110101011100100010000001101000
         01100001011011100110010001110011001000
         00001110100010110100101001001000000101
         01000110100001100001011011100110101101
         11001100100000011001100110111101110010
         00100000011101010111001101101001011011
         10011001110010000001110100011010000110
         01010010000001010011011011110110001101
         10100101100001011011000010110101000101
         01101110011001110110100101101110011001
         01011001010111001000100000010101000110
         11110110111101101100011010110110100101
         11010000100000001010100110100001110101
         011001110111001100101010""" + bcolors.ENDC)

    if menu == 10:
        print(bcolors.GREEN + """
@@@@@@@   @@@@@@   @@@@@@@@     @@@   @@@       @@@@@@@      @@@@@@   @@@@@@@@  @@@  @@@   @@@@@@   @@@@@@@@  @@@  
@@@@@@@@  @@@@@@@  @@@@@@@@    @@@@   @@@       @@@@@@@     @@@@@@@   @@@@@@@@  @@@@ @@@  @@@@@@@   @@@@@@@@  @@@  
@@!  @@@      @@@  @@!        @@!@!   @@!         @@!       !@@       @@!       @@!@!@@@  !@@       @@!       @@!  
!@!  @!@      @!@  !@!       !@!!@!   !@!         !@!       !@!       !@!       !@!!@!@!  !@!       !@!       !@!  
@!@  !@!  @!@!!@   @!!!:!   @!! @!!   @!!         @!!       !!@@!!    @!!!:!    @!@ !!@!  !!@@!!    @!!!:!    !!@  
!@!  !!!  !!@!@!   !!!!!:  !!!  !@!   !!!         !!!        !!@!!!   !!!!!:    !@!  !!!   !!@!!!   !!!!!:    !!!  
!!:  !!!      !!:  !!:     :!!:!:!!:  !!:         !!:            !:!  !!:       !!:  !!!       !:!  !!:       !!:  
:!:  !:!      :!:  :!:     !:::!!:::   :!:        :!:           !:!   :!:       :!:  !:!      !:!   :!:       :!:  
 :::: ::  :: ::::   ::          :::    :: ::::     ::       :::: ::    :: ::::   ::   ::  :::: ::    :: ::::   ::  
:: :  :    : : :    :           :::   : :: : :     :        :: : :    : :: ::   ::    :   :: : :    : :: ::   :""" + bcolors.ENDC)

    if menu == 11:
        print(bcolors.backBlue + r"""
@@@@@@@@@@    @@@@@@    @@@@@@@@      @@@@@@   @@@@@@@@@@    @@@@@@   
@@@@@@@@@@@  @@@@@@@   @@@@@@@@@     @@@@@@@   @@@@@@@@@@@  @@@@@@@   
@@! @@! @@!  !@@       !@@           !@@       @@! @@! @@!  !@@       
!@! !@! !@!  !@!       !@!           !@!       !@! !@! !@!  !@!       
@!! !!@ @!@  !!@@!!    !@! @!@!@     !!@@!!    @!! !!@ @!@  !!@@!!    
!@!   ! !@!   !!@!!!   !!! !!@!!      !!@!!!   !@!   ! !@!   !!@!!!   
!!:     !!:       !:!  :!!   !!:          !:!  !!:     !!:       !:!  
:!:     :!:      !:!   :!:   !::         !:!   :!:     :!:      !:!   
:::     ::   :::: ::    ::: ::::     :::: ::   :::     ::   :::: ::   
 :      :    :: : :     :: :: :      :: : :     :      :    :: : :""" + bcolors.ENDC)

    if menu == 12:
        print(bcolors.YELLOW + r'''
O~~       O~~ O~~ ~~   O~~~~          O~~ ~~ O~~       O~~ O~~ ~~  
O~ O~~   O~~O~~    O~O~    O~~      O~~    O~O~ O~~   O~~O~~    O~~
O~~ O~~ O O~~O~~    O~~              O~~     O~~ O~~ O O~~O~~      
O~~  O~~  O~~  O~~  O~~                O~~   O~~  O~~  O~~  O~~    
O~~   O~  O~~     O~O~~   O~~~~           O~~O~~   O~  O~~     O~~ 
O~~       O~O~~    O~O~~    O~      O~~    O~O~~       O~O~~    O~~
O~~       O~~ O~~ ~~  O~~~~~          O~~ ~~ O~~       O~~ O~~ ~~ ''')

    if menu == 13:
        print(bcolors.RED + r"""
                      ..:::::::::..
                  ..:::aad8888888baa:::..
              .::::d:?88888888888?::8b::::.
            .:::d8888:?88888888??a888888b:::.
          .:::d8888888a8888888aa8888888888b:::.
         ::::dP::::::::88888888888::::::::Yb::::
        ::::dP:::::::::Y888888888P:::::::::Yb::::
       ::::d8:::::::::::Y8888888P:::::::::::8b::::
      .::::88::::::::::::Y88888P::::::::::::88::::.
      :::::Y8baaaaaaaaaa88P:T:Y88aaaaaaaaaad8P:::::
      :::::::Y88888888888P::|::Y88888888888P:::::::
      ::::::::::::::::888:::|:::888::::::::::::::::
      `:::::::::::::::8888888888888b::::::::::::::'
       :::::::::::::::88888888888888::::::::::::::
        :::::::::::::d88888888888888:::::::::::::
         ::::::::::::88::88::88:::88::::::::::::
          `::::::::::88::88::88:::88::::::::::'
            `::::::::88::88::P::::88::::::::'
              `::::::88::88:::::::88::::::'
                 ``:::::::::::::::::::''
                      ``:::::::::''""" + bcolors.ENDC)

    if menu == 14:
        print(bcolors.BOLD + """
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XX                                                                          XX
XX   MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMMMMMMMMssssssssssssssssssssssssssMMMMMMMMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMMMss'''                          '''ssMMMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMyy''                                    ''yyMMMMMMMMMMMM   XX
XX   MMMMMMMMyy''                                            ''yyMMMMMMMM   XX
XX   MMMMMy''                                                    ''yMMMMM   XX
XX   MMMy'                                                          'yMMM   XX
XX   Mh'                                                              'hM   XX
XX   -                                                                  -   XX
XX                                                                          XX
XX   ::                                                                ::   XX
XX   MMhh.        ..hhhhhh..                      ..hhhhhh..        .hhMM   XX
XX   MMMMMh   ..hhMMMMMMMMMMhh.                .hhMMMMMMMMMMhh..   hMMMMM   XX
XX   ---MMM .hMMMMdd:::dMMMMMMMhh..        ..hhMMMMMMMd:::ddMMMMh. MMM---   XX
XX   MMMMMM MMmm''      'mmMMMMMMMMyy.  .yyMMMMMMMMmm'      ''mmMM MMMMMM   XX
XX   ---mMM ''             'mmMMMMMMMM  MMMMMMMMmm'             '' MMm---   XX
XX   yyyym'    .              'mMMMMm'  'mMMMMm'              .    'myyyy   XX
XX   mm''    .y'     ..yyyyy..  ''''      ''''  ..yyyyy..     'y.    ''mm   XX
XX           MN    .sMMMMMMMMMss.   .    .   .ssMMMMMMMMMs.    NM           XX
XX           N`    MMMMMMMMMMMMMN   M    M   NMMMMMMMMMMMMM    `N           XX
XX            +  .sMNNNNNMMMMMN+   `N    N`   +NMMMMMNNNNNMs.  +            XX
XX              o+++     ++++Mo    M      M    oM++++     +++o              XX
XX                                oo      oo                                XX
XX           oM                 oo          oo                 Mo           XX
XX         oMMo                M              M                oMMo         XX
XX       +MMMM                 s              s                 MMMM+       XX
XX      +MMMMM+            +++NNNN+        +NNNN+++            +MMMMM+      XX
XX     +MMMMMMM+       ++NNMMMMMMMMN+    +NMMMMMMMMNN++       +MMMMMMM+     XX
XX     MMMMMMMMMNN+++NNMMMMMMMMMMMMMMNNNNMMMMMMMMMMMMMMNN+++NNMMMMMMMMM     XX
XX     yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy     XX
XX   m  yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy  m   XX
XX   MMm yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy mMM   XX
XX   MMMm .yyMMMMMMMMMMMMMMMM     MMMMMMMMMM     MMMMMMMMMMMMMMMMyy. mMMM   XX
XX   MMMMd   ''''hhhhh       odddo          obbbo        hhhh''''   dMMMM   XX
XX   MMMMMd             'hMMMMMMMMMMddddddMMMMMMMMMMh'             dMMMMM   XX
XX   MMMMMMd              'hMMMMMMMMMMMMMMMMMMMMMMh'              dMMMMMM   XX
XX   MMMMMMM-               ''ddMMMMMMMMMMMMMMdd''               -MMMMMMM   XX
XX   MMMMMMMM                   '::dddddddd::'                   MMMMMMMM   XX
XX   MMMMMMMM-                                                  -MMMMMMMM   XX
XX   MMMMMMMMM                                                  MMMMMMMMM   XX
XX   MMMMMMMMMy                                                yMMMMMMMMM   XX
XX   MMMMMMMMMMy.                                            .yMMMMMMMMMM   XX
XX   MMMMMMMMMMMMy.                                        .yMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMy.                                    .yMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMMMs.                                .sMMMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMMMMMss.           ....           .ssMMMMMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMMMMMMMNo         oNNNNo         oNMMMMMMMMMMMMMMMMMMMM   XX
XX                                                                          XX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    .o88o.                               o8o                .
    888 `"                               `"'              .o8
   o888oo   .oooo.o  .ooooo.   .ooooo.  oooo   .ooooo.  .o888oo oooo    ooo
    888    d88(  "8 d88' `88b d88' `"Y8 `888  d88' `88b   888    `88.  .8'
    888    `"Y88b.  888   888 888        888  888ooo888   888     `88..8'
    888    o.  )88b 888   888 888   .o8  888  888    .o   888 .    `888'
   o888o   8""888P' `Y8bod8P' `Y8bod8P' o888o `Y8bod8P'   "888"      d8'
                                                                .o...P'
                                                                `XER0'
""" + bcolors.ENDC)

##################################################
#  Concernant le Chiffrement par fonction affine #
##################################################
 
def tirage_aleatoire(k):
    k=random.randint(1,25)    
    return k

def prepare(saisie):
    li1=["âà","éèêë","îï","ô","ûü","ç"]
    li2=["A","E","I","O","U","C"]
    i=0
    # Remplacement des caractères accentués éventuels
    for mot in li1:
       repl=li2[i]
       for lettre in mot:
           saisie=saisie.replace(lettre,repl)
       i+=1      
    saisie=saisie.upper()    # Passage en majuscules
    return saisie

# Tirage aléatoire de la Clé avec a et b différents
k=0
k=tirage_aleatoire(k)
a=k
while k==a:
    k=tirage_aleatoire(k)
b=k
a,b=21,13

##################################
#  Concernant le Chiffrement RSA #
##################################

FirstNumbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
73, 79, 83, 89, 97, 101, 103, 107, 109, 113,
127, 131, 137, 139, 149, 151, 157, 163, 167, 173,
179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
233, 239, 241, 251, 257, 263, 269, 271, 277, 281,
283, 293, 307, 311, 313, 317, 331, 337, 347, 349,
353, 359, 367, 373, 379, 383, 389, 397, 401, 409,
419, 421, 431, 433, 439, 443, 449, 457, 461, 463,
467, 479, 487, 491, 499, 503, 509, 521, 523, 541,
547, 557, 563, 569, 571, 577, 587, 593, 599, 601,
607, 613, 617, 619, 631, 641, 643, 647, 653, 659,
661, 673, 677, 683, 691, 701, 709, 719, 727, 733,
739, 743, 751, 757, 761, 769, 773, 787, 797, 809,
811, 821, 823, 827, 829, 839, 853, 857, 859, 863,
877, 881, 883, 887, 907, 911, 919, 929, 937, 941,
947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013,
1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069,
1087, 1091, 1093, 1097, 1103, 1109, 1117, 1123, 1129, 1151,
1153, 1163, 1171, 1181, 1187, 1193, 1201, 1213, 1217, 1223,
1229, 1231, 1237, 1249, 1259, 1277, 1279, 1283, 1289, 1291,
1297, 1301, 1303, 1307, 1319, 1321, 1327, 1361, 1367, 1373,
1381, 1399, 1409, 1423, 1427, 1429, 1433, 1439, 1447, 1451,
1453, 1459, 1471, 1481, 1483, 1487, 1489, 1493, 1499, 1511,
1523, 1531, 1543, 1549, 1553, 1559, 1567, 1571, 1579, 1583,
1597, 1601, 1607, 1609, 1613, 1619, 1621, 1627, 1637, 1657,
1663, 1667, 1669, 1693, 1697, 1699, 1709, 1721, 1723, 1733,
1741, 1747, 1753, 1759, 1777, 1783, 1787, 1789, 1801, 1811 ]

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def multiplication_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi
    
    while e > 0:
        temp1 = temp_phi/e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2
        
        x = x2- temp1* x1
        y = d - temp1 * y1
        
        x2 = x1
        x1 = x
        d = y1
        y1 = y
    
    if temp_phi == 1:
        return d + phi

'''
Teste pour vérifier que le nombre est premier.
'''
def est_premier(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in xrange(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

def generer_paire_de_cle(p, q):
    if not (est_premier(p) and est_premier(q)):
        raise ValueError('[!] Les nombres doivent être premier.')
    elif p == q:
        raise ValueError('p et q ne peuvent pas être egaux')
    #n = pq
    n = p * q
    phi = (p-1) * (q-1)
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    d = multiplication_inverse(e, phi)
    
    #Retourner la paire de clée pubique et privée
    #Clée publique est (e, n) et clée privée est (d, n)
    return ((e, n), (d, n))

#Début des fonctions de cryptage
"""cryptage César revisité"""
"""le decalage va dependre de la longueur du message saisie"""
def CCesar(saisie):
	decalage=len(saisie)
	texte_crypter=""
	for x in saisie:
		if (x.islower()):
			texte_crypter += chr((ord(x)-ord(' ')-decalage)%95+ord(' '))

		elif (x.isupper()):
			texte_crypter += chr((ord(x)-ord(' ')-decalage)%95+ord(' '))

		else:
			texte_crypter += x

	return texte_crypter
	
def DCesar(saisi):
	decalage=len(saisi)
	texte_decrypter=""
	for x in saisi:
		if (x.islower()):
			texte_decrypter += chr((ord(x)-ord(' ')+decalage)%95+ord(' '))

		elif (x.isupper()):
			texte_decrypter += chr((ord(x)-ord(' ')+decalage)%95+ord(' '))

		else:
			texte_decrypter += x

	return texte_decrypter

#Je galère un peu sur le DCesar. les charactères [\^_`] ne se decryptent pas.

"""cryptage Morse"""
def CMorse(self):

#en attente

	print ("en attente")

def DMorse(self):

#en attente

	print ("en attente")

"""cryptage Affine"""
def CAffine(self):
	lg=len(saisie)
	MessageCrypte=""
	for i in range(lg):
	    lettre = saisie[i]
	    if lettre in " ',-;:!?.":
		MessageCrypte += lettre
	    else:
		MessageCrypte += chr((a*(ord(lettre)-65)+ b)%26 + 65)
	   
	# Affichage du résultat
	# Si tu le souhaite tu peux print ('Clé : ('+ str(a) + ' ; '+ str(b)+')')
	return MessageCrypte.capitalize()

def DAffine(self):
	lg=len(saisie)
	MessageClair=""

	# Recherche de la clé sachant que L --> K et  E --> T
	# Affectation des valeurs des lettres : ax+b=y puis axx+b=yy
	x,y = ord('L')-65,ord('K')-65
	xx,yy = ord('E')-65,ord('T')-65

	# Résolution du système
	u,v=xx-x,yy-y
	if u < 0:
	    u,v=x-xx,y-yy
	k=0
	while not ((v+26*k)%u==0 and v+26*k >0):
	    k+= 1
	a = int((v+26*k)/u)

	b=y-a*x
	k=0
	while not y-a*x+26*k > 0:
	    k+= 1
	b = y-a*x+26*k

	# Déchiffrement proprement dit
	for i in range(lg):
	    lettre = saisie[i]
	    if lettre in " ',-;:!?.":
		MessageClair+= lettre
	    else:
		res,k=ord(lettre)-65-b,0
		while (res+26*k)%a>0 or res+26*k<0:
		    k+=1
		MessageClair += chr((res+26*k)/a+65)
	   
	# Affichage du résultat
	# Si tu le souhaite tu peux print ('Avec L --> K  et  E --> T, la Clé est : ('+ str(a) + ' ; '+ str(b)+')')
	return MessageClair.capitalize()

"""cryptage RSA"""
def CRSA(pk, texte_saisie):
    cle, n = pk
    #Convertir chaque lettre de texte_saisie en nombre basé sur le caractère utilisant a^b mod m
    chiffreur = [(ord(char) ** cle) % n for char in texte_saisie]
    return chiffreur

def DRSA(pk, texte_crypter):
    cle, n = pk
    #Générer le text_saisie à partir du texte_crypter et une clé utilisant a^b mod m
    plan = [chr((char ** cle) % n) for char in texte_crypter]
    return ''.join(plan)

#juste un script pour que tu teste les cryptages
"""saisie= raw_input('Entrer le texte à crypter(Affine)> ')
saisie=prepare(saisie)
print ("Cryptage affine: "+CAffine(saisie))
saisie = raw_input('Entrer le texte à décrypter(Affine)> ')
saisie=prepare(saisie)
print ("Décryptage affine: "+DAffine(saisie))
saisie= raw_input('Entrer le texte à crypter(Cesar)> ')
print ("Cryptage cesar: "+CCesar(saisie))
saisie= raw_input('Entrer le texte à décrypter(Cesar)> ')
print ("Décryptage cesar: "+DCesar(saisie))
saisie = raw_input('Entrer le texte à crypter(Affine et Cesar)> ')
saisie=prepare(saisie)
print ("Cryptage combiné: "+CCesar(CAffine(saisie)))
saisie= raw_input('Entrer le texte à décrypter(Affine et Cesar)> ')
saisie=prepare(saisie)
print ("Décryptage combiné: "+DAffine(DCesar(saisie)))
saisie = raw_input("> ")
saisie = saisie.split(' ')
saisie0 = saisie[0]
saisie1 = saisie[1]
saisie2 = saisie[2]
if len(saisie) == 3:
	saisie0 = CCesar(saisie[0])
	saisie1 = CCesar(saisie[1])
	saisie2 = CCesar(saisie[2])
	del saisie[:]
	saisie.append(saisie0)
	saisie.append(saisie1)
	saisie.append(saisie2)
	saisie = " ".join(saisie)
	print (saisie)
elif len(saisie) == 1:
	print ("teste")
else:
	print ("Le message saisie contient plus de trois mots ou aucun")
"""
#Fin des fonctions de cryptage


# Menu

def __main__():
	if verif_os() == "posix":
		os.system("clear")
	if verif_os() == "windows":
		os.system("cls")
	banner()
	print ("\n")
__main__()

try:
	status = True

	while status == True :
		print (bcolors.ENDC + "Pour le manuel d'ulisation, tape "+ bcolors.GREEN +"h / help / aide")
		print (bcolors.ENDC + "Pour quitter le programme, tape "+ bcolors.RED +"quit / exit / bye")
		menu = input(bcolors.GREEN + "\n> ")

		if menu == "h" or menu == "aide" or menu == "help" :
			print(bcolors.ENDC + "\n[1] Pour envoyer un message par opérateur mobile\n[2] Pour envoyer un message via mail(Gmail, Hotmail ou Live)\n")

		if menu == "quit" or menu == "exit" or menu == "bye":
			print ("\n\n[-] QUITTING ...")
			sys.exit(0)

		if menu == "1":
			print (bcolors.RED + "[1] Envoyer un message crypté \n[2] Décrypter un message reçu\n")
			GSM = str(input(bcolors.RED + "> "))

			if GSM == "1":
				client = TwilioRestClient()
				client.messages.create(from_= input("Entre ton numéro: "),
							to = input("Entre son numéro: "),
							body = input("Entre ton message: "))
 
			if GSM == "2":
#En attente de code qui permet de recevoir les sms
				print("En attente du code qui permet de recevoir les sms")

		if menu == "2":
			print (bcolors.DARKCYAN + "[1] Envoyer un mail crypté\n[2] Decrypter un mail reçu")
			mail = str(input(bcolors.DARKCYAN + "> "))

			if mail == "1":
				boucle = True
				while boucle == True:

				    try:
					server_disponible = ["Gmail","Hotmail","Yahoo"] #Les seuls serveurs dont j'ai quelques infos 
					compteur = 1

					for server in server_disponible:
					    print ("["+str(compteur)+"]"+server)
					    compteur += 1

					server = str(input("Selectionner votre serveur: "))

					if server == "1":
						server = "smtp.gmail.com"
						port = 587

					if server == "2":
						server = "smtp.live.com"
						port = 587

					if server == "3":
						server= "smtp.mail.yahoo.com"
						port = 587

					compte_email = input("Entrez votre addresse gmail: ")
				 	password = getpass.getpass("Entrez votre mot de passe: ")
					email = input("L'addresse de la correspondant: ")
					message = input("Votre message:"+bcolors.CYAN+"\n\t") #Il fait egalement l'option spam
					print (bcolors.DARKCYAN+"Message crypté a envoyer>"+bcolors.GREEN+CCesar(message))
					NM = input(bcolors.DARKCYAN+"Entrez le nombre de fois que message dois être envoyé: "+bcolors.RED)  
					envoyer = 0

					try:
					    server = smtplib.SMTP(server, port)
					    server.ehlo()
					    server.starttls()
					    server.login(compte_email,password)

					    while (NM > envoyer):
						msg = "Vous avez envoyer dépuis cette addresse: "+compte_email+"\n Ce message: "+message+"\n"+str(envoyer)+"fois"
						server.sendmail(compte_email,email,message)
						envoyer += 1 
					    	print (envoyer)
						server.quit()
						print msg

					except KeyboardInterrupt:
					    print ("Stop\n"+msg)

					else:
					    print (bcolors.RED+"Aucun serveur ne correspond à votre demande!")
					    continue

				    except NameError:
					print (bcolors.RED+"Erreur. \nVeillez saisir correctement votre identifiant"+bcolors.DARKCYAN)
					boucle = True

				    except KeyboardInterrupt:
					print ("\nFin du programme")
					exit()

			if mail == "2":
#En attente de code qui permet de recevoir les mails
				print ("En attente du code qui permet de recevoir les mails")
except KeyboardInterrupt:
	print ("\nFin du programme")
	exit()
