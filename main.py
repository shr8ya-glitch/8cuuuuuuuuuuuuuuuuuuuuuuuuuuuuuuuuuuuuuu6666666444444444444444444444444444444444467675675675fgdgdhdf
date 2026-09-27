scores=[1,3,5,7,9,11,13,15,17]
input("List:"+str(scores)+"n=9 Press Enter.")

guess=int(input("Enter any number in the list you wish to check"))

input("Binary search divides the array and checks.Press Enter.")
low,high=0,len(scores)-1
steps=0
while low<high:
    mid=((low+high))//2
    steps+=1
    print("Steps taken=",steps)
    if scores[mid]==guess:
        break
    elif scores[mid]<guess:
        low=mid+1
    elif scores[mid]>guess:
        high=mid-1
        print("Target element",guess,"present at",mid+1,"Postion")
        print("Steps grow slowly with n thus complexity is O(logn)")