def list_with_and(inputlist: list)-> str:
    """A function that takes a list as input and returns a strin"""
    output_str = ''
    if inputlist != []:
        for i in range(len(inputlist)-1):
            output_str = output_str + inputlist[i] + ', '
        
        output_str= output_str + "and " + inputlist[len(inputlist)-1]
        print(output_str)

#examples
list_with_and(['one', 'two'])
list_with_and(['one', 'two', 'three'])
list_with_and([])





