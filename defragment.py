import pickle
def read_chunks(name):
	with open(f'chunks/{name}_chunks', 'rb') as fp:
		return pickle.load(fp)

def create_file(data):
	r_name = data['name']
	r_ext = data['ext']
	r_chunks = data['chunks']

	with open(f'out/{r_name}.{r_ext}', 'wb') as fp:
		ot = b''.join(r_chunks)
		fp.write(ot)

def recover_file(name):
	data = read_chunks(name)
	create_file(data)

name = 'test'
recover_file(name)
