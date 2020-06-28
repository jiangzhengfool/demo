from multiprocessing  import Event

e = Event()
e.set()
print(e.is_set())