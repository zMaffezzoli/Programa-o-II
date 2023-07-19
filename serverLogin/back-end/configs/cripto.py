from hashlib import blake2b

def cifrar(senha):
    h = blake2b()
    em_bytes = bytes(senha, encoding = 'utf-8')
    h.update(em_bytes)
    return h.hexdigest()