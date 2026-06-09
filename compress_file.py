import pickle
import compress_pickle

# normal pkl load
with open("similarity.pkl", "rb") as f:
    similarity = pickle.load(f)

# compressed save
compress_pickle.dump(similarity, "similarity.lzma")