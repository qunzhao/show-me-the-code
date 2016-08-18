#!/usr/bin/python -tt
# coding: utf-8

#激活码一般是由26个大写字母和10个数字任意组合而成，长度为12位或者16位的居多。
#一个激活码里的字符是可以重复的，而且必须要保证激活码是不能重复的。可以分别随
#机生成16个字符，然后组成一个字符串，放在字典中，通过字典来判断是否有重复的激
#活码。以下代码是用Python生成200个16位的激活码。
import random
import string

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
      #print 'SAME'
      pass
    act_code = ''
  
  print code_dict
  return code_dict
  
if __name__ == "__main__":  
  number = 20  
  length = 16
  gene_activation_code(number,length) 
