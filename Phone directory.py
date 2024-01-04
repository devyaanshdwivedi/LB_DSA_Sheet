#User function Template for python3

import re
class Solution:
    def displayContacts(self, n, contact, s):
        hoi=sorted(contact)
        jo = ' '.join(hoi)
        lst = []
        x = ''
        for i in s:
            x += i
            d = []
            orderRegex= re.compile(r'(\b{})'.format(x))
            mo= orderRegex.findall('{}'.format(jo))
            if mo:
                for j in hoi:
                    if re.search(r'\b{}'.format(mo[0]),j):
                        d.append(j)
                    if len(d)>=2 and d[-1]==d[-2]:
                        d.remove(d[-1])
                lst.append(d)
            else:
                lst.append([0])

        return lst