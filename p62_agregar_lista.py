# Agregar elementos lista

nums = [80.3, 12.5, 60.2, 30.4]
otros = [110,120,130]

print(nums,len(nums))
nums.append(90)
nums.append(100)
print(nums,len(nums))
nums.insert(4,80)
print(nums,len(nums))
nums.extend(otros)
print(nums,len(nums))

