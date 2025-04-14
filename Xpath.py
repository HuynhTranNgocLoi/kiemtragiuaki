from selenium.webdriver.common.by import By
 
 class ProductDetailPage:
     def __init__(self, driver):
         self.driver = driver
 
         # Fix các XPath để chính xác hơn
         self.product_image = (By.XPATH, "//img[contains(@class, 'image-gallery-image')]")  # Ảnh sản phẩm
         self.product_name = (By.XPATH, "//h2[contains(@class, 'chakra-heading')]")  # Tên sản phẩm
         self.product_description = (By.XPATH, "//div[contains(@class, 'chakra-card__body')]/p[contains(text(), 'Description')]")  # Mô tả sản phẩm
         self.product_price = (By.XPATH, "//div[contains(@class, 'chakra-card__body')]/p[contains(text(), '$')]")  # Giá sản phẩm
         self.login_button = (By.XPATH, "//a[@href='/signin']")  # Nút đăng nhập (fix)
         self.register_button = (By.XPATH, "//a[@href='/signup']")  # Nút đăng ký (fix)
         self.add_to_bag_button = (By.XPATH, "//button[contains(text(), 'Add to Cart') or contains(text(), 'Add to Bag')]")  # Nút thêm vào giỏ hàng
 
     # Hàm để nhấn vào nút đăng nhập
     def click_login_button(self):
         self.driver.find_element(*self.login_button).click()
 
     # Hàm để nhấn vào nút đăng ký
     def click_register_button(self):
         self.driver.find_element(*self.register_button).click()
 
     # Hàm để nhấn vào nút thêm giỏ hàng
     def click_add_to_bag_button(self):
         self.driver.find_element(*self.add_to_bag_button).click()
 
     # Hàm để lấy tên sản phẩm
     def get_product_name(self):
         return self.driver.find_element(*self.product_name).text
 
     # Hàm để lấy mô tả sản phẩm
     def get_product_description(self):
         return self.driver.find_element(*self.product_description).text
 
     # Hàm để lấy giá sản phẩm
     def get_product_price(self):
         return self.driver.find_element(*self.product_price).text  