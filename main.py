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


def chk_pw(user,passwd,method='text'):
    '''
    chkpw(method,username,password)
    '''
    if(user == 'adam' and passwd == '123'):
        pass
        return 1
    return 0

def main():

    k=chk_pw(user='adam', passwd='123')
    print k


if __name__ == '__main__':
    main()
