def main():
    print_welcome()
    play_game()

def print_welcome():
    print("""
----------------------------------------------------------
----------- Welcome to the Legend of Link RPG! -----------
----------------------------------------------------------

A dark shadow was cast over the lands of Heirulez. You are
the chosen one who shall venture through the forests of
the web to defeat what lurks a few links off Google's main
results. The wwworld needs you to restore peaceful linking
to the internet...

""")

def play_game():
    creatures = [
        Creature('.docx', 1)
        Creature('FTP-Server', 5)
        Creature('www.xxx.com', 10)
        Creature('.php', 15)
        Creature('Pop-up Ad', 20)
        Creature('Paywall', 30)
        Creature('Wordpress-Site', 50)
        Creature('Google Data Center', 500)
    ]

if __name__ == '__main__':
    main()
