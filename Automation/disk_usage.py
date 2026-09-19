import shutil
du = shutil.disk_usage("/")
print("Total: %d GiB" % (du.total / (2**30)))

diskfree = du.free/du.total * 100
print("Disk Free: %d%%" % diskfree)