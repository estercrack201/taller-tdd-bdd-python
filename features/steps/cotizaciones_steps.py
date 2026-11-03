import os
import sys
sys.path.insert(0, os.getcwd())

from behave import given, when, then
from cotizacion_service import QuotationService


@given('un proveedor existente con NIT "{nit}"')
def step_proveedor_existente(context, nit):
    context.service = QuotationService()
    context.service.agregar_proveedor(nit)
    context.nit = nit


@given('una solicitud de cotización "{codigo}" en estado "{estado}"')
def step_solicitud(context, codigo, estado):
    context.service.agregar_solicitud(codigo, estado)
    context.codigo = codigo


@when('el proveedor registra una cotización por {monto:d}')
def step_registrar(context, monto):
    context.cotizacion = context.service.registrar_cotizacion(
        context.nit, context.codigo, monto
    )


@then('la cotización queda en estado "{estado}"')
def step_estado(context, estado):
    assert context.cotizacion["estado"] == estado


@then('el monto cotizado es {monto:d}')
def step_monto(context, monto):
    assert context.cotizacion["monto"] == monto
