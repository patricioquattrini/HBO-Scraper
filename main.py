import time
from login import login
from getId import getIds

if __name__ == "__main__":

    user = input("Ingrese Usuario de HBO GO ")
    passw = input("Ingrese Contraseña ")
    url_movies = "https://www.hbogola.com/category/a68afa24-8b69-11e9-810e-0050569a010f/a68afa24-8b69-11e9-810e-0050569a010f/4"
    url_series = "https://www.hbogola.com/category/c00bb751-8b69-11e9-810e-0050569a010f/c00bb751-8b69-11e9-810e-0050569a010f/4"
    driver = login(user, passw)
    time.sleep(5)
    getIds(driver, url_movies, True)
    time.sleep(1)
    getIds(driver,url_series, False)

