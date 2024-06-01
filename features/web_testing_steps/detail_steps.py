from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.detail_page import DetailsPage
from behave import when, then    


@when(u'I click on the product with name "{product_name}"')
def step_impl(context, product_name):
    context.inventory_page.go_to_product_details(product_name)
    context.detail_page = DetailsPage(context.browser)

@then(u'I should see the detail page of the product wit all its content and the correct product name "{name}", "{price}", "{description}"') 
def step_impl(context, name, price, description):
    assert context.detail_page.get_product_name() == name
    assert context.detail_page.get_product_price() == price
    assert context.detail_page.get_product_description() == description
    
    


@when(u'I click on the "Add to cart" button')
def step_impl(context):
    context.detail_page.add_to_cart()


@then(u'I go to the cart page')
def step_impl(context):
    context.detail_page.go_to_cart()
    context.cart_page = CartPage(context.browser)


@then(u'I should see the product "{product_name}" in the cart')
def step_impl(context,product_name):
    assert context.cart_page.check_existence_of_item(product_name)