# Importar la biblioteca de Selenium y otros módulos necesarios
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Crear una instancia del controlador de Chrome
driver = webdriver.Chrome()

# Go to https://www.saucedemo.com/
driver.get('https://www.saucedemo.com/')

# Log in to the application with the “standard_user” user.
user_input = driver.find_element(By.ID, 'user-name')
user_input.send_keys('standard_user')

# Encontrar el elemento de entrada de contraseña y rellenarlo
password_input = driver.find_element(By.ID, 'password')
password_input.send_keys('secret_sauce')

# Encontrar el botón de inicio de sesión y hacer clic en él
login_button = driver.find_element(By.CLASS_NAME, 'btn_action')
login_button.click()

# Esperar a que se cargue la página de productos
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'add-to-cart-sauce-labs-backpack')))
    
# Add any product to the cart.
product = driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack')
product.click()

# Get the text value (name of the item – the one red highlighted) of the item you add to the cart.
item_name_from_list = driver.find_element(By.CLASS_NAME, 'inventory_item_name').text

# Go to the cart page.
product = driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
product.click()

# Validate that the item name text is the same that you got in step 3.1
item_name_from_cart = driver.find_element(By.CLASS_NAME, 'inventory_item_name').text

assert item_name_from_list == item_name_from_cart, f'Error: el nombre del producto esperado es {item_name_from_list}, pero el obtenido es {item_name_from_cart}'

#if item_name_from_list != item_name_from_cart:
 #   driver.quit()

# Click on Checkout.
checkout_button = driver.find_element(By.ID, 'checkout')
checkout_button.click()

# Esperar a que se cargue la página de información del pedido
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'first-name')))

# Fill in the information and continue to the next page.
first_name_input = driver.find_element(By.ID, 'first-name')
first_name_input.send_keys('John')

last_name_input = driver.find_element(By.ID, 'last-name')
last_name_input.send_keys('Doe')

postal_code_input = driver.find_element(By.ID, 'postal-code')
postal_code_input.send_keys('12345')

# Hacer clic en el botón "CONTINUAR"
continue_button = driver.find_element(By.ID, 'continue')
continue_button.click()

# Esperar a que se cargue la página de resumen del pedido
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'finish')))

# In the “CHECKOUT: OVERVIEW” page, validate that the item name text is the same that you got in step 3.1
item_name_from_overview = driver.find_element(By.CLASS_NAME, 'inventory_item_name').text

assert item_name_from_overview == item_name_from_list, f'Error: el nombre del producto esperado es {item_name_from_overview}, pero el obtenido es {item_name_from_list}'

# Finish the order.
finish_button = driver.find_element(By.ID, 'finish')
finish_button.click()

# Esperar a que se cargue la página de confirmación del pedido
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'title')))

# Obtener el texto de confirmación del pedido
checkout_complete = driver.find_element(By.CLASS_NAME, 'title').text

# Validate that you finish the order.
assert checkout_complete == "CHECKOUT: COMPLETE!", f'Error: el mensaje esperado es CHECKOUT: COMPLETE!, pero el obtenido es {checkout_complete}'

menu_button = driver.find_element(By.ID, 'react-burger-menu-btn')
menu_button.click()

# Wait for Logout button to be clickable
logout_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'logout_sidebar_link')))
logout_button = driver.find_element(By.ID, 'logout_sidebar_link')
logout_button.click()


