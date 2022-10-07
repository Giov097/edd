from linked_stack_ext import LinkedStackExt


client = LinkedStackExt()

client.push(1)
client.push(20)
client.push(3)
client.push(3)
client.push(3)
client.push(3)
client.push(45)
client.push(70)
print("Original", client.__str__())
print("*"*50)
client.multi_pop(2)
print("After multi-pop", client.__str__()) # 6
client.exchange()
print("*"*50)
print("After exchange", client.__str__()) #1
client.replace_all(3, 4)
print("*"*50)
print("After replace", client.__str__())

