#!/bin/python

import math
import os
import random
import re
import sys

def is_matched(expr):
  left_braces = "({["  
  right_braces = ")}]" 
  stack = []
  for i in expr:
    if i in left_braces:
      stack.append(i) # push left delimiter on stack
    elif i in right_braces:
      if not stack:
        return False # nothing to match with
      if right_braces.index(i) != left_braces.index(stack.pop( )):
        return False # mismatched
  if not stack:
    return True
  else:
    return False

value = int(input())
for number in range(value):
  input_text = raw_input()
  if (is_matched(input_text) == True):
    print "Braces are balanced"
  else:
    print "Braces are not balanced"
