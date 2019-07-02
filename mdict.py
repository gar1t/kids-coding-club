class mdict(dict):

    def __getitem__(self, key):
        if isinstance(key, tuple):
            return tuple((self[k] for k in key))
        return super(mdict, self).__getitem__(key)
