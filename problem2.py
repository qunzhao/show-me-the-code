#!/usr/bin/python -tt
# coding: utf-8

import random
import string
import mysql.connector

def gene_activation_code(number,length):  
  '''
  @number:生成激活码的个数 
  @length:生成激活码的长度 
  ''' 
  charlist = string.uppercase[:26]
  diglist = string.digits
  wlist = charlist + diglist
  
  #print charlist, diglist, wlist
  
  code_dict = {}
  code_num = 0
  act_code = ''
  while code_num < number:
    for i in range(length):
      randidx = random.randint(0, 35)
      act_code += wlist[randidx]
    if act_code not in code_dict:
      code_dict[act_code] = code_num
      code_num += 1
    else:
      print 'SAME'
    act_code = ''
  
  print code_dict
  return code_dict

def main():
  code_dict = gene_activation_code(10, 16)
  conn = mysql.connector.connect(user='root', password='Tqz+5276', database='test')
  cursor = conn.cursor()

  cursor.execute('drop table if exists code_list')
  cursor.execute('create table if not exists code_list (id integer primary key, code varchar(100))')
  
  for k, v in code_dict.items():
    #print k, v
    cursor.execute('insert into code_list (id, code) values (%d, "%s")' % (v, k))
  
  conn.commit()
  cursor.close()

  #cursor = conn.cursor()
  ##cursor.execute('select * from code_list where id = %d' % (1,))
  #cursor.execute('select * from code_list where id >= 0')
  #values = cursor.fetchall()
  #print values
  #cursor.close()
  #conn.close()


if __name__ == "__main__":  
  main()
