# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 17:23:33 2022

@author: Pedro
"""

def net_gain(volume: float, initial_price: float, final_price: float) -> str:
    """Devuelve la ganacia de la inversion
    Argumentos:
    volume -- cantidad de items comprados 
    initial_price -- precio unitario del item al momento de la compra (en GRO)
    final_price -- precio unitario del item al momento de la venta (en GRO)
    """
    profit = volume * (final_price - initial_price)
    return f"{profit} GROs"


def items_to_sell(volume: float, initial_price: float, final_price: float, book_price: float = 2831.97) -> str:
    """Devuelve la cantidad de items que se deben vender para comprar el libro y devolver los GROs prestados
    Arguments:
    volume -- cantidad de items comprados
    initial_price -- precio unitario del item al momento de la compra  (en GRO)
    final_price -- precio unitario del item al momento de la venta (en GRO)
    book_price -- precio del libro que queremos comprar
    """
    borrowed_gro = initial_price * volume
    used_gro = book_price + borrowed_gro
    items_sold = used_gro / final_price
    return f"{items_sold} items"
    