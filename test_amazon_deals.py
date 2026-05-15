from selenium import webdriver

def test_amazon_deals():
    
    driver = webdriver.Edge()
    driver.get("https://www.amazon.com.br/deals")

    assert "deals" in driver.current_url
    assert "Ofertas" in driver.title
    assert "Ofertas" in driver.page_source
    
    driver.quit()
