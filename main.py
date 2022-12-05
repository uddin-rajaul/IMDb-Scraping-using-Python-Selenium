import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

## Path for the driver in case
path = "C:\Program Files (x86)\chromedriver.exe"

def get_driver():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                                    options=chrome_options)
    return driver


if __name__ == "__main__":
    print("creating driver....")
    driver = get_driver()
    print('success')

    url = 'https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm'
    driver.get(url)
    driver.maximize_window()

    change = driver.find_elements(By.XPATH, '//tbody/tr/td[2]/div')
    name = driver.find_elements(By.XPATH, '//tbody/tr/td[2]/a')
    movie_date = driver.find_elements(By.XPATH, '//tbody/tr/td[2]/span')
    rating = driver.find_elements(By.XPATH, '//tbody/tr/td[3]')
    link = driver.find_elements(By.XPATH, '//tbody/tr/td[2]/a')
    thumbnail = driver.find_elements(By.XPATH, '//tbody/tr/td[1]/a/img')
    movie_data = []
    df_data = pd.DataFrame(columns=['SN', 'Movie Name', 'Release Date', 'IMDb Rating', 'IMDb Link', 'Thumbnail Link'])
    for i in range(len(name)):
        df_data = {
            'SN': change[i].text,
            'Movie Name': name[i].text,
            'Release Date': movie_date[i].text,
            'IMDb Rating': rating[i].text,
            'IMDb Link': link[i].get_attribute('href'),
            'Thumbnail Link': thumbnail[i].get_attribute('src'),
        }
        movie_data.append(df_data)
    print('Saving data to CSV...')
    df_movie = pd.DataFrame(movie_data)
    print(df_movie)
    df_movie.to_csv('popular_movies.csv', index=None)





