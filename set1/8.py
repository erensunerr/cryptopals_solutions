from multixor import HamDist
from one_char import ScoredData
from Cryptodome.Cipher import AES
import base64


et = open('8.txt', 'r').read().split('\n')
# print(et)
et_bytes = list()
for e in et:
    et_bytes.append(bytes.fromhex(e))


hamming_dist = []
for i in range(len(et_bytes)):
    hamming_dist.append(ScoredData(0, i))
    q = et_bytes[i]
    for block1 in range((len(et_bytes[0])//16)-1):
        for block2 in range((len(et_bytes[0])//16)-1):
            if block1 == block2:
                continue
            hamming_dist[i].score += (q[16*block1:16*(block1+1)] == q[16*(block2):16*(block2+1)])
            print(q[16*block1:16*(block1+1)], q[16*(block2):16*(block2+1)])
            # print(q[16*block:16*(block+1)], q[16*(block+1):16*(block+2)])
            # print(block, block2)

        # input()


hamming_dist = sorted(hamming_dist, key=lambda x: x.score, reverse=True)
print(hamming_dist)
print(et_bytes[155])
