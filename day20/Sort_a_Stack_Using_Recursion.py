def insertSorted(stack, element):
    if not stack or stack[-1] <= element:
        stack.append(element)
        return
    top = stack.pop()
    insertSorted(stack, element)
    stack.append(top)
def sortStack(stack):
    if len(stack) <= 1:
        return
    top = stack.pop()
    sortStack(stack)
    insertSorted(stack, top)
stack = [3, 1, 4, 2]
sortStack(stack)
print("Sorted stack:", stack)
