import os, pathlib, configparser

config = configparser.ConfigParser()

config['msfconsole'] = {
    'LHOST'  : '',
    'LPORT'  : '',
    'payload': '',
    'handler': ''
}

config['msfvenom'] = {
    'LHOST'  : '',
    'LPORT'  : '',
    'format' : '',
    'payload': '',
    'output_filename' : ''
}

cmd   = ''

def loadconfig():
    if(config.read('metarun.conf')):
        print(f'Found your config at {pathlib.Path().resolve()}/metarun.conf')
        print(f'[+] msfconsole configure:')
        print(f'[i] LHOST: {config["msfconsole"]["LHOST"]}')
        print(f'[i] LPORT: {config["msfconsole"]["LPORT"]}')
        print(f'[i] Handler: {config["msfconsole"]["handler"]}')
        print(f'[i] Payload: {config["msfconsole"]["payload"]}')
        print(f'Command will be like this : ')
        print(f"""[CMD] msfconsole -x 'use {config["msfconsole"]["handler"]}; set payload {config["msfconsole"]["payload"]};set -g LHOST {config["msfconsole"]["LHOST"]};set -g LPORT {config["msfconsole"]["LPORT"]};'
            """.replace('\n',''))
        print('-' * 100)
        print(f'[+] msfvenom configure:')
        print(f'[i] LHOST: {config["msfvenom"]["LHOST"]}')
        print(f'[i] LPORT: {config["msfvenom"]["LPORT"]}')
        print(f'[i] Payload: {config["msfvenom"]["payload"]}')
        print(f'[i] Format: {config["msfvenom"]["format"]}')
        print(f'[i] Output filename: {config["msfvenom"]["output_filename"]}')
        print(f'Command will be like this : ')
        print(f"""[CMD] msfvenom LHOST={config["msfvenom"]["LHOST"]} LPORT={config["msfvenom"]['LPORT']} -p {config["msfvenom"]['payload']} -f {config["msfvenom"]['format']} -o {config["msfvenom"]['output_filename']}
        """.replace('\n',''))
        print('-' * 100)

def run(cmd):
    os.system('clear')
    os.system(command=cmd)

def main():
    while True:
        os.system('clear')
        loadconfig()
        # Setup
        print('Select option:')
        print('1: config\n2: run msfconsole with config\n3: run msfvenom with config')
        select = input("select>")

        if(int(select) == 1):
            os.system('clear')
            print('Pick a item:')
            print('1: msfconsole\n2: msfvenom\nelse: back')
            _select = input("select>")
            
            if(int(_select) == 1):
                new_config = {
                    'LHOST'  : input(f'LHOST (current: {config["msfconsole"]["LHOST"]}) >'),
                    'LPORT'  : input(f'LPORT (current: {config["msfconsole"]["LPORT"]}) >'),
                    'handler': input(f'Handler (current: {config["msfconsole"]["handler"]}) >'),
                    'payload': input(f'Payload (current: {config["msfconsole"]["payload"]}) >')
                }

                config['msfconsole'].update( (k,v) for k,v in new_config.items() if v != "")

                with open('./metarun.conf','w') as configfile:
                    config.write(configfile)

            elif(int(_select) == 2):
                new_config = {
                    'LHOST'  : input(f'LHOST (current: {config["msfvenom"]["LHOST"]}) >'),
                    'LPORT'  : input(f'LPORT (current: {config["msfconsole"]["LPORT"]}) >'),
                    'payload': input(f'Payload (current: {config["msfconsole"]["payload"]}) >'),
                    'format' : input(f'Format (current: {config["msfconsole"]["format"]}) >'),
                    'output_filename' : input(f'Output filename (current: {config["msfvenom"]["output_filename"]}) >')
                }

                config['msfvenom'].update( (k,v) for k,v in new_config.items() if v != "")

                with open('./metarun.conf','w') as configfile:
                    config.write(configfile)

            else:
                print('[X] Invalid select')
            

        elif(int(select) == 2):
            cmd = f"""
            msfconsole -x 'use {config["msfconsole"]["handler"]}; set payload {config["msfconsole"]["payload"]};set -g LHOST {config["msfconsole"]["LHOST"]};set -g LPORT {config["msfconsole"]["LPORT"]};'
            """.replace('\n','')
            run(cmd=cmd)
            break
            
        elif(int(select) == 3):
            cmd = f"""
                msfvenom LHOST={config["msfvenom"]["LHOST"]} LPORT={config["msfvenom"]['LPORT']} -p {config["msfvenom"]['payload']} -f {config["msfvenom"]['format']} -o {config["msfvenom"]['output_filename']}
            """.replace('\n','')
            run(cmd=cmd)
            break

        else:
            print('[X] Invalid select')


if __name__ == '__main__':
    main()
