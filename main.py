# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name: check_password
# Purpose: Make sure username and password are correct
#
# Author:      adaam
#
# Created:     12/12/2013
# Copyright:   (c) adaam 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# pickle provide function to write python data stracture to file, for performance can use cPickle
import pickle
import md5, sqlite3,random

def chk_pw(user,passwd,method='text'):
    '''
    chk_pw(user,passwd,method='text')
    '''

    if (method=='text') :
        if(user == 'adam' and passwd == '123'):
            pass
            return 1
        return 0
    if (method=='sql'):
##        import sqlite3
        conn = sqlite3.connect("C:\\Users\\user\\Downloads\\adam\\python\\SMS Project\\person_holiday\\user.db")
        cu = conn.cursor()
        cu.execute("select * from user where user = $user")
        res = cu.fetchall()
        if(passwd == res['password']):
            return 1
        return 0



def save_user(user,passwd,method='text'):
    '''
    save_user(user,passwd,method='text')
    '''
    if(method=='text'):
        f = open('C:\\Users\\user\\Downloads\\adam\\python\\SMS Project\\person_holiday\\pass.txt','rb+')
        user_dict = pickle.load(f)
##        f.close()
##        f = open('C:\\Users\user\Downloads\adam\python\SMS Project\person_holiday','wb')
        user_dict[user]=passwd
        pickle.dump(user_dict,f)
        f.close()
    if(method=='sql'):
##        import sqlite3
        conn = sqlite3.connect("C:\\Users\\user\\Downloads\\adam\\python\\SMS Project\\person_holiday\\user.db")
        salt = []
        for k in range(60):
            salt.append(random.choice('qwertyuiopasdfghjklzxcvbnm8521963470'))
        conn.execute("insert into user(name,password) values($user,$passwd)")
        conn.commit()


def main():

    k=chk_pw(user='adam', passwd='123')
    print k

if __name__ == '__main__':
    main()
