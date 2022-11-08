#This Programm will be used to finish off some university assigments for taxes AV2 exam 
custo = float(input("How much did you pay for the product: "))
taxa_imposto = float(input("Please, insert the amount of taxes: "))
taxa_imposto = taxa_imposto /100
soma_imposto = (custo * taxa_imposto) 

print(f'The amount of taxes was: {soma_imposto}')
print(f'The amount of it with the taxes was: {custo - soma_imposto}')
