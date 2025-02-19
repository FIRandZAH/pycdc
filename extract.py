lllllllllllllll, llllllllllllllI, lllllllllllllIl = open, range, print
from os.path import exists as IIIlIIIIIlIIll
from Crypto.Cipher import AES as lIlllllIIIIIll
from Crypto.Protocol.KDF import scrypt as lIIIIlllIlllIl
def IIIIlllIIlIIIllllI(llIIlIIlllIlIlIIll, IlIllIIIlllIllIIlI):
    return lIIIIlllIlllIl(llIIlIIlllIlIlIIll.encode(), IlIllIIIlllIllIIlI, 32, N=2 ** 14, r=8, p=1)
def IIIIIIIIllIIIIlIlI(IIIlIlIIIlIIIIlllI, IIIIllIIllIIIlIlll):
    IIlIllIllIIlIIIIll = IIIlIlIIIlIIIIlllI[:16]
    lIlllIlIIIIIIllIll = IIIlIlIIIlIIIIlllI[16:]
    IIlIIIIIIlllllIllI = lIlllllIIIIIll.new(IIIIllIIllIIIlIlll, lIlllllIIIIIll.MODE_CBC, IIlIllIllIIlIIIIll)
    lIllIlIIIIIIIlIIll = IIlIIIIIIlllllIllI.decrypt(lIlllIlIIIIIIllIll)
    IIlIIIllIlIlIllIlI = lIllIlIIIIIIIlIIll[-1]
    llIllIllIlllIIllll = lIllIlIIIIIIIlIIll[:-IIlIIIllIlIlIllIlI]
    return llIllIllIlllIIllll
def lIIIllIllIIlIllIlI(IlllllIIIlllIlIlII, llIIlIIlllIlIlIIll, IIlIIllIIIIlllllll=20):
    lIIlIIlIllIlIIIIll = f'{IlllllIIIlllIlIlII}.salt'
    if not IIIlIIIIIlIIll(lIIlIIlIllIlIIIIll):
        lllllllllllllIl('failed.')
        return
    with lllllllllllllll(lIIlIIlIllIlIIIIll, 'rb') as IIlIlIIlIIllIIIlIl:
        IlIllIIIlllIllIIlI = IIlIlIIlIIllIIIlIl.read()
    IIIIllIIllIIIlIlll = IIIIlllIIlIIIllllI(llIIlIIlllIlIlIIll, IlIllIIIlllIllIIlI)
    with lllllllllllllll(IlllllIIIlllIlIlII, 'wb') as IIllIIlIIlllIlIlIl:
        for lIlIIIIllllllllllI in llllllllllllllI(1, IIlIIllIIIIlllllll + 1):
            IlIlIlIlllIlllIlII = f'{IlllllIIIlllIlIlII}{lIlIIIIllllllllllI}'
            with lllllllllllllll(IlIlIlIlllIlllIlII, 'rb') as IIllIIIlIIlIIlIllI:
                llIllIlIlllIIlIIll = IIllIIIlIIlIIlIllI.read()
                lIlllIlIlIllIIllIl = IIIIIIIIllIIIIlIlI(llIllIlIlllIIlIIll, IIIIllIIllIIIlIlll)
                IIllIIlIIlllIlIlIl.write(lIlllIlIlIllIIllIl)
    lllllllllllllIl(f'successfully extracted: {IlllllIIIlllIlIlII}')
lIIIllIllIIlIllIlI('firzah_pycdc', 'firzah', 20)
