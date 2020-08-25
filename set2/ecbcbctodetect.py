from cbcmode import CBCD, CBCE
from Cryptodome.Random import get_random_bytes, random
from Cryptodome.Cipher import AES
from pkcs7pad import padpkcs7
from datetime import datetime
def encrypt(inp: bytes):
    key = get_random_bytes(16)
    s = get_random_bytes(random.randint(4, 11))
    e = get_random_bytes(random.randint(4, 11))
    inp = s + inp + e
    inp = padpkcs7(inp, 16)
    iv = get_random_bytes(16)
    isCBC = random.choice([True, False])
    if isCBC:
        out = CBCE(inp, iv, key).hex()
    else:
        aes = AES.new(key, AES.MODE_ECB)
        out = aes.encrypt(inp).hex()

    return out, isCBC


def generate_dataset(n=10000):
    f = open('ECBCBCDetectionDataSet-{}.csv'.format(datetime.now()), 'w')
    print("GENERATING")
    for i in range(n):
        out, isCBC = encrypt(get_random_bytes(random.randint(10, 70)))
        f.write(f"{out}, {isCBC},")
    f.close()
    print("DATASET GENERATION DONE")

import tensorflow as tf
import matplotlib.pyplot as plt

def import_data(file_path):
    CSV_COLUMNS = ['ct', 'CBC']
    dataset = tf.data.experimental.make_csv_dataset(file_path, batch_size=100)
    return dataset

def show_batch(dataset):
    for batch, label in dataset.take(1):
        for key, value in batch.items():
          print("{}: {}".format(key, value))

def plot_graphs(history, metric):
  plt.plot(history.history[metric])
  plt.plot(history.history['val_'+metric], '')
  plt.xlabel("Epochs")
  plt.ylabel(metric)
  plt.legend([metric, 'val_'+metric])
  plt.show()

def guess_mode_ai(inp: bytes):
    pass
