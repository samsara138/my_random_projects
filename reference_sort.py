#input reference list from file
def infile(name):
    text = []
    with open(name,'r') as reader:
        for line in reader:
            #clean end line character and empty lines
            line = line[:-1]
            if(line!=''):
                text.append(line)
    return text

#output sorted reference
def outfile(name,text):
    with open(name,'w') as writer:
        for i in text:
            writer.write(i)
            writer.write('\n\n')

def main():
    #change infile/outfile name if desire
    text = infile("reference.txt")
    text.sort()
    outfile("output.txt",text)

if __name__ == "__main__":
main()
