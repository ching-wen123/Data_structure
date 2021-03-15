#!/usr/bin/env python
# coding: utf-8

# In[60]:


from Cryptodome.Hash import MD5

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity

    def add(self, key):

        key_MD5 = self.mycryptoMD5(key)   #經過加密後的十進位數
        key_bucket = key_MD5 % (self.capacity)  #找出key對應的bucket
        #print(key + " bucket(add): ")
        #print(key_bucket)
        #cur = self.data[key_bucket]
        
        if self.data[key_bucket] is None:
             self.data[key_bucket] = ListNode(key_MD5)
        else:   #cur內有值
            cur = self.data[key_bucket]
            while cur.next is not None:
                cur = cur.next
            cur.next = ListNode(key_MD5)
        
    def remove(self, key):

        key_MD5 = self.mycryptoMD5(key)  #經過加密後的十進位數
        key_bucket = key_MD5 % self.capacity #找出key對應的bucket
        cur = self.data[key_bucket]
        pre = None
        
        if self.data[key_bucket] is None:
            return False
        else:      #bucket有值
            while cur is not None:
                if cur.val == key_MD5:
                    if pre is None:
                        self.data[key_bucket] = cur.next
                        pre = None
                        cur = self.data[key_bucket]
                    else:
                        pre.next = cur.next
                        pre = cur
                        cur = cur.next
                else:
                    pre = cur
                    cur = cur.next
                
    def contains(self, key):
 
        key_MD5 = self.mycryptoMD5(key)  #經過加密後的十進位數
        key_bucket = key_MD5 % self.capacity #找出key對應的bucket
        cur = self.data[key_bucket]
        
        if cur is None:
            return False
        else:   #cur is not None
            while cur is not None:
                if cur.val == key_MD5:
                    return True
                else:
                    cur = cur.next
            return False
            
    
    def mycryptoMD5(self, key):
        h=MD5.new()
        h.update(key.encode("utf-8"))
        h.hexdigest()       
        int(h.hexdigest(), 16)   
        return int(h.hexdigest(), 16)









