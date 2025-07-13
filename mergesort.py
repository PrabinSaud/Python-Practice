#Merge and Sort Two Lists Using Bubble Sort Algrothim

def bubble_sort(arr):
    n= len(arr)
    for i in range(n):  # Outher loop
        for j in range(0,n-i-1): # Inner loop
            if arr[j]>arr[j+1]: 
                #Swaping the values
                arr[j],arr[j+1]=arr[j+1],arr[j]
               
    return arr
list1=[3,1,7]
list2=[4,2,5]
# Mergeing the list
merged_arr=list1+list2
print("Merged List: ",merged_arr)
# Calling the bubble_sort function
sorted_arr=bubble_sort(merged_arr)
print("Sorted List: ",sorted_arr)