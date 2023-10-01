
# acessing
Courses=['History','Math','Physics','Comp Sci']
print(Courses)
print(Courses[0:2])
print(Courses[:3])
print(Courses[-1])


courses=['History','Math','Physics','CompSci']
courses_2=['Art','Education']
# courses.append(courses_2)
courses.insert(0,courses_2)
courses.reverse();
print(courses[0]);

courses.remove('Math')
print(courses)
courses.pop()
print(courses)

# Sorting
courses=['History','Math','Physics','CompSci']
courses.sort()
print(courses)

# min,max,sum function
nums=[12,13,90,24,2,67]
nums.sort()
print(nums)
print(min(nums))
print(max(nums))
print(sum(nums))



# list(mutable)
List_1=['History','Math','Physics','CompSci']
List_2=List_1
print(List_1)
print(List_2)
List_1[0]='Art'
print(List_1)
print(List_2)


# immutable(tuple)
tuple_1=('History','Math','Physics','CompSci')
tupel_2=tuple_1
print(tuple_1)
print(tupel_2)
tuple_1[0]='Art'
print(tuple_1)
print(tupel_2)



# sets(intersection,union,difference)
set_1={'History','Math','Physics','CompSci'}
set_2={'History','Math','design','Sanskrit'}
# print(set)

print((set_1).intersection(set_2))
print((set_1).difference(set_2))
print((set_1).union(set_2))
