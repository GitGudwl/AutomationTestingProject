from behave import given, when, then
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@then(u'I should see all inventory items')
def step_impl(context):
    items = context.inventory_page.get_all_items_names()
    assert len(items) > 0


@when(u'I click the "Add to cart" button for the item with name "Sauce Labs Backpack"')
def step_impl(context):
    item = ['sauce-labs-backpack']
    context.inventory_page.add_items_to_cart(item)

@then('i clik the cart button')
def step_impl(context):
    context.inventory_page.go_to_cart()
    assert "cart.html" in context.browser.current_url
    context.cart_page = CartPage(context.browser)


@then(u'I should see the item with name "Sauce Labs Backpack" in the cart')
def step_impl(context):
    items = context.cart_page.get_Cart_item_names()
    assert 'Sauce Labs Backpack' in items


@when(u'I sort the inventory items by price low to high')
def step_impl(context):
    context.inventory_page.sort('lohi')

@then(u'I should see the inventory items sorted by price low to high')
def step_impl(context):
    assert context.inventory_page.check_sorting_prices()


@when(u'I sort the inventory items by name A to Z')
def step_impl(context):
    context.inventory_page.sort('az')


@then(u'I should see the inventory items sorted by name A to Z')
def step_impl(context):
    assert context.inventory_page.check_sorting_names()
    



@when(u'I sort the inventory items by price high to low')
def step_impl(context):
    context.inventory_page.sort('hilo')

@then(u'I should see the inventory items sorted by price high to low')
def step_impl(context):
    assert context.inventory_page.check_sorting_prices_desc()


@when(u'I sort the inventory items by name Z to A')
def step_impl(context):
    context.inventory_page.sort('za')


@then(u'I should see the inventory items sorted by name Z to A')
def step_impl(context):
    assert context.inventory_page.check_sorting_names_desc()

