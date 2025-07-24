
from django.db import models

class Snapshot(models.Model):
    kolo = models.IntegerField()
    created_ad = models.DateTimeField(auto_now_add=True)

class Aliance(models.Model):
    label = models.CharField(max_length=100)
    
    def __str__(self):
        return self.label

class Hrac(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    alance = models.ForeignKey(Aliance, related_name='hraci', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Zeme(models.Model):
    hrac = models.ForeignKey(Hrac, on_delete=models.CASCADE, related_name='zeme')
    name = models.CharField(max_length=100)
    snapshot = models.ForeignKey(Snapshot, on_delete=models.CASCADE)
    number = models.IntegerField()
    odehrana_kola = models.IntegerField()
    volna_kola = models.IntegerField()
    zasobnik_kola = models.IntegerField()
    ali_forum = models.CharField(max_length=10)
    logout = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.name}({self.number})-{self.hrac.name}({self.hrac.number})'
    

class ZemePrestige(models.Model):
    zeme = models.OneToOneField(Zeme, on_delete=models.CASCADE)
    prestiz = models.IntegerField() # (k)
    vojaku = models.IntegerField() # (k)
    tanku  = models.FloatField() # (k)
    stihacek = models.FloatField() # (k)
    bunkru = models.FloatField() # (k)
    mechu = models.IntegerField() # (k)
    agentu = models.IntegerField()

class ZemeBuildings(models.Model):
    zeme = models.OneToOneField(Zeme, on_delete=models.CASCADE)
    rozloha = models.FloatField() # (k)
    vesnice = models.IntegerField() # (k)
    mesta = models.IntegerField() # (k)
    obchodni_zony = models.IntegerField() # (k)
    farmy = models.IntegerField() # (k)
    laboratore = models.FloatField() # (k)
    tovarny = models.FloatField() # (k)
    kasarny = models.FloatField() # (k)
    elektrarny = models.FloatField() # (k)
    zabavních_stredisek = models.FloatField() # (k)
    vojenskych_zakladen = models.FloatField() # (k)
    stavebni_firmy = models.IntegerField()
    nezastavene_uzemi = models.FloatField() # (k)
    ruiny = models.FloatField() # (k)

class ZemeTechnologie(models.Model):
    zeme = models.OneToOneField(Zeme, on_delete=models.CASCADE)
    hospodarskych_celkem = models.FloatField() # (k)
    rychlost_stavby = models.FloatField() # (k)
    obchod = models.FloatField() # (k)
    hustota_zalidneni = models.FloatField() # (k)
    zemedelstvi = models.FloatField() # (k)
    automatizace_tovaren = models.FloatField() # (k)
    energie = models.FloatField() # (k)
    vojenskych_celkem = models.IntegerField() # (k)
    sila_zbrani = models.IntegerField() # (k)
    domaci_trh = models.FloatField() # (k)
    vyvoj_raket = models.FloatField() # (k)
    protiraketova_obrana = models.FloatField() # (k)
    sila_rozvedky = models.IntegerField() # (k)
    vyzkum_vesmiru = models.IntegerField() # (k)

class ZemeRakets(models.Model):
    zeme = models.OneToOneField(Zeme, on_delete=models.CASCADE)
    konvencnich = models.IntegerField()
    bio = models.IntegerField()
    emp = models.IntegerField()
    nuklearnich = models.IntegerField()

class ZemeBonus(models.Model):
    zeme = models.OneToOneField(Zeme, on_delete=models.CASCADE)
    vesnice = models.CharField(max_length=10)
    farmy = models.CharField(max_length=10)
    laboratore = models.CharField(max_length=10)
    tovarny = models.CharField(max_length=10)
    kasarny = models.CharField(max_length=10)
    elektrarny = models.CharField(max_length=10)
    vojenske_zakladny = models.CharField(max_length=10)
    penize = models.CharField(max_length=10)
    max_hospodarskych = models.CharField(max_length=10)
    max_vojenskych = models.CharField(max_length=10)
    efekt_hospodarskych = models.CharField(max_length=10)
    utok = models.CharField(max_length=10)
    obrana = models.CharField(max_length=10)
    kolonizace = models.CharField(max_length=10)
    zoldy = models.CharField(max_length=10)

class ZemeProduction(models.Model):
    zeme = models.OneToOneField(Zeme, on_delete=models.CASCADE)
    prirustek_penez = models.IntegerField() # (k)
    prirustek_jidla = models.IntegerField()
    prirustek_energie = models.IntegerField()
    prirustek_vojaku = models.IntegerField()
    prirustek_dilu_jednotek = models.IntegerField()
    prirustek_technologii = models.IntegerField()

class ZemeEvents(models.Model):
    zeme = models.OneToOneField(Zeme, on_delete=models.CASCADE)
    rozvoj_zacatek = models.CharField(max_length=10)
    hospodarska_pomoc = models.CharField(max_length=10)
    dostal_hp = models.IntegerField()
    poslal_hp = models.IntegerField()
    humanitarni_pomoc = models.CharField(max_length=10)
    do_pokladny = models.FloatField(max_length=10)
    z_pokladny = models.FloatField() # (m)

class ZemeComodits(models.Model):
    zeme = models.OneToOneField(Zeme, on_delete=models.CASCADE)
    penez = models.FloatField() # (m)
    jidla = models.FloatField() # (k)
    energie = models.FloatField() # (k)
    na_trhu = models.IntegerField()
    obyvatel = models.FloatField() # (m)
    

class ZemeAbilities(models.Model):
    zeme = models.OneToOneField(Zeme, on_delete=models.CASCADE)
    zkusennosti_armady = models.IntegerField() # (k)
    hodnost = models.IntegerField()
    zkusennosti_vek = models.IntegerField() # (k)
    sesvacenost = models.CharField(max_length=10)
    operaci_rozvedky = models.IntegerField()
    embargo_hlas = models.IntegerField()
    spokojenost = models.CharField(max_length=10)

class ZemeOthers(models.Model):
    zeme = models.OneToOneField(Zeme, on_delete=models.CASCADE)
    vesmir = models.FloatField(max_length=10)
    utopie_spokojenost = models.FloatField() # (k)
    android = models.CharField(max_length=10)
    ufo_sance = models.CharField(max_length=10)
