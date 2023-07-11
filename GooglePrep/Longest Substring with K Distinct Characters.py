def KDistinct(string, K):
  #O(n) time and O(n) space - sliding window
  #come up with hashmap to store frequencies of chars and their occurences
  table = {}
  start = 0
  end = 0
  longest = 0 #to keep track of the longst char

  for end in range(string):
    newchar = string[end]
    #if char is not in hashmap, add else, update hashmap
    if newchar in table:
      table[newchar] += 1
    else:
      table[newchar] = 1

  #iterate, checking if len of hashmap is greater than k
  while len(table) > k:
    startchar = string[start]
    start += 1
    table[startchar] -= 1

  #if frequency is 0 remove char'
  if table[startchar] == 0:
    table.pop(startchar)

  #if new length is greater than longest
  if (end - start + 1) > longest:
    longest  = end - start + 1
  return longest
