#!/usr/bin/python
#-*-coding:utf-8-*-

import random
import os

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

