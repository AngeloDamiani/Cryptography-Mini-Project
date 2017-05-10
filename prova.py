import src.utility.AsciiConverter as AC
import src.utility.cryptography.Des as Des

d = Des("a67tiuhiuhjopjiogoijhd")
asd = "ciao diulojhiojlkkkkkkhsa"
casd = d.encrypt(asd)
print("Cyphertext = "+casd)
print(len(casd))
print("DecryptedText = "+d.decrypt(casd))
print(len(d.decrypt(casd)))

