import random
import string
from model.project import Project

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [
            Project(name=random_string("proj", 5))
            for name in range(1)]