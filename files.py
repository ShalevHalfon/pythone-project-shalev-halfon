import pickle

def load_items(filename="items.pickle"):
    
    try:
        with open(filename, "rb") as f:
            items=pickle.load(f)
            return items
    except:
        with open(filename, "wb") as f:
            pickle.dump([], f)
            return []


def save_items(filename="items.pickle", items=[]):
    with open(filename, "wb") as f:
        pickle.dump(items, f)
    