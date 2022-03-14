from django.db import models

# Create your models here.
class Pedido(models.Model):
    cliente = models.CharField(max_length=30)
    total = models.DecimalField(max_digits=6, decimal_places=2)
    entrega = models.BooleanField(default=False)
    obs = models.TextField(blank=True, null=True)
    data = models.DateField(auto_now_add=True, auto_now=False)

    
    #Cardápio de Lanches
    Lanche_choice = (
        ('----','----'),
        ('X-Salada', 'X-Salada'),
        ('X-Duplo Salada','X-Duplo Salada'),
        ('X-Burger','X-Burger'),
        ('Frango','X-Frango'),
        ('X-Frango Bacon','X-Frango Bacon'),
        ('X-Frango Egg', 'X-Frango Egg'),
        ('X-Frango Bacon Egg','X-Frango Bacon Egg'),
        ('X-Egg', 'X-Egg'),
        ('X-Bacon','X-Bacon'),
        ('X-Bacon Egg','X-Bacon Egg'),
        ('Hot Dog', 'Hot Dog'),
        ('Dog Egg', 'Dog Egg'),
        ('Dog Bacon','Dog Bacon'),
        ('Dog Bacon Egg','Dog Bacon Egg'),
        ('X-Dogão', 'X-Dogão'),
        ('X-Calabresa','X-Calabresa'),
        ('X-Tudo','X-Tudo')
    )
    l1_lanche = models.CharField(max_length=20, verbose_name='Lanche', choices=Lanche_choice, default='----')
    l1_alface = models.BooleanField(default=False, verbose_name='s/ Alface')
    l1_tomate = models.BooleanField(default=False, verbose_name='s/ Tomate')
    l1_maionese = models.BooleanField(default=False, verbose_name='s/ Maionese')
    l1_hellmanns = models.BooleanField(default=False, verbose_name='c/ Hellmanns')
    l1_pure = models.BooleanField(default=False, verbose_name='s/ Purê')
    l1_milho = models.BooleanField(default=False, verbose_name='s/ Milho')
    l1_anel = models.BooleanField(default=False, verbose_name='c/ Anel de Cebola')
    l1_cheddar = models.BooleanField(default=False, verbose_name='c/ Cheddar')
    l1_catupiry = models.BooleanField(default=False, verbose_name='c/ Catupiry')
    l1_quant_lanche = models.IntegerField(blank=True, null=True, verbose_name='Quantidade')
    l1_preco_lanche = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Preço')
    l1_total_lanche = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Total', blank=True, null=True)
    l1_adicional_maionese = models.BooleanField(default=False, verbose_name='Adicional de Maionese')

    l2_lanche = models.CharField(max_length=20, choices=Lanche_choice, default='----', verbose_name='Lanche')
    l2_alface = models.BooleanField(default=False, verbose_name='s/ Alface')
    l2_tomate = models.BooleanField(default=False, verbose_name='s/ Tomate')
    l2_maionese = models.BooleanField(default=False, verbose_name='s/ Maionese')
    l2_hellmanns = models.BooleanField(default=False, verbose_name='c/ Hellmanns')
    l2_pure = models.BooleanField(default=False, verbose_name='s/ Purê')
    l2_milho = models.BooleanField(default=False, verbose_name='s/ Milho')
    l2_anel = models.BooleanField(default=False, verbose_name='c/ Anel de Cebola')
    l2_cheddar = models.BooleanField(default=False, verbose_name='c/ Cheddar')
    l2_catupiry = models.BooleanField(default=False, verbose_name='c/ Catupiry')
    l2_quant_lanche = models.IntegerField(blank=True, null=True, verbose_name='Quantidade')
    l2_preco_lanche = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Preço')
    l2_total_lanche = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Total', blank=True, null=True)
    l2_adicional_maionese = models.BooleanField(default=False, verbose_name='Adicional de Maionese')
   
    l3_lanche = models.CharField(max_length=20, choices=Lanche_choice, default='----', verbose_name='Lanche')
    l3_alface = models.BooleanField(default=False, verbose_name='s/ Alface')
    l3_tomate = models.BooleanField(default=False, verbose_name='s/ Tomate')
    l3_maionese = models.BooleanField(default=False, verbose_name='s/ Maionese')
    l3_hellmanns = models.BooleanField(default=False, verbose_name='c/ Hellmanns')
    l3_pure = models.BooleanField(default=False, verbose_name='s/ Purê')
    l3_milho = models.BooleanField(default=False, verbose_name='s/ Milho')
    l3_anel = models.BooleanField(default=False, verbose_name='c/ Anel de Cebola')
    l3_cheddar = models.BooleanField(default=False, verbose_name='c/ Cheddar')
    l3_catupiry = models.BooleanField(default=False, verbose_name='c/ Catupiry')
    l3_quant_lanche = models.IntegerField(blank=True, null=True, verbose_name='Quantidade')
    l3_preco_lanche = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Preço')
    l3_total_lanche = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Total', blank=True, null=True)
    l3_adicional_maionese = models.BooleanField(default=False, verbose_name='Adicional de Maionese')   
   
    l4_lanche = models.CharField(max_length=20, choices=Lanche_choice, default='----', verbose_name='Lanche')
    l4_alface = models.BooleanField(default=False, verbose_name='s/ Alface')
    l4_tomate = models.BooleanField(default=False, verbose_name='s/ Tomate')
    l4_maionese = models.BooleanField(default=False, verbose_name='s/ Maionese')
    l4_hellmanns = models.BooleanField(default=False, verbose_name='c/ Hellmanns')
    l4_pure = models.BooleanField(default=False, verbose_name='s/ Purê')
    l4_milho = models.BooleanField(default=False, verbose_name='s/ Milho')
    l4_anel = models.BooleanField(default=False, verbose_name='c/ Anel de Cebola')
    l4_cheddar = models.BooleanField(default=False, verbose_name='c/ Cheddar')
    l4_catupiry = models.BooleanField(default=False, verbose_name='c/ Catupiry')
    l4_quant_lanche = models.IntegerField(blank=True, null=True, verbose_name='Quantidade')
    l4_preco_lanche = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Preço')
    l4_total_lanche = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Total', blank=True, null=True)
    l4_adicional_maionese = models.BooleanField(default=False, verbose_name='Adicional de Maionese')   

    l5_lanche = models.CharField(max_length=20, choices=Lanche_choice, default='----', verbose_name='Lanche')
    l5_alface = models.BooleanField(default=False, verbose_name='s/ Alface')
    l5_tomate = models.BooleanField(default=False, verbose_name='s/ Tomate')
    l5_maionese = models.BooleanField(default=False, verbose_name='s/ Maionese')
    l5_hellmanns = models.BooleanField(default=False, verbose_name='c/ Hellmanns')
    l5_pure = models.BooleanField(default=False, verbose_name='s/ Purê')
    l5_milho = models.BooleanField(default=False, verbose_name='s/ Milho')
    l5_anel = models.BooleanField(default=False, verbose_name='c/ Anel de Cebola')
    l5_cheddar = models.BooleanField(default=False, verbose_name='c/ Cheddar')
    l5_catupiry = models.BooleanField(default=False, verbose_name='c/ Catupiry')
    l5_quant_lanche = models.IntegerField(blank=True, null=True, verbose_name='Quantidade')
    l5_preco_lanche = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Preço')
    l5_total_lanche = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Total', blank=True, null=True)
    l5_adicional_maionese = models.BooleanField(default=False, verbose_name='Adicional de Maionese')   
   
    l6_lanche = models.CharField(max_length=20, choices=Lanche_choice, default='----', verbose_name='Lanche')
    l6_alface = models.BooleanField(default=False, verbose_name='s/ Alface')
    l6_tomate = models.BooleanField(default=False, verbose_name='s/ Tomate')
    l6_maionese = models.BooleanField(default=False, verbose_name='s/ Maionese')
    l6_hellmanns = models.BooleanField(default=False, verbose_name='c/ Hellmanns')
    l6_pure = models.BooleanField(default=False, verbose_name='s/ Purê')
    l6_milho = models.BooleanField(default=False, verbose_name='s/ Milho')
    l6_anel = models.BooleanField(default=False, verbose_name='c/ Anel de Cebola')
    l6_cheddar = models.BooleanField(default=False, verbose_name='c/ Cheddar')
    l6_catupiry = models.BooleanField(default=False, verbose_name='c/ Catupiry')
    l6_quant_lanche = models.IntegerField(blank=True, null=True, verbose_name='Quantidade')
    l6_preco_lanche = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Preço')
    l6_total_lanche = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Total', blank=True, null=True)
    l6_adicional_maionese = models.BooleanField(default=False, verbose_name='Adicional de Maionese')   
   
    l7_lanche = models.CharField(max_length=20, choices=Lanche_choice, default='----', verbose_name='Lanche')
    l7_alface = models.BooleanField(default=False, verbose_name='s/ Alface')
    l7_tomate = models.BooleanField(default=False, verbose_name='s/ Tomate')
    l7_maionese = models.BooleanField(default=False, verbose_name='s/ Maionese')
    l7_hellmanns = models.BooleanField(default=False, verbose_name='c/ Hellmanns')
    l7_pure = models.BooleanField(default=False, verbose_name='s/ Purê')
    l7_milho = models.BooleanField(default=False, verbose_name='s/ Milho')
    l7_anel = models.BooleanField(default=False, verbose_name='c/ Anel de Cebola')
    l7_cheddar = models.BooleanField(default=False, verbose_name='c/ Cheddar')
    l7_catupiry = models.BooleanField(default=False, verbose_name='c/ Catupiry')
    l7_quant_lanche = models.IntegerField(blank=True, null=True, verbose_name='Quantidade')
    l7_preco_lanche = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Preço')
    l7_total_lanche = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Total', blank=True, null=True)
    l7_adicional_maionese = models.BooleanField(default=False, verbose_name='Adicional de Maionese')  

    l8_lanche = models.CharField(max_length=20, choices=Lanche_choice, default='----', verbose_name='Lanche')
    l8_alface = models.BooleanField(default=False, verbose_name='s/ Alface')
    l8_tomate = models.BooleanField(default=False, verbose_name='s/ Tomate')
    l8_maionese = models.BooleanField(default=False, verbose_name='s/ Maionese')
    l8_hellmanns = models.BooleanField(default=False, verbose_name='c/ Hellmanns')
    l8_pure = models.BooleanField(default=False, verbose_name='s/ Purê')
    l8_milho = models.BooleanField(default=False, verbose_name='s/ Milho')
    l8_anel = models.BooleanField(default=False, verbose_name='c/ Anel de Cebola')
    l8_cheddar = models.BooleanField(default=False, verbose_name='c/ Cheddar')
    l8_catupiry = models.BooleanField(default=False, verbose_name='c/ Catupiry')
    l8_quant_lanche = models.IntegerField(blank=True, null=True, verbose_name='Quantidade')
    l8_preco_lanche = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Preço')
    l8_total_lanche = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Total', blank=True, null=True)
    l8_adicional_maionese = models.BooleanField(default=False, verbose_name='Adicional de Maionese')    

    l9_lanche = models.CharField(max_length=20, choices=Lanche_choice, default='----', verbose_name='Lanche')
    l9_alface = models.BooleanField(default=False, verbose_name='s/ Alface')
    l9_tomate = models.BooleanField(default=False, verbose_name='s/ Tomate')
    l9_maionese = models.BooleanField(default=False, verbose_name='s/ Maionese')
    l9_hellmanns = models.BooleanField(default=False, verbose_name='c/ Hellmanns')
    l9_pure = models.BooleanField(default=False, verbose_name='s/ Purê')
    l9_milho = models.BooleanField(default=False, verbose_name='s/ Milho')
    l9_anel = models.BooleanField(default=False, verbose_name='c/ Anel de Cebola')
    l9_cheddar = models.BooleanField(default=False, verbose_name='c/ Cheddar')
    l9_catupiry = models.BooleanField(default=False, verbose_name='c/ Catupiry')
    l9_quant_lanche = models.IntegerField(blank=True, null=True, verbose_name='Quantidade')
    l9_preco_lanche = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Preço')
    l9_total_lanche = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Total', blank=True, null=True)
    l9_adicional_maionese = models.BooleanField(default=False, verbose_name='Adicional de Maionese')   

    l10_lanche = models.CharField(max_length=20, choices=Lanche_choice, default='----', verbose_name='Lanche')
    l10_alface = models.BooleanField(default=False, verbose_name='s/ Alface')
    l10_tomate = models.BooleanField(default=False, verbose_name='s/ Tomate')
    l10_maionese = models.BooleanField(default=False, verbose_name='s/ Maionese')
    l10_hellmanns = models.BooleanField(default=False, verbose_name='c/ Hellmanns')
    l10_pure = models.BooleanField(default=False, verbose_name='s/ Purê')
    l10_milho = models.BooleanField(default=False, verbose_name='s/ Milho')
    l10_anel = models.BooleanField(default=False, verbose_name='c/ Anel de Cebola')
    l10_cheddar = models.BooleanField(default=False, verbose_name='c/ Cheddar')
    l10_catupiry = models.BooleanField(default=False, verbose_name='c/ Catupiry')
    l10_quant_lanche = models.IntegerField(blank=True, null=True, verbose_name='Quantidade')
    l10_preco_lanche = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Preço')
    l10_total_lanche = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Total', blank=True, null=True)
    l10_adicional_maionese = models.BooleanField(default=False, verbose_name='Adicional de Maionese')   

    #Cardápio de bebidas
    bebida_choice = (
        ('----','----'),
        ('Refrigerante Lata', 'Refrigerante Lata'),
        ('Refrigerante 600','Refrigerante 600'),
        ('Refrigerante 1,5L','Refrigerante 1,5L'),
        ('Suco com água','Suco com água'),
        ('Suco com leite','Suco com leite'),
    )
    l1_bebida = models.CharField(max_length=20, choices=bebida_choice, default='----', verbose_name='Bebida')
    l1_quant_bebida = models.IntegerField(blank=True, null=True, verbose_name='Quantidade')
    l1_preco_bebida = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Preço')
    l1_total_bebida = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Total')

    l2_bebida = models.CharField(max_length=20, choices=bebida_choice, default='----', verbose_name='Bebida')
    l2_quant_bebida = models.IntegerField(blank=True, null=True, verbose_name='Quantidade')
    l2_preco_bebida = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Preço')
    l2_total_bebida = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Total')

    l3_bebida = models.CharField(max_length=20, choices=bebida_choice, default='----', verbose_name='Bebida')
    l3_quant_bebida = models.IntegerField(blank=True, null=True, verbose_name='Quantidade')
    l3_preco_bebida = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Preço')
    l3_total_bebida = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Total')

    l4_bebida = models.CharField(max_length=20, choices=bebida_choice, default='----', verbose_name='Bebida')
    l4_quant_bebida = models.IntegerField(blank=True, null=True, verbose_name='Quantidade')
    l4_preco_bebida = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Preço')
    l4_total_bebida = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Total')

    l5_bebida = models.CharField(max_length=20, choices=bebida_choice, default='----', verbose_name='Bebida')
    l5_quant_bebida = models.IntegerField(blank=True, null=True, verbose_name='Quantidade')
    l5_preco_bebida = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Preço')
    l5_total_bebida = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Total')

    l6_bebida = models.CharField(max_length=20, choices=bebida_choice, default='----', verbose_name='Bebida')
    l6_quant_bebida = models.IntegerField(blank=True, null=True, verbose_name='Quantidade')
    l6_preco_bebida = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Preço')
    l6_total_bebida = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Total')

    l7_bebida = models.CharField(max_length=20, choices=bebida_choice, default='----', verbose_name='Bebida')
    l7_quant_bebida = models.IntegerField(blank=True, null=True, verbose_name='Quantidade')
    l7_preco_bebida = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Preço')
    l7_total_bebida = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Total')

    l8_bebida = models.CharField(max_length=20, choices=bebida_choice, default='----', verbose_name='Bebida')
    l8_quant_bebida = models.IntegerField(blank=True, null=True, verbose_name='Quantidade')
    l8_preco_bebida = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Preço')
    l8_total_bebida = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Total')

    l9_bebida = models.CharField(max_length=20, choices=bebida_choice, default='----', verbose_name='Bebida')
    l9_quant_bebida = models.IntegerField(blank=True, null=True, verbose_name='Quantidade')
    l9_preco_bebida = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Preço')
    l9_total_bebida = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Total')

    l10_bebida = models.CharField(max_length=20, choices=bebida_choice, default='----', verbose_name='Bebida')
    l10_quant_bebida = models.IntegerField(blank=True, null=True, verbose_name='Quantidade')
    l10_preco_bebida = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Preço')
    l10_total_bebida = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Total')

    #Cardápio de porções
    porcao_choice = (
        ('----','----'),
        ('Batata Meia', 'Batata Meia'),
        ('Batata Inteira','Batata Inteira'),
        ('Anel de Cebola','Anel de Cebola'),
        ('Frango','Fango'),
        ('Mini fritas', 'Mini fritas'),
        ('Especial','Especial'),
    )
    l1_porcao = models.CharField(max_length=20, choices=porcao_choice, verbose_name='Porção', default='----')
    l1_bacon = models.BooleanField(default=False, verbose_name='c/ Bacon')
    l1_cheddarp = models.BooleanField(default=False, verbose_name='c/ Cheddar')
    l1_quant_porcao = models.IntegerField(blank=True, null=True, verbose_name='Quantidade')
    l1_preco_porcao = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Preço')
    l1_total_porcao = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Total')

    l2_porcao = models.CharField(max_length=20, choices=porcao_choice, verbose_name='Porção', default='----')
    l2_bacon = models.BooleanField(default=False, verbose_name='c/ Bacon')
    l2_cheddarp = models.BooleanField(default=False, verbose_name='c/ Cheddar')
    l2_quant_porcao = models.IntegerField(blank=True, null=True, verbose_name='Quantidade')
    l2_preco_porcao = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Preço')
    l2_total_porcao = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Total')

    l3_porcao = models.CharField(max_length=20, choices=porcao_choice, verbose_name='Porção', default='----')
    l3_bacon = models.BooleanField(default=False, verbose_name='c/ Bacon')
    l3_cheddarp = models.BooleanField(default=False, verbose_name='c/ Cheddar')
    l3_quant_porcao = models.IntegerField(blank=True, null=True, verbose_name='Quantidade')
    l3_preco_porcao = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Preço')
    l3_total_porcao = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Total')

    l4_porcao = models.CharField(max_length=20, choices=porcao_choice, verbose_name='Porção', default='----')
    l4_bacon = models.BooleanField(default=False, verbose_name='c/ Bacon')
    l4_cheddarp = models.BooleanField(default=False, verbose_name='c/ Cheddar')
    l4_quant_porcao = models.IntegerField(blank=True, null=True, verbose_name='Quantidade')
    l4_preco_porcao = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Preço')
    l4_total_porcao = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Total')

    l4_porcao = models.CharField(max_length=20, choices=porcao_choice, verbose_name='Porção', default='----')
    l4_bacon = models.BooleanField(default=False, verbose_name='c/ Bacon')
    l4_cheddarp = models.BooleanField(default=False, verbose_name='c/ Cheddar')
    l4_quant_porcao = models.IntegerField(blank=True, null=True, verbose_name='Quantidade')
    l4_preco_porcao = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Preço')
    l4_total_porcao = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Total')

    l5_porcao = models.CharField(max_length=20, choices=porcao_choice, verbose_name='Porção', default='----')
    l5_bacon = models.BooleanField(default=False, verbose_name='c/ Bacon')
    l5_cheddarp = models.BooleanField(default=False, verbose_name='c/ Cheddar')
    l5_quant_porcao = models.IntegerField(blank=True, null=True, verbose_name='Quantidade')
    l5_preco_porcao = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Preço')
    l5_total_porcao = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Total')

    l6_porcao = models.CharField(max_length=20, choices=porcao_choice, verbose_name='Porção', default='----')
    l6_bacon = models.BooleanField(default=False, verbose_name='c/ Bacon')
    l6_cheddarp = models.BooleanField(default=False, verbose_name='c/ Cheddar')
    l6_quant_porcao = models.IntegerField(blank=True, null=True, verbose_name='Quantidade')
    l6_preco_porcao = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Preço')
    l6_total_porcao = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Total')

    l7_porcao = models.CharField(max_length=20, choices=porcao_choice, verbose_name='Porção', default='----')
    l7_bacon = models.BooleanField(default=False, verbose_name='c/ Bacon')
    l7_cheddarp = models.BooleanField(default=False, verbose_name='c/ Cheddar')
    l7_quant_porcao = models.IntegerField(blank=True, null=True, verbose_name='Quantidade')
    l7_preco_porcao = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Preço')
    l7_total_porcao = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Total')

    l8_porcao = models.CharField(max_length=20, choices=porcao_choice, verbose_name='Porção', default='----')
    l8_bacon = models.BooleanField(default=False, verbose_name='c/ Bacon')
    l8_cheddarp = models.BooleanField(default=False, verbose_name='c/ Cheddar')
    l8_quant_porcao = models.IntegerField(blank=True, null=True, verbose_name='Quantidade')
    l8_preco_porcao = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Preço')
    l8_total_porcao = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Total')

    l9_porcao = models.CharField(max_length=20, choices=porcao_choice, verbose_name='Porção', default='----')
    l9_bacon = models.BooleanField(default=False, verbose_name='c/ Bacon')
    l9_cheddarp = models.BooleanField(default=False, verbose_name='c/ Cheddar')
    l9_quant_porcao = models.IntegerField(blank=True, null=True, verbose_name='Quantidade')
    l9_preco_porcao = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Preço')
    l9_total_porcao = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Total')

    l10_porcao = models.CharField(max_length=20, choices=porcao_choice, verbose_name='Porção', default='----')
    l10_bacon = models.BooleanField(default=False, verbose_name='c/ Bacon')
    l10_cheddarp = models.BooleanField(default=False, verbose_name='c/ Cheddar')
    l10_quant_porcao = models.IntegerField(blank=True, null=True, verbose_name='Quantidade')
    l10_preco_porcao = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Preço')
    l10_total_porcao = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Total')

    #Cardápio de açaí
    acai_choice = (
        ('----','----'),
        ('400ml','400ml'),
        ('500ml','500ml'),
        ('700ml','700ml'),
    )
    l1_acai = models.CharField(max_length=30, choices=acai_choice, verbose_name='Açaí', default='----')
    l1_quant_acai = models.IntegerField(blank=True, null=True, verbose_name='Quantidade')
    l1_preco_acai = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Preço')
    l1_total_acai = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Total')

    l2_acai = models.CharField(max_length=30, choices=acai_choice, verbose_name='Açaí', default='----')
    l2_quant_acai = models.IntegerField(blank=True, null=True, verbose_name='Quantidade')
    l2_preco_acai = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Preço')
    l2_total_acai = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Total')

    l3_acai = models.CharField(max_length=30, choices=acai_choice, verbose_name='Açaí', default='----')
    l3_quant_acai = models.IntegerField(blank=True, null=True, verbose_name='Quantidade')
    l3_preco_acai = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Preço')
    l3_total_acai = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Total')

    l4_acai = models.CharField(max_length=30, choices=acai_choice, verbose_name='Açaí', default='----')
    l4_quant_acai = models.IntegerField(blank=True, null=True, verbose_name='Quantidade')
    l4_preco_acai = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Preço')
    l4_total_acai = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Total')

    l5_acai = models.CharField(max_length=30, choices=acai_choice, verbose_name='Açaí', default='----')
    l5_quant_acai = models.IntegerField(blank=True, null=True, verbose_name='Quantidade')
    l5_preco_acai = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Preço')
    l5_total_acai = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Total')

    l6_acai = models.CharField(max_length=30, choices=acai_choice, verbose_name='Açaí', default='----')
    l6_quant_acai = models.IntegerField(blank=True, null=True, verbose_name='Quantidade')
    l6_preco_acai = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Preço')
    l6_total_acai = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Total')

    l7_acai = models.CharField(max_length=30, choices=acai_choice, verbose_name='Açaí', default='----')
    l7_quant_acai = models.IntegerField(blank=True, null=True, verbose_name='Quantidade')
    l7_preco_acai = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Preço')
    l7_total_acai = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Total')

    l8_acai = models.CharField(max_length=30, choices=acai_choice, verbose_name='Açaí', default='----')
    l8_quant_acai = models.IntegerField(blank=True, null=True, verbose_name='Quantidade')
    l8_preco_acai = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Preço')
    l8_total_acai = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Total')

    l9_acai = models.CharField(max_length=30, choices=acai_choice, verbose_name='Açaí', default='----')
    l9_quant_acai = models.IntegerField(blank=True, null=True, verbose_name='Quantidade')
    l9_preco_acai = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Preço')
    l9_total_acai = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Total')

    l10_acai = models.CharField(max_length=30, choices=acai_choice, verbose_name='Açaí', default='----')
    l10_quant_acai = models.IntegerField(blank=True, null=True, verbose_name='Quantidade')
    l10_preco_acai = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Preço')
    l10_total_acai = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Total')

    def __str__(self):
        return "{} - {} - {} - {} - {}".format(self.id, self.data, self.cliente, self.total, self.entrega)