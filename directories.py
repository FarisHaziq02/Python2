import os 
print(os.getcwd())

print(os.listdir())
os.mkdir('test_dir')
os.chdir('test_dir')
print(os.getcwd())

with open('test_file.txt', 'w') as f:
    pass

os.remove('test_file.txt')
os.chdir('..')
os.rmdir('test_dir')