from .models import Pedido
from django import forms

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente','total','entrega','obs','l1_lanche','l1_alface','l1_tomate','l1_maionese','l1_hellmanns','l1_pure','l1_milho','l1_anel','l1_cheddar','l1_catupiry','l1_quant_lanche','l1_total_lanche','l1_adicional_maionese','l1_bebida','l1_quant_bebida','l1_total_bebida','l1_porcao','l1_bacon','l1_cheddarp','l1_quant_porcao','l1_total_porcao','l1_acai','l1_quant_acai','l1_total_acai','l2_lanche','l2_alface','l2_tomate','l2_maionese','l2_hellmanns','l2_pure','l2_milho','l2_anel','l2_cheddar','l2_catupiry','l2_quant_lanche','l2_total_lanche','l2_adicional_maionese','l2_bebida','l2_quant_bebida','l2_total_bebida','l2_porcao','l2_bacon','l2_cheddarp','l2_quant_porcao','l2_total_porcao','l2_acai','l2_quant_acai','l2_total_acai','l3_lanche','l3_alface','l3_tomate','l3_maionese','l3_hellmanns','l3_pure','l3_milho','l3_anel','l3_cheddar','l3_catupiry','l3_quant_lanche','l3_total_lanche','l3_adicional_maionese','l3_bebida','l3_quant_bebida','l3_total_bebida','l3_porcao','l3_bacon','l3_cheddarp','l3_quant_porcao','l3_total_porcao','l3_acai','l3_quant_acai','l3_total_acai','l4_lanche','l4_alface','l4_tomate','l4_maionese','l4_hellmanns','l4_pure','l4_milho','l4_anel','l4_cheddar','l4_catupiry','l4_quant_lanche','l4_total_lanche','l4_adicional_maionese','l4_bebida','l4_quant_bebida','l4_total_bebida','l4_porcao','l4_bacon','l4_cheddarp','l4_quant_porcao','l4_total_porcao','l4_acai','l4_quant_acai','l4_total_acai','l5_lanche','l5_alface','l5_tomate','l5_maionese','l5_hellmanns','l5_pure','l5_milho','l5_anel','l5_cheddar','l5_catupiry','l5_quant_lanche','l5_total_lanche','l5_adicional_maionese','l5_bebida','l5_quant_bebida','l5_total_bebida','l5_porcao','l5_bacon','l5_cheddarp','l5_quant_porcao','l5_total_porcao','l5_acai','l5_quant_acai','l5_total_acai','l6_lanche','l6_alface','l6_tomate','l6_maionese','l6_hellmanns','l6_pure','l6_milho','l6_anel','l6_cheddar','l6_catupiry','l6_quant_lanche','l6_total_lanche','l6_adicional_maionese','l6_bebida','l6_quant_bebida','l6_total_bebida','l6_porcao','l6_bacon','l6_cheddarp','l6_quant_porcao','l6_total_porcao','l6_acai','l6_quant_acai','l6_total_acai','l7_lanche','l7_alface','l7_tomate','l7_maionese','l7_hellmanns','l7_pure','l7_milho','l7_anel','l7_cheddar','l7_catupiry','l7_quant_lanche','l7_total_lanche','l7_adicional_maionese','l7_bebida','l7_quant_bebida','l7_total_bebida','l7_porcao','l7_bacon','l7_cheddarp','l7_quant_porcao','l7_total_porcao','l7_acai','l7_quant_acai','l7_total_acai','l8_lanche','l8_alface','l8_tomate','l8_maionese','l8_hellmanns','l8_pure','l8_milho','l8_anel','l8_cheddar','l8_catupiry','l8_quant_lanche','l8_total_lanche','l8_adicional_maionese','l8_bebida','l8_quant_bebida','l8_total_bebida','l8_porcao','l8_bacon','l8_cheddarp','l8_quant_porcao','l8_total_porcao','l8_acai','l8_quant_acai','l8_total_acai','l9_lanche','l9_alface','l9_tomate','l9_maionese','l9_hellmanns','l9_pure','l9_milho','l9_anel','l9_cheddar','l9_catupiry','l9_quant_lanche','l9_total_lanche','l9_adicional_maionese','l9_bebida','l9_quant_bebida','l9_total_bebida','l9_porcao','l9_bacon','l9_cheddarp','l9_quant_porcao','l9_total_porcao','l9_acai','l9_quant_acai','l9_total_acai','l10_lanche','l10_alface','l10_tomate','l10_maionese','l10_hellmanns','l10_pure','l10_milho','l10_anel','l10_cheddar','l10_catupiry','l10_quant_lanche','l10_total_lanche','l10_adicional_maionese','l10_bebida','l10_quant_bebida','l10_total_bebida','l10_porcao','l10_bacon','l10_cheddarp','l10_quant_porcao','l10_total_porcao','l10_acai','l10_quant_acai','l10_total_acai', 'l1_preco_lanche', 'l2_preco_lanche', 'l3_preco_lanche', 'l4_preco_lanche', 'l5_preco_lanche', 'l6_preco_lanche', 'l7_preco_lanche', 'l8_preco_lanche', 'l9_preco_lanche', 'l10_preco_lanche', 'l1_preco_bebida', 'l2_preco_bebida', 'l3_preco_bebida', 'l4_preco_bebida', 'l4_preco_bebida', 'l5_preco_bebida', 'l6_preco_bebida', 'l7_preco_bebida', 'l8_preco_bebida', 'l9_preco_bebida', 'l10_preco_bebida', 'l1_preco_porcao', 'l2_preco_porcao', 'l3_preco_porcao', 'l4_preco_porcao', 'l5_preco_porcao', 'l6_preco_porcao', 'l7_preco_porcao', 'l8_preco_porcao', 'l9_preco_porcao', 'l10_preco_porcao', 'l1_preco_acai', 'l2_preco_acai', 'l3_preco_acai', 'l4_preco_acai', 'l5_preco_acai', 'l6_preco_acai', 'l7_preco_acai', 'l8_preco_acai', 'l9_preco_acai', 'l10_preco_acai']
    
class BuscaPedidoForm(forms.ModelForm):
    gerar_pedido = forms.BooleanField(required=False)
    class Meta:
        model = Pedido
        fields = ['gerar_pedido','cliente']

class AtualizaPedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente','total','entrega','obs','l1_lanche','l1_alface','l1_tomate','l1_maionese','l1_hellmanns','l1_pure','l1_milho','l1_anel','l1_cheddar','l1_catupiry','l1_quant_lanche','l1_total_lanche','l1_adicional_maionese','l1_bebida','l1_quant_bebida','l1_total_bebida','l1_porcao','l1_bacon','l1_cheddarp','l1_quant_porcao','l1_total_porcao','l1_acai','l1_quant_acai','l1_total_acai','l2_lanche','l2_alface','l2_tomate','l2_maionese','l2_hellmanns','l2_pure','l2_milho','l2_anel','l2_cheddar','l2_catupiry','l2_quant_lanche','l2_total_lanche','l2_adicional_maionese','l2_bebida','l2_quant_bebida','l2_total_bebida','l2_porcao','l2_bacon','l2_cheddarp','l2_quant_porcao','l2_total_porcao','l2_acai','l2_quant_acai','l2_total_acai','l3_lanche','l3_alface','l3_tomate','l3_maionese','l3_hellmanns','l3_pure','l3_milho','l3_anel','l3_cheddar','l3_catupiry','l3_quant_lanche','l3_total_lanche','l3_adicional_maionese','l3_bebida','l3_quant_bebida','l3_total_bebida','l3_porcao','l3_bacon','l3_cheddarp','l3_quant_porcao','l3_total_porcao','l3_acai','l3_quant_acai','l3_total_acai','l4_lanche','l4_alface','l4_tomate','l4_maionese','l4_hellmanns','l4_pure','l4_milho','l4_anel','l4_cheddar','l4_catupiry','l4_quant_lanche','l4_total_lanche','l4_adicional_maionese','l4_bebida','l4_quant_bebida','l4_total_bebida','l4_porcao','l4_bacon','l4_cheddarp','l4_quant_porcao','l4_total_porcao','l4_acai','l4_quant_acai','l4_total_acai','l5_lanche','l5_alface','l5_tomate','l5_maionese','l5_hellmanns','l5_pure','l5_milho','l5_anel','l5_cheddar','l5_catupiry','l5_quant_lanche','l5_total_lanche','l5_adicional_maionese','l5_bebida','l5_quant_bebida','l5_total_bebida','l5_porcao','l5_bacon','l5_cheddarp','l5_quant_porcao','l5_total_porcao','l5_acai','l5_quant_acai','l5_total_acai','l6_lanche','l6_alface','l6_tomate','l6_maionese','l6_hellmanns','l6_pure','l6_milho','l6_anel','l6_cheddar','l6_catupiry','l6_quant_lanche','l6_total_lanche','l6_adicional_maionese','l6_bebida','l6_quant_bebida','l6_total_bebida','l6_porcao','l6_bacon','l6_cheddarp','l6_quant_porcao','l6_total_porcao','l6_acai','l6_quant_acai','l6_total_acai','l7_lanche','l7_alface','l7_tomate','l7_maionese','l7_hellmanns','l7_pure','l7_milho','l7_anel','l7_cheddar','l7_catupiry','l7_quant_lanche','l7_total_lanche','l7_adicional_maionese','l7_bebida','l7_quant_bebida','l7_total_bebida','l7_porcao','l7_bacon','l7_cheddarp','l7_quant_porcao','l7_total_porcao','l7_acai','l7_quant_acai','l7_total_acai','l8_lanche','l8_alface','l8_tomate','l8_maionese','l8_hellmanns','l8_pure','l8_milho','l8_anel','l8_cheddar','l8_catupiry','l8_quant_lanche','l8_total_lanche','l8_adicional_maionese','l8_bebida','l8_quant_bebida','l8_total_bebida','l8_porcao','l8_bacon','l8_cheddarp','l8_quant_porcao','l8_total_porcao','l8_acai','l8_quant_acai','l8_total_acai','l9_lanche','l9_alface','l9_tomate','l9_maionese','l9_hellmanns','l9_pure','l9_milho','l9_anel','l9_cheddar','l9_catupiry','l9_quant_lanche','l9_total_lanche','l9_adicional_maionese','l9_bebida','l9_quant_bebida','l9_total_bebida','l9_porcao','l9_bacon','l9_cheddarp','l9_quant_porcao','l9_total_porcao','l9_acai','l9_quant_acai','l9_total_acai','l10_lanche','l10_alface','l10_tomate','l10_maionese','l10_hellmanns','l10_pure','l10_milho','l10_anel','l10_cheddar','l10_catupiry','l10_quant_lanche','l10_total_lanche','l10_adicional_maionese','l10_bebida','l10_quant_bebida','l10_total_bebida','l10_porcao','l10_bacon','l10_cheddarp','l10_quant_porcao','l10_total_porcao','l10_acai','l10_quant_acai','l10_total_acai', 'l1_preco_lanche', 'l2_preco_lanche', 'l3_preco_lanche', 'l4_preco_lanche', 'l5_preco_lanche', 'l6_preco_lanche', 'l7_preco_lanche', 'l8_preco_lanche', 'l9_preco_lanche', 'l10_preco_lanche', 'l1_preco_bebida', 'l2_preco_bebida', 'l3_preco_bebida', 'l4_preco_bebida', 'l4_preco_bebida', 'l5_preco_bebida', 'l6_preco_bebida', 'l7_preco_bebida', 'l8_preco_bebida', 'l9_preco_bebida', 'l10_preco_bebida', 'l1_preco_porcao', 'l2_preco_porcao', 'l3_preco_porcao', 'l4_preco_porcao', 'l5_preco_porcao', 'l6_preco_porcao', 'l7_preco_porcao', 'l8_preco_porcao', 'l9_preco_porcao', 'l10_preco_porcao', 'l1_preco_acai', 'l2_preco_acai', 'l3_preco_acai', 'l4_preco_acai', 'l5_preco_acai', 'l6_preco_acai', 'l7_preco_acai', 'l8_preco_acai', 'l9_preco_acai', 'l10_preco_acai']