array1 = [0, 3, 6, 26, 823]
array2 = [1, 8, 78]

def medians(nums1, nums2):
    o = sorted(nums1 + nums2)
    if len(o) % 2 == 0:
        m = ((o[len(o) // 2 - 1] + o[len(o) // 2]) / 2)
        print(f'{m} - медиана списка {o}')
        return m
    else:
        m = o[len(o) // 2]
        print(f'{m} - медиана списка {o}')
        return m
    
medians(array1, array2)