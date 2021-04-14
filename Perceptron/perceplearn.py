import sys
import os
import re
import glob
from collections import Counter
import random
# Análisis proporcionado en _
# Automatically Classifying Functional and Non-functional Requirements Using Supervised Machine Learning_
#
# | Categoría | Cantidad | Porcentage | Tamaño |
# | - | -: | -: | -: |
# | Funcional (F) | 255 | 40.80% | 20 |
# | Avalilability (A) | 21 | 3.36% | 19 |
# | Faul Tolerance (FT) | 10 | 1.60% | 19 |
# | Legal (L) | 13 | 2.08% | 18 |
# | Look & Feel (LF) | 38 | 6.08% | 20 |
# | Mantainabilty (MN) | 17 | 2.72% | 28 |
# | Operational (O) | 62 | 9.92% | 20 |
# | Performance (PE) | 54 | 8.64% | 22 |
# | Portability (PO) | 1 | 0.16% | 14 |
# | Scalability (SC) | 21 | 3.36% | 18 |
# | Security (SE) | 66 | 10.56% | 20 |
# | Usability (US) | 67 | 10.72% | 22 |
# | **Total** | **625** | **100%** |  |
def remove_stop_words(words):
    valid_words = []
    for word in words:
        if word not in stop_words:
            valid_words.append(word)
    return valid_words

def get_word_count(file):
    review = open(file, 'r').read().lower()
    review = re.sub(r"[^a-zA-Z]+", ' ', review)
    words = review.split()
    words = remove_stop_words(words)
    word_count_dict = Counter(words)
    return word_count_dict

def get_count_dictionary(files):
    count_dict = Counter()
    for file in files:
        count_dict += get_word_count(file)
    return dict(count_dict)

def initialize():
    for word in features:
        F['weights'][word] = 0
        A['weights'][word] = 0
        FT['weights'][word] = 0
        L['weights'][word] = 0
        LF['weights'][word] = 0
        MN['weights'][word] = 0
        O['weights'][word] = 0
        PE['weights'][word] = 0
        PO['weights'][word] = 0
        SC['weights'][word] = 0
        SE['weights'][word] = 0
        US['weights'][word] = 0

        F['weights_cached'][word] = 0
        A['weights_cached'][word] = 0
        FT['weights_cached'][word] = 0
        L['weights_cached'][word] = 0
        LF['weights_cached'][word] = 0
        MN['weights_cached'][word] = 0
        O['weights_cached'][word] = 0
        PE['weights_cached'][word] = 0
        PO['weights_cached'][word] = 0
        SC['weights_cached'][word] = 0
        SE['weights_cached'][word] = 0
        US['weights_cached'][word] = 0

def learn_metadata(classifier_type):
    classifier = metadata[classifier_type]
    classifier['activation'] = update_activation(classifier['activation'], classifier['bias'])
    if classifier['y'] * classifier['activation'] <= 0:
        for word in word_count_dict:
            classifier['weights'][word] = update_weight(classifier['weights'][word], classifier['y'], word_count_dict[word])
            classifier['weights_cached'][word] = update_cache_weight(classifier['weights_cached'][word], classifier['y'], c, word_count_dict[word])
        classifier['bias'] = update_bias(classifier['bias'], classifier['y'])
        classifier['bias_cached'] = update_cache_bias(classifier['bias_cached'], classifier['y'], c)

def update_activation(a, b):
    return a + b

def update_weight(w, y, x):
    return w + y * x

def update_cache_weight(u, y, c, x):
    return u + y * c * x

def update_bias(b, y):
    return b + y

def update_cache_bias(b, y, c):
    return b + y * c

def get_averaged_value(w, u, c):
    return w - (u/c)

def create_model(file_name, w1, b1, w2, b2, features):
    with open(file_name, 'w') as f:
        f.write("weights_polarity=" + str(w1) + "\n")
        f.write("bias_polarity=" + str(b1) + "\n")
        f.write("weights_origin=" + str(w2) + "\n")
        f.write("bias_origin=" + str(b2) + "\n")
        f.write("features=" + str(features) + "\n")


# folder = 'op_spam_training_data'
folder = sys.argv[1]

all_files = glob.glob(os.path.join(folder, '*/*/*/*.txt'))
stop_words = []

features = get_count_dictionary(all_files)
c = 1



metadata = {'polarity': {'activation': 0, 'weights': {}, 'weights_cached': {}, 'bias': 0, 'bias_cached': 0, 'y': 0},
            'origin': {'activation': 0, 'weights': {}, 'weights_cached': {}, 'bias': 0, 'bias_cached': 0, 'y': 0},
            'F': {'activation': 0, 'weights': {}, 'weights_cached': {}, 'bias': 0, 'bias_cached': 0, 'y': 0},
            'A': {'activation': 0, 'weights': {}, 'weights_cached': {}, 'bias': 0, 'bias_cached': 0, 'y': 0},
            'FT': {'activation': 0, 'weights': {}, 'weights_cached': {}, 'bias': 0, 'bias_cached': 0, 'y': 0},
            'L': {'activation': 0, 'weights': {}, 'weights_cached': {}, 'bias': 0, 'bias_cached': 0, 'y': 0},
            'LF': {'activation': 0, 'weights': {}, 'weights_cached': {}, 'bias': 0, 'bias_cached': 0, 'y': 0},
            'MN': {'activation': 0, 'weights': {}, 'weights_cached': {}, 'bias': 0, 'bias_cached': 0, 'y': 0},
            'O': {'activation': 0, 'weights': {}, 'weights_cached': {}, 'bias': 0, 'bias_cached': 0, 'y': 0},
            'PE': {'activation': 0, 'weights': {}, 'weights_cached': {}, 'bias': 0, 'bias_cached': 0, 'y': 0},
            'PO': {'activation': 0, 'weights': {}, 'weights_cached': {}, 'bias': 0, 'bias_cached': 0, 'y': 0},
            'SC': {'activation': 0, 'weights': {}, 'weights_cached': {}, 'bias': 0, 'bias_cached': 0, 'y': 0},
            'SE': {'activation': 0, 'weights': {}, 'weights_cached': {}, 'bias': 0, 'bias_cached': 0, 'y': 0},
            'US': {'activation': 0, 'weights': {}, 'weights_cached': {}, 'bias': 0, 'bias_cached': 0, 'y': 0},
            }
polarity = metadata['polarity']
origin = metadata['origin']
F = metadata['F']
A = metadata['A']
FT = metadata['FT']
L = metadata['L']
LF = metadata['LF']
MN = metadata['MN']
O = metadata['O']
PE = metadata['PE']
PO = metadata['PO']
SC = metadata['SC']
SE = metadata['SE']
US = metadata['US']

initialize()

for k in range(0, 10):
    random.Random(k * 5).shuffle(all_files)
    for file in all_files:
        F['activation'] = 0
        A['activation'] = 0
        FT['activation'] = 0
        L['activation'] = 0
        LF['activation'] = 0
        MN['activation'] = 0
        O['activation'] = 0
        PE['activation'] = 0
        PO['activation'] = 0
        SC['activation'] = 0
        SE['activation'] = 0
        US['activation'] = 0

        F['y'] = 1 if "F" in file else -1
        A['y'] = 1 if "A" in file else -1
        FT['y'] = 1 if "FT" in file else -1
        L['y'] = 1 if "L" in file else -1
        LF['y'] = 1 if "LF" in file else -1
        MN['y'] = 1 if "MN" in file else -1
        O['y'] = 1 if "O" in file else -1
        PE['y'] = 1 if "PE" in file else -1
        PO['y'] = 1 if "PO" in file else -1
        SC['y'] = 1 if "SC" in file else -1
        SE['y'] = 1 if "SE" in file else -1
        US['y'] = 1 if "US" in file else -1
        word_count_dict = get_word_count(file)
        for word in word_count_dict:
            if F['weights'][word] != 0:
                polarity['activation'] += polarity['weights'][word] * word_count_dict[word]
                origin['activation'] += origin['weights'][word] * word_count_dict[word]
                F['activation'] += F['weights'][word] * word_count_dict[word]
                A['activation'] += A['weights'][word] * word_count_dict[word]
                FT['activation'] += FT['weights'][word] * word_count_dict[word]
                L['activation'] += L['weights'][word] * word_count_dict[word]
                LF['activation'] += LF['weights'][word] * word_count_dict[word]
                MN['activation'] += MN['weights'][word] * word_count_dict[word]
                O['activation'] += O['weights'][word] * word_count_dict[word]
                PE['activation'] += PE['weights'][word] * word_count_dict[word]
                PO['activation'] += PO['weights'][word] * word_count_dict[word]
                SC['activation'] += SC['weights'][word] * word_count_dict[word]
                SE['activation'] += SE['weights'][word] * word_count_dict[word]
                US['activation'] += US['weights'][word] * word_count_dict[word]
        learn_metadata('polarity')
        learn_metadata('origin')
        learn_metadata('F')
        learn_metadata('A')
        learn_metadata('FT')
        learn_metadata('L')
        learn_metadata('LF')
        learn_metadata('MN')
        learn_metadata('O')
        learn_metadata('PE')
        learn_metadata('PO')
        learn_metadata('SC')
        learn_metadata('SE')
        learn_metadata('US')
        c += 1

create_model("vanillamodel.txt", polarity['weights'], polarity['bias'], origin['weights'], origin['bias'], features)

for word in polarity['weights']:
    polarity['weights'][word] = get_averaged_value(polarity['weights'][word], polarity['weights_cached'][word], c)
    origin['weights'][word] = get_averaged_value(origin['weights'][word], origin['weights_cached'][word], c)
polarity['bias'] = get_averaged_value(polarity['bias'], polarity['bias_cached'], c)
origin['bias'] = get_averaged_value(origin['bias'], origin['bias_cached'], c)

create_model("averagedmodel.txt", polarity['weights'], polarity['bias'], origin['weights'], origin['bias'], features)
