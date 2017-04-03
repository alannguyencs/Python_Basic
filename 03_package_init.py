import demopackage
import imp

imp.reload(demopackage)

print (demopackage.__doc__)
print (demopackage.create_file.__doc__)