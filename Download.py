_A='Download selesai'
import os,requests
try:from tqdm import tqdm
except:os.system('python -m pip install tqdm')
from urllib.parse import urlparse
import ntpath
tautan='https://raw.githubusercontent.com/FIRandZAH/FIRZAH/refs/heads/main/firzah_pycdc'
def njupuk_jeneng_berkas(saka_tautan):A=urlparse(saka_tautan);return ntpath.basename(A.path)
jeneng_berkas=njupuk_jeneng_berkas(tautan)
ukuran_wates=14*1024*1024
def ngundhuh(saka_tautan):
	A=requests.get(saka_tautan,stream=True);D=int(A.headers.get('content-length',0));E=1024;B=bytearray()
	with tqdm(total=D,unit='B',unit_scale=True,desc='Download')as F:
		for C in A.iter_content(E):B.extend(C);F.update(len(C))
	return bytes(B)
if os.path.exists(jeneng_berkas):
	ukuran_berkas=os.path.getsize(jeneng_berkas)
	if ukuran_berkas>=ukuran_wates:print('File udah ada')
	else:
		isi_berkas=ngundhuh(tautan)
		with open(jeneng_berkas,'wb')as f:f.write(isi_berkas)
		print(_A)
else:
	isi_berkas=ngundhuh(tautan)
	with open(jeneng_berkas,'wb')as f:f.write(isi_berkas)
	print(_A)
