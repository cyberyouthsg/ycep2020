from selenium import webdriver


print("Starting speed typer script...")
browser = webdriver.Firefox()
URL_TO_CONNECT = "http://localhost:5000" # or wherever the file is
browser.get(URL_TO_CONNECT)

def speed_type():
    text = browser.find_element_by_id("text").text
    input_field = browser.find_element_by_name("Input")
    form = browser.find_elements_by_css_selector("form")[0]

    input_field.send_keys(text)
    form.submit()


speed_type()