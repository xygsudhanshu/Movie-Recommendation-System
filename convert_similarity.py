import lzma
import pickle
import numpy as np

with lzma.open("similarity.lzma", "rb") as f:
    similarity = pickle.load(f)

print("Before:", similarity.dtype)

similarity = similarity.astype(np.float32)

print("After:", similarity.dtype)

with lzma.open("similarity_float32.lzma", "wb") as f:
    pickle.dump(similarity, f)

print("Done")