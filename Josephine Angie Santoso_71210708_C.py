class NodeTabungan:
    no_rekening = None
    nama = None
    saldo = None
    next = None

    def __init__(self, no_rekening, nama, saldo=0):
        self.no_rekening = no_rekening
        self.nama = nama
        self.saldo = saldo


class SLNC:
    def __init__(self):
        self.no_rekening = None
        self.nama = None
        self.saldo = 0

    def __len__(self):
        return self.saldo

    def isEmpty(self):
        return self.saldo == 0

    def insert_head(self, e, nama, saldo):
        baru = NodeTabungan(e, nama, saldo)
        if self.isEmpty() == True:
            self._no_rekening = baru
            self._nama = baru
            self._saldo = baru
            self._saldo._next = None
        else:
            baru._next = self.insert_norekening
            self._norekening = baru
        self._saldo += 1
        print("Data masuk nomor rekening!")

    def printAll(self):
        if self.isEmpty() == False:
            bantu = self.no_rekening
            while(bantu != None):
                print(bantu.element, " ", end='')
                bantu = bantu.next
            print()
        else:
            print("Maaf besaran persen harus diantara 0-100")


slnc = SLNC()
slnc.insert_head(201, "Hanif", 250000)
slnc.insert_head(110, "Yudha", 150000)
slnc.print()
slnc.filter(100)
slnc.print()
slnc.update(200)
slnc.update(50)
slnc.print()
