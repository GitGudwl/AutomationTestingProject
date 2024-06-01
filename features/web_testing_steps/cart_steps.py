
from behave import when, then


@when('the user returns to inventory from the cart page')
def step_impl(context):
    context.cart_page.return_to_inventory()

@then('the user should be on the inventory page')
def step_impl(context):
    assert "inventory.html" in context.browser.current_url

@when('the user checks the cart item names and prices')
def step_impl(context):
    context.cart_item_names = context.cart_page.get_Cart_item_names()
    context.cart_item_prices = context.cart_page.get_Cart_item_prices()

@then('the cart item names should be correct')
def step_impl(context):
    expected_item_names = ['Sauce Labs Backpack', 'Sauce Labs Bike Light', 'Sauce Labs Bolt T-Shirt']
    assert context.cart_item_names == expected_item_names

@then('the cart item prices should be correct')
def step_impl(context):
    expected_item_prices = ['$29.99', '$9.99', '$15.99']
    assert context.cart_item_prices == expected_item_prices

@when('the user removes an item from the cart')
def step_impl(context):
    context.cart_page.remove_item('Sauce Labs Backpack')

@then(u'the user check if the item is removed from the cart')
def step_impl(context):
    assert not context.cart_page.check_existence_of_item('Sauce Labs Backpack')