from django.db import models


class Personel(models.Model):
	#----------------------- Varsayılan Kolonlar -----------------------
	IsSaved    = models.BooleanField(default=False)
	IsVerified = models.BooleanField(default=False)
	IsDeleted  = models.BooleanField(default=False)
	IsCanceled = models.BooleanField(default=False)
	IsActive   = models.BooleanField(default=False)
	IsHidden   = models.BooleanField(default=False)
	CreateUser = models.CharField(max_length=50)
	CreateDate = models.DateTimeField()
	LastUpUser = models.CharField(max_length=50,null=True)
	LastUpDate = models.DateTimeField(null=True)
	#----------------------- Personel Tanımlamaları -----------------------
	Kodu             = models.CharField(max_length=10)
	IseGirisTarihi   = models.DateField()
	OgrenimDurumu    = models.CharField(max_length=50)
	Meslek           = models.CharField(max_length=50)
	DepartmanKodu    = models.CharField(max_length=10)
	GrupKodu         = models.CharField(max_length=10,null=True) 
	MuhasebeKodu     = models.CharField(max_length=10,null=True)
	IdariAmirKodu    = models.CharField(max_length=10,null=True)
	TeknikAmirKodu   = models.CharField(max_length=10,null=True)
	SigortaKodu      = models.CharField(max_length=10,null=True)
	SigortaBelgeTuru = models.CharField(max_length=50,null=True)
	Mevsim           = models.CharField(max_length=50,null=True)
	Kapsam           = models.CharField(max_length=50,null=True)
	UcretTipi        = models.CharField(max_length=10)
	DovizCinsi       = models.CharField(max_length=10,null=True)
	#----------------------- Personel Tercihleri -----------------------
	ServisNo            = models.CharField(max_length=10,null=True)
	OzurDerecesi        = models.CharField(max_length=50,null=True)	
	IzinGunu            = models.CharField(max_length=10,null=True)	
	SeyehatEngeli       = models.BooleanField(default=False)
	MesaiYapabilir      = models.BooleanField(default=False)
	MesaiTipi           = models.CharField(max_length=10,null=True)
	GeceVardiyasi       = models.BooleanField(default=False)
	IbadetIzni          = models.BooleanField(default=False)
	#----------------------- Personel İş Çıkışı \ İş Sonlandırma -----------------------
	CikisTarihi = models.DateField(null=True) #CikisTarihi
	CikisNedeni = models.CharField(max_length=1000,null=True)#CikisNedeni
	#----------------------- Personel Özlük Bilgileri -----------------------
	Isim                    = models.CharField(max_length=50)
	Soyisim                 = models.CharField(max_length=50)
	EskiSoyisim             = models.CharField(max_length=50,null=True)
	OrjinalDildeIsimSoyisim = models.CharField(max_length=50,null=True)
	KimlikNo                = models.IntegerField()
	Uyruk                   = models.CharField(max_length=50)
	Cinsiyet                = models.CharField(max_length=10)
	MedeniHal               = models.CharField(max_length=10)
	KanGrubu                = models.CharField(max_length=5)
	DogumTarihi             = models.DateField()
	DogumYeri               = models.CharField(max_length=50,null=True)
	KimlikteDin             = models.CharField(max_length=20)
	KimlikSeriNo            = models.CharField(max_length=9,null=True)
	Il                      = models.CharField(max_length=50,null=True)
	Ilce                    = models.CharField(max_length=50,null=True)
	Mahalle                 = models.CharField(max_length=50,null=True)	
	Koy                     = models.CharField(max_length=50,null=True)
	CiltNo                  = models.CharField(max_length=50,null=True) 
	SayfaNo                 = models.CharField(max_length=50,null=True)
	KutukNo                 = models.CharField(max_length=50,null=True)
	VerilisNedeni           = models.CharField(max_length=50,null=True)
	KayitNo                 = models.CharField(max_length=50,null=True)
	Tel1                    = models.CharField(max_length=15,null=True) 	
	Tel2                    = models.CharField(max_length=15,null=True)
	Tel3                    = models.CharField(max_length=15,null=True)
	Email                   = models.EmailField(max_length=50,null=True)
	KEP                     = models.EmailField(max_length=50,null=True)
	AcilDurumKisi1          = models.CharField(max_length=50,null=True)
	AcilDurumKisi1Tel       = models.CharField(max_length=20,null=True) 	
	AcilDurumKisi2          = models.CharField(max_length=50,null=True)
	AcilDurumKisi2Tel       = models.CharField(max_length=20,null=True)
	ReferansKisi1           = models.CharField(max_length=50,null=True)
	ReferansKisi1Tel        = models.CharField(max_length=20,null=True)
	ReferansKisi2           = models.CharField(max_length=50,null=True)
	ReferansKisi2Tel        = models.CharField(max_length=20,null=True)
	OzelNot                 = models.CharField(max_length=1000,null=True)

	def __str__(self):
		return self.Kodu