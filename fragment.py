import pickle

def get_bytes_from_file(filename):
    return open(filename, "rb").read()

def make_chunks(size, bts):
	return [bts[i:i + size] for i in range(0, len(bts), size)]

def save_chunks(data, name):
	with open(f'chunks/{name}', 'wb') as fp:
		pickle.dump(data, fp)

def prc_file(name, ext, chunk_size):
	input = get_bytes_from_file(f'input/{name}.{ext}')
	
	out =  {
		'name' : name, 
		'ext' : ext, 
		'chunks' : make_chunks(chunk_size, input)
	}

	save_chunks(out, f'{name}_chunks')

name = 'test'
ext = 'psb'

prc_file(name, ext, 1000)
