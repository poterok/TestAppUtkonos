
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
# desired_caps['platformVersion'] = '9.0'
desired_caps['deviceName'] = 'Android'
desired_caps['appPackage'] = 'ru.utkonos.android.utkonoid'
desired_caps['appActivity'] = 'ru.utkonos.for_customers.online_store.presentation.activity.splash_screen.SplashScreenActivity'



driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.find_element_by_xpath('//android.widget.FrameLayout[@content-desc="Каталог"]/android.widget.ImageView').click()
