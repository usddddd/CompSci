def sort_fruits(infile, outfile):
    """
    Write out alphabetically sorted fruits from input file unsorted_fruits.txt
    """
    input = open(infile, 'r')
    output = open(outfile, 'w')
    unsorted = input.readlines()
    
    unsorted.sort()
    count = 0
    for i in unsorted:
        print "Writing line %d" % count
        output.write(i)
        count += 1
    
    input.close()
    output.close()

        
if __name__ == '__main__':
    sort_fruits('unsorted_fruits.txt', 'sorted_fruits.txt')
    
    