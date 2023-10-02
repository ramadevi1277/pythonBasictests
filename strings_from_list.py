lst = ['integers and floats', 'Int hint', 'Minting INT money', 'iNtegers and floats', 'Number integers float']
#for each in lst:
 #   lower = each.lower()
  #  if lower.startswith("int"):
   #         print (each)

#### Lambda function with filter.......

lst = list(filter(lambda x:  x.lower().startswith("int"), lst))
print('Filtered List : ', lst)
