class MyLocators():
    driver_path = './webdrivers/chromedriver'
    URL = 'https://www.saucedemo.com/'
    root_csv = './Data/test_matrix.csv'
    name_user_name = "user-name"
    name_user_password = "password"
    
    #Items
    add_to_cart_items = {
        "backpack": "add-to-cart-sauce-labs-backpack",
        "bike_light": "add-to-cart-sauce-labs-bike-light", 
        "onesie": "add-to-cart-sauce-labs-onesie",
        "jacket": "add-to-cart-sauce-labs-fleece-jacket",
        "t_shirt_black": "add-to-cart-sauce-labs-bolt-t-shirt",
        "t_shirt_red": "add-to-cart-test.allthethings()-t-shirt-(red)"
    }
    
    class_shopping_cart_link = "shopping_cart_link"
    
    #Remove second item
    cart_item_element = "cart_item"
    remove_cart_button = "cart_button"
    name_checkout_button = "checkout"
    
    #Checkout information
    name_continue_button = "continue"
    name_first_name = "firstName"
    name_last_name = "lastName"
    name_postal_code = "postalCode"
    
    #
    xpath_payment_information = "/html/body/div/div/div/div[2]/div/div[2]/div[1]"
    xpath_shipping_information = "/html/body/div/div/div/div[2]/div/div[2]/div[3]"
    xpath_price_total_information = "/html/body/div/div/div/div[2]/div/div[2]/div[5]"
    name_finish_button = "finish"
    
    id_burger_menu_button = "react-burger-menu-btn"
    class_name_complete_header = "complete-header"
    id_logout_sidebar_link = "logout_sidebar_link"
    