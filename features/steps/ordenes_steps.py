import os
import sys
sys.path.insert(0, os.getcwd())

from behave import given, when, then
from orden_service import OrdenService


@given('el proveedor "{nombre}" con presupuesto disponible de {presupuesto:d}')
def step_proveedor_presupuesto(context, nombre, presupuesto):
    context.service = OrdenService()
    context.service.agregar_proveedor(nombre, presupuesto)
    context.proveedor = nombre


@given('una orden "{codigo}" por {monto:d} en estado "{estado}"')
def step_orden(context, codigo, monto, estado):
    context.service.agregar_orden(codigo, context.proveedor, monto, estado)
    context.codigo_orden = codigo


@when('el jefe de compras aprueba la orden')
def step_aprobar(context):
    context.orden = context.service.aprobar_orden(context.codigo_orden)


@then('la orden cambia a "{estado}"')
def step_estado_orden(context, estado):
    assert context.orden["estado"] == estado


@then('el presupuesto del proveedor se reduce a {esperado:d}')
def step_presupuesto_reducido(context, esperado):
    actual = context.service.presupuesto_de(context.proveedor)
    assert actual == esperado, f"Esperado {esperado}, pero hay {actual}"
