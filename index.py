from webdriver import WebDriver, By
import pandas as pd

browser = WebDriver()

# The webpage we want to scrap
browser.get('https://github.com/collections/machine-learning')

projects = browser.find_elements(by=By.XPATH, value='//h1[@class="h3 lh-condensed"]')
projects_dict: dict[str, str] = { }

for p in projects:
    name = p.text

    # Getting the first 'href' inside the selected h1 tag
    url = p.find_elements(by=By.XPATH, value='//a')[0].get_attribute('href')
    
    projects_dict[name] = url

browser.quit()

projects_df = pd.DataFrame.from_dict(data=projects_dict, orient='index')
projects_df['name'] = projects_df.index
projects_df.columns = ['url', 'name'] #type: ignore
projects_df = projects_df.reset_index(drop=True)

# Create CSV file from the dictionary
projects_df.to_csv('projects_list.csv')