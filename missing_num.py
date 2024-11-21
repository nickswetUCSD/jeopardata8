def missing_num(arr):
  '''Returns the single missing number from a list of all integers from 1 to n.'''

  n = len(arr) + 1
  return (n + 1)*n//2 - sum(arr)

def missing_num_bonus(arr):
  '''Returns the missing numbers and duplicated numbers from a list of all integers from 1 to n. ASSUMES LIST IS SORTED.'''
  
  # Create hash table
  ht = {}
  for i in arr:
    if i in ht:
      ht[i] += 1
    else:
      ht[i] = 1

  # Iterate through hash
  missing = []
  dup = []

  i = 0
  while i < arr[-1]:
    i += 1
    if i not in ht:
      missing.append(i)
    else:
      if ht[i] != 1:
        dup.append(i)
  return missing, dup